import QtQuick 2.15

Flickable {
    id: flickArea

    property alias contentImage: contentImage.image
    property alias isZoomed: contentImage.isZoomed

    function refresh(){
        contentImage.refresh()
    }

    contentHeight: height
    contentWidth: width

    boundsBehavior: Flickable.StopAtBounds

    ImagePinchArea{
        id: pinchArea

        containerContentWidth: flickArea.contentWidth
        containerContentHeight: flickArea.contentHeight

        containerContentX: flickArea.contentX
        containerContentY: flickArea.contentY

        containerWidth: flickArea.width
        containerHeight: flickArea.height

        onResizeContent: flickArea.resizeContent(width, height, center)

        onPinchFinished: flickArea.returnToBounds()


        ContentImage{
            id: contentImage

            width: flickArea.contentWidth
            height: flickArea.contentHeight

            isZoomed: flickArea.contentHeight > flickArea.height

            onResetZoom: flickArea.resizeContent(flickArea.width, flickArea.height, Qt.point(mouse_x, mouse_y))
            onZoomIn: flickArea.resizeContent(flickArea.contentWidth*1.3, flickArea.contentHeight*1.3, Qt.point(mouse_x, mouse_y))

        }

    }

}
