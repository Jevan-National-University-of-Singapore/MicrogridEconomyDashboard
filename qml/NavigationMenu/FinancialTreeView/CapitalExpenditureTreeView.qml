import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

import "../Delegates"

Item {
    id: root

    signal capitalExpenditureItemsSelected
    signal exchangeRateSelected
    signal depreciationSelected

    implicitHeight: parentView.height + subTreeViews.height
    width: childrenRect.width


    visible: opacity    


    Behavior on opacity { SmoothedAnimation { velocity: 5 } }
    Behavior on height { SmoothedAnimation { velocity: 200 } }    

    function deselectAll(){
        capitalExpenditureItems.isSelected = false
        exchangeRate.isSelected = false
        depreciation.isSelected = false
    }

    function collapseSubSection(){
        root.deselectAll()
        subTreeViews.state = "collapsed"
        capitalExpenditureItems.state = "collapsed"
        exchangeRate.state = "collapsed"
        depreciation.state = "collapsed"
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

        text: "Capital Expenditure"

        onSubTreeExpand: {
            subTreeViews.state = "expanded"
            capitalExpenditureItems.state = "expanded"
            exchangeRate.state = "expanded"
            depreciation.state = "expanded"
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
            id: capitalExpenditureItems

            text: "Capital Expenditure Items"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: subTreeViews.top
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                exchangeRate.isSelected = false
                depreciation.isSelected = false
                root.capitalExpenditureItemsSelected()
            }
        }

        LeafDelegate{
            id: exchangeRate

            text: "Exchange Rate"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }

            expandedAnchor.anchors.top: capitalExpenditureItems.bottom
            collapsedAnchor.anchors.top: subTreeViews.top   

            onSelected: {
                capitalExpenditureItems.isSelected = false
                depreciation.isSelected = false
                root.exchangeRateSelected()
            }         
        }
        LeafDelegate{
            id: depreciation

            text: "Depreciation"
            height: implicitHeight; width: implicitWidth
            
            anchors {
                left: parent.left
                
                top: subTreeViews.top
            }
            
            expandedAnchor.anchors.top: exchangeRate.bottom
            collapsedAnchor.anchors.top: subTreeViews.top

            onSelected: {
                capitalExpenditureItems.isSelected = false
                exchangeRate.isSelected = false
                root.depreciationSelected()
            }
        }


    }
}


