import QtQuick 
import QtQuick.Controls.Material
import QtQuick.Window 2.2

import "Technical"
import "ChargingAndDemand"
import "Financial"


ApplicationWindow {
    id: root 

    visible: true
    // visibility: "FullScreen"

    width: Screen.width
    height: Screen.height/1.08
    title: "TechnoEconomic"

    Material.theme: Material.Dark
    Material.accent: Material.Teal
    Material.primary: "#4a4a4e"
    Material.foreground: "white"

    property int activePage: 0

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

                // visible: false

                Row {
                    ToolButton {
                        text: qsTr("⋮")
                        font.pixelSize:24
                        // onClicked: menu.open()
                    }

                    ToolButton {
                        text: qsTr("Charging and Demand")
                        onClicked: {
                            // technical.visible = true
                            root.activePage = 0
                        }
                    }

                    ToolSeparator{}


                    ToolButton {
                        text: qsTr("Technical")
                        onClicked: {
                            root.activePage = 1
                        }
                    }

                    ToolSeparator{}

                    ToolButton {
                        text: qsTr("Financial")
                        onClicked: {
                            root.activePage = 2
                        }
                    }
                    


                }
            }


    ChargingAndDemand {
        id: chargingAndDemand
        
        visible: root.activePage == 0

        anchors.fill: parent
    }


    Technical{
        id: technical

        visible: root.activePage == 1

        anchors.fill: parent
    }

    Financial{
        id: financial

        visible: root.activePage == 2

        anchors.fill: parent
    }
}