import QtQuick
import "../../Templates" as Templates


Templates.Page{
    id: root

    Templates.SubSection {
        id: subsectionItems

        subsection: "Capital Expenditure Items"

        Templates.LabelledInput {
            id: solarPvRectification

            label: "Solar PV Rectification"
            units: "RM"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.solarPvRectification = solarPvRectification.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.solarPvRectification
        }

        Templates.LabelledInput {
            id: dcChargers

            label: "DC Chargers"
            units: "RM"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.dcChargers = dcChargers.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.dcChargers
        }

        Templates.LabelledInput {
            id: ess301kWh

            label: "301 kWh ESS"
            units: "RM"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.ess301kWh = ess301kWh.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.ess301kWh
        }

        Templates.LabelledInput {
            id: pcs200kW

            label: "200 kW PCS"
            units: "RM"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.pcs200kW = pcs200kW.inputText

            inputText: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.pcs200kW
        }


        Templates.LabelledText {
            id: totalCapex

            labelText: "Total Capex"
            units: "RM"

            text: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.capitalExpenditureItems.totalCapex
        }

    }
}