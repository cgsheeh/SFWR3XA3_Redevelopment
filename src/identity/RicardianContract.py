import hashlib
import json
import time


##
# RicardianContract
#     Implements the interface of a Ricardian Contract
#     Will store each state of the contract as it progresses through signing
#
class RicardianContract(object):


    ##
    # Creates a Ricardian Contract from the specified contract data,
    # using the user data specified in seller_settings
    #     @param contract_dict: data about the contract
    #     @param seller_settings: settings for contract creator
    def __init__(self, contract_dict, seller_settings):
        self.contract = dict()
        ##
        # Add the metadata components to the contract
        self.contract['metadata'] = dict(expiry=contract_dict['expiry'],
                                         date=time.strftime("%Y:%m:%d:%H:%M:%S"))

        ##
        # Add the id components to the contract
        self.contract['id'] = {}
        self.contract['id']['seller'] = seller_settings
        self.contract['id']['buyer'] = dict()
        self.contract['id']['notary'] = dict()

        ##
        # Add the trade components to the contract
        self.contract['trade'] = dict(price=contract_dict['price'],
                                      name=contract_dict['item_name'],
                                      keywords=contract_dict['keywords'])

        ##
        # Add the ledger to the contract
        self.contract['ledger'] = dict()

    ##
    # Returns the specified module from this contract instance
    def get_module(self, module):
        return self.contract[module]

    ##
    # Return a hash of the contract
    def contract_hash(self):
        return hashlib.sha256(json.dumps(self.contract))

    ##
    # Returns raw dict data for contract
    # TODO improve this
    def get_dict(self):
        return self.contract

    ##
    # Returns list of keywords associated with this contract
    def get_keywords(self):
        return self.contract.get_module('trade')['keywords']