import os

unit_s = [ "B", "K", "M", "G", "T" ]

class dir_info:
	def __init__(self, path, deep):
		self.path = path
		self.deep = deep
		self.total_size = 0
		self.data = self.__format_data(self.path, self.deep)
		self.__get_per()
		self.__sort_data()
		
	def __change_unit(self, size, unit = 0):
		cu = size / 1024
		if unit > len(unit_s):
			return "%.2f%s"%(size, unit_s[-1])
		if cu <= 1:
			return "%.2f%s"%(size, unit_s[unit])
		else:
			return self.__change_unit(cu, unit+1)
		
		
		
	def __add_info(self, ilist, info):
		name = info.name
		size = self.__get_size(info.path)
		self.total_size += size 
		ilist.append({"name" : name, "size" : size, "cu" : self.__change_unit(size)})
		
	def __format_data(self, path, deep):
		if deep < 2:
			info = []
			for i in os.scandir(path):
				self.__add_info(info, i)
			return info
		else:
			info = []
			for i in os.scandir(path):
				if i.is_file():
					self.__add_info(info, i)
				elif i.is_dir():
					for k in self.__format_data(os.path.join(path, i.name), deep - 1):
						k["name"] = os.path.join(i.name, k["name"])
						info.append(k)
				else:continue
			return info
			
	def __get_size(self, path):
		try:path = path.path
		except:pass
		if os.path.isfile(path):
			return os.path.getsize(path)
		else:
			return sum(map(self.__get_size, os.scandir(path)))
	
	def __get_per(self):
		for d in self.data:
			d["per"] = "%.0f"%(d["size"]/self.total_size*100)
	
	def __sort_data(self):
		self.data = sorted(self.data,key=lambda x: x["size"], reverse=True )