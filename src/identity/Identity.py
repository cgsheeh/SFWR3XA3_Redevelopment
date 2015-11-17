__author__ = 'connor & danny'

##
# Identity module
#     This class holds all the data related to a user identity,
#     including all submodule decompositions (settings, notary, store, contract)
class Identity(object):
    def __init__(self, guid, pubkey, privkey):
            self.guid = guid
            self.pubkey = pubkey
            self.privkey = privkey
            self.settings = Identity.Settings()


        # Returns all identity data as a dictionary
    def get(self):
        return dict(guid=self.guid,
                    pubkey=self.pubkey,
                    settings=self.settings)

    ##
    # Settings module
    #     Holds all data related to user settings
    #
    class Settings(object):

        def __init__(self):
            self.store = Identity.Store()
            self.notary = Identity.Notary()
            self.contracts = Identity.Contracts()

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
            self.isNotary = "No"
            self.percentage = ""
            self.description = ""

        def get(self):
            return dict(isNotary=self.isNotary,
                        percentage=self.percentage,
                        description=self.description)

        def set(self,dict):
            self.isNotary = dict['isNotary']
            self.percentage = dict['percentage']
            self.description = dict['description']
    ##
    # Contract module
    #     Holds all data relevant to contracts
    class Contracts(object):
        def __init__(self):
            self.expiredContracts = []
            self.onGoingContracts = []

        def getExpiredContracts(self):
            return  self.expiredContracts

        def getOnGoingContracts(self):
            return self.onGoingContracts

        def addContract(self, contract):
            self.onGoingContracts.append(contract)

        def addExpiredContract(self, contract):
            self.expiredContracts.append(contract)








