import QtQuick 2.15
import QtQuick.Controls 2.12

import "../../System"

FocusScope {
    id: surfaceScope
    property alias color: surface.color
    property alias radius: surface.radius

    Rectangle {
        id: surface

        anchors.fill: surfaceScope

        color: ColorTheme.surfaceColor
        radius: width > height? width/20 : height/20
    }
}
