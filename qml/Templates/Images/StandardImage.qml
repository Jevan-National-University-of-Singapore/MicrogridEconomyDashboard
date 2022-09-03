import QtQuick 2.15
import QtQuick.Controls 2.12
import QtGraphicalEffects 1.15

import "../../System"

Item{
    id: imageComponent

    property alias image: image
    property alias source: image.source

    function refresh(){
        var image_source = image.source
        image.source = ""
        image.source = image_source
    }

    Image {
        id: image

        anchors.fill: imageComponent

        fillMode: Image.PreserveAspectFit
        antialiasing: true
        asynchronous: true
    }

}
