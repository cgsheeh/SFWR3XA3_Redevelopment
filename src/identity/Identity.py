import pickle
from OBStrings import OBStrings
from RicardianContract import *
##
# Identity module
#     This class holds all the data related to a user identity,
#     including all submodule decompositions (settings, notary, store, contract)
class Identity(object):
    def __init__(self, guid, pubkey, privkey):
            self.guid = guid
            self.pubkey = pubkey
            self.privkey = privkey
            self.settings = Settings()

    ##
    # Returns all identity data as a dictionary
    #
    def get_settings(self):
        ret = self.settings.store.get()
        ret.update(self.settings.notary.get())
        ret['guid'] = self.guid
        ret['pubkey'] = self.pubkey
        return ret

    ##
    # Updates local settings to be saved to the identity pickle file
    # @param settings_dict dictionary of settings to be saved to the state
    def set_settings(self, settings_dict):
        self.settings.store.set(settings_dict)
        self.settings.notary.set(settings_dict)
        self.save()

    ##
    # Adds new contract data to the respective nodes
    # @param contract_dict dict representation of the Ricardian Contract
    def new_contract(self, contract_dict):
        contract = RicardianContract(contract_dict, self.settings.store.get())
        ##
        # Add the contract to the contracts module
        # TODO Add the contract to the node/dht module
        self.settings.contracts.addContract(contract)
        self.save()

    ##
    # Returns contracts created by the user
    def get_my_contracts(self):
        return self.settings.contracts.getOnGoingContracts()

    ##
    # Save current object configuration to pickle file
    def save(self):
        pickle.dump(self, open(OBStrings.identity_pickle, 'w'))

##
# Settings module
#     Holds all data related to user settings
#     @field store is a Store object which holds data about this node's store, as well as all stores known to the node
#     @field notary is a Notary object holding data about known notaries
#     @field contracts is a Contracts object holding data about known contracts
#
class Settings(object):
    def __init__(self):
        self.store = Store()
        self.notary = Notary()
        self.contracts = Contracts()

##
# Store module
#     Holds all data relevant to stores
class Store(object):
    ##
    # Store()
    #     Initializes this node's Store module with default data/settings
    #
    def __init__(self):
        self.email = ""
        self.nickname = ""
        self.avatarURL = ""
        self.bitcoinReceivingAddress = ""
        self.storeDescription = ""
        self.shippingInformation = {'recipient': '',
                                  'street1': '',
                                  'street2': '',
                                  'city': '',
                                  'province/state/region': '',
                                  'postal/zip': '',
                                  'country': ''}
        self.myMerchants = []

    ##
    # Returns a dictionary of local user settings
    def get(self):
        return dict(email=self.email,
                    nickname=self.nickname,
                    avatarURL=self.avatarURL,
                    bitcoinReceivingAddress=self.bitcoinReceivingAddress,
                    storeDescription=self.storeDescription,
                    shippingInformation=self.shippingInformation,
                    myMerchants=self.myMerchants)

    ##
    # Sets the merchant settings specified in dict
    #     @param dict: dictionary of settings related to this module
    def set(self, dict):
        self.email = dict['email']
        self.nickname = dict['nickname']
        self.avatarURL = dict['avatarURL']
        self.bitcoinReceivingAddress = dict['bitcoinReceivingAddress']
        self.storeDescription = dict['storeDescription']
        self.shippingInformation = dict['shippingInformation']
        self.myMerchants = dict['myMerchants']

    ##
    # Adds a merchant to the list of merchants
    #     @param merchant: merchant to be added
    def addMerchant(self, merchant):
        self.myMerchants.append(merchant)

##
# Notary module
#     Holds all data relevant to notaries
class Notary(object):
    def __init__(self):
        self.isNotary = False
        self.percentage = "0"
        self.description = ""

    ##
    # Returns information about notaries
    def get(self):
        return dict(isNotary=self.isNotary,
                    percentage=self.percentage,
                    description=self.description)

    ##
    # Sets local user notary settings
    def set(self, settings_dict):
        self.isNotary = settings_dict['isNotary']
        self.percentage = settings_dict['percentage']
        self.description = settings_dict['description']

##
# Contract module
#     Holds all data relevant to contracts
class Contracts(object):
    ##
    # Contracts()
    #     Initializes this node's Contract module
    def __init__(self):
        self.expiredContracts = []
        self.onGoingContracts = []

    ##
    # Returns a list of expired contracts
    def getExpiredContracts(self):
        return self.expiredContracts

    ##
    # Returns a list of ongoing user contracts
    def getOnGoingContracts(self):
        return self.onGoingContracts

    ##
    # Adds a new ongoing contract
    def addContract(self, contract):
        self.onGoingContracts.append(contract)









