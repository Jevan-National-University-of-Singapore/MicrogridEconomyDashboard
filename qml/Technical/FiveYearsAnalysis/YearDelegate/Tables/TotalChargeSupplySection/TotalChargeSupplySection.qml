import QtQuick
import QtQuick.Controls.Material
import Qt.labs.qmlmodels 1.0

import "Delegate"

TableView {
    id: tableView

    // implicitHeight: contentHeight
    // implicitWidth: parent.width - label.font.pixelSize
    clip: true

    model: TableModel {
        TableModelColumn {display: "header"} 
        TableModelColumn { display: "0" }
        TableModelColumn { display: "1" }
        TableModelColumn { display: "2" }
        TableModelColumn { display: "3" }
        TableModelColumn { display: "4" }
        TableModelColumn { display: "5" }
        TableModelColumn { display: "8" }
        TableModelColumn { display: "7" }
        TableModelColumn { display: "8" }
        TableModelColumn { display: "9" }
        TableModelColumn { display: "10" }
        TableModelColumn { display: "11" }          
        TableModelColumn { display: "12" }
        TableModelColumn { display: "13" }
        TableModelColumn { display: "14" }
        TableModelColumn { display: "15" }
        TableModelColumn { display: "16" }
        TableModelColumn { display: "17" }
        TableModelColumn { display: "18" }
        TableModelColumn { display: "19" }
        TableModelColumn { display: "20" }
        TableModelColumn { display: "21" }
        TableModelColumn { display: "22" }      
        TableModelColumn { display: "23" }                                       
        rows: [
            {
                "header" : "Solar Power Generation",
                "0": "00:00", "1": "01:00", "2": "02:00", "3": "03:00", "4": "04:00", "5": "05:00", "6": "06:00", "7": "07:00",
                "8": "08:00", "9": "09:00", "10": "10:00", "11": "11:00", "12": "12:00", "13": "13:00", "14": "14:00", "15": "15:00",
                "16": "16:00", "17": "17:00", "18": "18:00", "19": "19:00", "20": "20:00", "21": "21:00", "22": "22:00", "23": "23:00"
            },
            {
                "header" : "Grid Off-Peak"
            },
            {
                "header" : "Grid Peak"
            },
            {
                "header" : "Total Charge Supply"
            }

        ]
    }

    delegate: Delegate{
        // row: row
        // column: column
    }
}

