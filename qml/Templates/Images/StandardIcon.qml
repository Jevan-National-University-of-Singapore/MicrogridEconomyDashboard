import QtQuick 2.15
import QtQuick.Controls 2.12
import QtGraphicalEffects 1.15

import "../../System"

Item{
    id: imageComponent

    property alias image: image
    property string source: ""

    Image {
        id: image

        anchors.fill: imageComponent

        source: System.systemImagesHomeDirectory + imageComponent.source

        fillMode: Image.PreserveAspectFit

        antialiasing: true
        asynchronous: true
        cache:true
    }

}
