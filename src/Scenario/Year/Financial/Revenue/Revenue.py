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
        five_year_lifetime: FiveYearLifetime|None = None,
        per_annum: PerAnnum|None = None,
        tariff_assumption: TariffAssumption|None = None
    ):
        super().__init__()
        self.five_year_lifetime: FiveYearLifetime = FiveYearLifetime() if five_year_lifetime is None else five_year_lifetime
        self.per_annum: PerAnnum = PerAnnum() if per_annum is None else per_annum
        self.tariff_assumption: TariffAssumption = TariffAssumption() if tariff_assumption is None else tariff_assumption

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