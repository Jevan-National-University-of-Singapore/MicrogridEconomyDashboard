import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

// ColumnLayout {
//     id: root

//     property alias subsection: subsectionLabel.text
//     property alias label: subsectionLabel

//     Label {
//         id: subsectionLabel

//         text: ""

//         verticalAlignment: Text.AlignVCenter

//         font.pixelSize: 24
//     }


// }

GroupBox {
    id: root
    property alias subsection: root.title

    default property alias subItems: subItems.data

    // title: qsTr("Synchronize")
    ColumnLayout {
        id: subItems

    }
}