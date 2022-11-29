import QtQuick
import QtQuick.Controls.Material

import "Sections/SolarPowerGeneration"
// import "Sections/OperatingExpenditure"
// import "Sections/Revenue"

Item {
    id: root


    SolarPowerGeneration{
        id: solarPowerGeneration

        anchors {
            top: root.top
            topMargin: root.height/40

            left: root.left
            leftMargin: root.width/40
        }

    }

    // OperatingExpenditure {
    //     id: operatingExpenditure

    //     anchors {
    //         top: root.top
    //         topMargin: root.height/40

    //         left: capitalExpenditure.right
    //         leftMargin: root.width/40
    //     }

    //     width: root.width/2.5
    //     height: root.height/2.5
    // }


}