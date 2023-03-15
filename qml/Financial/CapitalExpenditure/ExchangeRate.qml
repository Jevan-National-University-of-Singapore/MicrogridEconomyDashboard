import QtQuick
import "../../Templates" as Templates

Templates.Page{
    id: root
    
    Templates.SubSection {
        id: subsectionItems

        subsection: "Exchange Rate"

        Templates.LabelledInput {
            id: rmPerUsd

            label: "RM/USD"
            units: "RM"

            input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.exchangeRate.rmPerUsd = parseFloat(rmPerUsd.inputText)

            inputText: Scenario.years[Scenario.currentYearIndex].financial.capitalExpenditure.exchangeRate.rmPerUsd.toFixed(2)
        }

    }
}