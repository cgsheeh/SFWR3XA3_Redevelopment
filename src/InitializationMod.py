__author__ = 'connor'
from subprocess import call
import os
import gnupg
import hashlib
import pickle
from Identity import Identity

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
    # Creates a new GUID from the signed pubkey
    @staticmethod
    def create_GUID(signed_pubkey):
        sha256 = hashlib.sha256()
        rip160 = hashlib.new('ripemd160')
        sha256.update(signed_pubkey)
        tfs_hash = sha256.digest()
        rip160.update(tfs_hash)
        return rip160.hexdigest()

    def initialize_Bazaar(self):
        gpg_which = which('gpg')
        if gpg_which == None:
            print "You do not have gpg installed. Please install gpg."
            exit()
        else:
            ##
            #  Generate the gpg key in the identity directory,
            #  export the armored key, create a GUID
            #
            call([gpg_which, '--batch', '--gen-key', 'unattend_init'])
            gpg = gnupg.GPG(homedir='../identity')
            pub_key_armor = gpg.export_keys(gpg.list_keys()[0]['keyid'])
            priv_key_armor = gpg.export_keys(gpg.list_keys()[0]['keyid'], secret=True)
            guid = BazaarInit.create_GUID(str(gpg.sign(pub_key_armor, binary=True)))

            ##
            #  Add GUID, keys to Identity object.
            #  Serialize and store in identity folder
            id = Identity(guid, pub_key_armor, priv_key_armor)
            pickle.dump(id, open('identity/identity.p', 'w'))


BazaarInit().initialize_Bazaar()
