import QtQuick
import QtQuick.Controls.Material

Rectangle {
    id: root

    property alias thickness: root.width
    property alias length: root.height

    color: Material.primary

    radius: thickness

    width: 1
    height: width * 10
}