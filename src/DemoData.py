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
        merch_dict2 = dict()
        merch_dict3 = dict()
        merch_dict4 = dict()

        #listing dictionary
        listing_dict = dict()
        listing_dict2 = dict()
        listing_dict3 = dict()
        listing_dict4 = dict()
        listing_dict5 = dict()
        listing_dict6 = dict()


        #listings for merchant 1
        listing_dict['expiry'] = "12/25/15"
        listing_dict['price'] = "1000"
        listing_dict['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        listing_dict['item_name'] = "Custom Computer Intel Core i7, 16GB Ram, 3TB"
        listing_dict['keywords'] = "custom, computer, liquidcooling, used, intel, core, i7"
        listing_dict['description'] = "Slightly used custom built gaming computer. Specs are as follows: Intel Core i7 4770K, 16GB Ram, 3TB, 240GB SSD, GTX 760ti"
        listing_dict['images'] = list()

        #add image to listing
        listing_dict['images'].append(DemoDataStrings.computer)


        #listings for merchant 2
        listing_dict2['expiry'] = "12/25/16"
        listing_dict2['price'] = "50"
        listing_dict2['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        listing_dict2['item_name'] = "Cleveland Indians Fitted (7 1/2)"
        listing_dict2['keywords'] = "fiftyninefifty,fitted,lids,mlb,baseball,hat"
        listing_dict2['description'] = "Cleveland Inidians Original MLB Fitted"
        listing_dict2['images'] = list()

        #add image to listing
        listing_dict2['images'].append(DemoDataStrings.cleveland)

        #listings for merchant 3
        listing_dict3['expiry'] = "12/25/16"
        listing_dict3['price'] = "1000"
        listing_dict3['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        listing_dict3['item_name'] = "1/2 Carat Diamond Ring"
        listing_dict3['keywords'] = "ring,carat,diamond,gift,wedding"
        listing_dict3['description'] = "1/2 carat diamond ring, beautiful clarity, incredible sparkle, your significant other will adore you!"
        listing_dict3['images'] = list()

        #add image to listing
        listing_dict3['images'].append(DemoDataStrings.ring)

        listing_dict4['expiry'] = "12/25/15"
        listing_dict4['price'] = "10000"
        listing_dict4['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        listing_dict4['item_name'] = "1 Carat Diamond Necklace"
        listing_dict4['keywords'] = "necklace,carat,diamond,gift,beautiful"
        listing_dict4['description'] = "Diamond necklace perfect for that special somebody!"
        listing_dict4['images'] = list()

        #add image to listing
        listing_dict4['images'].append(DemoDataStrings.necklace)

        #listings for merchant 4
        listing_dict5['expiry'] = "12/25/15"
        listing_dict5['price'] = "100"
        listing_dict5['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        listing_dict5['item_name'] = "PVL Iso-Gold Premium Isolated Whey Protein *Exclusive Bonus Size!*, 6 lbs"
        listing_dict5['keywords'] = "protein,whey,gold,premium"
        listing_dict5['description'] = "PVL has always been a manufacturer of superior protein products, and the new 2012 formula of Iso-Gold exceeds expectations. Using the latest research this formula improves on their already premier formula, you can expect to see the extra features help boost your immune system and digest the protein even easier. Taking Iso-Gold before or after training will excel your recovery rate and improve on building muscles."
        listing_dict5['images'] = list()

        #add image to listing
        listing_dict5['images'].append(DemoDataStrings.protienfront)
        listing_dict5['images'].append(DemoDataStrings.protienback)

        #listings for merchant 4atman
        listing_dict6['expiry'] = "12/25/15"
        listing_dict6['price'] = "50"
        listing_dict6['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        listing_dict6['item_name'] = "BSN N.O.-XPLODE *Exclusive Bonus Size*, 999 Grams"
        listing_dict6['keywords'] = "preworkout,energy,noxplode"
        listing_dict6['description'] = "The Original Pre-Workout Igniter. Re-engineered."
        listing_dict6['images'] = list()

        #add image to listing
        listing_dict6['images'].append(DemoDataStrings.prefront)
        listing_dict6['images'].append(DemoDataStrings.preback)



        merch_dict['guid'] = guid
        merch_dict['pubkey'] = pub_key_armor
        merch_dict['email'] = "mandeldr@mcmaster.ca"
        merch_dict['nickname'] = "DanuelGinobli"
        merch_dict['bitcoinReceivingAddress'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        merch_dict['storeDescription'] = "The best computer wholesaler on the OpenBazaar"
        merch_dict['myListings'] = [identity.RicardianContract(listing_dict, merch_dict, guid, pub_key_armor)]
        merch_dict['avatar'] = ImageStorage(DemoDataStrings.danny_profile)

        merch_dict2['guid'] = guid
        merch_dict2['pubkey'] = pub_key_armor
        merch_dict2['email'] = "info@hatman.ca"
        merch_dict2['nickname'] = "The Hat Man"
        merch_dict2['bitcoinReceivingAddress'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        merch_dict2['storeDescription'] = "The best fitted hat wholesaler on the OpenBazaar"
        merch_dict2['myListings'] = [identity.RicardianContract(listing_dict2, merch_dict2, guid, pub_key_armor)]
        merch_dict2['avatar'] = ImageStorage(DemoDataStrings.hatman)

        merch_dict3['guid'] = guid
        merch_dict3['pubkey'] = pub_key_armor
        merch_dict3['email'] = "marilyn@marilynsjewellery.com"
        merch_dict3['nickname'] = "Marilyn's Jewellery"
        merch_dict3['bitcoinReceivingAddress'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        merch_dict3['storeDescription'] = "The hottest diamonds on the OpenBazaar"
        merch_dict3['myListings'] = [identity.RicardianContract(listing_dict3, merch_dict3, guid, pub_key_armor), identity.RicardianContract(listing_dict4, merch_dict3, guid, pub_key_armor)]
        merch_dict3['avatar'] = ImageStorage(DemoDataStrings.marlyn)

        merch_dict4['guid'] = guid
        merch_dict4['pubkey'] = pub_key_armor
        merch_dict4['email'] = "popeyes@popeyessupplements.com"
        merch_dict4['nickname'] = "Popeye's Supplement Store"
        merch_dict4['bitcoinReceivingAddress'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        merch_dict4['storeDescription'] = "Supplements Lowest Prices!"
        merch_dict4['myListings'] = [identity.RicardianContract(listing_dict5, merch_dict4, guid, pub_key_armor), identity.RicardianContract(listing_dict6, merch_dict4, guid, pub_key_armor)]
        merch_dict4['avatar'] = ImageStorage(DemoDataStrings.popeye)


        self.merchant_data.append(identity.Merchant(merch_dict4))
        self.merchant_data.append(identity.Merchant(merch_dict3))
        self.merchant_data.append(identity.Merchant(merch_dict2))
        self.merchant_data.append(identity.Merchant(merch_dict))

        #code to create a notary
        #give notary instance to DemoData
        

        #create an empty dict and populate fields with notary data
        notary_dict = dict()
        notary_dict['pubkey'] = pub_key_armor
        notary_dict['fee'] = "0.5"
        notary_dict['name'] = "Marilyn's Jewellery"
        notary_dict['guid'] = guid
        notary_dict['bitcoinReceivingAddress'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        notary_dict['email'] = "marilyn@marilynsjewellery.com"
        notary_dict['description'] = "The Hottest Service"
        notary_dict['avatar'] = ImageStorage(DemoDataStrings.marlyn)

        notary_dict1 = dict()
        notary_dict1['pubkey'] = pub_key_armor
        notary_dict1['fee'] = "0.25"
        notary_dict1['name'] = "DanuelGinobli"
        notary_dict1['guid'] = guid
        notary_dict1['bitcoinReceivingAddress'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        notary_dict1['email'] = "mandeldr@mcmaster.ca"
        notary_dict1['description'] = "Standard notarization services, great service, fair prices!"
        notary_dict1['avatar'] = ImageStorage(DemoDataStrings.danny_profile)

        notary_dict2 = dict()
        notary_dict2['pubkey'] = pub_key_armor
        notary_dict2['fee'] = "0.1"
        notary_dict2['name'] = "Popeye's Supplement Store"
        notary_dict2['guid'] = guid
        notary_dict2['bitcoinReceivingAddress'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        notary_dict2['email'] = "popeyes@popeyessupplements.com"
        notary_dict2['description'] = "The strongest service in town"
        notary_dict2['avatar'] = ImageStorage(DemoDataStrings.popeye)

        notary_dict3 = dict()
        notary_dict3['pubkey'] = pub_key_armor
        notary_dict3['fee'] = "free"
        notary_dict3['name'] = "The Hat Man"
        notary_dict3['guid'] = guid
        notary_dict3['bitcoinReceivingAddress'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        notary_dict3['email'] = "info@hatman.ca"
        notary_dict3['description'] = "Standard notarization services, great service, fair prices!"
        notary_dict3['avatar'] = ImageStorage(DemoDataStrings.hatman)

        #now set the notary settings
        self.notary_data.append(identity.NotaryRepresentation(notary_dict))
        self.notary_data.append(identity.NotaryRepresentation(notary_dict1))
        self.notary_data.append(identity.NotaryRepresentation(notary_dict2))
        self.notary_data.append(identity.NotaryRepresentation(notary_dict3))


    def get_notary_data(self):
        return self.notary_data

    def get_merchant_data(self):
        return self.merchant_data



class DemoDataStrings(object):
    computer = "images/demo/computer.jpg"
    danny_profile = "images/demo/danny_profile.jpg"

    cleveland = "images/demo/cleveland.jpg"
    hatman = "images/demo/hatman.jpg"

    marlyn = "images/demo/marilyn.jpg"
    ring = "images/demo/ring.jpg"
    necklace = "images/demo/necklace.jpg"

    popeye = "images/demo/popeyes.png"
    protienback = "images/demo/protienback.jpg"
    protienfront = "images/demo/protienfront.png"
    preback = "images/demo/preback.png"
    prefront = "images/demo/prefront.jpg"
