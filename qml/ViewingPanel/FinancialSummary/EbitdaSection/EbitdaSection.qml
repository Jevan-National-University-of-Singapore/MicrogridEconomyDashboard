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
                "header" : "Revenue",
                "0": "0"
            },
            {
                "header" : "    Chargers"
            },
            {
                "header" : "    Retail to Facility"
            },
            {
                "header" : "(-) Opex (2% escalation)"
            },
            {
                "header" : "EBITDA"
            }

        ]
    }

    delegate: Delegate{
        // row: row
        // column: column
    }
}

