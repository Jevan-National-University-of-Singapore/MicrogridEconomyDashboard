import QtQuick 2.15

import Templates 1.0

Item {
    id: fullPreviewImage

    height: image.image.sourceSize.height/image.image.sourceSize.width * width

    property alias sourcePinchableImage: imageUI.flickArea //Pass a PinchableImage type which is a Flickable type

    property alias image: image
    property alias imageUI: imageUI

    function refresh(){
        image.refresh()
    }

    ContentImage{
        id: image

        source: sourcePinchableImage.contentImage.source

        anchors.fill: fullPreviewImage
    }

    ThumbnailUI{
        id: imageUI

        z: image.z + 1
        anchors.fill: fullPreviewImage

        flickArea: sourcePinchableImage

        imageHeight: image.height
        imageWidth: image.width
    }




}
