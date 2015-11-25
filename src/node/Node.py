import stun
from kademlia.network import Server
from twisted.internet import reactor
from threading import Thread

##
# Node
#     Implements an OpenBazaar node
#
class OBNode(object):
    def __init__(self, guid, port):
        ##
        # Create server object, set it to listen on port
        self.dynamic_ip = stun.get_ip_info()[1]
        self.node_guid = guid
        self.node_port = port
        self.ob_server = Server(id=self.node_guid)
        self.ob_server.listen(self.node_port)

        ##
        # Attempt bootstrap to network.
        # TODO If the bootstrap fails, let user know
        possible_bootstraps = self.ob_server.bootstrappableNeighbors()
        self.ob_server.bootstrap(possible_bootstraps).addCallback(self.bootstrap_done, self.ob_server, "test")
        self.ob_server.saveState('node/knode.p')
        ##
        # Run networking event loop
        Thread(target=reactor.run, args=(False,)).start()


    def bootstrap_done(self, *args):
        print "BOOTSTRAPPED"

    ##
    # Start the Kademlia node from the saved state
    def start_node(self, port):
        self.dynamic_ip = stun.get_ip_info()[1]
        try:
            self.ob_server.loadState('node/knode.p')
        except IOError:
            print "Network not saved yet as no peers exist"

        listening = False
        while not listening:
            try:
                self.ob_server.listen(port)
                listening = True
                self.node_port = port
            except:
                port += 1

    ##
    # Attempt to bootstrap the application to the network
    def attempt_bootstrap(self, ip, port):
        self.ob_server.bootstrap([(ip, port,)]).addCallback(self.bootstrap_done, self.ob_server, "test2")

class PubContract(object):
    def __init__(self):
        self.t = 1

class DHT(object):
    def __init__(self):
        self.t = 10

#n = OBNode(1, 5090)
