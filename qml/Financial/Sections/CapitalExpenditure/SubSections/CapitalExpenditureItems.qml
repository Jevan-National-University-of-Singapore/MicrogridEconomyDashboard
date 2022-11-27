import QtQuick

import "../../../../Templates"

SubSection {
    id: root

    subsection: "Capital Expenditure Items"

    LabelledInput {
        id: solarPvRectification

        label: "Solar PV Rectification"
        units: "RM"

        input.onEditingFinished: Scenario.financial.capitalExpenditure.capitalExpenditureItems.solarPvRectification = solarPvRectification.inputText

        inputText: Scenario.financial.capitalExpenditure.capitalExpenditureItems.solarPvRectification
    }

    LabelledInput {
        id: dcChargers

        label: "DC Chargers"
        units: "RM"

        input.onEditingFinished: Scenario.financial.capitalExpenditure.capitalExpenditureItems.dcChargers = dcChargers.inputText

        inputText: Scenario.financial.capitalExpenditure.capitalExpenditureItems.dcChargers
    }

        LabelledInput {
        id: ess301kWh

        label: "301 kWh ESS"
        units: "RM"

        input.onEditingFinished: Scenario.financial.capitalExpenditure.capitalExpenditureItems.ess301kWh = ess301kWh.inputText

        inputText: Scenario.financial.capitalExpenditure.capitalExpenditureItems.ess301kWh
    }

    LabelledInput {
        id: pcs200kW

        label: "200 kW PCS"
        units: "RM"

        input.onEditingFinished: Scenario.financial.capitalExpenditure.capitalExpenditureItems.pcs200kW = pcs200kW.inputText

        inputText: Scenario.financial.capitalExpenditure.capitalExpenditureItems.pcs200kW
    }


    LabelledText {
        id: totalCapex

        labelText: "Total Capex"
        units: "RM"

        text: Scenario.financial.capitalExpenditure.capitalExpenditureItems.totalCapex
    }

}