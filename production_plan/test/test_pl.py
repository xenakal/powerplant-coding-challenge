import json
import unittest
import json

from priority_listing import optimise_priority_listing
from powerplant import PowerPlantFactory
from payload_parser import PayloadParser

class PriorityListingTests(unittest.TestCase):

    BASE_PAYLOADS_PATH = "payloads/"

    def load_input_json(self, path): 
        with open(self.get_full_path(path)) as payload:
            test_payload = json.load(payload)
        return PayloadParser(test_payload)

    def get_full_path(self, filename):
        return PriorityListingTests.BASE_PAYLOADS_PATH + filename

    def test_pl_1(self):
        self.payload_test("payload1.json", 480)

    def test_pl_2(self):
        self.payload_test("payload2.json", 480)

    def test_pl_3(self):
        self.payload_test("payload3.json", 910)

    def payload_test(self, filename, load):
        parser = self.load_input_json(filename)
        powerplants = [PowerPlantFactory.init_powerplant(p, parser) for p in parser.get_powerplants_names()]
        output = optimise_priority_listing(powerplants, load)
        print(output)
        self.verify_output(output, load)

    def verify_output(self, output, load):
        actual_load = 0
        for p in output:
            actual_load += float(p["p"])
        self.assertEqual(load, actual_load)