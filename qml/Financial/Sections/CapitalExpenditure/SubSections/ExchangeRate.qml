import QtQuick
import "../../../../Templates"


SubSection {
    id: root

    subsection: "Exchange Rate"

    LabelledInput {
        id: rmPerUsd

        label: "RM/USD"
        units: "RM"

        input.onEditingFinished: Scenario.financial.capitalExpenditure.exchangeRate.rmPerUsd = rmPerUsd.inputText

        inputText: Scenario.financial.capitalExpenditure.exchangeRate.rmPerUsd
    }

}