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
irc.send ( 'PASS pjmtpjmt\r\n')
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

def GetMsg(data)
	x = data.split('#')[1]
	x = x.split(':')[1]
	info[0] = info[0].strip(' \t\n\r')
	return(message)
	
def GetNick(data)
	nick = data.split('!')[0]
	nick = nick.replace(':', ' ')
      	nick = nick.replace(' ', '')
      	nick = nick.strip(' \t\n\r')
      	return nick
      	
def Joins(data)
      	time.sleep(0.5)
      	wb = random.choice(["Welcome Back", "Hello", "Welcome"])
	GetNick(data)
      	datafile = file('joinlog.txt')
      	open("joinlog.txt", 'a').write(data)
      	for line in datafile:
  		if nick in line:
  			Send(wb + ' ' + nick)
            		break
         else:
            	Send('Welcome To The Matrix, ' +nick)
            	open("joinlog.txt", 'a').write(data)
    
    
def GetChan(data)
	chan1 = data.split('PRIVMSG ')[1]
	chan1 = chan1.replaec(':', ' ')
      	chan1 = chan1.replace(' ', '')
      	chan1 = chan1.strip(' \t\n\r')
      	return chan
#sample :jesuspiece|america!~jesuspiece@net-d32.1t2.215.74.IP PRIVMSG #modernpowers :hahah you're good
#------------------------------------------------------------------------------#
while True:
    action = 'none'
    data = irc.recv ( 4096 )
    print data

    if data.find ( 'Welcome to...' ) != -1:
            Join(homechan)
            irc.send('MODE PolyBot +B')

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
