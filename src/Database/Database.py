import os

import sqlite3
from sqlite3 import Error

from functools import partialmethod
from typing import Iterable

from Database.Tables.EssSystemTable import EssSystemTable
from Database.Tables.GridChargingTable import GridChargingTable
from Database.Tables.ChargingPortsTable import ChargingPortsTable
from Database.Tables.DemandTable import DemandTable
from Database.Tables.ExcessToFacilityTable import ExcessToFacilityTable
from Database.Tables.EvCharacteristicsTable import EvCharacteristicsTable

'''
[EssSystem]
[GridCharging]
[ChargingPorts]
[Demand]
[ExcessToFacility]
[EvCharacteristics]
'''
class Database:
    def __init__(self, path:str):
        self.path = path
        self.ess_system_table = EssSystemTable()
        self.grid_charging_table = GridChargingTable()
        self.charging_ports_table = ChargingPortsTable()
        self.demand_table = DemandTable()
        self.excess_to_facility_table = ExcessToFacilityTable()
        self.ev_characteristics_table = EvCharacteristicsTable()

        self.tables = {
            "ess_system": self.ess_system_table,
            "grid_charging_table": self.grid_charging_table,
            "charging_ports_table" : self.charging_ports_table,
            "demand_table" : self.demand_table,
            "excess_to_facility_table" : self.excess_to_facility_table,
            "ev_characteristics_table" : self.ev_characteristics_table
        }

        for table in self.tables.items():
            table.create = partialmethod(self._create_table, table.create_message)
            table.create()

    @classmethod
    def exists(cls, path):
        return os.path.exists(path)

    def query(self, query_string:str , query_arguments: Iterable):
        try:
            with self._connect() as connection:
                cursor = connection.cursor()
                cursor.execute(query_string, query_arguments)
                connection.commit()
        except Error as e:
            print(e)

    def create_table(self, query_string:str):
        try:
            with sqlite3.connect(self.path) as connection:
                cursor = connection.cursor()
                cursor.execute(query_string)
        except Error as e:
            print(e)



    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path)



'''
LEGACY
'''

    # def update(self, query_string: str, query_arguments: Iterable):
    #     return self.query

    # def insert(self, query_string: str, query_arguments: Iterable):
    #     return self.query()