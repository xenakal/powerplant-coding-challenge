import logging

def optimise_priority_listing(powerplants, load):
    """ 
    Returns a close-to-optimal production plan (minimising total cost) that is valid for the given load, with the given powerplants. 

    Params
    ------
    powerplants: list of Powerplant objects
    load       : energy load to be met
    """
    sorted_powerplants = sort_by_merit_order(powerplants)
    total_generated = 0
    for powerplant in sorted_powerplants:
        remaining = load - total_generated
        produces = 0

        if remaining == 0:
            return to_output_format(powerplants)

        if remaining < powerplant.pmin:  
            # try to decrease the production of a previous powerplant by the diff and produce pmin
            decreased = decrease_previous_powerplant_production(powerplants, powerplant.pmin - remaining)
            if decreased != -1:  
                powerplant.produces = powerplant.pmin
                return to_output_format(powerplants)  # load met
            else:
                continue # if it didn't work, skip this powerplant
        
        # produce as much as possible
        produces = min(powerplant.pmax, remaining)
        total_generated += produces
        powerplant.produces = produces
    
    # logging.info("Problem not feasible: load can't be met.")
    logging.info("Solution not found")
    return to_output_format(powerplants)

def sort_by_merit_order(powerplants):
    """Sort powerplants by merit order"""
    # return sort_by_marginal_cost(powerplants)
    return sort_by_flac(powerplants)

def sort_by_flac(powerplants):
    """Sort powerplants by full load average cost."""
    return sorted(powerplants, key=lambda p: p.get_flac()) 

def sort_by_marginal_cost(powerplants):
    """Sort powerplants by marginal cost"""
    return sorted(powerplants, key=lambda p: p.get_marginal_cost()) 

def decrease_previous_powerplant_production(powerplant_list, amount):
    """Decrease production of an active powerplant with the biggest marginal cost (if its constraints allow it)."""
    for powerplant in reversed(powerplant_list):
        if powerplant.is_active() and powerplant.produces - amount > powerplant.pmin:
            powerplant.produces -= amount
            return amount
    return -1
    
def increase_next_powerplant_production(powerplants, remaining):
    pass

def to_output_format(powerplants):
    return [p.to_output_format() for p in powerplants]