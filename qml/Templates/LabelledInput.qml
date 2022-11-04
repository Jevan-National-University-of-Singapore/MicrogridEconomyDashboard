import QtQuick
import QtQuick.Controls.Material

Row {
    id: root

    property string label: ""

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


}