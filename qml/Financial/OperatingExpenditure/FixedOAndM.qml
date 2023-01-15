import QtQuick
import "../../Templates" as Templates


Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Fixed O&M"

        Templates.LabelledInput {
            id: solarPvOAndM

            label: "Solar PV O&M"
            units: "USD/kW/year"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.operatingExpenditure.fixedOAndM.solarPvOAndM = solarPvOAndM.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].financial.operatingExpenditure.fixedOAndM.solarPvOAndM
        }

        Templates.LabelledInput {
            id: evChargerOAndM

            label: "EV Charger O&M"
            units: "USD/charger/year"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.operatingExpenditure.fixedOAndM.evChargerOAndM = evChargerOAndM.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].financial.operatingExpenditure.fixedOAndM.evChargerOAndM
        }


        Templates.LabelledInput {
            id: lfpAndM

            label: "LFP O&M"
            units: "USD/kW/year"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.operatingExpenditure.fixedOAndM.lfpAndM = lfpAndM.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].financial.operatingExpenditure.fixedOAndM.lfpAndM
        }

    }
}