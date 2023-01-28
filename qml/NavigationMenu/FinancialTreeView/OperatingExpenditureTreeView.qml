import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

import "../Delegates"

Item {
    id: root

    signal operatingExpenditureItemsSelected
    signal fixedOAndMSelected

    implicitHeight: parentView.height + subTreeViews.height
    width: childrenRect.width

    visible: opacity    

    Behavior on opacity { SmoothedAnimation { velocity: 5 } }
    Behavior on height { SmoothedAnimation { velocity: 200 } }   


    function deselectAll(){
        operatingExpenditureItems.isSelected = false
        fixedOAndM.isSelected = false
    }

    function collapseSubSection(){
        root.deselectAll()
        subTreeViews.state = "collapsed"
        operatingExpenditureItems.state = "collapsed"
        fixedOAndM.state = "collapsed"
    }

    function collapse(){
        root.collapseSubSection()
        parentView.collapse()
        root.state = "collapsed"
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

        // height: implicitHeight; width: implicitWidth
        text: "Operating Expenditure"

        onSubTreeExpand: {
            subTreeViews.state = "expanded"
            operatingExpenditureItems.state = "expanded"
            fixedOAndM.state = "expanded"
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
            id: operatingExpenditureItems

            text: "Operating Expenditure Items"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: subTreeViews.top
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                fixedOAndM.isSelected = false
                root.operatingExpenditureItemsSelected()
            }


        }

        LeafDelegate{
            id: fixedOAndM

            text: "Fixed O\&&M"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: operatingExpenditureItems.bottom
            collapsedAnchor.anchors.top: subTreeViews.top   

            onSelected: {
                operatingExpenditureItems.isSelected = false
                root.fixedOAndMSelected()
            }         
        }

    }
}


