import unittest2 as unittest
import identity.RicardianContract
import identity.Identity
import InitializationMod
import node.Node
import hashlib
import time


class RicardianContractTests(unittest.TestCase):

    def test_constructor(self):

        contract_dict = dict()
        contract_dict['expiry'] = "30/12/15"
        contract_dict['price'] = "50"
        contract_dict['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        contract_dict['item_name'] = "Hat"
        contract_dict['keywords'] = "Head"

        idthing = identity.Identity.Identity("adsasdffds23423423","asdadsfw3324","asdasdfasdf")
        seller_settings = idthing.get_settings()

        testRicardianContract = identity.RicardianContract.RicardianContract(contract_dict, seller_settings)
        self.assertIsInstance(testRicardianContract, identity.RicardianContract.RicardianContract, "Constructor returns the correct instance type (Ricardian Contract)")

    def test_get_module(self):

        #contract_dict
        contract_dict = dict()
        contract_dict['expiry'] = "30/12/15"
        contract_dict['price'] = "50"
        contract_dict['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        contract_dict['item_name'] = "Hat"
        contract_dict['keywords'] = "Head"

        idthing = identity.Identity.Identity("adsasdffds23423423","asdadsfw3324","asdasdfasdf")
        seller_settings = idthing.get_settings()

        testRicardianContract = identity.RicardianContract.RicardianContract(contract_dict, seller_settings)

        tradeDict = testRicardianContract.get_module('trade')
        price = tradeDict['price']
        item_name = tradeDict['name']
        keywords = tradeDict['keywords']
        self.assertTrue(keywords == 'Head', "The keyword is: " + keywords)
        self.assertTrue(item_name == 'Hat', "The item name is: " + item_name)
        self.assertTrue(price == "50", "The price is: " + price)

    def test_contract_hash(self):
        #contract_dict
        contract_dict = dict()
        contract_dict['expiry'] = "30/12/15"
        contract_dict['price'] = "50"
        contract_dict['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        contract_dict['item_name'] = "Hat"
        contract_dict['keywords'] = "Head"

        idthing = identity.Identity.Identity("adsasdffds23423423","asdadsfw3324","asdasdfasdf")
        seller_settings = idthing.get_settings()

        testRicardianContract = identity.RicardianContract.RicardianContract(contract_dict, seller_settings)

        hash1 = testRicardianContract.contract_hash()
        hash2 = testRicardianContract.contract_hash()

        self.assertEqual(hash1, hash2, "The hashes are the same for identitcal contracts")

        #contract_dict
        #different contract details
        newcontract_dict = dict()
        newcontract_dict['expiry'] = "30/12/17"
        newcontract_dict['price'] = "70"
        newcontract_dict['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        newcontract_dict['item_name'] = "Scarf"
        newcontract_dict['keywords'] = "Neck"

        idthing = identity.Identity.Identity("adsasdffds23423423","asdadsfw3324","asdasdfasdf")
        seller_settings = idthing.get_settings()

        testRicardianContract2 = identity.RicardianContract.RicardianContract(newcontract_dict, seller_settings)

        hash3 = testRicardianContract2.contract_hash()
        self.assertFalse(hash3 == hash1)


    def test_get_dict(self):
        #contract_dict
        contract_dict = dict()
        contract_dict['expiry'] = "30/12/15"
        contract_dict['price'] = "50"
        contract_dict['bitcoin_address'] = "19PhnZCxayeitE3D3SjWWJ3QbN9UEU2mMV"
        contract_dict['item_name'] = "Hat"
        contract_dict['keywords'] = "Head"

        idthing = identity.Identity.Identity("adsasdffds23423423","asdadsfw3324","asdasdfasdf")
        seller_settings = idthing.get_settings()

        testRicardianContract = identity.RicardianContract.RicardianContract(contract_dict, seller_settings)
        self.assertIsInstance(testRicardianContract.get_dict(), dict, "returns a dictionary incorrectly")

class IdentityTests(unittest.TestCase):

    def test_constructor(self):
        idthing = identity.Identity.Identity("adsasdffds23423423","asdadsfw3324","asdasdfasdf")
        self.assertIsInstance(idthing, identity.Identity.Identity, "Constructor returned incorrect object")

    def test_get_settings(self):
        idthing = identity.Identity.Identity("adsasdffds23423423","asdadsfw3324","asdasdfasdf")
        settings = idthing.get_settings()
        self.assertIsInstance(settings, dict, "Did not return the correct object type")

    def test_set_settings(self):
        return None

    def test_new_contract(self):
        return None

    def test_get_my_contracts(self):
        return None

    def test_save(self):
        return None
#
# class SettingsTests(unittest.TestCase):
#
#     def test_constructor(self):
#         return None
#
# class StoreTests(unittest.TestCase):
#
#     def test_constructor(self):
#         return None
#
#     def test_get(self):
#         return None
#
#     def test_set(self):
#         return None
#
#     def test_addMerchant(self):
#         return None
#
# class NotaryTests(unittest.TestCase):
#
#     def test_constructor(self):
#         return None
#
#     def test_get(self):
#         return None
#
#     def test_set(self):
#         return None
#
# class ContractsTests(unittest.TestCase):
#
#     def test_constructor(self):
#         return None
#
#     def test_getExpiredContracts(self):
#         return None
#
#     def test_getOnGoingContracts(self):
#         return None
#
#     def test_addContract(self):
#         return None
#
# class DHTModTests(unittest.TestCase):
#
#     def test_constructor(self):
#         return None
#
#     def test_ping(self):
#         return None
#
#     def test_store(self):
#         return None
#
#     def test_find_node(self):
#         return None
#
#     def test_find_keyword(self):
#         return None
#
# class InitializationModTests(unittest.TestCase):
#
#     def test_create_GUID(self):
#         return None
#
#     def test_initialize_Bazaar(self):
#         return None
#
#     def test_which(self):
#         return None
#
# class NotaryModTests(unittest.TestCase):
#
#     def test_constructor(self):
#         return None
#
#     def test_get_all(self):
#         return None
#
#     def test_get(self):
#         return None
#
# class OBNodeTests(unittest.TestCase):
#
#     def test_constructor(self):
#         return None
#
#     def test_start_node(self):
#         return None
#
#     def test_listen_on_here(self):
#         return None
#
#     def test_attempt_bootstrap(self):
#         return None
#
#     def test_bootstrap_done(self):
#         return None
#
#     def test_saveState(self):
#         return None

if __name__ == '__main__':
    unittest.main()












