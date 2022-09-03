import QtQuick 2.15
import QtQuick.Controls 2.12

import "../../System"

FocusScope {
    id: surfaceScope

    property string color: ColorTheme.boundingBorderColor

    property alias radius: surface.radius
    property alias thickness: surface.border.width

    Rectangle {
        id: surface

        anchors.fill: surfaceScope

        color: "transparent"
        border {
            color: surfaceScope.color
            width: 2
        }
    }
}
