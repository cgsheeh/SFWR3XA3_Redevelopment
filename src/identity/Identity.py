__author__ = 'connor'

##
# Identity module
#     This class holds all the data related to a user identity,
#     including all submodule decompositions (settings, notary, store, contract)
class Identity(object):
    def __init__(self, guid, pubkey, privkey):
            self.guid = guid
            self.pubkey = pubkey
            self.privkey = privkey
            #self.settings = self.Settings()
            #self.notary_mod = self.Notary()
            #self.store_mod = self.Store()
            #self.contract_mod = self.Contracts()


        # Returns all identity data as a dictionary
    def get_data(self):
        return

    ##
    # Settings module
    #     Holds all data related to user settings
    #
    class Settings(object):

        def __init__(self):
            self.nickname = ""
            self.email = ""
            self.bitcoin_receiving = ""
            self.store_desc = ""
            self.is_notary = False
            self.shipping_info = {'recipient': '',
                                      'street1': '',
                                      'street2': '',
                                      'city': '',
                                      'region': '',
                                      'postal': '',
                                      'country': ''}
        ##
        # Returns user settings
        def get(self):
            return dict(nickname=self.nickname,
                    email=self.email,
                    address=self.bitcoin_receiving,
                    store_desc=self.store_desc,
                    isNotary=self.is_notary,
                    shipping=self.shipping_info)

        ##
        # Sets user settings
        #
        def set(self, sett_dict):
            return
    ##
    # Store module
    #     Holds all data relevant to stores
    class Store(object):
        def __init__(self):
            self.t = 1
    ##
    # Notary module
    #     Holds all data relevant to notaries
    class Notary(object):
        def __init__(self):
            self.t = 1
    ##
    # Contract module
    #     Holds all data relevant to contracts
    class Contracts(object):
        def __init__(self):
            self.t = 1


