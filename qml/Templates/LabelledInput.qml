import QtQuick
import QtQuick.Controls.Material
import QtQuick.Controls.Universal as Universal
import QtQuick.Controls.Basic as Basic

Row {
    id: root

    property string label: ""
    property alias input: input
    property alias inputText: input.text
    property alias units: units.text

    spacing: Qt.application.font.pixelSize/2

    Label {
        id: label

        text: root.label + ":"
        height: font.pixelSize * 2
        verticalAlignment: Text.AlignVCenter
    }

    Universal.TextField {
        id: input

        Universal.Universal.theme: Universal.Universal.Dark
        Universal.Universal.accent: Universal.Universal.Teal
        Universal.Universal.background: "#212121"
        Universal.Universal.foreground: "white"

        text: ""

        height: font.pixelSize * 1.5
        width: font.pixelSize * 5

        bottomPadding: font.pixelSize/8
        
    }

    // Basic.TextField {
    //     id: input

    //     // Basic.Basic.theme: Basic.Basic.Dark
    //     // Basic.Basic.accent: Basic.Basic.Teal
    //     // Universal.Universal.primary: "#4a4a4e"
    //     // Basic.Basic.foreground: "white"

    //     text: ""

    //     height: font.pixelSize * 1.5

    //     bottomPadding: font.pixelSize/8
        
    // }


    // TextField {
    //     id: input


    //     text: ""

    //     height: font.pixelSize * 1.5

    //     bottomPadding: 0
        
    // }


    Label {
        id: units

        height: label.height
        verticalAlignment: Text.AlignVCenter
    }


}