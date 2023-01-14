import QtQuick
import QtQuick.Controls.Material

ToolButton {
    id: root

    property bool isSelected: false
    down: isSelected

    implicitHeight:Qt.application.font.pixelSize * 2

    property alias expandedAnchor:expandedAnchor
    property alias collapsedAnchor:collapsedAnchor

    visible: opacity

    signal selected

    state: "collapsed"

    MouseArea {
        anchors.fill: parent

        onClicked: {
            root.selected()
            root.isSelected = true
        }
    }

    states: [
        State {
            name: "expanded"
            AnchorChanges { 
                id: expandedAnchor

                target: root
            }

            PropertyChanges {
                target: root

                opacity: 1
            }
        },
        State {
            name: "collapsed"
            AnchorChanges { 
                id: collapsedAnchor

                target: root
            }

            PropertyChanges {
                target: root

                opacity: 0
            }
        }
    ]

    transitions: Transition {
        AnchorAnimation { duration: 150 }
    }

    Behavior on opacity { SmoothedAnimation { velocity: 8 } }



}