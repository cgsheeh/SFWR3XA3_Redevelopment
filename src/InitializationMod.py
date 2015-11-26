__author__ = 'connor'
from subprocess import call
import os
import gnupg
import hashlib
import pickle
from OBStrings import *
from identity.Identity import *
from node.Node import OBNode

##
# If program does not exist as a callable on the OS, return None
#
def which(program):
    import os
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

##
# This class holds the procedure to set up OpenBazaar on first run.
#
class BazaarInit(object):
    ##
    #  Creates a new GUID from the signed pubkey
    @staticmethod
    def create_GUID(signed_pubkey):
        sha256 = hashlib.sha256()
        rip160 = hashlib.new('ripemd160')
        sha256.update(signed_pubkey)
        tfs_hash = sha256.digest()
        rip160.update(tfs_hash)
        guid = rip160.hexdigest()
        return hashlib.sha1(guid).digest()

    ##
    # Generates GPG keys
    @staticmethod
    def gen_keys(gpg_path):
        call([gpg_path, '--batch', '--gen-key', 'init/unattend_init'])
        return gnupg.GPG(homedir='./identity')
    ##
    # Initializes the OpenBazaar
    #
    @staticmethod
    def initialize_Bazaar(port):
        gpg_which = which('gpg')
        if gpg_which == None:
            print "You do not have gpg installed. Please install gpg using \'sudo apt-get install gpg\' or some alternative."
            exit()
        else:
            ##
            #  Generate the gpg key in the identity directory,
            #  export the armored key, create a GUID
            #

            gpg = BazaarInit.gen_keys(gpg_which)
            pub_key_armor = gpg.export_keys(gpg.list_keys()[0]['keyid'])
            priv_key_armor = gpg.export_keys(gpg.list_keys()[0]['keyid'], secret=True)
            guid = BazaarInit.create_GUID(str(gpg.sign(pub_key_armor, binary=True)))

            ##
            #  Create Node object
            #

            node = OBNode(guid, port)


            ##
            # Create Identity module
            #
            id_mod = Identity(guid, pub_key_armor, priv_key_armor)

            ##
            # Dump state of id and node objects for future retrieval.
            #
            pickle.dump(id_mod, open(OBStrings.identity_pickle, 'w'))
            node.saveState()
