import consistent_hashing

"""
    test consistent hashing
    1.Balance
    2.Monotonicity
    3.extend

"""
test_str = "test%d.git,branch:%d"
#creat 100 git, 10 branch
test_data = []
for g in range(50):
    for b in range(5):
        test_data.append(test_str%(g, b))

for k in test_data:
    for i in range(10):
        server = consistent_hashing.main(k)
        print("%s-%s"%(k, server))

        

   



