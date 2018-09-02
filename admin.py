import pickle
#@arcobi. creator of this bot
MAIN_ADMIN = 214576309

file_name = 'admins.dat'

def reset():
	file = open(file_name, 'wb')
	pickle.dump([MAIN_ADMIN], file)
	file.close()

def newadmin(newadminid):
	if isadmin(newadminid):
		return False
	admins = getadmins()
	admins.append(newadminid)
	file = open(file_name, 'wb')
	pickle.dump(admins, file)
	file.close()
	return True

def isadmin(id):
	return id in getadmins()

def getadmins():
	file = open(file_name, 'rb')
	admins = pickle.load(file)
	file.close()
	return admins

def removeadmin(id):
	if id == MAIN_ADMIN:
		return False
	admins = getadmins()
	if (id in admins) is False:
		return False
	else: 
		newadmins = list()
		for admin in admins:
			if admin is not id:
				newadmins.append(admin)
		file = open(file_name, 'wb')
		pickle.dump(newadmins, file)
		file.close()
		return getadmins()


if __name__ == '__main__':
	print('resetted')
	print(getadmins())


