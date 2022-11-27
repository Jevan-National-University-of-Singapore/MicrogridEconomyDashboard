from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .FiveYearLifetime import FiveYearLifetime
from .PerAnnum import PerAnnum
from .TariffAssumption import TariffAssumption

class Revenue(QObject):
    fiveYearLifetimeChanged = Signal()
    perAnnumChanged = Signal()
    tariffAssumptionChanged = Signal()

    def __init__(self,
        five_year_lifetime: FiveYearLifetime = FiveYearLifetime(),
        per_annum: PerAnnum = PerAnnum(),
        tariff_assumption: TariffAssumption = TariffAssumption()
    ):
        super().__init__()
        self.five_year_lifetime: FiveYearLifetime = five_year_lifetime
        self.per_annum: PerAnnum = per_annum
        self.tariff_assumption: TariffAssumption = tariff_assumption

        self.per_annum.charging_revenue_required = round(self.five_year_lifetime.required_from_chargers/6, 2)
        
        self.five_year_lifetime.requiredFromChargersChanged.connect(self.update_PerAnnum_ChargingRevenueRequired)

    def emitUpdateSignals(self):
        self.five_year_lifetime.emitUpdateSignals()
        self.per_annum.emitUpdateSignals()
        self.tariff_assumption.emitUpdateSignals()


    @Property(FiveYearLifetime, notify=fiveYearLifetimeChanged) #getter
    def fiveYearLifetime(self) -> FiveYearLifetime:
        return self.five_year_lifetime
        
    @Property(PerAnnum, notify=perAnnumChanged) #getter
    def perAnnum(self) -> PerAnnum:
        return self.per_annum

    @Property(TariffAssumption, notify=tariffAssumptionChanged) #getter
    def tariffAssumption(self) -> TariffAssumption:
        return self.tariff_assumption

    @Slot()
    def update_PerAnnum_ChargingRevenueRequired(self):
        self.per_annum.charging_revenue_required = round(self.five_year_lifetime.required_from_chargers/6, 2)
        self.per_annum.chargingRevenueRequiredChanged.emit()