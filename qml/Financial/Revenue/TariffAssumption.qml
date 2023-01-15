import QtQuick
import "../../Templates" as Templates


Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Tariff Assumption"

        Templates.LabelledInput {
            id: electricityTariffRate

            label: "Electricity tariff rate"
            units: "RM/kWh"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.electricityTariffRate = electricityTariffRate.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.electricityTariffRate
        }

        Templates.LabelledInput {
            id: marginOnElectricitySoldToFacility

            label: "Margin on electricity sold to fa"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.marginOnElectricitySoldToFacility = marginOnElectricitySoldToFacility.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.marginOnElectricitySoldToFacility
        }


        Templates.LabelledInput {
            id: peakTariffRate

            label: "Peak tariff rate"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.peakTariffRate = peakTariffRate.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.peakTariffRate
        }

        Templates.LabelledInput {
            id: offPeakTariffRate

            label: "Off-peak tariff rate"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.offPeakTariffRate = offPeakTariffRate.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.offPeakTariffRate
        }

    }
}