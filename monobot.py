import socket
import sys
from random import randint
import re
import time
import random

#----------------------------------- Settings --------------------------------------#
network = 'irc.goat.chat'
port = 6667
homechan = '#voat'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'PASS monobot\r\n')
irc.send ( 'NICK monobot\r\n' )
irc.send ( 'USER monobot monobot monobot :monoxane Python IRC bot\r\n' )
#----------------------------------------------------------------------------------#

#---------------------------------- Functions -------------------------------------#

def Send(chan, msg):
    irc.send('PRIVMSG ' + chan + ' :' + msg +  '\r\n')

def Join(channel):
    irc.send ( 'JOIN ' + channel + '\r\n' )

def Part(chan):
    irc.send ( 'PART ' + chan + '\r\n' )

def Parse(data)
	x = data.split('#')[1]
	x = x.split(':')[1]
	info = x.split(' ')
	info[0] = info[0].strip(' \t\n\r')
	return(message)
	x = data.split('#')[0]
	x = x.split(':')[0]
	info = x.split(' ')
	info[0] = info[0].strip(' \t\n\r')
	
def Joins(data)
      open("joinlog.txt", 'a').write(data)
      time.sleep(0.5)
      wb = random.choice(["Welcome Back", "Hello", "Welcome"])
      nick = data.split('!')[0]
      nick = nick.replace(':', ' ')
      nick = nick.replace(' ', '')
      nick = nick.strip(' \t\n\r')
      datafile = file('joinlog.txt')
      for line in datafile:
        if nick in line:
          Send('Welcome To The Matrix, ' +nick)
            break
          else:
            Send(wb + ' ' + nick)
            break
    
#------------------------------------------------------------------------------#
while True:
    action = 'none'
    data = irc.recv ( 4096 )
    print data

    if data.find ( 'Welcome to...' ) != -1:
            Join(homechan)
            irc.send('MODE PolyBot +B')
            time.sleep(2)
            data = ''

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

		if action == 'JOIN':
      Joins(data)
