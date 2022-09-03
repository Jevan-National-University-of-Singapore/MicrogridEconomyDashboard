import QtQuick 2.15
import QtQuick.Controls 2.15

import "../../System"

Rectangle {
    id: surface

    implicitHeight: content.implicitHeight
    implicitWidth: content.implicitWidth

    color: "transparent"

    property alias content: content
    property alias text: content.text

    property alias fontSize: content.font.pointSize
    property alias fontColor: content.color
//    property int fontSize: surface.fontSettings.fontSize
//    property string fontColor: surface.colorTheme.textColor


    Text {
        id: content

        anchors.fill: surface

        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter

        text: ""
        color: ColorTheme.textColor
        font.pointSize: FontSettings.fontSize
    }


}
