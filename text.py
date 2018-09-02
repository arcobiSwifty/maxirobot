'''
#italian
def start_text():
	return 'Benvenuto al bot ufficial di ItaGive, per conoscere i comandi disponibili, /help'
#todo: finish help_text
def help_text():
	return 'Ecco i comandi che puoi usare su questo bot:\n/'
#todo: finish admin_help_text
def admin_help_text():
	return help_text() + '\nEcco i comandi admin: /kick, /ban, /warn, /unkick, /unban, /unwarn'

def permission_denied(username):
	return '@'+username+'non hai i permessi necessari per eseguire questo comando. #permissiondenied
'''
#english
def start_text():
	return 'Welcome to maxi robot! To know wich commands are available you can use the /help command'
#todo finish text
def help_text():
	return 'This bot offers these commands: /solution, /challenge /mymaster /admins'

def admin_help_text():
	return help_text() + '\n /ban, /kick, /warn, /unban, /unkick, /unwarn'

def permission_denied(username):
	return '@'+username+' you don\' have permission to access these commands'