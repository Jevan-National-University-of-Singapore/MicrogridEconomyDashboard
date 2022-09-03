import QtQuick 2.15
import QtQuick.Controls 2.12
import QtGraphicalEffects 1.15

import "../Images"


Item {
    id: button

    property string color: "transparent" //if you want to have surface: ColorTheme.mainButtonColor
    property string pressedColor: "transparent" //if you want to have surface: ColorTheme.mainButtonPressedColor

    property alias icon: buttonIcon
    property alias iconSource: buttonIcon.source

    signal clicked
    signal pressed
    signal released

    Rectangle {
        id: buttonSurface

        anchors.fill: button

        color: button.color
        radius: width/20

        StandardIcon {
            id: buttonIcon

            anchors.fill: buttonSurface
        }

        HueSaturation {
            id: buttonIconOverlay

            visible: false
            z: buttonIcon.z + 1

            anchors.fill: buttonIcon
            source: buttonIcon
            lightness: -0.5
        }


        MouseArea {
            id: touchHandler

            anchors.fill: buttonSurface

            onClicked: button.clicked()

            onPressed: {
                buttonSurface.color = button.pressedColor
                buttonIconOverlay.visible = true
                button.pressed()
            }

            onReleased: {
                buttonSurface.color = button.color
                buttonIconOverlay.visible = false
                button.released()
            }

        }

    }

}
