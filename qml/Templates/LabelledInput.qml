import QtQuick
import QtQuick.Controls.Material

Row {
    id: root

    property string label: ""
    property alias input: input
    property alias inputText: input.text
    property alias units: units.text

    spacing: height/5

    Label {
        id: label

        text: root.label + ":"
        height: root.height
        verticalAlignment: Text.AlignVCenter
    }

    TextField {
        id: input


        text: ""
        
    }

    Label {
        id: units

        height: root.height
        verticalAlignment: Text.AlignVCenter
    }


}