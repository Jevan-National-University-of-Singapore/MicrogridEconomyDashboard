import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls.Material 2.12
import QtQuick.Controls.Material.impl 2.12

Rectangle {
    id: root

    color: Material.background

    property bool draggable: true
        
    Material.elevation: 6

    radius: 5// Math.max(root.height, root.width)/20

    layer.enabled: root.enabled && root.Material.elevation > 0
    layer.effect: ElevationEffect {
        elevation: root.Material.elevation
    }

    MouseArea {
        id: dragArea
        property var overlay: root.parent

        anchors.fill: root

        onPressed: {
            if (root.draggable){
                root.anchors.left = undefined
                root.anchors.right = undefined
                root.anchors.top = undefined
                root.anchors.bottom = undefined
                root.anchors.horizontalCenter = undefined
                root.anchors.verticalCenter = undefined
                root.anchors.centerIn = undefined
                root.anchors.fill = undefined
            }
        }

        drag.target: root
        drag.minimumX: 0
        drag.maximumX: overlay.width - root.width
    }
}
