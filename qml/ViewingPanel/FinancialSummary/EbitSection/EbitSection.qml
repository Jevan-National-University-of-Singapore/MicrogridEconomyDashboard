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
                "header" : "(-) Depreciation",
                "0": "0"
            },
            {
                "header" : "    Charger"
            },
            {
                "header" : "    ESS"
            },
            {
                "header" : "EBIT"
            }

        ]
    }

    delegate: Delegate{
        // row: row
        // column: column
    }
}

