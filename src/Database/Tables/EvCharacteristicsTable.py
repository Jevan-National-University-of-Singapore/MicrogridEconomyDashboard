from functools import partialmethod

from Table import Table
from ..Database import Database
'''
ev_battery_voltage
capacity
'''
class EvCharacteristicsTable(Table):
    name = "EvCharacteristics"
    create_string = """ 
                        CREATE TABLE IF NOT EXISTS EvCharacteristics (
                            scenario text PRIMARY KEY,
                            ev_battery_voltage real NOT NULL,
                            capacity real NOT NULL
                        ); 
                    """
    fields = {
        "scenario",
        "ev_battery_voltage",
        "capacity"
    }

    def __init__(self, database: Database):
        super().__init__(database)
        self.update_ev_battery_voltage = partialmethod(super().update_record, field_name = "ev_battery_voltage")
        self.update_capacity = partialmethod(super().update_record, field_name = "capacity")



'''
LEGACY
'''
        # self.ev_battery_voltage : Field = Field(
        #                                 name = "ev_battery_voltage",
        #                                 data_type = float
        #                             )

        # self.capacity : Field = Field(
        #                         name = "capacity",
        #                         data_type = float
        #                     )
                                                                 
        # self.fields = {
        #     "scenario" : self.scenario,
        #     "ev_battery_voltage" : self.ev_battery_voltage,
        #     "capacity" : self.capacity
        # }