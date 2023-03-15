import QtQuick
import "../../Templates" as Templates


Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Capital Expenditure Items"

        Templates.LongLabelledInput {
            id: solarPvRectification

            label: "Solar PV Rectification"
            units: "RM"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.solarPvRectification = parseFloat(solarPvRectification.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.solarPvRectification.toFixed(2)
        }

        Templates.LongLabelledInput {
            id: dcChargers

            label: "DC Chargers"
            units: "RM"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.dcChargers = parseFloat(dcChargers.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.dcChargers.toFixed(2)
        }

        Templates.LongLabelledInput {
            id: ess301kWh

            label: "301 kWh ESS"
            units: "RM"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.ess301kWh = parseFloat(ess301kWh.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.ess301kWh.toFixed(2)
        }

        Templates.LongLabelledInput {
            id: pcs200kW

            label: "200 kW PCS"
            units: "RM"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.pcs200kW = parseFloat(pcs200kW.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.pcs200kW.toFixed(2)
        }


        Templates.LabelledText {
            id: totalCapex

            labelText: "Total Capex"
            units: "RM"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.totalCapex.toFixed(2)
        }

    }
}