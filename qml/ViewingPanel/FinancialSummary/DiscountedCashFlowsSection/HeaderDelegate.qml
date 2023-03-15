import QtQuick
import QtQuick.Controls.Material
    

Item {
    id: root

    property string backgroundColor
    property string foregroundColor

    property alias header: header

    visible : column === 0

    implicitHeight: header.height
    implicitWidth: header.font.pixelSize * 10
   
    Rectangle {
        id: headerSurface

        opacity: 0.7

        anchors.fill: parent
        
        color : backgroundColor

        radius: 2
        border {
            color: foregroundColor
            width: 1
        }
    }

    Label {
        id: header

        width: implicitWidth; height: implicitHeight * 1.2
        anchors.fill: parent

        verticalAlignment: Text.AlignVCenter
        // horizontalAlignment: Text.AlignHCenter
        leftPadding: Qt.application.font.pixelSize

        Material.foreground : root.foregroundColor

        text: visible? display : ""
    }
}