import QtQuick.Layouts

import "../../../Templates"
import "../../../Templates/Separators"
import "SubSections"


Section {
    id: root

    section: "Charging and Demand"


    ColumnLayout {
        id: column1

        spacing: chargingPorts.label.font.pixelSize

        ChargingPorts {
            id: chargingPorts
        }

        HorizontalSeparator {
            id: chargingPortsSeparator

            Layout.alignment: Qt.AlignCenter

            length: chargingPorts.width - column1.spacing
        }

        Load {
            id: load
        }

        HorizontalSeparator {
            id: evCharacteristicsSeparator

            Layout.alignment: Qt.AlignCenter

            length: load.width - column1.spacing
        }

        ExcessToFacility {
            id: excessToFacility
        }

    }

    VerticalSeparator {
        id: column1Separator

        anchors {
            left: column1.right
            leftMargin: column1.spacing

            verticalCenter: column1.verticalCenter
        }

        length: column1.height - column1.spacing
    }

    ColumnLayout {
        id: column2

        spacing: column1.spacing

        anchors {
            left: column1Separator.right
            leftMargin: column1.spacing
        }

        Demand {
            id: demand
        }

        HorizontalSeparator {
            id: demandSeparator

            Layout.alignment: Qt.AlignCenter
            length: demand.width - column2.spacing
        }

        EvCharacteristics {
            id: evCharacteristics
        }

    }

}