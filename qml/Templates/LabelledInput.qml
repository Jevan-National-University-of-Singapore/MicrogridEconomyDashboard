import QtQuick
import QtQuick.Controls.Material

Row {
    id: root

    property string label: ""
    property alias input: input
    property alias inputText: input.text
    property alias units: units.text

    spacing: label.font.pixelSize

    Label {
        id: label

        text: root.label + ":"
        height: font.pixelSize * 2.5
        verticalAlignment: Text.AlignVCenter
    }

    TextField {
        id: input


        text: ""
        
    }

    Label {
        id: units

        height: label.height
        verticalAlignment: Text.AlignVCenter
    }


}