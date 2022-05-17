import unittest
import json
import jsonschema
from jsonschema.exceptions import ValidationError
from payload_parser import PayloadParser
 
class PayloadParserTests(unittest.TestCase):
 
    BASE_PAYLOADS_PATH = "payloads/"

    def setUp(self):
        self.load_input_json("payload1.json")

    def tearDown(self):
        pass
    
    def load_input_json(self, path): 
        with open(self.get_full_path(path)) as payload:
            self.test_payload = json.load(payload)
        self.parser = PayloadParser(self.test_payload)

    def get_full_path(self, filename):
        return PayloadParserTests.BASE_PAYLOADS_PATH + filename
    
    #### TESTS ####

    '''Checks if the json schema defined follows the input structure.'''
    def test_schema_valid_input(self):
        self.load_input_json("payload1.json")
        try: 
            jsonschema.validate(self.test_payload, PayloadParser.PAYLOAD_SCHEMA) 
        except jsonschema.exceptions.ValidationError:
            self.fail("Fail test valid input check")
         
    '''Check that an invalid input raises an error with the encoded schema'''
    def test_schema_invalid_input(self):
        self.load_input_json("missing_arg_payload.json")
        with self.assertRaises(ValidationError):
            jsonschema.validate(self.test_payload, PayloadParser.PAYLOAD_SCHEMA)

    '''Checks if the correct load is extracted.'''
    def test_get_load(self):
        self.load_input_json("payload1.json")
        real_load = 480
        extracted_load = self.parser.get_load()
        self.assertEqual(real_load, extracted_load)

    '''Checks if the correct co2 cost is extracted.'''
    def test_get_co2_cost(self):
        real_cost = 20
        extracted_cost = self.parser.get_co2_cost()
        self.assertEqual(real_cost, extracted_cost)

    '''Checks if the correct powerplant is returned'''
    def test_get_powerplant(self):
        extracted_powerplant_eff = self.parser.get_powerplant("tj1")[PayloadParser.POWERPLANT_EFF_KEY]
        actual_eff = 0.3
        # TODO 

if __name__ == "__main__":
    unittest.main()