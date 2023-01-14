import QtQuick
import QtQuick.Controls.Material

Label {
    id: root

    visible: row === 0 && column !== 0

    verticalAlignment: Text.AlignVCenter
    horizontalAlignment: Text.AlignHCenter

    text: visible? display : ""

}