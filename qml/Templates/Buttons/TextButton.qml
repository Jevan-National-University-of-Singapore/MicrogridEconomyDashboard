import QtQuick 2.15
import QtQuick.Controls 2.12

import "../../System"
import "../Texts"

Item {
    id: button

    implicitHeight: buttonText.implicitHeight * 1.2
    implicitWidth: buttonText.implicitWidth * 1.5

    property string color: ColorTheme.buttonColor
    property string pressedColor: ColorTheme.buttonPressedColor

    property string borderColor: ColorTheme.boxColor
    property string borderPressedColor: ColorTheme.buttonColor

    property alias text: buttonText.text

    property alias surface: buttonSurface
    property alias border: buttonSurface.border

    signal clicked
    signal pressed
    signal released

    Rectangle {
        id: buttonSurface

        anchors.fill: button

        color: button.color
        radius: width/20

        border.color: button.borderPressedColor

        StandardText{
            id: buttonText

            anchors.fill: buttonSurface
        }

        MouseArea {
            id: touchHandler

            anchors.fill: buttonSurface

            onClicked: button.clicked()
            onPressed: {
                buttonSurface.color = button.pressedColor
                buttonSurface.border.color = button.borderPressedColor
                button.pressed()
            }

            onReleased: {
                buttonSurface.color = button.color
                buttonSurface.border.color = button.borderColor
                button.released()
            }

        }

    }

}
