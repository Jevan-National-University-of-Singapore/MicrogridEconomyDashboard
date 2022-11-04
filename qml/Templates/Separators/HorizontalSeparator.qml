import QtQuick
import QtQuick.Controls.Material

Rectangle {
    id: root

    property alias thickness: root.height
    property alias length: root.width

    color: Material.primary

    radius: thickness

    width: height * 10
    height: 1
}