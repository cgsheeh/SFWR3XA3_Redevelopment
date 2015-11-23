from kademlia.network import Server
from twisted.internet import reactor

##
# Node
#     Implements an OpenBazaar node
#
class OBNode(object):
    def __init__(self, guid, port):
        ##
        # Create server object, set it to listen on port
        #guid_number = int(guid, 16)
        self.ob_server = Server(id=guid)
        self.ob_server.listen(port)

        ##
        # Attempt bootstrap to network.
        # TODO If the bootstrap fails, let user know
        possible_bootstraps = self.ob_server.bootstrappableNeighbors()
        self.ob_server.bootstrap(possible_bootstraps).addCallback(self.bootstrapDone, self.ob_server, "test")
        self.ob_server.saveState('node/knode.p')
        print "test"
        ##
        # Run networking event loop
        reactor.run()


    def bootstrapDone(self, *args):
        print "BOOTSTRAPPED"

    ##
    # Start the Kademlia node from the saved state
    def start_node(self, port):
        try:
            self.ob_server.loadState('node/knode.p')
        except IOError:
            print "Network not saved yet as no peers exist"
        self.ob_server.listen(port)

    ##
    # Attempt to bootstrap the application to the network
    def attempt_bootstrap(self, ip, port):
        self.ob_server.bootstrap([(ip, port,)]).addCallback(self.bootstrapDone, self.ob_server, "test2")

class PubContract(object):
    def __init__(self):
        self.t = 1

class DHT(object):
    def __init__(self):
        self.t = 10

#n = OBNode(1, 5090)
