import QtQuick
import QtQuick.Controls.Material
import Qt.labs.qmlmodels 1.0

TableView {
    id: tableView

    clip: true

    model: TableModel {
        TableModelColumn {display: "header"} 
        TableModelColumn { display: "0" }                                   
        rows: [
            {
                "header" : "Initial Investment"
                // "0": "0"
            },
            {
                "header" : "Net Profits (Fair Value)"
            },
            {
                "header" : "Net Present Value"
            },
                        {
                "header" : "Internal Rate of Return (%)"
            }
        ]
    }

    delegate: Delegate{
        // row: row
        // column: column
    }
}

