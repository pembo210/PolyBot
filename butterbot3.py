# coding=UTF8
import socket
import time
import random
import urllib

#----------------------------------- Settings --------------------------------------#
network = 'irc.goat.chat'
port = 6667
homechan = 'rickandmorty'
#logchan = 'botlog'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
#irc.send ( 'PASS pjmtpjmt\r\n')
irc.send ( 'NICK ButterBot\r\n' )
irc.send ( 'USER ButterBot ButterBot ButterBot :Python IRC\r\n' )

#---------------------------------- Functions -------------------------------------#

def Send(msg):
	irc.send('PRIVMSG #' + homechan + ' :' + msg +  '\r\n')

def Botlog(logmsg):
	irc.send('PRIVMSG #' + logchan + ' :' + logmsg +  '\r\n')
	open("botlog.txt", 'a').write(logmsg +'\n')


def Join(chan):
	irc.send ( 'JOIN #' + chan + '\r\n' )

def Part(chan):
	irc.send ( 'PART #' + chan + '\r\n' )

def NewNick():
	datafile = file('joinlog.txt')
	for line in datafile:
		if nick in line:
			found = True
			break
	return found

def Commands(x):
	info = x.split(' ')
	info[0] = info[0].strip(' \t\n\r')
	nick = data.split('!')[0]
	nick = nick.replace(':', ' ')
	nick = nick.replace(' ', '')
	nick = nick.strip(' \t\n\r')

	
#------------------------------------------------------------------------------#
while True:
    action = 'none'
    data = irc.recv ( 4096 )
    print data

    if data.find ( 'End of message of the day.' ) != -1:
            Join(homechan)
            Join(logchan)
            irc.send('MODE ButterBot +B \r\n')
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
#				
#			if data.find('shrugface') != -1:
#				Send(' ¯\_(ツ)_/¯')
#
   #-------------------------Rick Actions -----------------------------------#
			if data.find('texting') != -1:
				irc.send ( 'NICK Rick_Sanchez\r\n' )
				Send('Get off your high horse, Summer! ' )
				Send("We all got pinkeye because you wouldn't stop texting on the toilet. " )
				irc.send ( 'NICK ButterBot\r\n' )

			if data.find('unity') != -1:
				irc.send ( 'NICK Rick_Sanchez\r\n' )
				Send("I'm not looking for judgement, just a yes or no. " )
				Send("Can you assimilate a giraffe? " )
				irc.send ( 'NICK ButterBot\r\n' )

			if data.find('schwifty') != -1:
				irc.send ( 'NICK Rick_Sanchez\r\n' )
				Send("Ohh yea, you gotta get schwifty. " )
				irc.send ( 'NICK ButterBot\r\n' )

			if data.find('robots') != -1:
				irc.send ( 'NICK Rick_Sanchez\r\n' )
				Send("It's a figure of speech, Morty! They're bureaucrats! I don't respect them. " )
				Send("Just keep shooting, Morty! You have no idea what prison is like here! " )
				irc.send ( 'NICK ButterBot\r\n' )

			if data.find('vagina') != -1:
				irc.send ( 'NICK Rick_Sanchez\r\n' )
				Send("Puffy vagina. " )
				irc.send ( 'NICK ButterBot\r\n' )

    #-------------------------Morty Actions ----------------------------------#
			if data.find('get your shit together') != -1:
				irc.send ( 'NICK Morty_Smith\r\n' )
				Send("Well then get your shit together. " )
				Send("Get it all together and put it in a backpack, all your shit, so it's together. " )
				Send("...and if you gotta take it somewhere, take it somewhere ya know? " )
				Send("Take it to the shit store and sell it, or put it in a shit museum. " )
				Send("I don't care what you do, you just gotta get it together... Get your shit together. " )
				irc.send ( 'NICK ButterBot\r\n' )

    #-------------------------Summer Actions ---------------------------------#
			if data.find('my testicles') != -1:
				irc.send ( 'NICK Summer_Smith\r\n' )
				Send("Oh, wow. That's an intense line of questioning, Snuffles. " )
				irc.send ( 'NICK ButterBot\r\n' )

    #-------------------------Beth Actions -----------------------------------#
			if data.find('doctor') != -1:
 				irc.send ( 'NICK Beth_Smith\r\n' )
 				Send("I'm a horse surgeon. " )
 				irc.send ( 'NICK ButterBot\r\n' )

    #-------------------------Jerry Actions ----------------------------------#
			if data.find('shotgun') != -1:
 				irc.send ( 'NICK Jerry_Smith\r\n' )
 				Send("I wish that shotgun was my penis. " )
 				irc.send ( 'NICK ButterBot\r\n' )

			if data.find('get it') != -1:
 				irc.send ( 'NICK Jerry_Smith\r\n' )
 				Send("I don't get it and I don't need to. " )
 				irc.send ( 'NICK ButterBot\r\n' )

			if data.find('Pluto') != -1:
 				irc.send ( 'NICK Jerry_Smith\r\n' )
 				Send("Pluto's a planet. " )
 				irc.send ( 'NICK ButterBot\r\n' )

    #-------------------------Meeseeks Actions ----------------------------------#
			if data.find('meeseeks') != -1:
 				irc.send ( 'NICK Mr_Meeseeks\r\n' )
 				Send("HI! I'M MR MEESEEKS! LOOK AT ME! " )
 				irc.send ( 'NICK ButterBot\r\n' )

    #-------------------------Bird Actions ----------------------------------#
			if data.find('bird culture') != -1:
 				irc.send ( 'NICK Bird_Person\r\n' )
 				Send("In bird culture, that is considered a dick move. " )
 				irc.send ( 'NICK ButterBot\r\n' )

    #----------------------End NICK Actions ----------------------------------#

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
					irc.send ( 'NICK Rick_Sanchez\r\n' )
					Send('Wake up, uurp, Morty. I have a surprise for you. Buuuurp. You have to get up. ' )
					Send("C'mon Morty, get up. We're going to try this thing out Morty. " )
					Send("It's, it's, it's a chat thing. A brand new chat, uuuurp, thing that's just starting. " )
					Send('You, you gotta visit the sub too Morty! \00310 https://voat.co/v/rickandmorty\003' )
					Send("I hope you were listening, because, buuuurp, I'm not going to repeat myself." )
					irc.send ( 'NICK ButterBot\r\n' )

				elif info[0] == 'pass the butter':
					Send('What is my purpose? ' )

				elif info[0] == 'you pass butter':
					Send('OH, MY GOD! ' )

				elif info[0] == 'ping':
					Send('pong')

				elif info[0] == 'hi':
#					GetNick(data)
					Send('What is my purpose?')


				elif info[0] == 'version':
					Send('2.0')

				elif info[0] == 'help':
					Send('The followingo words and phrases trigger the bot: ' )
					Send('texting, unity, schwifty, robots, vagina, ' )
					Send('get your shit together, ' )
					Send('my testicles, doctor, shotgun, get it, Pluto, ' )
					Send('meeseeks, bird culture' )

				else:
					nick = data.split('!')[0]
					nick = nick.replace(':', ' ')
					nick = nick.replace(' ', '')
					nick = nick.strip(' \t\n\r')
					Send("I'm sorry "+ nick +", I only pass butter")


		if action == 'JOIN':
			open("joinlog.txt", 'a').write("Goatchat: " + data)
			time.sleep(0.5)
			nick = data.split('!')[0]
			nick = nick.replace(':', ' ')
			nick = nick.replace(' ', '')
			nick = nick.strip(' \t\n\r')
			normal = random.choice(["Happy Ricksgiving", "What up my glip glop", "That was Rickdiculous", "Dimension C-137 my Glip Glops!"])
			rare = random.choice(["Happy Ricksgiving", "What up my glip glop", "That was Rickdiculous", "Dimension C-137 my Glip Glops!"])
			if nick == 'hydra':
				Send('HAIL HYDRA')
			else:
				for line in file('joinlog.txt'):
					if nick in line:
						Send('That was Rickdiculous, ' +nick)
						break
					else:
						Send(random.choice([normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, normal, rare]) + ' ' + nick)
					break
