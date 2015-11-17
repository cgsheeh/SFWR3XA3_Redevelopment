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
            self.isNotary = "No"
            self.percentage = ""
            self.description = ""

    def get(self):
            return dict(pubkey=self.pubkey,
                    email=self.email,
                    nickname=self.nickname,
                    avatarURL=self.avatarURL,
                    bitcoinReceivingAddress=self.bitcoinReceivingAddress,
                    storeDescription=self.storeDescription,
                    shippingInformation=self.shippingInformation,
                    isNotary=self.isNotary,
                    percentage=self.percentage,
                    description=self.description
                    )

    def set(self, dict):
            self.pubkey = dict['pubkey']
            self.email = dict['email']
            self.nickname = dict['nickname']
            self.avatarURL = dict['avatarURL']
            self.bitcoinReceivingAddress = dict['bitcoinReceivingAddress']
            self.storeDescription = dict['storeDescription']
            self.shippingInformation = dict['shippingInformation']
            self.isNotary = dict['isNotary']
            self.percentage = dict['percentage']
            self.description = dict['description']










