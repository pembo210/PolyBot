import socket
import sys
from random import randint
import re
import time
import random
#----------------------------------- Settings --------------------------------------#
#     Based on github.com/monoxane/polybot
#-----------------------------------------------------------------------------------#
network = 'irc.goat.chat'
port = 6667
homechan = '#rickandmorty'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK ButterBot\r\n' )
irc.send ( 'USER ButterBot ButterBot ButterBot :Python IRC\r\n' )
# irc.send ( 'PASS pjmtpjmt\r\n')
#----------------------------------------------------------------------------------#

#---------------------------------- Functions -------------------------------------#

def Send(msg):
    irc.send('PRIVMSG ' + homechan + ' :' + msg +  '\r\n')

def Join(chan):
    irc.send ( 'JOIN ' + chan + '\r\n' )

def Part(chan):
    irc.send ( 'PART ' + chan + '\r\n' )

def NewNick():
    datafile = file('joinlog.txt')
    for line in datafile:
        if nick in line:
            found = True
            break
    return found

#------------------------------------------------------------------------------#
while True:
    action = 'none'
    data = irc.recv ( 4096 )
    print data

    if data.find ( 'Welcome to...' ) != -1:
            Join(homechan)
            irc.send('MODE ButterBot +B')

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


			if data.find('v/') != -1:
				x = data.split('#')[1]
				x = x.split('v/')[1]
				subverse = x.split(' ')
				subverse[0] = subverse[0].strip(' \t\n\r')
                # since we dont't have jenni #
				Send(str('https://voat.co/v/') + subverse)

			if data.find('pass the butter') != -1:
				Send('What is my purpose? ')

			if data.find('you pass butter') != -1:
				Send('OH, MY GOD! ')

			if data.find('ButterBot, ') != -1:
				x = data.split('#')[1]
				x = x.split('ButterBot, ')[1]
				info = x.split('\t\n\r')
				info[0] = info[0].strip(' \t\n\r')

				if info[0] == 'info':
					Send('Wake up, uurp, Morty. I have a surprise for you. Buuuurp. You have to get up. ' )
					Send("C'mon Morty, get up. We're going to try this thing out Morty. " )
					Send("It's, it's, it's a chat thing. A brand new chat, uuuurp, thing that's just starting. " )
					Send('You, you gotta visit the sub too Morty! \00310 https://voat.co/v/rickandmorty\003' )
					Send("I hope you were listening, because I, I, I'm not going to repeat myself" )
                    
				elif info[0] == 'pass the butter':
					Send('What is my purpose? ' )
                    
				elif info[0] == 'you pass butter':
					Send('OH, MY GOD! ' )
                    
				elif info[0] == 'ping':
					Send('pong')

				elif info[0] == 'hi':
#					GetNick(data)
					Send('What is my purpose?')
		                elif info[0] == 'spam':
					Send('---------------Spam Spam Spam Spammity Spam----------------')

				elif info[0] == 'version':
					Send('2.0')

				else:
					nick = data.split('!')[0]
					nick = nick.replace(':', ' ')
					nick = nick.replace(' ', '')
					nick = nick.strip(' \t\n\r')
					Send("I'm sorry "+ nick +", I pass butter")

    if action == 'JOIN':
        open("joinlog.txt", 'a').write(data)
        time.sleep(0.5)
        wb = random.choice(["Happy Ricksgiving", "What up my glip glop", "That was Rickdiculous", "Dimension C-137 my Glip Glops!"])
        nick = data.split('!')[0]
        nick = nick.replace(':', ' ')
        nick = nick.replace(' ', '')
        nick = nick.strip(' \t\n\r')
        datafile = file('joinlog.txt')
        for line in datafile:
            if nick in line:
                Send('Dimension C-137 my Glip Glops!, ' +nick)
                break
            else:
                Send(wb + ' ' + nick)
                break
