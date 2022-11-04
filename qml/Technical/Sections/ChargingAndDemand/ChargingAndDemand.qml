import QtQuick.Layouts

import "../../../Templates"
import "../../../Templates/Separators"
import "SubSections"


Section {
    id: root

    section: "Charging and Demand"


    ColumnLayout {
        id: column1

        spacing: root.height/40

        ChargingPorts {
            id: chargingPorts
        }
        HorizontalSeparator {
            id: chargingPortsSeparator

            Layout.alignment: Qt.AlignCenter
            Layout.preferredWidth: 200
        }

        Load {
            id: load
        }

        HorizontalSeparator {
            id: evCharacteristicsSeparator

            Layout.alignment: Qt.AlignCenter
            Layout.preferredWidth: 200
        }

        ExcessToFacility {
            id: excessToFacility
        }

    }

    VerticalSeparator {
        id: column1Separator

        anchors {
            left: column1.right
            leftMargin: column1.width/20

            verticalCenter: column1.verticalCenter
        }

        length: column1.height/1.2
    }

    ColumnLayout {
        id: column2

        spacing: root.height/40

        anchors {
            left: column1Separator.right
            leftMargin: column1.width/20
        }

        Demand {
            id: demand
        }

        HorizontalSeparator {
            id: demandSeparator

            Layout.alignment: Qt.AlignCenter
            Layout.preferredWidth: 200
        }

        EvCharacteristics {
            id: evCharacteristics
        }

    }

}