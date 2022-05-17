class PowerPlantTypes: 
    WINDTURBINE = "windturbine"
    TURBOJET = "turbojet"
    GASFIRED = "gasfired"


class PowerPlantFactory: 
    @staticmethod
    def init_powerplant(p_name, payload_parser):
        """ Factory method for creation of Powerplants."""
        p_type = payload_parser.get_powerplant_type(p_name)
        if p_type == PowerPlantTypes.WINDTURBINE:
            return WindTurbine(p_name, payload_parser)
        elif p_type == PowerPlantTypes.TURBOJET:
            return Turbojet(p_name, payload_parser)
        elif p_type == PowerPlantTypes.GASFIRED:
            return GasFired(p_name, payload_parser)
        else:
            return PowerPlant(p_name, payload_parser)


class PowerPlant: 
    """Basic class representing a powerplant."""
    def __init__(self, p_name, payload_parser):
        self.name = p_name
        self.payload_parser = payload_parser
        self.efficiency, self.pmin, self.pmax = payload_parser.get_powerplant_specs(p_name)
        self.produces = 0

    def is_active(self):
        return self.produces != -1

    def get_marginal_cost(self):
        return self.get_fuel_cost()/self.efficiency 

    def get_fuel_cost(self):
        pass

    def can_produce(self):
        return self.pmax

    def to_output_format(self):
        return { 'name': self.name, 'p': "{:.1f}".format(self.produces) }


class WindTurbine(PowerPlant):
    def get_fuel_cost(self):
        return 0

    def can_produce(self):
        wind_percentage = self.payload_parser.get_wind_percentage()
        return self.pmax*wind_percentage/100.0


class Turbojet(PowerPlant):
    def get_fuel_cost(self):
        return self.payload_parser.get_kerosine_cost()


class GasFired(PowerPlant):
    def __init__(self, p_name, payload_parser):
        super().__init__(p_name, payload_parser)
        self.co2_ton_per_mwh = 0.3

    def get_fuel_cost(self):
        return self.payload_parser.get_gas_cost()
 
    def get_marginal_cost(self):
        return super().get_marginal_cost() + self.co2_ton_per_mwh*self.payload_parser.get_co2_cost()