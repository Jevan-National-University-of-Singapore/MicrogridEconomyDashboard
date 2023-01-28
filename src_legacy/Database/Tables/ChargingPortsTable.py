from Table import Table
from functools import partialmethod
from ..Database import Database

class ChargingPortsTable(Table):
    name = "ChargingPorts"
    create_string = """ 
                        CREATE TABLE IF NOT EXISTS ChargingPorts (
                            scenario text PRIMARY KEY,
                            dc_Charger_1_rating real NOT NULL,
                            num_of_dc_charger_1 integer NOT NULL,
                            dc_Charger_2_rating real NOT NULL,
                            num_of_dc_charger_2 integer NOT NULL
                        ); 
                    """
    fields = {
        "scenario",
        "dc_charger_1_rating",
        "num_of_dc_charger_1",
        "dc_charger_2_rating",
        "num_of_dc_charger_2"
    }

    def __init__(self, database: Database):
        super().__init__(database)
        self.update_dc_charger_1_rating = partialmethod(super().update_record, field_name = "dc_charger_1_rating")
        self.update_num_of_dc_charger_1 = partialmethod(super().update_record, field_name = "num_of_dc_charger_1")
        self.update_dc_charger_2_rating = partialmethod(super().update_record, field_name = "dc_charger_2_rating")
        self.update_num_of_dc_charger_2 = partialmethod(super().update_record, field_name = "num_of_dc_charger_2")
        

'''
LEGACY
'''
        # self.dc_Charger_1_rating : Field = Field(
        #                                 name = "dc_Charger_1_rating",
        #                                 data_type = float
        #                             )

        # self.num_of_dc_charger_1 : Field = Field(
        #                                 name = "num_of_dc_charger_1",
        #                                 data_type = int
        #                             )

        # self.dc_Charger_2_rating : Field = Field(
        #                                 name = "dc_Charger_2_rating",
        #                                 data_type = float
        #                             )

        # self.num_of_dc_charger_2 : Field = Field(
        #                                 name = "num_of_dc_charger_2",
        #                                 data_type = int
        #                             )                                                                        
        # self.fields = {
        #     "scenario" : self.scenario,
        #     "dc_Charger_1_rating" : self.dc_Charger_1_rating,
        #     "num_of_dc_charger_1" : self.num_of_dc_charger_1,
        #     "dc_Charger_2_rating" : self.dc_Charger_2_rating,
        #     "num_of_dc_charger_2" : self.num_of_dc_charger_2
        # }