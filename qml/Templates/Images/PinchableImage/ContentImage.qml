import QtQuick 2.15
import QtQuick.Window 2.2

import Templates 1.0 as Templates
import Assets 1.0 as Assets

Templates.StandardImage{
    id: contentImage

    property bool isZoomed: false

    signal resetZoom(var mouse_x, var mouse_y)
    signal zoomIn(var mouse_x, var mouse_y)

    image.autoTransform: true

    MouseArea {
        id: touchHandler

        anchors.fill: contentImage

        onDoubleClicked: {
            if (contentImage.isZoomed){
                contentImage.resetZoom(mouseX, mouseY)
            } else {
                contentImage.zoomIn(mouseX, mouseY)
            }
        }

    }

}
