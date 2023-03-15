from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class TariffAssumption(QObject):
    '''
    Electricity tariff rate
    Margin on electricity sold to facility
    Peak tariff rate
    Off-peak tariff rate
    '''
    electricityTariffRateChanged = Signal()
    marginOnElectricitySoldToFacilityChanged = Signal()
    peakTariffRateChanged = Signal()
    offPeakTariffRateChanged = Signal()

    def __init__(self,

        electricity_tariff_rate: float = 0.53,
        margin_on_electricity_sold_to_facility: float = 0.8,
        peak_tariff_rate: float = 0.58,
        off_peak_tariff_rate: float = 0.28,
    ):
        super().__init__()
        self.electricity_tariff_rate:float = electricity_tariff_rate
        self.margin_on_electricity_sold_to_facility:float = margin_on_electricity_sold_to_facility
        self.peak_tariff_rate:float = peak_tariff_rate
        self.off_peak_tariff_rate:float = off_peak_tariff_rate

    def emitUpdateSignals(self):
        self.electricityTariffRateChanged.emit()
        self.marginOnElectricitySoldToFacilityChanged.emit()
        self.peakTariffRateChanged.emit()
        self.offPeakTariffRateChanged.emit()

    
    @Property(float, notify=electricityTariffRateChanged) #getter
    def electricityTariffRate(self) -> float:
        return self.electricity_tariff_rate

    @electricityTariffRate.setter
    def electricityTariffRate(self, electricity_tariff_rate:float) -> None:
        if self.electricity_tariff_rate != electricity_tariff_rate:
            self.electricity_tariff_rate = electricity_tariff_rate
            self.electricityTariffRateChanged.emit()



    @Property(float, notify=marginOnElectricitySoldToFacilityChanged) #getter
    def marginOnElectricitySoldToFacility(self) -> float:
        return self.margin_on_electricity_sold_to_facility

    @marginOnElectricitySoldToFacility.setter
    def marginOnElectricitySoldToFacility(self, margin_on_electricity_sold_to_facility:str) -> None:
        if self.margin_on_electricity_sold_to_facility != margin_on_electricity_sold_to_facility:
            self.margin_on_electricity_sold_to_facility = margin_on_electricity_sold_to_facility
            self.marginOnElectricitySoldToFacilityChanged.emit()



    @Property(float, notify=peakTariffRateChanged) #getter
    def peakTariffRate(self) -> float:
        return self.peak_tariff_rate

    @peakTariffRate.setter
    def peakTariffRate(self, peak_tariff_rate:float) -> None:
        if self.peak_tariff_rate != peak_tariff_rate:
            self.peak_tariff_rate = peak_tariff_rate
            self.peakTariffRateChanged.emit()



    @Property(float, notify=offPeakTariffRateChanged) #getter
    def offPeakTariffRate(self) -> float:
        return self.off_peak_tariff_rate

    @offPeakTariffRate.setter
    def offPeakTariffRate(self, off_peak_tariff_rate:float) -> None:
        if self.off_peak_tariff_rate != off_peak_tariff_rate:
            self.off_peak_tariff_rate = off_peak_tariff_rate
            self.offPeakTariffRateChanged.emit()

