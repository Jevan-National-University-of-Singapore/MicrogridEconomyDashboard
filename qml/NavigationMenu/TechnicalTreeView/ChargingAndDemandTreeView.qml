import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

import "../Delegates"

Item {
    id: root

    signal chargingPortsSelected
    signal demandSelected
    signal loadSelected
    signal excessToFacilitySelected
    signal evCharacteristicsSelected
    signal hourlyDemandSelected

    implicitHeight: parentView.height + subTreeViews.height
    width: childrenRect.width

    Behavior on opacity { SmoothedAnimation { velocity: 5 } }
    Behavior on height { SmoothedAnimation { velocity: 200 } }    

    visible: opacity    

    function deselectAll(){
        chargingPorts.isSelected = false
        demand.isSelected = false
        load.isSelected = false
        excessToFacility.isSelected = false
        evCharacteristics.isSelected = false
        hourlyDemand.isSelected = false
    }

    function collapseSubSection(){
        root.deselectAll()
        subTreeViews.state = "collapsed"
        chargingPorts.state = "collapsed"
        demand.state = "collapsed"
        load.state = "collapsed"
        excessToFacility.state = "collapsed"
        evCharacteristics.state = "collapsed"
        hourlyDemand.state = "collapsed"
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

        text: "Charging And Demand"

        onSubTreeExpand: {
            subTreeViews.state = "expanded"
            chargingPorts.state = "expanded"
            demand.state = "expanded"
            load.state = "expanded"
            excessToFacility.state = "expanded"
            evCharacteristics.state = "expanded"
            hourlyDemand.state = "expanded"
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
            id: chargingPorts

            text: "Charging Ports"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: subTreeViews.top
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                demand.isSelected = false
                load.isSelected = false
                excessToFacility.isSelected = false
                evCharacteristics.isSelected = false
                hourlyDemand.isSelected = false
                root.chargingPortsSelected()
            }


        }

        LeafDelegate{
            id: demand

            text: "Demand"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: chargingPorts.bottom
            collapsedAnchor.anchors.top: subTreeViews.top   

            onSelected: {
                chargingPorts.isSelected = false
                load.isSelected = false
                excessToFacility.isSelected = false
                evCharacteristics.isSelected = false
                hourlyDemand.isSelected = false
                root.demandSelected()
            }         
        }
        LeafDelegate{
            id: load

            text: "Load  "
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }
            
            expandedAnchor.anchors.top: demand.bottom
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                chargingPorts.isSelected = false
                demand.isSelected = false
                excessToFacility.isSelected = false
                evCharacteristics.isSelected = false
                hourlyDemand.isSelected = false
                root.loadSelected()
            }
        }

        LeafDelegate{
            id: excessToFacility

            text: "Excess To Facility"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }
            
            expandedAnchor.anchors.top: load.bottom
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                chargingPorts.isSelected = false
                demand.isSelected = false
                load.isSelected = false
                evCharacteristics.isSelected = false
                hourlyDemand.isSelected = false
                root.excessToFacilitySelected()
            }
        }

        LeafDelegate{
            id: evCharacteristics

            text: "EV Characteristics"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }
            
            expandedAnchor.anchors.top: excessToFacility.bottom
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                chargingPorts.isSelected = false
                demand.isSelected = false
                load.isSelected = false
                excessToFacility.isSelected = false
                hourlyDemand.isSelected = false
                root.evCharacteristicsSelected()
            }
        }

        LeafDelegate{
            id: hourlyDemand

            text: "Hourly Demand"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }
            
            expandedAnchor.anchors.top: evCharacteristics.bottom
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                chargingPorts.isSelected = false
                demand.isSelected = false
                load.isSelected = false
                excessToFacility.isSelected = false
                evCharacteristics.isSelected = false
                root.hourlyDemandSelected()
            }
        }

    }
}


