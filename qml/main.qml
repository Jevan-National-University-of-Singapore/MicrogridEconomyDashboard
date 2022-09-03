import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.2

import "System"

// import "./Viewfinder"

ApplicationWindow {
    id: root 

    visible: true
    // visibility: "FullScreen"

    width: Screen.width/1.1
    height: Screen.height/1.1
    title: "TechnoEconomic"
    color: ColorTheme.rootColor//"black"

    // ApplicationStack {
    //     id: applicationStack

    //     focus: true

    //     anchors.fill: parent
    // }


    // Component.onCompleted: {
    //     // Server.connectToHost()
    //     applicationStack.forceActiveFocus()
    //     // Qt.inputMethod.show()
    // }

}