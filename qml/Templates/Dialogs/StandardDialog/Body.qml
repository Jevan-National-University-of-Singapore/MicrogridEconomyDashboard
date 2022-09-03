import QtQuick 2.15
import QtQuick.Controls 2.12

import "../../System"

Item {
    id: dialogBody

    property alias surface: dialogBodySurface

    property real headerHeight: 0
    property real footerHeight: 0

    property Margins margins: Margins{}

    property Item content: Item{}

    function setContent(){
        content.parent = dialogBody

        content.x = margins.leftMargin
        content.y = margins.topMargin
        content.z = dialogBodySurface.z + 1

        content.height = dialogBody.height - margins.topMargin - margins.bottomMargin
        content.width = dialogBody.width - margins.leftMargin - margins.rightMargin
    }


    clip: true


    Rectangle {
        id: dialogBodySurface

        height: dialogBody.height + (dialogBody.headerHeight) + (dialogBody.footerHeight)

        anchors {
            verticalCenter: dialogBody.verticalCenter
            verticalCenterOffset: (0.5*dialogBody.footerHeight) - (0.5*dialogBody.headerHeight)

            left: dialogBody.left
            right: dialogBody.right
        }

        radius: 0

        color: ColorTheme.dialogColor

//        DebugRectangle {
//            id: debugRect2

//            border.color: "red"

//            anchors.fill: dialogBodySurface
//        }
    }

    onContentChanged: dialogBody.setContent()

    Component.onCompleted: dialogBody.setContent()


}
