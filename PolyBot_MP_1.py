import socket
import time
import random

network = 'irc.goat.chat'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
irc.send ( 'NICK PolyBot\r\n' )
irc.send ( 'USER PolyBot PolyBot PolyBot :Python IRC\r\n' )
irc.send ( 'JOIN #modernpowers\r\n' )
time.sleep(10)
irc.send ( 'PRIVMSG nickserv identify pjmtpjmt\r\n' )

while True:
   data = irc.recv ( 4096 )
   print(data)
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( '$Leavebot' ) != -1: #leave
      irc.send ( 'PRIVMSG #modernpowers :OK Cya!\r\n' )
      irc.send ( 'QUIT\r\n' )
   if data.find ( 'KICK' ) != -1:#kick+rejoin
      irc.send ( 'JOIN #modernpowers\r\n' )
   if data.find ( '$claims' ) != -1:
      irc.send ( 'PRIVMSG #modernpowers :Claims Info,\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Current Claimed and Unclaimed Countries:\r\n' )
      irc.send ( 'PRIVMSG #modernpowers : \00310    https://goo.gl/UgOP6f\003 \r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Claims Form:\r\n' )
      irc.send ( 'PRIVMSG #modernpowers : \00310    https://goo.gl/awtdj6\003 \r\n' )
   if data.find ( '$info' ) != -1:
      irc.send ( 'PRIVMSG #modernpowers :This is the IRC channel for Modern Powers,\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :We are a country roleplaying game\r\n' )
      irc.send ( 'PRIVMSG #modernpowers : \r\n' )
      irc.send ( 'PRIVMSG #modernpowers :We are based at v/modernpowers\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :For more info go to:\00310 voat.co/v/modernpowers\003 \r\n' )
      irc.send ( 'PRIVMSG #modernpowers :For a starters guide go to:\00310 http://goo.gl/1xsyR3\003\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :For the rules go to:\00310 http://goo.gl/eiXwlL\003\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :And for a timeline of events go to:\00310 http://goo.gl/alZZvM \003\r\n' )
   if data.find ( '$poem' ) != -1:#hi
      irc.send ( 'PRIVMSG #modernpowers :Do not go gentle into that good night,\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Old age should burn and rave at close of day;\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Rage, rage against the dying of the light.\r\n' )
      irc.send ( 'PRIVMSG #modernpowers : \r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Though wise men at their end know dark is right,\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Because their words had forked no lightning they\r\n' )
      irc.send ( 'PRIVMSG #modernpowers :Do not go gentle into that good night.\r\n' )
   if data.find ( ':Halofreak1171|UK!webchat@net-ldblsl.bigpond.net.au PRIVMSG #modernpowers :hm' ) != -1:#hm
      irc.send ( 'PRIVMSG #modernpowers Shut the Fuck Up Halo!\r\n' )
   if data.find ( ':Halofreak1171|UK!webchat@net-rk7.3jk.103.101.IP PRIVMSG #modernpowers :Hm' ) != -1:#hm
      irc.send ( 'PRIVMSG #modernpowers :Shut the Fuck Up Halo!\r\n' )
   if data.find ( 'net-tsjmgt.as13285') != -1:#MrBlue and Alts
      irc.send ( 'PRIVMSG #modernpowers :Fuck Off Mr Blue/Alt\r\n' )
   if data.find ( '$spam' ) != -1:#spam
      irc.send ( 'PRIVMSG #modernpowers : ==== SPAM, SPAM, SPAM, SPAMMITY SPAM! ==== \r\n' )
   if data.find ( 'JOIN :#modernpowers' ) != -1:#joins
      time.sleep(2)
      wb = random.choice(["Welcome Back!", "Hello!", "Welcome!"])
      irc.send ( 'PRIVMSG #modernpowers :' + wb + '\r\n' )
      open("joinlog.txt", 'a').write(data)
   if data.find ( 'MODE #modernpowers +o PolyBot' ) != -1:#joins
      irc.send ( 'MODE #modernpowers +oo Polygoner|* Polygoner|Russia\r\n' )
      irc.send ( 'MODE #modernpowers -ooo Halofreak1171|UK jesuspiece|America Jidlaph|Doc_Congo \r\n' )
   if data.find ( '$halo' ) != -1:#spam
      irc.send ( 'PRIVMSG #modernpowers :.tell Halofreak1171|UK Hey Halo. (This is an automated message) \r\n' )
   if data.find ( '$test' ) != -1: #test
      irc.send ( 'PRIVMSG #modernpowers :Pong, Working now?\r\n' )
print(data)
