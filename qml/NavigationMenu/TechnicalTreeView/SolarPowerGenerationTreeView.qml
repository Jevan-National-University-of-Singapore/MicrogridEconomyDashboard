import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

import "../Delegates"

Item {
    id: root

    signal installedCapacitySelected
    signal ayerKerohSiteConditionsSelected
    signal solarEnergyProductionSelected

    function deselectAll(){
        installedCapacity.isSelected = false
        ayerKerohSiteConditions.isSelected = false
        solarEnergyProduction.isSelected = false
    }
    
    Delegate{
        id: parentView

        height: implicitHeight; width: implicitWidth
        text: "Solar Power Generation"

        onSubTreeExpand: {
            subTreeViews.state = "expanded"
            installedCapacity.state = "expanded"
            ayerKerohSiteConditions.state = "expanded"
            solarEnergyProduction.state = "expanded"
        }

        onSubTreeCollapse: {
            subTreeViews.state = "collapsed"
            installedCapacity.state = "collapsed"
            ayerKerohSiteConditions.state = "collapsed"
            solarEnergyProduction.state = "collapsed"
        }
    }

    Item{
        id: subTreeViews

        height: contentHeight; width: contentWidth

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
                
                top: subTreeViews.bottom
            }

            expandedAnchor.anchors.top: subTreeViews.top
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                ayerKerohSiteConditions.isSelected = false
                solarEnergyProduction.isSelected = false
                root.installedCapacitySelected()
            }
        }

        LeafDelegate{
            id: ayerKerohSiteConditions

            text: "AyerKerohSiteConditions"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: installedCapacity.bottom
            }

            expandedAnchor.anchors.top: installedCapacity.bottom
            collapsedAnchor.anchors.top: subTreeViews.top   

            onSelected: {
                installedCapacity.isSelected = false
                solarEnergyProduction.isSelected = false
                root.ayerKerohSiteConditionsSelected()
            }         
        }
        LeafDelegate{
            id: solarEnergyProduction

            text: "Solar Energy Production"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: ayerKerohSiteConditions.bottom
            }
            
            expandedAnchor.anchors.top: ayerKerohSiteConditions.bottom
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                installedCapacity.isSelected = false
                ayerKerohSiteConditions.isSelected = false
                root.solarEnergyProductionSelected()
            }
            
        }

    }
}


