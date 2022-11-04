import QtQuick 
import QtQuick.Controls.Material
import QtQuick.Window 2.2

import "Technical"


ApplicationWindow {
    id: root 

    visible: true
    // visibility: "FullScreen"

    width: Screen.width/1.1
    height: Screen.height/1.1
    title: "TechnoEconomic"

    Material.theme: Material.Dark
    Material.accent: Material.Teal
    Material.primary: "#4a4a4e"
    Material.foreground: "white"

    menuBar: MenuBar {
        Menu {
            title: qsTr("&File")
            Action { text: qsTr("&New...") }
            Action { text: qsTr("&Open...") }
            Action { text: qsTr("&Save") }
            Action { text: qsTr("Save &As...") }
            MenuSeparator { }
            Action { text: qsTr("&Quit") }
        }
        Menu {
            title: qsTr("&Edit")
            Action { text: qsTr("Cu&t") }
            Action { text: qsTr("&Copy") }
            Action { text: qsTr("&Paste") }
        }
        Menu {
            title: qsTr("&Help")
            Action { text: qsTr("&About") }
        }
    }
    header: ToolBar{
                Material.primary: Material.background

                Row {
                    ToolButton {
                        text: qsTr("⋮")
                        font.pixelSize:24
                        // onClicked: menu.open()
                    }
                    ToolButton {
                        text: qsTr("Technical")
                        onClicked: {
                            technical.visible = true
                        }
                    }

                    ToolSeparator{}

                    ToolButton {
                        text: qsTr("Financial")
                        onClicked: {
                            technical.visible = false
                        }
                    }
                    


                }
            }


    Technical{
        id: technical

        anchors.fill: parent
    }


}