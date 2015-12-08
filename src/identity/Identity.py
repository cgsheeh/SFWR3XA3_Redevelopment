import pickle
import os
import gnupg
from RicardianContract import *
from ImageStorage import *
##
# This class holds all the data related to a user identity,
# including all submodule decompositions (settings, notary, store, contract)
class Identity(object):
    ##
    # Initializes the identity module
    #     @param guid: OpenBazaar GUID
    #     @param pubkey: GPG public key
    #     @param privkey: GPG private key
    #     @param gpg_obj: gnupg.GPG object
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
    #     @param settings_dict: dictionary of settings to be saved to the state
    def set_settings(self, settings_dict):
        self.settings.store.set(settings_dict)
        self.settings.notary.set(settings_dict)
        self.save()

    ##
    # Adds new contract data to the respective nodes
    #     @param contract_dict: dict representation of the Ricardian Contract
    def new_contract(self, contract_dict):
        contract = RicardianContract(contract_dict, self.settings.store.get(), self.guid, self.pubkey)
        contract.sign(self.gpg_obj)
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
    #     @return: list of contracts matching keywords
    def search(self, keywords):
        matching_contracts = list()
        for word in keywords:
            matching_contracts += self.settings.contracts.find_local_keyword(word)
            matching_contracts += self.settings.store.find_local_keyword(word)

        return matching_contracts

    ##
    # This method returns the Merchant representation of this node
    def merchant_repr(self):
        ##
        # Pull public data out of module
        settings = self.get_settings()
        wanted_info = ['guid',
                       'pubkey',
                       'email',
                       'bitcoinReceivingAddress',
                       'storeDescription',
                       'myListings',
                       'nickname',
                       'avatar']
        info_dict = dict([(i, settings[i]) for i in wanted_info if i in settings])

        ##
        # Add my current listings to Merchant representation
        info_dict['myListings'] = self.settings.contracts.getOnGoingContracts()

        return Merchant(info_dict)

    ##
    # Adds a new merchant to the list of known merchants
    #     @param merchant_repr: merchant representation to be added
    def new_merchant(self, merchant_repr):
        self.settings.store.addMerchant(merchant_repr)
        self.save()

    ##
    # Adds a new notary to the list of known notaries
    #     @param notary_repr: notary representation to be added
    def new_notary(self, notary_repr):
        self.settings.notary.add_notary(notary_repr)
        self.save()

    ##
    # Takes another user's RicardianContract and signs it for purchase.
    #     @param desired_contract: contract to be purchased by user.
    def make_purchase(self, desired_contract):
        desired_contract.purchase(self.gpg_obj)
        self.settings.contracts.addContract(desired_contract)

    ##
    # Load identity module from default location
    #     @return: identity module created from encrypted file
    @staticmethod
    def get_id_mod():
        gpg = gnupg.GPG(homedir='identity')

        decrypt = open(IdentityStrings.identity_encrypted, 'rb')
        gpg.decrypt_file(decrypt, output=IdentityStrings.identity_pickle)
        decrypt.close()

        # Above lines handle encryption
        id_mod = pickle.load(open(IdentityStrings.identity_pickle, 'rb'))
        os.remove(IdentityStrings.identity_pickle)
        return id_mod

    ##
    # Returns true if identity has already been initialized
    #     @return: does the encrypted identity file exist
    @staticmethod
    def is_init():
        return os.path.isfile(IdentityStrings.identity_encrypted)

##
# Settings module
#     Holds all data related to user settings
#     @field store: a Store object which holds data about this node's store, as well as all stores known to the node
#     @field notary: a Notary object holding data about known notaries
#     @field contracts: a Contracts object holding data about known contracts
class Settings(object):
    def __init__(self):
        self.store = Store()
        self.notary = Notary()
        self.contracts = Contracts()

##
# Holds all data relevant to stores
class Store(object):
    ##
    # Initializes this node's Store module with default data/settings
    def __init__(self):
        self.email = ""
        self.nickname = "Give yourself a nickname!"
        self.avatar = ImageStorage(IdentityStrings.identity_avatar)
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
                    avatar=self.avatar,
                    bitcoinReceivingAddress=self.bitcoinReceivingAddress,
                    storeDescription=self.storeDescription,
                    shippingInformation=self.shippingInformation,
                    myMerchants=self.myMerchants)

    ##
    # Sets the merchant settings specified in dict
    #     @param sett_dict: dictionary of settings related to this module
    def set(self, sett_dict):
        self.email = sett_dict['email']
        self.nickname = sett_dict['nickname']
        self.bitcoinReceivingAddress = sett_dict['bitcoinReceivingAddress']
        self.storeDescription = sett_dict['storeDescription']
        self.shippingInformation = sett_dict['shippingInformation']
        try:
            self.avatar = sett_dict['avatar']
        except KeyError:
            pass

    ##
    # Adds a merchant to the list of merchants
    #     @param merchant: merchant to be added
    def addMerchant(self, merchant):
        self.myMerchants.append(merchant)

    ##
    # Finds listings from merchants that match the keyword
    #     @param word: keyword to search for
    #     @return: list of RicardianContracts that match
    def find_local_keyword(self, word):
        matching = []
        for merchant in self.myMerchants:
            for listing in merchant.get_listings():
                if word in listing.get_keywords():
                    matching.append(listing)

        return matching

##
# Holds all data relevant to notaries
class Notary(object):
    ##
    # Initializes the Notary module
    def __init__(self):
        self.isNotary = False
        self.percentage = "0"
        self.description = ""
        self.my_notaries = list()

    ##
    # Returns information about notaries
    def get(self):
        return dict(isNotary=self.isNotary,
                    percentage=self.percentage,
                    description=self.description,
                    notaries=self.my_notaries)

    ##
    # Sets local user notary settings
    #     @param settings_dict: dictionary of settings
    def set(self, settings_dict):
        self.isNotary = settings_dict['isNotary']
        self.percentage = settings_dict['percentage']
        self.description = settings_dict['description']

    ##
    # Adds a new notary to the list of known notaries
    def add_notary(self, notary_repr):
        self.my_notaries.append(notary_repr)

##
# Holds all data relevant to contracts
class Contracts(object):
    ##
    # Initializes this node's Contract module
    def __init__(self):
        self.expiredContracts = list()
        self.onGoingContracts = list()
        self.my_contracts = list()

    ##
    # Returns listings created by the user
    def get_my_contracts(self):
        return self.my_contracts

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
# This class contains the representation of a merchant known to a node on the network
class Merchant(object):
    def __init__(self, info_dict):
        self.guid = info_dict['guid']
        self.key = info_dict['pubkey']
        self.bitcoin_address = info_dict['bitcoinReceivingAddress']
        self.current_listings = info_dict['myListings']
        self.email = info_dict['email']
        self.store_description = info_dict['storeDescription']
        self.name = info_dict['nickname']
        self.avatar = info_dict['avatar']

    ##
    # GUID accessor
    def get_guid(self):
        return self.guid

    ##
    # Pubkey accessor
    def get_key(self):
        return self.key

    ##
    # Bitcoin address accessor
    def get_bitcoin_address(self):
        return self.bitcoin_address

    ##
    # Merchant email accessor
    def get_email(self):
        return self.email

    ##
    # Merchant description accessor
    def get_description(self):
        return self.store_description

    ##
    # Merchant name accessor
    def get_name(self):
        return self.name

    ##
    # Merchant avatar accessor
    def get_avatar(self):
        return self.avatar

    ##
    # Merchant listing accessor
    def get_listings(self):
        return self.current_listings


##
# This class contains an object representation of a notary known to a node
class NotaryRepresentation(object):

    ##
    # Initializes the Notary module
    def __init__(self, settings_dict):
        self.data = settings_dict

    ##
    # Returns information about notaries
    def get(self):
        return self.data

    ##
    # Sets local user notary settings
    #     @param settings_dict: dictionary of settings
    def set(self, settings_dict):
        self.data['pubkey'] = settings_dict['pubkey']
        self.data['fee'] = settings_dict['fee']
        self.data['name'] = settings_dict['name']
        self.data['guid'] = settings_dict['guid']
        self.data['bitcoinReceivingAddress'] = settings_dict['bitcoinReceivingAddress']
        self.data['description'] = settings_dict['description']
        self.data['email'] = settings_dict['email']
        self.data['avatar'] = settings_dict['avatar']



##
# Contains strings needed by identity
class IdentityStrings(object):
    identity_pickle = 'identity/identity.p'
    identity_encrypted = 'identity/id_safe'
    identity_avatar = 'identity/images/default-avatar.png'



