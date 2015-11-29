import identity.Identity as identity
import gnupg
import InitializationMod
from identity.ImageStorage import ImageStorage
from identity.RicardianContract import *


class DemoData(object):

    def __init__(self):

        self.merchant_data = list()
        self.notary_data = list()

        gpg_which = InitializationMod.which('gpg')
        gpg = InitializationMod.BazaarInit.gen_keys(gpg_which)
        pub_key_armor = gpg.export_keys(gpg.list_keys()[0]['keyid'])
        priv_key_armor = gpg.export_keys(gpg.list_keys()[0]['keyid'], secret=True)
        guid = InitializationMod.BazaarInit.create_GUID(str(gpg.sign(pub_key_armor, binary=True)))



        #Code to create a merchant
        #merchant dictionary
        merch_dict = dict()

        #listing dictionary
        listing_dict = dict()

        listing_dict['expiry'] = "12/25/15"
        listing_dict['price'] = "1000"
        listing_dict['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        listing_dict['item_name'] = "Custom Computer Intel Core i7, 16GB Ram, 3TB"
        listing_dict['keywords'] = "custom, computer, liquidcooling, used, intel, core, i7"
        listing_dict['description'] = "Slightly used custom built gaming computer. Specs are as follows: Intel Core i7 4770K, 16GB Ram, 3TB, 240GB SSD, GTX 760ti"
        listing_dict['images'] = list()

        #get real images into src
        listing_dict['images'].append(DemoDataStrings.computer)

        merch_dict['guid'] = guid
        merch_dict['pubkey'] = pub_key_armor
        merch_dict['email'] = "mandeldr@mcmaster.ca"
        merch_dict['nickname'] = "DanuelGinobli"
        merch_dict['bitcoinReceivingAddress'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        merch_dict['storeDescription'] = "The best computer wholesaler on the OpenBazaar"
        merch_dict['myListings'] = [identity.RicardianContract(listing_dict, merch_dict, guid, pub_key_armor)]
        merch_dict['avatar'] = ImageStorage(DemoDataStrings.danny_profile)

        self.merchant_data.append(identity.Merchant(merch_dict))

        #code to create a notary
        #give notary instance to DemoData
        

        #create an empty dict and populate fields with notary data
        notary_dict = dict()
        notary_dict['pubkey'] = pub_key_armor
        notary_dict['fee'] = "0.5"
        notary_dict['name'] = "DanuelGinobli"
        notary_dict['guid'] = guid
        notary_dict['bitcoinReceivingAddress'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        notary_dict['email'] = "mandeldr@mcmaster.ca"
        notary_dict['description'] = "Standard notarization services, great service, fair prices!"

        #now set the notary settings
        self.notary_data.append(identity.NotaryRepresentation(notary_dict))

    def get_notary_data(self):
        return self.notary_data

    def get_merchant_data(self):
        return self.merchant_data



class DemoDataStrings(object):
    computer = "images/demo/computer.jpg"
    danny_profile = "images/demo/danny_profile.jpg"

