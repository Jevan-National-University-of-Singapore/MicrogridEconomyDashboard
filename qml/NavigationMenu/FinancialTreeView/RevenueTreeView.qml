import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

import "../Delegates"

Item {
    id: root

    signal revenueItemsSelected
    signal pricingSelected
    signal tariffAssumptionSelected

    implicitHeight: parentView.height + subTreeViews.height
    width: childrenRect.width

    Behavior on opacity { SmoothedAnimation { velocity: 5 } }
    Behavior on height { SmoothedAnimation { velocity: 200 } }    

    visible: opacity    

    function deselectAll(){
        revenueItems.isSelected = false
        pricing.isSelected = false
        tariffAssumption.isSelected = false
    }

    function collapseSubSection(){
        root.deselectAll()
        subTreeViews.state = "collapsed"
        revenueItems.state = "collapsed"
        pricing.state = "collapsed"
        tariffAssumption.state = "collapsed"
    }

    function collapse(){
        root.collapseSubSection()
        parentView.collapse()
        root.state = "collapse"
    }

    function show(){
        root.state = "expanded"
    }

    state: "collapsed"

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

        text: "Revenue"

        onSubTreeExpand: {
            subTreeViews.state = "expanded"
            revenueItems.state = "expanded"
            pricing.state = "expanded"
            tariffAssumption.state = "expanded"
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
            id: revenueItems

            text: "revenue items"
            height: implicitHeight; width: implicitWidth

            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: subTreeViews.top
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                pricing.isSelected = false
                tariffAssumption.isSelected = false
                root.revenueItemsSelected()
            }


        }

        LeafDelegate{
            id: pricing

            text: "pricing"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: revenueItems.bottom
            collapsedAnchor.anchors.top: subTreeViews.top   

            onSelected: {
                revenueItems.isSelected = false
                tariffAssumption.isSelected = false
                root.pricingSelected()
            }         
        }

        LeafDelegate{
            id: tariffAssumption

            text: "tariff Assumption"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }
            
            expandedAnchor.anchors.top: pricing.bottom
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                revenueItems.isSelected = false
                pricing.isSelected = false
                root.tariffAssumptionSelected()
            }
        }

    }
}


