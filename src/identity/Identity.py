import pickle
import os
import gnupg
from RicardianContract import *
##
# Identity module
#     This class holds all the data related to a user identity,
#     including all submodule decompositions (settings, notary, store, contract)
class Identity(object):
    def __init__(self, guid, pubkey, privkey, gpg_obj):
            self.guid = guid
            self.pubkey = pubkey
            self.privkey = privkey
            self.gpg_obj = gpg_obj
            self.settings = Settings()

    ##
    # Returns all identity data as a dictionary
    def get_settings(self):
        ret = self.settings.store.get()
        ret.update(self.settings.notary.get())
        ret['guid'] = self.guid
        ret['pubkey'] = self.pubkey
        return ret

    ##
    # Updates local settings to be saved to the identity pickle file
    #     @param settings_dict dictionary of settings to be saved to the state
    def set_settings(self, settings_dict):
        self.settings.store.set(settings_dict)
        self.settings.notary.set(settings_dict)
        self.save()

    ##
    # Adds new contract data to the respective nodes
    #     @param contract_dict dict representation of the Ricardian Contract
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
        orig = open(IdentityStrings.identity_pickle, 'wb')
        pickle.dump(self, orig)
        orig.close()

        # Below we encrypt locally and save
        to_crypt = open(IdentityStrings.identity_pickle, 'rb')
        keyid = self.gpg_obj.list_keys()[0]['keyid']
        data = self.gpg_obj.encrypt(to_crypt, keyid, output=IdentityStrings.identity_encrypted)
        to_crypt.close()
        os.remove(IdentityStrings.identity_pickle)


    ##
    # Searches for contracts with the specified keyword
    #     @param keywords: list of keywords to search for
    def search(self, keywords):
        matching_contracts = list()
        for word in keywords:
            matching_contracts += self.settings.contracts.find_local_keyword(keywords)

        return matching_contracts


    ##
    # Load identity module from default location
    @staticmethod
    def get_id_mod():
        gpg = gnupg.GPG(homedir='identity')

        decrypt = open(IdentityStrings.identity_encrypted, 'rb')
        gpg.decrypt_file(decrypt, output=IdentityStrings.identity_pickle)
        decrypt.close()

        # Above lines handle encryption
        return pickle.load(open(IdentityStrings.identity_pickle, 'rb'))

    ##
    # Returns true if identity has already been initialized
    @staticmethod
    def is_init():
        return os.path.isfile(IdentityStrings.identity_encrypted)

##
# Settings module
#     Holds all data related to user settings
#     @field store: a Store object which holds data about this node's store, as well as all stores known to the node
#     @field notary: a Notary object holding data about known notaries
#     @field contracts: a Contracts object holding data about known contracts
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
    def set(self, sett_dict):
        self.email = sett_dict['email']
        self.nickname = sett_dict['nickname']
        self.avatarURL = sett_dict['avatarURL']
        self.bitcoinReceivingAddress = sett_dict['bitcoinReceivingAddress']
        self.storeDescription = sett_dict['storeDescription']
        self.shippingInformation = sett_dict['shippingInformation']
        self.myMerchants = sett_dict['myMerchants']

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
    #     @param contract: RicardianContract object to be added to local contract cache
    def addContract(self, contract):
        self.onGoingContracts.append(contract)

    ##
    # Searches locally stored contracts for the keyword specified
    #     @param keyword: keyword to search for within local contracts
    #     @return: list of RicardianContract instances containing the specified keyword
    def find_local_keyword(self, keyword):
        found = list()
        for contract in self.onGoingContracts:
            if keyword in contract.get_keywords():
                found.append(contract)

        return found


##
# Contains strings needed by identity
class IdentityStrings(object):
    identity_pickle = 'identity/identity.p'
    identity_encrypted = 'identity/id_safe'




