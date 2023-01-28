import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

import "../Delegates"

Item {
    id: root

    signal essSystemSelected
    signal dischargeSelected
    signal gridChargingSelected

    implicitHeight: parentView.height + subTreeViews.height
    width: childrenRect.width


    visible: opacity    


    Behavior on opacity { SmoothedAnimation { velocity: 5 } }
    Behavior on height { SmoothedAnimation { velocity: 200 } }    

    function deselectAll(){
        essSystem.isSelected = false
        discharge.isSelected = false
        gridCharging.isSelected = false
    }

    function collapseSubSection(){
        root.deselectAll()
        subTreeViews.state = "collapsed"
        essSystem.state = "collapsed"
        discharge.state = "collapsed"
        gridCharging.state = "collapsed"
    }

    function collapse(){
        root.collapseSubSection()
        parentView.collapse()
        root.state = "collapsed"
    }

    function show(){
        root.state = "expanded"
    }

    state: "expanded"

    states: [
        State {
            name: "expanded"

            PropertyChanges {
                target: root

                opacity: 1
                implicitHeight: parentView.height + subTreeViews.height
            }
        },
        State {
            name: "collapsed"

            PropertyChanges {
                target: root

                opacity: 0
                implicitHeight:0
            }
        }
    ]

    
    Delegate{
        id: parentView

        text: "Battery Storage"

        onSubTreeExpand: {
            subTreeViews.state = "expanded"
            essSystem.state = "expanded"
            discharge.state = "expanded"
            gridCharging.state = "expanded"
        }

        onSubTreeCollapse: root.collapseSubSection()
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
            id: essSystem

            text: "ESS System"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: subTreeViews.top
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                discharge.isSelected = false
                gridCharging.isSelected = false
                root.essSystemSelected()
            }
        }

        LeafDelegate{
            id: discharge

            text: "Discharge"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: essSystem.bottom
            collapsedAnchor.anchors.top: subTreeViews.top   

            onSelected: {
                essSystem.isSelected = false
                gridCharging.isSelected = false
                root.dischargeSelected()
            }         
        }
        LeafDelegate{
            id: gridCharging

            text: "Grid Charging"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }
            
            expandedAnchor.anchors.top: discharge.bottom
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                essSystem.isSelected = false
                discharge.isSelected = false
                root.gridChargingSelected()
            }
        }


    }
}


