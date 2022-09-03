import QtQuick 2.15
import QtQuick.Controls 2.12
// import QtGraphicalEffects 1.15


FocusScope {
    id: slidingDrawer

    visible: width > 0

    property real displayWidth: 0

    function show(){
        showAnimation.start()
    }

    function hide(){
        hideAnimation.start()
    }

    Surface {
        id: surface

        radius: height/50
        height: slidingDrawer.height
        width: slidingDrawer.width + surface.radius
    }

    NumberAnimation {
        id: showAnimation

        target: slidingDrawer
        properties: "width"
        to: slidingDrawer.displayWidth
        duration: 200
    }


    NumberAnimation {
        id: hideAnimation

        target: slidingDrawer
        properties: "width"
        to: 0
        duration: 200
    }
}
