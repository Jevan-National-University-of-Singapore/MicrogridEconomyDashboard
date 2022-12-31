import QtQuick
import QtQuick.Window
import QtQuick.Controls.Material
import Qt.labs.qmlmodels 1.0

import "../../../Templates"
import "YearDelegate"

Section {
    id: root

    section: "Five Year Analysis"

    width: Screen.width/1.2

    Row {
        id: yearSelection
        anchors.horizontalCenter: parent.horizontalCenter

        spacing: label.font.pixelSize/2

        // height: previous.height
        // width: previous.width + year.width + next.width

        Button {
            id: previous

            height: year.height; width: height

            // text: "‹"
            // font.pixelSize: root.label.font.pixelSize


            contentItem: Label {
                text: "‹"

                font.pixelSize: root.label.font.pixelSize

                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter

                bottomPadding: font.pixelSize/4

            }

        }

        Label {
            id: year

            text: qsTr("Year %1").arg(fiveYearsView.currentIndex)

            font.pixelSize: root.label.font.pixelSize

            height: implicitHeight; width: implicitWidth

            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter
        }

        Button {
            id: next

            width: previous.width; height: previous.height

            contentItem: Label {
                text: "›"

                font.pixelSize: root.label.font.pixelSize

                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter

                bottomPadding: font.pixelSize/4

            }
        }
    }


    ListView {
        id: fiveYearsView

        anchors{
            top: yearSelection.bottom
            topMargin: yearSelection.spacing
            
            horizontalCenter: parent.horizontalCenter
        }

        model: Scenario.technical.fiveYearsAnalysis.years

        orientation: ListView.Horizontal

        clip: true

        width: root.width - root.label.font.pixelSize
        height: 500//contentHeight


        delegate: YearDelegate{
            width: fiveYearsView.width            

            tables.spacing: root.label.font.pixelSize/2
        }

    }


}