import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Fixed O&M"

    LabelledInput {
        id: solarPvOAndM

        label: "Solar PV O&M"
        units: "USD/kW/year"

        input.onEditingFinished: Scenario.financial.operatingExpenditure.fixedOAndM.solarPvOAndM = solarPvOAndM.inputText

        inputText: Scenario.financial.operatingExpenditure.fixedOAndM.solarPvOAndM
    }

    LabelledInput {
        id: evChargerOAndM

        label: "EV Charger O&M"
        units: "USD/charger/year"

        input.onEditingFinished: Scenario.financial.operatingExpenditure.fixedOAndM.evChargerOAndM = evChargerOAndM.inputText

        inputText: Scenario.financial.operatingExpenditure.fixedOAndM.evChargerOAndM
    }


    LabelledInput {
        id: lfpAndM

        label: "LFP O&M"
        units: "USD/kW/year"

        input.onEditingFinished: Scenario.financial.operatingExpenditure.fixedOAndM.lfpAndM = lfpAndM.inputText

        inputText: Scenario.financial.operatingExpenditure.fixedOAndM.lfpAndM
    }




}