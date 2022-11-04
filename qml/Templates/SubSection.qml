import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

ColumnLayout {
    id: root

    property alias subsection: subsectionLabel.text
    

    Label {
        id: subsectionLabel

        text: ""

        verticalAlignment: Text.AlignVCenter

        font.pixelSize: 24
    }


}