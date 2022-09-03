import QtQuick 2.15
import QtQuick.Controls 2.12

import "../../System"


Item {
    id: dialogHeader

    implicitHeight: content.height + margins.topMargin + margins.bottomMargin
    implicitWidth: content.width

    property alias surface: dialogHeaderSurface

    property Margins margins: Margins{}

    property Item content: Item{}

    function setContent(){
        content.parent = dialogHeader

        content.y = margins.topMargin
        content.z = dialogHeaderSurface.z + 1

        content.width = dialogHeader.width - margins.leftMargin - margins.rightMargin
    }

    clip: true

    Rectangle {
        id: dialogHeaderSurface

        height: dialogHeader.height + radius

        anchors {
            top: dialogHeader.top

            left: dialogHeader.left
            right: dialogHeader.right
        }

        radius: 0

        color: ColorTheme.dialogHeaderColor
    }


    onContentChanged: dialogHeader.setContent()

    Component.onCompleted: dialogHeader.setContent()

}
