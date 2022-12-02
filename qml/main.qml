import QtQuick 
import QtQuick.Controls.Material
// import QtQuick.Window 2.2

import "SolarPowerGeneration"
import "ChargingAndDemand"
import "Technical"
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
                        text: qsTr("Solar Power Generation")
                        onClicked: {
                            applicationStack.currentIndex = 0
                        }
                    }

                    ToolSeparator{}

                    ToolButton {
                        text: qsTr("Charging and Demand")
                        onClicked: {
                            applicationStack.currentIndex = 1
                        }
                    }

                    ToolSeparator{}


                    ToolButton {
                        text: qsTr("Technical")
                        onClicked: {
                            applicationStack.currentIndex = 2
                        }
                    }

                    ToolSeparator{}

                    ToolButton {
                        text: qsTr("Financial")
                        onClicked: {
                            applicationStack.currentIndex = 3
                        }
                    }
                    


                }
            }
    SwipeView{
        id: applicationStack
        anchors.fill: parent

        SolarPowerGeneration {
            id: solarPowerGeneration


            height: root.height - root.menuBar.height - root.header.height
            width: root.width
        }


        ChargingAndDemand {
            id: chargingAndDemand
            

            height: root.height - root.menuBar.height - root.header.height
            width: root.width
        }


        Technical{
            id: technical


            height: root.height - root.menuBar.height - root.header.height
            width: root.width
        }

        Financial{
            id: financial


            height: root.height - root.menuBar.height - root.header.height
            width: root.width
        }
    }
}