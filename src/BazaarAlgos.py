__author__ = 'connor'
import hashlib

class Algorithms:

    # Calculates distance between two given nodes
    def calculate_node_distance(self, node1, node2):
        return node1 ^ node2

    # Creates a new GUID from the signed pubkey
    def create_GUID(self, signed_pubkey):
        sha256 = hashlib.sha256()
        rip160 = hashlib.new('ripemd160')
        sha256.update(signed_pubkey)
        tfs_hash = sha256.digest()
        rip160.update(tfs_hash)
        return rip160.digest()


