def data_type(name):
	if type(name) is str:
		return len(name):
	else:
		return "no value"
	if type(name) is bool:
		return name
	elif type(name) is int:
		if name<100:
			return "The number is less than a hundred"
		elif name>100:
			return "The number is greater than a hundred"
		elif name==100:
			return "The number is equal to a hundred"
	elif type(name)	is list:
		if len(name)>2:
			return name[2]
		else:
			return None
data_type("Glue")