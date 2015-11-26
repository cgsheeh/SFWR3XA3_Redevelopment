import pickle
import stun

from kademlia.network import Server
from twisted.internet import reactor
from threading import Thread

##
# OBNode2
#     This class implements the information held by a node on the OB network
class OBNode(Server):
    ##
    # Constructor
    #     Initializes the OBNode
    #     @param guid: 160 bit guid for the node
    #     @param port: port for the server to listen on
    def __init__(self, guid, port):
        super(OBNode, self).__init__(id=guid)
        self.listen_on_here(port)
        self.dynamic_ip = stun.get_ip_info()[1]
        self.saveState()
        Thread(target=reactor.run, args=(False,)).start()

    ##
    # Start the Kademlia node from the saved state
    def start_node(self, port):
        self.dynamic_ip = stun.get_ip_info()[1]
        try:
            self.loadState('node/knode.p')
        except IOError:
            print "knode.p does not exist, network has not been saved."



        print "%s:\t%s" % (self.dynamic_ip, self.node.port,)

    ##
    # Tries to listen on a port, starting at the specified
    def listen_on_here(self, port):
        ##
        # Start attempting to listen on a port. Add 1 and continue if fail
        listening = False
        while not listening:
            try:
                self.listen(port)
                listening = True
            except Exception as e:
                print e.message
                port += 1

    ##
    # Attempt to bootstrap the application to the network
    #     @param ip: ip to attempt to bootstrap with
    #     @param port: port to connect to on ip
    def attempt_bootstrap(self, ip, port):
        self.bootstrap([(ip, port,)]).addCallback(self.bootstrap_done, self, "test2")
        print "attempt_bootstrap(%s, %s)" % (ip, port,)

    ##
    # Callback method for bootstrap calls
    def bootstrap_done(self, *args, **kwargs):
        print "bootstrap callback"

    ##
    # Saves the node state
    # Override from Server
    def saveState(self):
        super(OBNode, self).saveState('node/knode.p')
        pickle.dump(self, open('node/node.p', 'w'))

    ##
    # Searches the network for the requested keyword
    #     @param keywords: keywords to query the network for
    def search_keywords(self, keywords):
        results = list()
        def addCallbackToList():

        for word in keywords:
            self.get(word).addCallback()



class PubContract(object):
    def __init__(self):
        self.t = 1

class DHT(object):
    def __init__(self):
        self.t = 10

#n = OBNode(1, 5090)
