import pickle
import stun

from kademlia.network import Server
from twisted.internet import reactor
from twisted.application import service, internet
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
        super(OBNode, self).__init__()
        self.listen_on_here(port)
        self.dynamic_ip = stun.get_ip_info()[1]
        self.saveState()


        Thread(target=reactor.run, args=(False,)).start()


    ##
    # Start the Kademlia node from the saved state
    def start_node(self, port):
        self.dynamic_ip = stun.get_ip_info()[1]
        try:
            self.loadState(OBNodeStrings.knode_pickle)
        except IOError:
            print "knode.p does not exist, network has not been saved."



        print "%s:\t%s" % (self.dynamic_ip, self.node.port,)

    ##
    # Sets the node to list on the specified port.
    # If the port is already in use, increment by 1 and try that port.
    # This process continues until a successful port is found.
    #     @param port: the port to listen on
    def listen_on_here(self, port):
        ##
        # Start attempting to listen on a port. Add 1 and continue if fail
        listening = False
        while not listening:
            try:
                self.listen(port)
                listening = True
            except Exception as e:
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
        super(OBNode, self).saveState(OBNodeStrings.knode_pickle)
        pickle.dump(self, open(OBNodeStrings.obnode_pickle, 'w'))

    ##
    # Searches the network for the requested keyword
    #     @param keywords: list of keywords to query the network for
    #     @return:
    def search_keywords(self, keywords):
        results = list()
        for key, value in self.storage.iteritems():
            for word in value.split(','):
                if word in keywords:
                    results.append()


class OBNodeStrings(object):
    obnode_pickle = 'node/node.p'
    knode_pickle = 'node/knode.p'