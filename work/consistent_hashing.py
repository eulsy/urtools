#!/usr/bin/python3
import sys, os
import hashlib

LOAD_SERVER_FILE = "LOAD_SERVER"
VIRTUAL_NODE = 100
VIRTUAL_SEP = "#"

def help():
    help_info = """
    Example: 
        python consistent_hashing.py checkinfo 
    """
    print(help_info)

#Create hash
def get_hash(s):
    return hashlib.md5(s.encode()).hexdigest()

def quick_sort(s_list):
    list_length = len(s_list)
    if list_length <= 1:return s_list
    l_list = []
    r_list = []
    mid = len(s_list) // 2
    mid_v = s_list[mid]
    for i in range(list_length):
        if i == mid:continue
        if str(s_list[i]) <= str(mid_v):l_list.append(s_list[i])
        else:r_list.append(s_list[i])
    return quick_sort(l_list) + [mid_v] + quick_sort(r_list) 

#Create ring hash space
def init_hash_space():
    result = {}
    with open(os.path.join(sys.path[0],LOAD_SERVER_FILE), mode='r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            for node in range(VIRTUAL_NODE):
                node_virtual = "%s%s%d"%(line,VIRTUAL_SEP,node)
                node_hash = get_hash(node_virtual)
                result[node_hash] = node_virtual
    return result, quick_sort(list(result.keys()))

#Binary Search,search info location information.
def binary_search(b_list, info):
    left = 0
    right = len(b_list) -1
    while left <= right:
        mid = ( left + right ) // 2
        if b_list[mid] >= info : right = mid - 1
        else: left = mid +1
    return right
    
def main(s_str):
    server_map, hash_ring = init_hash_space()
    h_str = get_hash(s_str)
    node = server_map[hash_ring[binary_search(hash_ring, h_str)]]
    server = node.split(VIRTUAL_SEP)[0]
    return server
    
if __name__ == "__main__":
    if len(sys.argv) < 2 :
        print("Error: need 1 argument 0 gave!!!")
        help()
        exit(1)
    print(main(sys.argv[1]))