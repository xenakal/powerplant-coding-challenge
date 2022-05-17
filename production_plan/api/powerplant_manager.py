from powerplant import PowerPlantFactory
from priority_listing import optimise_priority_listing

def get_optimal_powerplants_for_load(payload_parser, logger=None, method="PL"):
    """Calculates a production plan for the powerplants of the payload_parser.
    Params:
    ------
    payload_parser: instance of the PayloadParser class.
    logger        : used for logging
    method        : Optimisation method used.
        - "BB": Branch and bounds
        - "PL": Priority listing

    """
    if method == "BB":
        # TODO
        pass
    elif method == "PL":
        powerplant_names = payload_parser.get_powerplants_names()
        powerplants = [PowerPlantFactory.init_powerplant(pname, payload_parser) for pname in powerplant_names]
        return optimise_priority_listing(powerplants, payload_parser.get_load())


