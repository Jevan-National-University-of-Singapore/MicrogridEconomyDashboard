import QtQuick
import QtQuick.Controls.Material
import Qt.labs.qmlmodels 1.0

import "../../../Templates"
import "../../../Templates/Separators"

// import "SubSections"


Section {
    id: root

    section: "Hourly Solar Generation"

    width: 1500
    height: 400

    TableView {
        height: root.height
        width: root.width
        clip: true

        model: TableModel {
            TableModelColumn { display: "0" }
            TableModelColumn { display: "1" }
            TableModelColumn { display: "2" }
            TableModelColumn { display: "3" }
            TableModelColumn { display: "4" }
            TableModelColumn { display: "5" }
            TableModelColumn { display: "6" }
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
                    "0": "00:00", "1": "01:00", "2": "02:00", "3": "03:00", "4": "04:00", "5": "05:00", "6": "06:00", "7": "07:00",
                    "8": "08:00", "9": "09:00", "10": "10:00", "11": "11:00", "12": "12:00", "13": "13:00", "14": "14:00", "15": "15:00",
                    "16": "16:00", "17": "17:00", "18": "18:00", "19": "19:00", "20": "20:00", "21": "21:00", "22": "22:00", "23": "23:00"
                },
                {

                },
                {

                },
                {

                }

            ]
        }

        delegate: Frame {
            id: delegate

            implicitWidth: font.pixelSize * 5
            implicitHeight: row === 1 ? inputDelegate.height : readOnlyDelegate.height

            Label {
                id: readOnlyDelegate

                visible: row !== 1

                width: delegate.width; height: implicitHeight * 1.2
                anchors.centerIn: parent

                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter

                text: row === 0? display :  
                    row === 2?  
                    Scenario.solarPowerGeneration.percentageOfDailyKwh[column] :
                    Scenario.solarPowerGeneration.estimatedKwhGenerated[column]
            }


            TextField {
                id: inputDelegate

                visible: row === 1

                width: readOnlyDelegate.font.pixelSize * 4; height: implicitHeight
                anchors.centerIn: parent

                text: Scenario.solarPowerGeneration.percentageOfMaxKw[column]
            }
        }
    }
    

}