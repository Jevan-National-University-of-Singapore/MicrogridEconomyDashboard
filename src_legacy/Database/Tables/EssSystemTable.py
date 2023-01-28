from functools import partialmethod

from Table import Table
from ..Database import Database

class EssSystemTable(Table):
    name = "EssSystem"
    create_string = """ 
                        CREATE TABLE IF NOT EXISTS EssSystem (
                            scenario text PRIMARY KEY,
                            installed_capacity real NOT NULL,
                            soc_upper_limit real NOT NULL,
                            soc_lower_limit real NOT NULL,
                            eol_capacity real NOT NULL,
                            ess_nameplate_lifecycle real NOT NULL
                        ); 
                    """
    fields = {
        "scenario",
        "installed_capacity",
        "operational_Time",
        "soc_upper_limit",
        "soc_lower_limit",
        "eol_capacity",
        "ess_nameplate_lifecycle"
    }

    def __init__(self, database: Database):
        super().__init__(database)
        self.update_installed_capacity = partialmethod(super().update_record, field_name = "installed_capacity")
        self.update_operational_Time = partialmethod(super().update_record, field_name = "operational_Time")
        self.update_soc_upper_limit = partialmethod(super().update_record, field_name = "soc_upper_limit")
        self.update_soc_lower_limit = partialmethod(super().update_record, field_name = "soc_lower_limit")
        self.update_eol_capacity = partialmethod(super().update_record, field_name = "eol_capacity")
        self.update_ess_nameplate_lifecycle = partialmethod(super().update_record, field_name = "ess_nameplate_lifecycle")



        '''
        LEGACY
        '''
        # self.installed_capacity : Field = Field(
        #                                         name = "installed_capacity",
        #                                         data_type = float
        #                                     )

        # self.operational_Time : Field = Field(
        #                                     name = "operational_Time",
        #                                     data_type = float
        #                                 )

        # self.soc_upper_limit : Field = Field(
        #                                     name = "soc_upper_limit",
        #                                     data_type = float
        #                                 )

        # self.soc_lower_limit : Field = Field(
        #                                     name = "soc_lower_limit",
        #                                     data_type = float
        #                                 )

        # self.eol_capacity : Field = Field(
        #                                     name = "eol_capacity",
        #                                     data_type = float
        #                                 )


        # self.ess_nameplate_lifecycle : Field = Field(
        #                                     name = "ess_nameplate_lifecycle",
        #                                     data_type = float
        #                                 )

        # self.fields = {
        #     "scenario" : self.scenario,
        #     "installed_capacity" : self.installed_capacity,
        #     "operational_Time" : self.operational_Time,
        #     "soc_upper_limit" : self.soc_upper_limit,
        #     "soc_lower_limit" : self.soc_lower_limit,
        #     "eol_capacity" : self.eol_capacity,
        #     "ess_nameplate_lifecycle" : self.ess_nameplate_lifecycle
        # }