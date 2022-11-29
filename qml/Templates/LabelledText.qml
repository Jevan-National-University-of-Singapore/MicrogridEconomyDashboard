import QtQuick
import QtQuick.Controls.Material

Row {
    id: root

    property string labelText: ""
    property alias text: text.text
    property alias units: units.text

    spacing: label.font.pixelSize

    Label {
        id: label

        text: root.labelText + ":"
        verticalAlignment: Text.AlignVCenter
        height: font.pixelSize * 2.5
    }

    Label {
        id: text

        text: ""

        verticalAlignment: Text.AlignVCenter
        height: label.height
    }

    Label {
        id: units

        verticalAlignment: Text.AlignVCenter
        height: label.height
    }



}