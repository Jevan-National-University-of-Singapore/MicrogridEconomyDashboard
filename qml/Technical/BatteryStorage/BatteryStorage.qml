import "../../../Templates"
import "../../../Templates/Separators"
import "SubSections"


Section {
    id: root

    section: "Battery Storage"

    EssSystem {
        id: essSystem
    }

    VerticalSeparator {
        id: essSystemSeparator

        anchors {
            left: essSystem.right
            leftMargin: essSystem.label.font.pixelSize
            verticalCenter: essSystem.verticalCenter
        }

        length: essSystem.height - essSystem.label.font.pixelSize
    }


    Discharge {
        id: discharge

        anchors {
            left: essSystemSeparator.right
            leftMargin: discharge.label.font.pixelSize
        }
    }

    HorizontalSeparator {
        id: dischargeSeparator

        anchors {
            top: discharge.bottom
            topMargin: discharge.label.font.pixelSize

            horizontalCenter: discharge.horizontalCenter
        }

        length: discharge.width - discharge.label.font.pixelSize
    }

    GridCharging {
        id: gridCharging

        anchors {
            top: dischargeSeparator.bottom
            topMargin: gridCharging.label.font.pixelSize

            left: discharge.left
        }
    }

}