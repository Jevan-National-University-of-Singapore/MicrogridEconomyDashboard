import QtQuick 2.15
import QtQuick.Controls 2.12

import "../../System"
import "../BaseTemplates" as BaseTemplates

BaseTemplates.StandardFocusScope {
    id: page

    property alias touchHandler: touchHandler
    property alias surface: pageSurface

    signal exited()

    function show(){
        page.visible = true
        page.forceActiveFocus()
    }

    function exit(){
        page.visible = false
        page.exited()
    }

    onBackKeyPressed: page.exit()

    Rectangle {
        id: pageSurface

        anchors.fill: page

        color: ColorTheme.rootColor

        MouseArea {
            id: touchHandler

            anchors.fill: pageSurface
        }

    }

}
