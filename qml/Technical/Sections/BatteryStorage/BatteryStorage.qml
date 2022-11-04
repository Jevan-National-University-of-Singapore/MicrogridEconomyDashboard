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
            leftMargin: essSystem.width/5
            verticalCenter: essSystem.verticalCenter
        }

        length: essSystem.height/1.2
    }


    Discharge {
        id: discharge

        anchors {
            left: essSystemSeparator.right
            leftMargin: discharge.width/8
        }
    }

    HorizontalSeparator {
        id: dischargeSeparator

        anchors {
            top: discharge.bottom
            topMargin: discharge.height/5
            horizontalCenter: discharge.horizontalCenter
        }

        length: discharge.width/1.2
    }

    GridCharging {
        id: gridCharging

        anchors {
            top: dischargeSeparator.bottom
            topMargin: gridCharging.height/8

            left: discharge.left
        }
    }

}