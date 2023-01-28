from functools import partialmethod

from Table import Table
from ..Database import Database

class GridChargingTable(Table):
    name = "GridCharging"
    create_string = """ 
                        CREATE TABLE IF NOT EXISTS GridCharging (
                            scenario text PRIMARY KEY,
                            grid_draw_limit real NOT NULL
                        ); 
                    """
    fields = {
        "scenario",
        "grid_draw_limit",
    }

    def __init__(self, database: Database):
        super().__init__(database)
        self.update_grid_draw_limit = partialmethod(super().update_record, field_name = "grid_draw_limit")


'''
LEGACY
'''
        # self.grid_draw_limit : Field = Field(
        #                                 name = "grid_draw_limit",
        #                                 data_type = float
        #                             )

        # self.fields = {
        #     "scenario" : self.scenario,
        #     "grid_draw_limit" : self.grid_draw_limit
        # }
