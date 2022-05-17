import logging
import numpy as np
from powerplant import PowerPlant

class PayloadParser:
    """Used to extract information from the payload, and holds information 
    about its structure. Assumes that post_data follows the PAYLOAD_SCHEMA.
    """

    LOAD_KEY            = 'load'
    POWERPLANTS_KEY     = 'powerplants'
    FUELS_KEY           = 'fuels'

    WIND_PERCENTAGE_KEY = 'wind(%)'
    CO2_COST_KEY        = 'co2(euro/ton)'
    KEROSINE_COST_KEY   = 'kerosine(euro/MWh)'
    GAS_COST_KEY        = 'gas(euro/MWh)'

    POWERPLANT_NAME_KEY = 'name'
    POWERPLANT_TYPE_KEY = 'type'
    POWERPLANT_EFF_KEY  = 'efficiency'
    POWERPLANT_PMAX_KEY = 'pmax'
    POWERPLANT_PMIN_KEY = 'pmin'

    PAYLOAD_SCHEMA = {
        'type': 'object',
        'properties': {
            f'{LOAD_KEY}': {
                'type': 'number',
                'minimum': 0
            },
            f'{FUELS_KEY}': {
                'type': 'object',
                'properties': {
                    f'{GAS_COST_KEY}': {
                        'type': 'number',
                        'minimum': 0
                    },
                    f'{KEROSINE_COST_KEY}': {
                        'type': 'number',
                        'minimum': 0
                    },
                    f'{CO2_COST_KEY}': {
                        'type': 'number',
                        'minimum': 0
                    },
                    f'{WIND_PERCENTAGE_KEY}': {
                        'type': 'number',
                        'minimum': 0,
                        'maximum': 100
                    }
                }
            },
            f'{POWERPLANTS_KEY}': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        f'{POWERPLANT_NAME_KEY}': {'type': 'string'},
                        f'{POWERPLANT_TYPE_KEY}': {'type': 'string'},
                        f'{POWERPLANT_EFF_KEY}': {
                            'type': 'number',
                            'minimum': 0,
                            'maximum': 1
                        },
                        f'{POWERPLANT_PMAX_KEY}': {
                            'type': 'number',
                            'minimum': 0,
                        },
                        f'{POWERPLANT_PMIN_KEY}': {
                            'type': 'number',
                            'minimum': 0,
                        },
                    }
                }
            }
        },
        'required': [f'{LOAD_KEY}', f'{FUELS_KEY}', f'{POWERPLANTS_KEY}']
    }


    def __init__(self, post_data, logger=logging):
        logger.debug("Init payload parser")
        self.set_payload(post_data)

    def set_payload(self, post_data):
        self.post_data = post_data

    def get_load(self):
        return self.post_data[PayloadParser.LOAD_KEY] 

    def get_powerplants(self):
        return self.post_data[PayloadParser.POWERPLANTS_KEY] 

    def get_fuels(self):
        return self.post_data[PayloadParser.FUELS_KEY] 

    def get_wind_percentage(self):
        return self.post_data[PayloadParser.FUELS_KEY][PayloadParser.WIND_PERCENTAGE_KEY]

    def get_co2_cost(self):
        return self.post_data[PayloadParser.FUELS_KEY][PayloadParser.CO2_COST_KEY]

    def get_gas_cost(self):
        return self.post_data[PayloadParser.FUELS_KEY][PayloadParser.GAS_COST_KEY]

    def get_kerosine_cost(self):
        return self.post_data[PayloadParser.FUELS_KEY][PayloadParser.KEROSINE_COST_KEY]

    def get_powerplant(self, p_name):
        powerplants = [p for p in self.post_data[PayloadParser.POWERPLANTS_KEY] if p[PayloadParser.POWERPLANT_NAME_KEY] == p_name]
        return powerplants[0] if powerplants else None

    def get_powerplant_type(self, p_name):
        powerplant = self.get_powerplant(p_name)
        return powerplant[PayloadParser.POWERPLANT_TYPE_KEY]

    def get_powerplant_specs(self, p_name):
        powerplant = self.get_powerplant(p_name)
        efficiency = powerplant[PayloadParser.POWERPLANT_EFF_KEY] 
        pmin = powerplant[PayloadParser.POWERPLANT_PMIN_KEY] 
        pmax = powerplant[PayloadParser.POWERPLANT_PMAX_KEY]
        return efficiency, pmin, pmax

    def get_powerplants_names(self):
        return [p[PayloadParser.POWERPLANT_NAME_KEY] for p in self.post_data[PayloadParser.POWERPLANTS_KEY]]

