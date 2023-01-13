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

    
    @Property(str, notify=electricityTariffRateChanged) #getter
    def electricityTariffRate(self) -> str:
        return str(self.electricity_tariff_rate)

    @electricityTariffRate.setter
    def electricityTariffRate(self, electricity_tariff_rate:str) -> None:
        self.electricity_tariff_rate = round(float(electricity_tariff_rate), 2)
        self.electricityTariffRateChanged.emit()



    @Property(str, notify=marginOnElectricitySoldToFacilityChanged) #getter
    def marginOnElectricitySoldToFacility(self) -> str:
        return str(round(self.margin_on_electricity_sold_to_facility*100, 2))

    @marginOnElectricitySoldToFacility.setter
    def marginOnElectricitySoldToFacility(self, margin_on_electricity_sold_to_facility:str) -> None:
        self.margin_on_electricity_sold_to_facility = round(float(margin_on_electricity_sold_to_facility)/100, 4)
        self.marginOnElectricitySoldToFacilityChanged.emit()



    @Property(str, notify=peakTariffRateChanged) #getter
    def peakTariffRate(self) -> str:
        return str(self.peak_tariff_rate)

    @peakTariffRate.setter
    def peakTariffRate(self, peak_tariff_rate:str) -> None:
        self.peak_tariff_rate = round(float(peak_tariff_rate), 2)
        self.peakTariffRateChanged.emit()



    @Property(str, notify=offPeakTariffRateChanged) #getter
    def offPeakTariffRate(self) -> str:
        return str(self.off_peak_tariff_rate)

    @offPeakTariffRate.setter
    def offPeakTariffRate(self, off_peak_tariff_rate:str) -> None:
        self.off_peak_tariff_rate = round(float(off_peak_tariff_rate), 2)
        self.offPeakTariffRateChanged.emit()

