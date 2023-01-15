import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Tariff Assumption"

    LabelledInput {
        id: electricityTariffRate

        label: "Electricity tariff rate"
        units: "RM/kWh"

        input.onEditingFinished: Scenario.financial.revenue.tariffAssumption.electricityTariffRate = electricityTariffRate.inputText

        inputText: Scenario.financial.revenue.tariffAssumption.electricityTariffRate
    }

    LabelledInput {
        id: marginOnElectricitySoldToFacility

        label: "Margin on electricity sold to fa"
        units: "%"

        input.onEditingFinished: Scenario.financial.revenue.tariffAssumption.marginOnElectricitySoldToFacility = marginOnElectricitySoldToFacility.inputText

        inputText: Scenario.financial.revenue.tariffAssumption.marginOnElectricitySoldToFacility
    }


    LabelledInput {
        id: peakTariffRate

        label: "Peak tariff rate"

        input.onEditingFinished: Scenario.financial.revenue.tariffAssumption.peakTariffRate = peakTariffRate.inputText

        inputText: Scenario.financial.revenue.tariffAssumption.peakTariffRate
    }

    LabelledInput {
        id: offPeakTariffRate

        label: "Off-peak tariff rate"

        input.onEditingFinished: Scenario.financial.revenue.tariffAssumption.offPeakTariffRate = offPeakTariffRate.inputText

        inputText: Scenario.financial.revenue.tariffAssumption.offPeakTariffRate
    }

}
