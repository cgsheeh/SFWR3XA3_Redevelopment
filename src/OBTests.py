import unittest2 as unittest
import identity.RicardianContract
import identity.Identity
import InitializationMod
import node.Node
import hashlib
import time
import gnupg
import os

##
# This class contains a set of tests for the RicardianContract class
class RicardianContractTests(unittest.TestCase):

    ##
    # This method tests the RicardianContract constructor
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

    ##
    # This method tests the get_module method
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

    ##
    # This method tests the contract_hash method
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

    ##
    # This method tests the get_dict accessor
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

##
# This class contains a set of tests for the Identity module
class IdentityTests(unittest.TestCase):



    ##
    # This method tests the Identity module constructor
    def test_constructor(self):
        idthing = identity.Identity.Identity("adsasdffds23423423","asdadsfw3324","asdasdfasdf")
        self.assertIsInstance(idthing, identity.Identity.Identity, "Constructor returned incorrect object")

    ##
    # This method tests the get_settings method
    def test_get_settings(self):
        idthing = identity.Identity.Identity("adsasdffds23423423","asdadsfw3324","asdasdfasdf")
        settings = idthing.get_settings()
        self.assertIsInstance(settings, dict, "Did not return the correct object type")

    ##
    # This method tests the set_settings method
    def test_set_settings(self):
        return None

    ##
    # This method tests the new_contract method
    def test_new_contract(self):
        return None

    ##
    # This method tests the get_my_contracts method
    def test_get_my_contracts(self):
        return None

    ##
    # This method tests the test_save method
    def test_save(self):
        return None

    ##
    # This method tests the static get_id_mod method
    def get_id_mod_test(self):
        return None

    ##
    # This method tests the static is_init method
    def is_init_test(self):
        return None

##
# This class contains tests for the Settings module
class SettingsTests(unittest.TestCase):

    ##
    # Setup a Settings module
    def setUp(self):
        self.settings = identity.Identity.Settings()

    ##
    # Test to make sure setup worked correctly
    def test_constructor(self):
        self.assertIsInstance(self.settings.contracts, identity.Identity.Contracts,
                              "The contract module was not instantiated")
        self.assertIsInstance(self.settings.notary, identity.Identity.Notary,
                              "The notary module was not instantiated")
        self.assertIsInstance(self.settings.store, identity.Identity.Store,
                              "The store module was not instantiated")
        self.assertIsInstance(self, identity.Identity.Settings,
                              "The Settings module was not correctly instantiated")

class StoreTests(unittest.TestCase):

    def test_constructor(self):
        return None

    def test_get(self):
        return None

    def test_set(self):
        return None

    def test_addMerchant(self):
        return None

class NotaryTests(unittest.TestCase):

    def test_constructor(self):
        return None

    def test_get(self):
        return None

    def test_set(self):
        return None

class ContractsTests(unittest.TestCase):

    def test_constructor(self):
        return None

    def test_getExpiredContracts(self):
        return None

    def test_getOnGoingContracts(self):
        return None

    def test_addContract(self):
        return None

##
# This class contains tests for the Initialization module
class InitializationModTests(unittest.TestCase):

    ##
    # To set up testing for the InitializationMod, we need to delete all saved user data
    def setUp(self):
        ##
        # Create keys for use in test_keys
        self.key_list = list()
        for i in range(10):
            gpg_temp = InitializationMod.BazaarInit.gen_keys(InitializationMod.which('gpg'))
            # key_list has tuples in form (pubkey, privkey, signed_pubkey,)
            self.key_list.append((gpg_temp.export_keys(gpg_temp.list_keys()[0]['keyid']),
                                  gpg_temp.export_keys(gpg_temp.list_keys()[0]['keyid'], secret=True),
                                  str(gpg_temp.sign(gpg_temp.export_keys(gpg_temp.list_keys()[0]['keyid']),
                                                    binary=True))))

        files = ['identity/identity.p',
                 'identity/pubring.gpg',
                 'identity/random_seed',
                 'identity/secring.gpg',
                 'identity/trustdb.gpg',
                 'node/node.p']

        ##
        # Try and remove all setup files
        for file in files:
            try:
                os.remove(file)
            except OSError:
                pass

        InitializationMod.BazaarInit.initialize_Bazaar(12345)

    ##
    # This method tests GUID creation
    def test_create_GUID(self):
        guids = list()
        for tup in self.key_list:
            guids.append(InitializationMod.BazaarInit.create_GUID(tup[2]))

        self.assertTrue(len(guids) == len(set(guids)), "create_GUID does not create unique GUID's")

    ##
    # This method tests the initialize_bazaar method
    def test_initialize_Bazaar(self):
        self.assertTrue(os.path.isfile('identity/id_safe'), "Initialize_Bazaar does not create encrypted id module")
        self.assertTrue(os.path.isfile('identity/pubring.gpg'), "initialize_bazaar does not create pubkey")
        self.assertTrue(os.path.isfile('identity/random_seed'), "initialize_bazaar does not create random_seed")
        self.assertTrue(os.path.isfile('identity/secring.gpg'), "initialize_bazaar does not create private key")
        self.assertTrue(os.path.isfile('identity/trustdb.gpg'), "initialize_bazaar does not create trust database")

        self.assertTrue(os.path.isfile('node/node.p'), "initialize_bazaar does not create node.p file")

    ##
    # This method tests the gen_keys_test method
    def gen_keys_test(self):
        self.assertTrue(len(self.key_list) == len(set(self.key_list)), "Generated keys are not all unique")


##
# This class contains test cases for the OBNode class
class OBNodeTests(unittest.TestCase):

    ##
    # This method tests the OBNode constructor
    def test_constructor(self):
        return None

    ##
    # This method tests the start_node method
    def test_start_node(self):
        return None

    ##
    # This method tests the listen_on_here method
    def test_listen_on_here(self):
        return None

    ##
    # This method tests the attempt_bootstrap method
    def test_attempt_bootstrap(self):
        return None

    ##
    # This method tests the bootstrap_done method
    def test_bootstrap_done(self):
        return None

    ##
    # This method tests the saveState method
    def test_saveState(self):
        return None

if __name__ == '__main__':
    unittest.main()












