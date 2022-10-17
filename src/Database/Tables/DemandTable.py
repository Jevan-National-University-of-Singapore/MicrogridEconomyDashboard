from Table import Table
from functools import partialmethod
from ..Database import Database

class DemandTable(Table):
    name = "Demand"
    create_string = """ 
                        CREATE TABLE IF NOT EXISTS Demand (
                            scenario text PRIMARY KEY,
                            soc_at_entry real NOT NULL,
                            soc_limit real NOT NULL
                        ); 
                    """
    fields = {
        "scenario",
        "soc_at_entry",
        "soc_limit"
    }

    def __init__(self, database:Database):
        super().__init__(database)
        self.update_soc_at_entry = partialmethod(super().update_record, field_name = "soc_at_entry")
        self.update_soc_limit = partialmethod(super().update_record, field_name = "soc_limit")


'''
LEGACY
'''
        # self.soc_at_entry : Field = Field(
        #                                 name = "soc_at_entry",
        #                                 data_type = float
        #                             )

        # self.soc_limit : Field = Field(
        #                                 name = "soc_limit",
        #                                 data_type = float
        #                             )                                                                      
        # self.fields = {
        #     "scenario" : self.scenario,
        #     "soc_at_entry" : self.soc_at_entry,
        #     "soc_limit" : self.soc_limit
        # }