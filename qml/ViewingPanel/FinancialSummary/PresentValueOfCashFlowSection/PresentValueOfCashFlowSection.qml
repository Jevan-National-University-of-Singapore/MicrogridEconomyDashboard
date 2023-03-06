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
                "header" : "Discounted Cash Flows"
                // "0": "0"
            },
            {
                "header" : "Present Value of Cash Flow"
            }
        ]
    }

    delegate: Delegate{
        // row: row
        // column: column
    }
}

