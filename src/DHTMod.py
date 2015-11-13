__author__ = 'connor'

class DHT(object):
    def __init__(self):
        self.some = 1

    # Return T/F, if node replies
    def ping(self, nodeInfo):
        return None

    # Store new node in module
    def store(self, nodeInfo):
        return False

    # Return info about node
    def find_node(self, nodeInfo):
        return True

    # Return info about keyword
    def find_keyword(self, word):
        return False