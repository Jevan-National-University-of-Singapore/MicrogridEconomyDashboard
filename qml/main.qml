import QtQuick 
import QtQuick.Controls.Material
// import QtQuick.Window 2.2

// import "SolarPowerGeneration"
// import "ChargingAndDemand"
import "Technical"
// import "Financial"


ApplicationWindow {
    id: root 

    visible: true
    // visibility: "FullScreen"

    width: Screen.width
    height: Screen.height/1.08
    title: "TechnoEconomic"
    font.capitalization: Font.MixedCase

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
                            applicationStack.currentIndex = 0
                        }
                    }

                    ToolSeparator{}

                    // ToolButton {
                    //     text: qsTr("Financial")
                    //     onClicked: {
                    //         applicationStack.currentIndex = 1
                    //     }
                    // }

                    // ToolSeparator{}

                    ComboBox {
                        currentIndex: 0
                        model: ListModel {
                            ListElement { text: "Year 1" }
                            ListElement { text: "Year 2" }
                            ListElement { text: "Year 3" }
                            ListElement { text: "Year 4" }
                            ListElement { text: "Year 5" }
                        }
                        // model: [0,1,2,3,4]
                    }
                    
                }
            }
    SwipeView{
        id: applicationStack
        anchors.fill: parent

        Technical{
            id: technical


            height: root.height - root.menuBar.height - root.header.height
            width: root.width
        }

        // Financial{
        //     id: financial


        //     height: root.height - root.menuBar.height - root.header.height
        //     width: root.width
        // }
    }

}