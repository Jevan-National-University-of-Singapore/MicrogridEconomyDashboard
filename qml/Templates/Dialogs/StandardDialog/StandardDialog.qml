import QtQuick 2.15
import QtQuick.Controls 2.12

import "../../System"

Item {
    id: dialog

    property alias touchHandler: touchHandler

    property alias radius: dialogBody.surface.radius

    property alias header: dialogHeader
    property alias headerSurface: dialogHeader.surface
    property alias headerContent: dialogHeader.content

    property alias body: dialogBody
    property alias bodySurface: dialogBody.surface
    property alias bodyContent: dialogBody.content

    property alias footer: dialogFooter
    property alias footerSurface: dialogFooter.surface
    property alias footerContent: dialogFooter.content

    Header {
        id: dialogHeader

        z: dialogBody.z

        anchors {
            top: dialog.top

            left: dialog.left
            right: dialog.right
        }

        surface.radius: dialogBody.surface.radius
        surface.opacity: 0.8
    }


    Body {
        id: dialogBody

        z: touchHandler.z + 1

        anchors {
            top: dialogHeader.bottom

            left: dialog.left
            right: dialog.right

            bottom: dialogFooter.top
        }

        headerHeight: dialogHeader.height
        footerHeight: dialogFooter.height

        surface.radius: 15
        surface.opacity: 0.7

    }

    Footer {
        id: dialogFooter

        z: dialogBody.z

        anchors {
            bottom: dialog.bottom

            left: dialog.left
            right: dialog.right
        }


        surface.radius: dialogBody.surface.radius
        surface.opacity: 0.5
    }



    MouseArea {
        id: touchHandler

        anchors.fill: dialog
    }
}
