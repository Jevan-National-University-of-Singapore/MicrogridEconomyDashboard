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

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.electricityTariffRate = parseFloat(electricityTariffRate.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.electricityTariffRate.toFixed(2)
        }

        Templates.LabelledInput {
            id: marginOnElectricitySoldToFacility

            label: "Margin on electricity sold to facility"
            units: "%"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.marginOnElectricitySoldToFacility = parseFloat(marginOnElectricitySoldToFacility.inputText)/100

            inputText: (Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.marginOnElectricitySoldToFacility*100).toFixed(2)
        }


        Templates.LabelledInput {
            id: peakTariffRate

            label: "Peak tariff rate"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.peakTariffRate = parseFloat(peakTariffRate.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.peakTariffRate.toFixed(2)
        }

        Templates.LabelledInput {
            id: offPeakTariffRate

            label: "Off-peak tariff rate"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.offPeakTariffRate = parseFloat(offPeakTariffRate.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].financial.revenue.tariffAssumption.offPeakTariffRate.toFixed(2)
        }

    }
}