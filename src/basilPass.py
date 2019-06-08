"""
Name : Basil-Pass
Version : 0.1
Description : Exposing files/folders over local network 
Python : 2.7.x
"""
# Imports
import socket
from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor

#Splash Message
print "\n\n\t\t\t Basil-Pass v0.1 \n\n"  

#Get location of file/folder to be shared
sharingLocation = raw_input("Location or file to share : ") 
print "\n"

#Get port number to expose the files 
port = raw_input("Enter a Port : ")

#Creating a Resource | Twisted Componenet
resource = File(str(sharingLocation))   #Create an File instance to be served over TCP
factory = Site(resource)                #Creates an File instance to be served over TCP
reactor.listenTCP(int(port),factory)    #Creates an Site where all resources are stored and can be exposed over any endpoint through TCP
print "Exposing resource on "+socket.gethostbyname(socket.gethostname())+":"+port #Server initiating message
reactor.run() #Initiating server
