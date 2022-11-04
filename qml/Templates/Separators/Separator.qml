import QtQuick

Rectangle{
    id: root

    property real thickness: 1
    property real length: thickness * 10

    property bool horizontal: false 

    radius: thickness

    width: horizontal? length: thickness
    height: horizontal? thickness: length
}