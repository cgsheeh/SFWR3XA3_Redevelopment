import pickle
import time
from OBStrings import OBStrings
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
    def set_settings(self, settings_dict):
        self.settings.store.set(settings_dict)
        self.settings.notary.set(settings_dict)
        self.save()

    ##
    # Adds new contract data to the respective nodes
    # Generate the Ricardian contract structure
    #     - Metadata
    #     - ID (buyer, seller, notary)
    #     - Trade
    #     - Ledger
    #
    def new_contract(self, contract_dict):
        contract = dict()
        ##
        # Add the metadata components to the contract
        contract['metadata'] = dict(expiry=contract_dict['expiry'],
                                    date=time.strftime("%Y:%m:%d:%H:%M:%S"))

        ##
        # Add the id components to the contract
        contract['id'] = {}
        contract['id']['seller'] = self.settings.store.get()
        contract['id']['buyer'] = dict()
        contract['id']['notary'] = dict()

        ##
        # Add the trade components to the contract
        contract['trade'] = dict(price=contract_dict['price'], name=contract_dict['item_name'])

        ##
        # Add the ledger to the contract
        contract['ledger'] = dict()

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

    def get(self):
        return dict(email=self.email,
                    nickname=self.nickname,
                    avatarURL=self.avatarURL,
                    bitcoinReceivingAddress=self.bitcoinReceivingAddress,
                    storeDescription=self.storeDescription,
                    shippingInformation=self.shippingInformation,
                    myMerchants=self.myMerchants)

    def set(self, dict):
        self.email = dict['email']
        self.nickname = dict['nickname']
        self.avatarURL = dict['avatarURL']
        self.bitcoinReceivingAddress = dict['bitcoinReceivingAddress']
        self.storeDescription = dict['storeDescription']
        self.shippingInformation = dict['shippingInformation']
        self.myMerchants = dict['myMerchants']

    def addMerchant(self, merchant):
        self.myMerchants.append(merchant)

##
# Notary module
#     Holds all data relevant to notaries
class Notary(object):
    def __init__(self):
        self.isNotary = False
        self.percentage = ""
        self.description = ""

    def get(self):
        return dict(isNotary=self.isNotary,
                    percentage=self.percentage,
                    description=self.description)

    def set(self, settings_dict):
        self.isNotary = settings_dict['isNotary']
        self.percentage = settings_dict['percentage']
        self.description = settings_dict['description']
##
# Contract module
#     Holds all data relevant to contracts
class Contracts(object):
    def __init__(self):
        self.expiredContracts = []
        self.onGoingContracts = []

    def getExpiredContracts(self):
        return self.expiredContracts

    def getOnGoingContracts(self):
        return self.onGoingContracts

    def addContract(self, contract):
        self.onGoingContracts.append(contract)









