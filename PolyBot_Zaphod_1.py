import socket
import sys
from random import randint
import re
import time
import random

#----------------------------------- Settings --------------------------------------#
network = 'irc.goat.chat'
port = 6667
homechan = '#zaphod'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'PASS pjmtpjmt\r\n')
irc.send ( 'NICK Zaphod\r\n' )
irc.send ( 'USER Zaphod PolyBot PolyBot :Python IRC\r\n' )
#----------------------------------------------------------------------------------#

#---------------------------------- Functions -------------------------------------#
def GetNick(data):
    nick = data.split('!')[0]
    nick = nick.replace(':', ' ')
    nick = nick.replace(' ', '')
    nick = nick.strip(' \t\n\r')
    return nick

def Join(chan):
    irc.send ( 'JOIN ' + chan + '\r\n' )

def Send(msg):
    irc.send('PRIVMSG ' + homechan + ' :' + msg +  '\r\n')
#------------------------------------------------------------------------------#
while True:
    action = 'none'
    data = irc.recv ( 4096 )
    print data

    if data.find ( 'Welcome to...' ) != -1:
            Join('#zaphod YHSC')

    if data.find ( 'PING' ) != -1:
            irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )

    #--------------------------- Action check --------------------------------#
    if data.find('#') != -1:
        action = data.split('#')[0]
        action = action.split(' ')[1]

    if data.find('NICK') != -1:
        if data.find('#') == -1:
            action = 'NICK'

    #----------------------------- Actions -----------------------------------#
    if action != 'none':
		
		if action == 'PRIVMSG':
			if data.find('Zaphod, ') != -1:
				x = data.split('#')[1]
				x = x.split('Zaphod, ')[1]
				info = x.split(' ')
				info[0] = info[0].strip(' \t\n\r')

				if info[0] == 'info':
					Send('Talk about shit here; Orange is Friends, Teal is bots and Blue is polsaker (he runs this thing)' )

				elif info[0] == 'poem':
					Send('Do not go gentle into that good night,')
					Send('Old age should burn and rave at close of day;')
					Send('Rage, rage against the dying of the light.')
					Send(' ')
					Send('Though wise men at their end know dark is right,')
					Send('Because their words had forked no lightning they')
					Send('Do not go gentle into that good night.')

				elif info[0] == 'ping':
					Send('pong')

    if action == 'JOIN':
        wb = random.choice(["Welcome Back", "Hello", "Welcome"])
        nick = data.split('!')[0]
        nick = nick.replace(':', ' ')
        nick = nick.replace(' ', '')
        nick = nick.strip(' \t\n\r')
        datafile = file('joinlog.txt')
        Send(wb + ' ' + nick)

