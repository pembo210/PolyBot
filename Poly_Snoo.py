import socket
import time
import random

network = 'irc.goat.chat'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
irc.send ( 'NICK Polygoner\r\n' )
irc.send ( 'USER Polygoner Polygoner Polygoner :Python IRC\r\n' )
irc.send ( 'JOIN #gaming\r\n' )
time.sleep(10)
irc.send ( 'PRIVMSG nickserv identify pjmtpjmt\r\n' )

while True:
   data = irc.recv ( 4096 )
   print(data)
   if data.find ( 'PING' ) != -1:
      irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
   if data.find ( 'A wild Snoo has appeared!' ) != -1:
      irc.send ( 'PRIVMSG #modernpowers :.bang\r\n' )
      irc.send ( 'QUIT\r\n' )
print(data)
