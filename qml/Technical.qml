import QtQuick
import QtQuick.Controls.Material

Item {
    TextInput {
        
        height: parent.height/20
        width: height * 2

        anchors {
            left: parent.left
            leftMargin: width

            top: parent.top
            topMargin: height
        }
    }

}