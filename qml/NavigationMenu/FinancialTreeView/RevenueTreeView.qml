import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

import "../Delegates"

Item {
    id: root

    signal fiveYearsLifetimeSelected
    signal perAnnumSelected
    signal tariffAssumptionSelected

    implicitHeight: parentView.height + subTreeViews.height
    width: childrenRect.width

    Behavior on opacity { SmoothedAnimation { velocity: 5 } }
    Behavior on height { SmoothedAnimation { velocity: 200 } }    

    visible: opacity    

    function deselectAll(){
        fiveYearsLifetime.isSelected = false
        perAnnum.isSelected = false
        tariffAssumption.isSelected = false
    }

    function collapseSubSection(){
        root.deselectAll()
        subTreeViews.state = "collapsed"
        fiveYearsLifetime.state = "collapsed"
        perAnnum.state = "collapsed"
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
            fiveYearsLifetime.state = "expanded"
            perAnnum.state = "expanded"
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
            id: fiveYearsLifetime

            text: "5 Years Lifetime"
            height: implicitHeight; width: implicitWidth

            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: subTreeViews.top
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                perAnnum.isSelected = false
                tariffAssumption.isSelected = false
                root.fiveYearsLifetimeSelected()
            }


        }

        LeafDelegate{
            id: perAnnum

            text: "Per Annum"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: fiveYearsLifetime.bottom
            collapsedAnchor.anchors.top: subTreeViews.top   

            onSelected: {
                fiveYearsLifetime.isSelected = false
                tariffAssumption.isSelected = false
                root.perAnnumSelected()
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
            
            expandedAnchor.anchors.top: perAnnum.bottom
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                fiveYearsLifetime.isSelected = false
                perAnnum.isSelected = false
                root.tariffAssumptionSelected()
            }
        }

    }
}


