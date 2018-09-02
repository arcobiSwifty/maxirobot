import pickle 

#format = [[0, 0], [id, status], [id, status]]

file_name = 'warn.dat'

def reset():
	file = open(file_name, 'wb')
	pickle.dump([[0, 0]], file)
	file.close()

def get_warned():
	file = open(file_name, 'rb')
	warned = pickle.load(file)
	file.close()
	return warned

def isidwarned(id):
	warned = get_warned()
	for u in warned:
		if id == u[0]:
			return True
	return False


def isidsetwarned(idset):
	warned = get_warned()
	if idset in get_warned():
		return True
	else: 
		return False

def warn(user_id):
	if user_id == 647496961:
		return
	currently_warned = get_warned()
	x = 1

	if isidwarned(user_id):
		for index in range(len(currently_warned)):
			u = currently_warned[index]
			if u[0] == user_id:
				x = currently_warned[index][1] 
				currently_warned[index][1] = x + 1
		
	else:
		currently_warned.append([user_id, x])
	new_warned = currently_warned
	file = open(file_name, 'wb')
	pickle.dump(new_warned, file)
	file.close()
	print(get_warned())
	return True
	
def get_status(id):

	warned = get_warned()
	for u in warned:
		if u[0] == id:
			return u[1]
	return 0


	

def unwarn(user_id):
	warned = get_warned()
	new_array = [[0, 0]]
	if isidwarned(user_id) is False:
		return False
	else:
		#warned = get_warned()
		for i in range(len(warned)):
			obj = warned[i]
			if obj[0] != user_id and obj[0] != 0:
				new_array.append(obj)
	
	file = open(file_name, 'wb')
	pickle.dump(new_array, file)
	file.close()
	return True

if __name__ == '__main__':
	reset()
	warn(203)
	print(get_status(203))









