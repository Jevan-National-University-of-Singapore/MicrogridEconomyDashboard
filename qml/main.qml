import QtQuick 
import QtQuick.Controls.Material
import QtQuick.Window 2.2

// import "System"

// import "./Viewfinder"

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
    // Material.primary: "#2a2a2e"
    // Material.primary: Material.Teal

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
                Row {
                    ToolButton {
                        text: qsTr("⋮")
                        font.pixelSize:24
                        // onClicked: menu.open()
                    }
                    ToolButton {
                        text: qsTr("Technical")
                        // onClicked: menu.open()
                    }

                    ToolSeparator{}

                    ToolButton {
                        text: qsTr("Financial")
                        // onClicked: menu.open()
                    }
                    


                }
            }

    Technical{

        anchors.fill: parent
        anchors.topMargin: parent.height/10
    }


}