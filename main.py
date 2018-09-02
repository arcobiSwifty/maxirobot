#SETUP:
#pip3 install python-telegram-bot
#python3 main.py 
#RESET ADMIN DATABASE:
#python3 admin.py

MAIN_ADMIN = 214576309
SECONDARY_SHITTY_ADMIN = 292857447

import text 
import admin
import warn as warnmodule

import telegram
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
import logging

bot_token = 'this is an example token. please don't use this.'
updater = Updater(token=bot_token)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

bot = telegram.Bot(token=bot_token)

def id(update):
	return update.message.from_user.id

def chatid(update):
	return update.message.chat_id

def auth(update):
	return True


def start(bot, update):
    bot.send_message(chat_id=chatid(update), text=text.start_text())

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def help(bot, update):
	response = ''
	if admin.isadmin(id(update)):
		response = text.admin_help_text()
	else:
		response = text.help_text()
	bot.send_message(chat_id=chatid(update), text=response)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

def ban(bot, update):
	if update.message.from_user.username.endswith('bot'):
		bot.send_message(chat_id=chatid(update), text='bots are not bannable by bots')
		return

	messagereplied = ''
	try:
		messagereplied = update.message.reply_to_message.from_user.id 
	except:
		bot.send_message(chat_id=chatid(update), text='please reply to the user you want to ban')
		return
	if admin.isadmin(id(update)):
		print('banned: @'+update.message.reply_to_message.from_user.username)
		bot.kick_chat_member(chatid(update), messagereplied, timeout=365*60*20*50)
		bot.send_message(chatid(update), text='ban succeded')
	else:
		bot.send_message(chat_id=chatid(update), text=text.permission_denied(update.message.from_user.username))

ban_handler = CommandHandler('ban', ban)
dispatcher.add_handler(ban_handler)

def unban(bot, update):

	messagereplied = ''
	try:
		messagereplied = update.message.reply_to_message.from_user.id 
	except:
		bot.send_message(chat_id=chatid(update), text='please reply to the user you want to unban')
		return
	if admin.isadmin(id(update)):
		bot.unban_chat_member(chat_id=chatid(update), user_id=messagereplied)
		bot.send_message(chatid(update), text='user unbanned')
	else:
		bot.send_message(chat_id=chatid(update), text=text.permission_denied(update.message.from_user.username))

unban_handler = CommandHandler('unban', unban)
dispatcher.add_handler(unban_handler)

def kick(bot, update, warn=False):
	if update.message.from_user.username.endswith('bot'):
		bot.send_message(chat_id=chatid(update), text='bots are not bannable by bots')
		return
	try:
		messagereplied = update.message.reply_to_message.from_user.id 
	except:
		bot.send_message(chat_id=chatid(update), text='please reply to the user you want to kick')
		return
	if admin.isadmin(id(update)):
		print('kick: @'+update.message.reply_to_message.from_user.username)
		bot.kick_chat_member(chat_id=chatid(update), user_id=messagereplied)
		unban(bot, update)
		if warn is False:
			bot.send_message(chat_id=chatid(update), text='kick succeded')
	else:
		bot.send_message(chat_id=chatid(update), text=text.permission_denied(update.message.from_user.username))

kick_handler = CommandHandler('kick', kick)
dispatcher.add_handler(kick_handler)

def warn(bot, update):
	try:
		messagereplied = update.message.reply_to_message.from_user.id 
	except:
		bot.send_message(chat_id=chatid(update), text='please reply to the user you want to kick')
		return
	if update.message.from_user.username.endswith('bot'):
		bot.send_message(chat_id=chatid(update), text='bots are not bannable by bots')
		return
	if admin.isadmin(id(update)):
		warning = warnmodule.warn(update.message.reply_to_message.from_user.id)
		status = warnmodule.get_status(update.message.reply_to_message.from_user.id)
		if status > 3:
			bot.send_message(chatid(update), 'User has been warned more than three times, beggining kick progress.')
			kick(bot, update)
			warn.unwarn(update.message.reply_to_message.from_user.id)
		else:
			bot.send_message(chatid(update), 'warned successfully. User has now: {0} out of 4 warns.'.format(status))
	else:
		bot.send_message(chat_id=chatid(update), text='you have to be admin to perform this command')

warn_handler = CommandHandler('warn', warn)
dispatcher.add_handler(warn_handler)

def unwarn(bot, update):
	if admin.isadmin(id(update)):
		warnmodule.unwarn(update.message.reply_to_message.from_user.id)
		status = warnmodule.get_status(update.message.reply_to_message.from_user.id)
		bot.send_message(chatid(update), 'user unwarned. user has now: {0}/4 warns'.format(status))
	else:
		bot.send_message(chat_id=chatid(update), text='you have to be admin to perform this command')

unwarn_handler = CommandHandler('unwarn', unwarn)
dispatcher.add_handler(unwarn_handler)

def mymaster(bot, update):
	bot.send_message(chatid(update), 'My master is maxi!')

mymaster_handler = CommandHandler('mymaster', mymaster)
dispatcher.add_handler(mymaster_handler)

def addadmin(bot, update):
	if admin.isadmin(id(update)):
		admin.newadmin(update.message.reply_to_message.from_user.id)
		bot.send_message(chatid(update), text='admin added')
	else:
		bot.send_message(chat_id=chatid(update), text=text.permission_denied(update.message.from_user.username))

addadmin_handler = CommandHandler('addadmin', addadmin)
dispatcher.add_handler(addadmin_handler)

def removeadmin(bot, update):
	if admin.isadmin(id(update)):
		admin.removeadmin(update.message.reply_to_message.from_user.id)
		bot.send_message(chatid(update), text='admin removed')

removeadmin_handler = CommandHandler('removeadmin', removeadmin)
dispatcher.add_handler(removeadmin_handler)

def admins(bot, update):
	bot.send_message(chatid(update), text='@linuxer4fun, @arcobi')

admin_handler = CommandHandler('admin', admins)
dispatcher.add_handler(admin_handler)

def welcomeNewUser(bot, update):
	bot.send_message(chatid(update), 'Welcome, having a teaching stay!')
 
welcome_handler = MessageHandler(Filters.status_update.new_chat_members, welcomeNewUser)
dispatcher.add_handler(welcome_handler)

def submitSolution(bot, update):
	if auth(update) is False:
		return 
	txt = update.message.text
	txtsplit = txt.split()
	for t in txtsplit:
		if 'http' in t:
			bot.send_message(MAIN_ADMIN, 'YOU GOT A SOLUTION!\nsender: @{0}\nlink: {1}'.format(update.message.from_user.username, t))
			bot.send_message(SECONDARY_SHITTY_ADMIN, 'YOU GOT A SOLUTION!\nsender: @{0}\nlink: {1}'.format(update.message.from_user.username, t))
			bot.send_message(chatid(update), 'Thank you for submitting a solution and for using maxibot. Your solution will be revised and posted on the solution channel')
			return
	bot.send_message(chatid(update), 'make sure your solution contains a link. any impropriate use will be reported')


submit_handler = CommandHandler('submit', submitSolution)
dispatcher.add_handler(submit_handler)

def submitChallenge(bot, update):
	if auth(update) is False:
		return

	txt = update.message.text 
	if txt is '/challenge':
		bot.send_message(chatid(update), 'make sure to include your challenge idea')
		return
	try:
		x = txt[10:]
	except:
		bot.send_message(chatid(update), 'make sure to include your challenge idea')
		return

	bot.send_message(MAIN_ADMIN, 'YOU GOT A CHALLENGE IDEA!\nsender: @{0}\nidea:{1}'.format(update.message.from_user.username, txt[1:]))
	bot.send_message(SECONDARY_SHITTY_ADMIN, 'YOU GOT A CHALLENGE IDEA!\nsender: @{0}\nidea:{1}'.format(update.message.from_user.username, txt[1:]))
	bot.send_message(chatid(update), 'Thank you for submitting us a challenge! It will be posted on the programming challenges channel, with credits if it gets the approval of maxi\nNote:any impropriate use will be signaled')

challenge_handler = CommandHandler('challenge', submitChallenge)
dispatcher.add_handler(challenge_handler)


print('Loaded succesfully: polling has started')

#must be added as last
def unknown(bot, update):
	bot.send_message(chat_id=chatid(update), text='Error 404: command not found')

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
updater.idle()
