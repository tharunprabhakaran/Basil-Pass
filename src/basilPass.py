from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor
import socket
print "\n\n\t\t\t Basil-Pass v0.1 \n\n" 
sharingLocation = raw_input("Location or file to share : ")
print "\n"
port = raw_input("Enter a Port : ")
resource = File(str(sharingLocation))
factory = Site(resource)
reactor.listenTCP(int(port),factory)
print "Files Exposed on "+socket.gethostbyname(socket.gethostname())+":"+port
reactor.run()
