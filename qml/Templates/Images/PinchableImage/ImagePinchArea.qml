import QtQuick 2.15

PinchArea {
    id: pinch

    width: Math.max(containerContentWidth, containerWidth)
    height: Math.max(containerContentHeight, containerHeight)

    property real initialWidth
    property real initialHeight

    property real containerContentWidth: 0
    property real containerContentHeight: 0

    property real containerContentX: 0
    property real containerContentY: 0

    property real containerWidth: 0
    property real containerHeight: 0


    signal resizeContent(var width, var height, var center)

    onPinchStarted: {
        initialWidth = containerContentWidth
        initialHeight = containerContentHeight
    }

    onPinchUpdated: {
        var newWidth = initialWidth * pinch.scale
        var newHeight = initialHeight * pinch.scale

        if (newWidth < containerWidth || newHeight < containerHeight) {
            resizeContent(containerWidth, containerHeight, Qt.point(containerWidth/2, containerHeight/2))
        }
        else {
            containerContentX += pinch.previousCenter.x - pinch.center.x
            containerContentY += pinch.previousCenter.y - pinch.center.y
            resizeContent(initialWidth * pinch.scale, initialHeight * pinch.scale, pinch.center)
        }
    }


}
