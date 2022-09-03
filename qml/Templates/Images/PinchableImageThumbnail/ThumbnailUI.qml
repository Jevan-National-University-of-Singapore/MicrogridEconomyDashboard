import QtQuick 2.15

Item {
    id: imageUI

    required property Flickable flickArea
    required property real imageWidth
    required property real imageHeight

    Rectangle{
        id: imageBoundingBox

        anchors.fill: imageUI

        color:"transparent"

        border{
            color: "white"
            width: 2
        }

        Rectangle{
            id: imageSeekingBox
            color: "transparent"
            border{
                color: "white"
                width: 1
            }
            width: imageWidth * imageUI.flickArea.width/imageUI.flickArea.contentWidth
            height: imageHeight * imageUI.flickArea.height/imageUI.flickArea.contentHeight
            anchors {
                left: imageBoundingBox.left
                top: imageBoundingBox.top
                leftMargin: imageWidth * imageUI.flickArea.contentX / imageUI.flickArea.contentWidth// + imageBoundingBox.border.width
                topMargin: imageHeight * imageUI.flickArea.contentY / imageUI.flickArea.contentHeight //+ imageBoundingBox.border.width
            }
        }
    }
}
