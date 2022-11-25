import QtQuick
// import QtQuick.Layouts
import QtQuick.Controls.Material


Card {
    id: root

    default property alias data: subSections.data

    property alias section: sectionLabel.text

    Label {
        id: sectionLabel

        anchors {
            top: root.top
            topMargin: root.radius/2

            horizontalCenter: root.horizontalCenter
        }

        width: root.width/2
        verticalAlignment: Text.AlignVCenter

        text: ""
        color: "lightSteelBlue"
        font.pixelSize: 36
    }

    Item {
        id: subSections

        anchors {
            top: sectionLabel.bottom
            topMargin: sectionLabel.height/4

            bottom: root.bottom
            bottomMargin: root.radius/2

            horizontalCenter: root.horizontalCenter
        }

        width: root.width-(0.02*root.width)//root.radius
    }


    // ColumnLayout {
    //     id: column

    //     anchors.centerIn : root

    //     height: root.height - root.radius
    //     width: root.width - root.radius
        
    //     Label {
    //         id: sectionLabel

    //         text: ""

    //         verticalAlignment: Text.AlignVCenter

    //         font.pixelSize: 36
    //     }

    // }
}