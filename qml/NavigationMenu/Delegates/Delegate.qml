import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

Item{
    id: root

    property alias label: label
    property alias text: label.text
    property bool isExpanded: true

    implicitHeight: carot.implicitHeight
    implicitWidth: contentWidth

    signal subTreeExpand
    signal subTreeCollapse

    
    function collapse(){
        isExpanded = false
        collpasing.start()
    }

    ToolButton {
        id: carot

        implicitHeight: label.implicitHeight * 2
        implicitWidth: implicitHeight

        onClicked: {
            isExpanded ^= true
            if (isExpanded){
                root.subTreeExpand()
                expanding.start()
            } else {
                root.subTreeCollapse()
                collpasing.start()
            }
        }

        contentItem: Label {
            id: carotSymbol

            text: "›"

            font.pixelSize: 24

            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter

            bottomPadding: font.pixelSize/4

            RotationAnimator {
                id: expanding

                target: carotSymbol;
                from: 0;
                to: 90;
                duration: 150
            }

            RotationAnimator {
                id: collpasing
                target: carotSymbol;
                from: 90;
                to: 0;
                duration: 150
            }
        }


    }

    Label{
        id: label

        anchors{
            left: carot.right
            verticalCenter: carot.verticalCenter
        }

        text: ""
    }

}