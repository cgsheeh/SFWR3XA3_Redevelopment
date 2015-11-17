__author__ = 'connor'

class Identity(object):
    def __init__(self, guid, pubkey, privkey):
        self.guid = guid
        self.pubkey = pubkey
        self.privkey = privkey
        self.nickname = ""
        self.email = ""
        self.bitcoin_receiving = dict()
        self.store_desc = ""
        self.is_notary = False
        self.shipping_info = {'recipient': '',
                                  'street1': '',
                                  'street2': '',
                                  'city': '',
                                  'region': '',
                                  'postal': '',
                                  'country': ''}

    # Returns all identity data as a dictionary
    def get_data(self):
        return dict(guid=self.guid,
                    nickname=self.nickname,
                    email=self.email,
                    address=self.bitcoin_receiving,
                    store_desc=self.store_desc,
                    shipping=self.shipping_info)

