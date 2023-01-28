from functools import partialmethod

from Table import Table
from ..Database import Database

class ExcessToFacilityTable(Table):
    name = "ExcessToFacility"
    create_string = """ 
                        CREATE TABLE IF NOT EXISTS ExcessToFacility (
                            scenario text PRIMARY KEY,
                            electricity_per_day real NOT NULL
                        ); 
                    """
    fields = {
        "scenario",
        "electricity_per_day",
    }

    def __init__(self, database: Database):
        super().__init__(database)
        self.update_electricity_per_day = partialmethod(super().update_record, field_name = "electricity_per_day")

'''
LEGACY
'''
        # self.electricity_per_day : Field = Field(
        #                                 name = "electricity_per_day",
        #                                 data_type = float
        #                             )
                                                                 
        # self.fields = {
        #     "scenario" : self.scenario,
        #     "electricity_per_day" : self.electricity_per_day
        # }