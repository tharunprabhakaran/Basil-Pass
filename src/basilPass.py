from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor

resource = File('/Users/tharun/Downloads/Dont')
factory = Site(resource)
reactor.listenTCP(8889,factory)
reactor.run()
