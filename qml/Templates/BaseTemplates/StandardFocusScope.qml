import QtQuick 2.15
import QtQuick.Controls 2.12

FocusScope {
    id: focusScope

    signal backKeyPressed

    Keys.onPressed: if (event.key === Qt.Key_Back) {
        event.accepted = true
        focusScope.backKeyPressed()
    }

}