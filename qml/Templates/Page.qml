import QtQuick
import QtQuick.Controls.Material

ScrollView {
    id: root

    wheelEnabled: scrim.opacity == 0

    contentHeight: page.height + root.bottomMargin
    contentWidth: page.width

    property real bottomMargin: 0

    signal outsideDialogAreaClicked

    default property alias defaultData: page.data

    Item {
        id: page

        height: childrenRect.height
        width: childrenRect.width
    }

    Rectangle {
        id: scrim

        height: Math.max(root.height,root.contentHeight)
        width: Math.max(root.width, root.contentWidth)

        z: page.z + 1
        color: "black"

        opacity: 0

        Behavior on opacity { SmoothedAnimation { velocity: 2.5 } }

        MouseArea {
            anchors.fill: parent

            enabled: scrim.opacity
            onClicked: {
                root.outsideDialogAreaClicked()
                closeDialog()
            }
        }
    }

    function openDialog(){
        scrim.opacity = 0.5
    }

    function closeDialog(){
        scrim.opacity = 0
    }

}