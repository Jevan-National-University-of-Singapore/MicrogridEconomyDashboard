import QtQuick 2.15
import QtQuick.Controls 2.12
import QtGraphicalEffects 1.15

import "../../System"

//import "../BaseTemplates" as BaseTemplates
import "../Dialogs/StandardDialog"

StandardPage {
    id: dialogPage

    visible: opacity > 0
    opacity: 0

    function show(){
        showAnimation.start()
        dialogPage.forceActiveFocus()
    }

    function exit(){
        dialogPage.exited()
        hideAnimation.start()
    }

    // background blur
    property alias blur: blur

    // animation
    property alias showAnimation: showAnimation
    property alias hideAnimation: hideAnimation

    // dialog
    property alias dialog: dialog

    property alias dialogTouchHandler: dialog.touchHandler

    property alias header: dialog.header
    property alias headerSurface: dialog.headerSurface
    property alias headerContent: dialog.headerContent

    property alias body: dialog.body
    property alias bodySurface: dialog.bodySurface
    property alias bodyContent: dialog.bodyContent

    property alias footer: dialog.footer
    property alias footerSurface: dialog.footerSurface
    property alias footerContent: dialog.footerContent

    touchHandler.onClicked: exit()


    StandardDialog{
        id: dialog

        width: dialogPage.width/1.05
        height: dialogPage.height/3.5
        z: blur.z + 1

        anchors {
            centerIn: dialogPage
            verticalCenterOffset: -height/5
        }
    }

    FastBlur {
        id: blur

        z: touchHandler.z + 1

        anchors.fill: dialogPage

        transparentBorder: true

        radius: dialogPage.opacity * 40
        opacity: 0.8
    }

    NumberAnimation {
        id: showAnimation

        target: dialogPage
        properties: "opacity"
        to: 1
        duration: 150
    }


    NumberAnimation {
        id: hideAnimation

        target: dialogPage
        properties: "opacity"
        to: 0
        duration: 150
    }


}
