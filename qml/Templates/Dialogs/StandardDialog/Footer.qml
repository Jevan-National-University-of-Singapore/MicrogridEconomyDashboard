 import QtQuick 2.15
import QtQuick.Controls 2.12

import "../../System"

Item {
    id: dialogFooter

    implicitHeight: content.height + margins.topMargin + margins.bottomMargin
    implicitWidth: content.width

    property alias surface: dialogFooterSurface

    property Margins margins: Margins{}

    property Item content: Item{}

    function setContent(){
        content.parent = dialogFooter

        content.y = margins.topMargin
        content.z = dialogFooterSurface.z + 1

        content.width = dialogFooter.width - margins.leftMargin - margins.rightMargin
    }

    clip: true

    Rectangle {
        id: dialogFooterSurface

        height: dialogFooter.height + radius

        anchors {
            bottom: dialogFooter.bottom

            left: dialogFooter.left
            right: dialogFooter.right
        }

        radius: 0

        color: ColorTheme.dialogFooterColor
    }

    onContentChanged: dialogFooter.setContent()

    Component.onCompleted: dialogFooter.setContent()

}
