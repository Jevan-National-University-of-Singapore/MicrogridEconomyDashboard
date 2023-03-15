from typing import Optional

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .RevenueItems import RevenueItems
from .Pricing import Pricing
from .TariffAssumption import TariffAssumption

class Revenue(QObject):
    revenueItemsChanged = Signal()
    pricingChanged = Signal()
    tariffAssumptionChanged = Signal()

    def __init__(self,
        revenue_items: Optional[RevenueItems] = None,
        pricing: Optional[Pricing] = None,
        tariff_assumption: Optional[TariffAssumption] = None
    ):
        super().__init__()
        self.revenue_items: RevenueItems = RevenueItems() if revenue_items is None else revenue_items
        self.pricing_: Pricing = Pricing() if pricing is None else pricing
        self.tariff_assumption: TariffAssumption = TariffAssumption() if tariff_assumption is None else tariff_assumption

    def emitUpdateSignals(self):
        self.revenue_items.emitUpdateSignals()
        self.pricing_.emitUpdateSignals()
        self.tariff_assumption.emitUpdateSignals()


    @Property(RevenueItems, notify=revenueItemsChanged) #getter
    def revenueItems(self) -> RevenueItems:
        return self.revenue_items
        
    @Property(Pricing, notify=pricingChanged) #getter
    def pricing(self) -> Pricing:
        return self.pricing_

    @Property(TariffAssumption, notify=tariffAssumptionChanged) #getter
    def tariffAssumption(self) -> TariffAssumption:
        return self.tariff_assumption