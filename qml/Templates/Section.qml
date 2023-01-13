import QtQuick
import QtQuick.Controls.Material


Card {
    id: root

    default property alias defaultData: subSections.data
    
    height: sectionLabel.height + sectionLabel.anchors.topMargin 
            + subSections.anchors.topMargin + subSections.height 
            + root.radius/2
            
    width: Math.max(sectionLabel.width, subSections.width) + radius

    property alias section: sectionLabel.text
    property alias label: sectionLabel

    Label {
        id: sectionLabel

        anchors {
            top: root.top
            topMargin: root.radius/2

            horizontalCenter: root.horizontalCenter
        }

        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter

        text: ""
        color: "lightSteelBlue"
        font.pixelSize: 36
    }

    Item {
        id: subSections

        anchors {
            top: sectionLabel.bottom
            topMargin: sectionLabel.font.pixelSize/2

            horizontalCenter: sectionLabel.horizontalCenter
        }

        width: childrenRect.width
        height: childrenRect.height

    }
}
