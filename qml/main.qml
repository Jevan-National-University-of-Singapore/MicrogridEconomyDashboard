import QtQuick 
import QtQuick.Controls.Material
// import QtQuick.Window 2.2

import "NavigationMenu"
import "AssistancePanel"
import "ViewingPanel"

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
                            workspace.currentIndex = 0
                        }
                    }

                    ToolSeparator{}

                    ToolButton {
                        text: qsTr("Financial")
                        // onClicked: {
                        //     workspace.currentIndex = 1
                        // }
                    }

                    ToolSeparator{}

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
    SplitView {
        id: splitView

        anchors.fill: parent
        orientation: Qt.Horizontal

        height: root.height - root.menuBar.height - root.header.height

        NavigationMenu {
            id: navigationMenu

            SplitView.maximumWidth: root.width/2
            SplitView.minimumWidth: Qt.application.font.pixelSize
            SplitView.preferredWidth: root.width/6

            Material.primary: root.Material.background
            Material.background: root.Material.primary

            height: splitView.height

            technical.solarPowerGeneration {
                onInstalledCapacitySelected: technicalWorkspace.goToInstalledCapacity()
                onAyerKerohSiteConditionsSelected: technicalWorkspace.goToAyerKerohSiteConditions()
                onSolarEnergyProductionSelected: technicalWorkspace.goToSolarEnergyProduction()
            }
        }


        SplitView {
            id: controls

            orientation: Qt.Vertical

            SplitView.maximumWidth: root.width
            SplitView.minimumWidth: Qt.application.font.pixelSize
            SplitView.preferredWidth: root.width - (5*root.width)/12    

            Material.primary: root.Material.background
            Material.background: "#181818"//root.Material.primary

            height: splitView.height

            SwipeView{
                id: workspace

                Technical{
                    id: technicalWorkspace

                    height: splitView.height
                }

                SplitView.maximumHeight: root.height
                SplitView.minimumHeight: Qt.application.font.pixelSize
                SplitView.preferredHeight: 700

                // Financial{
                //     id: financial


                //     height: root.height - root.menuBar.height - root.header.height
                //     width: root.width
                // }
            }
            ViewingPanel{
                SplitView.maximumHeight: root.height
                SplitView.minimumHeight: Qt.application.font.pixelSize
                SplitView.preferredHeight: 1

                Material.primary: root.Material.primary
                Material.background: root.Material.background
            }
        }

        AssistancePanel{
            id: assistancePanel

            // height: splitView.height

            Material.primary: root.Material.background
            Material.background: root.Material.primary

            SplitView.maximumWidth: root.width
            SplitView.preferredWidth: root.width/10

        }


    }

}