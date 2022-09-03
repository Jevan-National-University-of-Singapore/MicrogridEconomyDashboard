from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Demand(QObject):
    numOfUsersPerDayChanged = Signal()
    numOfUsersPerYearChanged = Signal()

    stateOfChargeAtEntryChanged = Signal()
    stateOfChargeLimitChanged = Signal()
    stateOfChargeToBeChargedChanged = Signal()

    totalWaitingTimeChanged = Signal()
    actualUsersServedPerDayChanged = Signal()
    actualEnergyServedPerDayChanged = Signal()

    def __init__(self,
        # required
        state_of_charge_at_entry:float,
        state_of_charge_limit:float,

        # optional
        num_of_users_per_day:int = 0,

        total_waiting_time:float = 0,
        actual_users_served_per_day:int = 0,
        actual_energy_served_per_day:float = 0
    ):
        super().__init__()
        self._num_of_users_per_day = num_of_users_per_day
        self._num_of_users_per_year = num_of_users_per_day * 365

        self._state_of_charge_at_entry = state_of_charge_at_entry
        self._state_of_charge_limit = state_of_charge_limit
        self._state_of_charge_to_be_charged = state_of_charge_limit - state_of_charge_at_entry

        self._total_waiting_time = total_waiting_time
        self._actual_users_served_per_day = actual_users_served_per_day
        self._actual_energy_served_per_day = actual_energy_served_per_day

    @Property(str, notify=numOfUsersPerDayChanged) #getter
    def numOfUsersPerDay(self) -> str:
        return str(self._num_of_users_per_day)

    @numOfUsersPerDay.setter
    def numOfUsersPerDay(self, num_of_users_per_day:str):
        self._num_of_users_per_day = int(num_of_users_per_day)

    @Property(str, notify=numOfUsersPerYearChanged) #getter
    def numOfUsersPerYear(self) -> str:
        return str(self._num_of_users_per_year)

    @numOfUsersPerYear.setter
    def numOfUsersPerYear(self, num_of_users_per_year:str):
        self._num_of_users_per_year = int(num_of_users_per_year)
    
    @Property(str, notify=stateOfChargeAtEntryChanged) #getter
    def stateOfChargeAtEntry(self) -> str:
        return str(self._state_of_charge_at_entry)

    @stateOfChargeAtEntry.setter
    def stateOfChargeAtEntry(self, state_of_charge_at_entry:str):
        self._state_of_charge_at_entry = float(state_of_charge_at_entry)
    
    @Property(str, notify=stateOfChargeLimitChanged) #getter
    def stateOfChargeLimit(self) -> str:
        return str(self._state_of_charge_limit)

    @stateOfChargeLimit.setter
    def stateOfChargeLimit(self, state_of_charge_limit:str):
        self._state_of_charge_limit = float(state_of_charge_limit)
    
    @Property(str, notify=stateOfChargeToBeChargedChanged) #getter
    def stateOfChargeToBeCharged(self) -> str:
        return str(self._state_of_charge_to_be_charged)

    @stateOfChargeToBeCharged.setter
    def stateOfChargeToBeCharged(self, state_of_charge_to_be_charged:str):
        self._state_of_charge_to_be_charged = float(state_of_charge_to_be_charged)
    
    @Property(str, notify=totalWaitingTimeChanged) #getter
    def totalWaitingTime(self) -> str:
        return str(self._total_waiting_time)

    @totalWaitingTime.setter
    def totalWaitingTime(self, total_waiting_time:str):
        self._total_waiting_time = float(total_waiting_time)
    
    @Property(str, notify=actualUsersServedPerDayChanged) #getter
    def actualUsersServedPerDay(self) -> str:
        return str(self._actual_users_served_per_day)

    @actualUsersServedPerDay.setter
    def actualUsersServedPerDay(self, actual_users_served_per_day:str):
        self._actual_users_served_per_day = int(actual_users_served_per_day)
    
    @Property(str, notify=actualEnergyServedPerDayChanged) #getter
    def actualEnergyServedPerDay(self) -> str:
        return str(self._actual_energy_served_per_day)

    @actualEnergyServedPerDay.setter
    def actualEnergyServedPerDay(self, actual_energy_served_per_day:str):
        self._actual_energy_served_per_day = float(actual_energy_served_per_day)