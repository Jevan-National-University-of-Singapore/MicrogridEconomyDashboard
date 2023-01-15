import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

import "../Delegates"

Item {
    id: root

    signal installedCapacitySelected
    signal ayerKerohSiteConditionsSelected
    signal solarEnergyProductionSelected
    signal hourlySolarPowerGenerationSelected


    height: parentView.height + subTreeViews.height
    width: childrenRect.width

    function deselectAll(){
        installedCapacity.isSelected = false
        ayerKerohSiteConditions.isSelected = false
        solarEnergyProduction.isSelected = false
        hourlySolarPowerGeneration.isSelected = false
    }
    
    Delegate{
        id: parentView

        // height: implicitHeight; width: implicitWidth
        text: "Solar Power Generation"

        onSubTreeExpand: {
            subTreeViews.state = "expanded"
            installedCapacity.state = "expanded"
            ayerKerohSiteConditions.state = "expanded"
            solarEnergyProduction.state = "expanded"
            hourlySolarPowerGeneration.state = "expanded"
        }

        onSubTreeCollapse: {
            subTreeViews.state = "collapsed"
            installedCapacity.state = "collapsed"
            ayerKerohSiteConditions.state = "collapsed"
            solarEnergyProduction.state = "collapsed"
            hourlySolarPowerGeneration.state = "collapsed"
        }
    }

    Item{
        id: subTreeViews

        height: childrenRect.height; width: childrenRect.width

        states: [
            State {
                name: "expanded"
                AnchorChanges { 
                    target: subTreeViews

                    anchors.top: parentView.bottom
                }
            },
            State {
                name: "collapsed"
                AnchorChanges { 

                    target: subTreeViews
                    anchors.top: parentView.top
                }
            }
        ]

        transitions: Transition {
            AnchorAnimation { duration: 150 }
        }

        anchors {
            left: parentView.left
            leftMargin: Qt.application.font.pixelSize * 3
            
            top: parentView.bottom
        }

        LeafDelegate{
            id: installedCapacity

            text: "Installed Capacity"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: subTreeViews.top
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                ayerKerohSiteConditions.isSelected = false
                solarEnergyProduction.isSelected = false
                hourlySolarPowerGeneration.isSelected = false
                root.installedCapacitySelected()
            }


        }

        LeafDelegate{
            id: ayerKerohSiteConditions

            text: "Ayer Keroh Site Conditions"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: installedCapacity.bottom
            collapsedAnchor.anchors.top: subTreeViews.top   

            onSelected: {
                installedCapacity.isSelected = false
                solarEnergyProduction.isSelected = false
                hourlySolarPowerGeneration.isSelected = false
                root.ayerKerohSiteConditionsSelected()
            }         
        }
        LeafDelegate{
            id: solarEnergyProduction

            text: "Solar Energy Production"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }
            
            expandedAnchor.anchors.top: ayerKerohSiteConditions.bottom
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                installedCapacity.isSelected = false
                ayerKerohSiteConditions.isSelected = false
                hourlySolarPowerGeneration.isSelected = false
                root.solarEnergyProductionSelected()
            }
        }

        LeafDelegate{
            id: hourlySolarPowerGeneration

            text: "Hourly Solar Power Generation"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }
            
            expandedAnchor.anchors.top: solarEnergyProduction.bottom
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                installedCapacity.isSelected = false
                ayerKerohSiteConditions.isSelected = false
                solarEnergyProduction.isSelected = false
                root.hourlySolarPowerGenerationSelected()
            }
        }

    }
}


