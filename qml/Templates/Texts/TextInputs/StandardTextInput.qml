import QtQuick 2.15
import QtQuick.Controls 2.12

import "../../../System"

FocusScope {
    id: textInputScope

    focus: true

    implicitHeight: textInput.implicitHeight
    implicitWidth: textInput.implicitWidth

    property alias content: textInput
    property alias text: textInput.text

    property alias fontSize: textInput.font.pointSize
    property alias fontColor: textInput.color

    TextInput{
        id:textInput

        focus: true

        anchors.fill: textInputScope

        activeFocusOnPress: true

        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignLeft

        text: ""

        color: ColorTheme.textColor
        font.pointSize: FontSettings.fontSize

    }

    onFocusChanged: if (focus){ Qt.inputMethod.show() }
}
