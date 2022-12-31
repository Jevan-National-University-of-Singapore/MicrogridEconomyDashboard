    import QtQuick
    import QtQuick.Controls.Material


    Row {
        id: root

        property int currentYear: 0

        // anchors.horizontalCenter: parent.horizontalCenter

        Button {
            id: previous

            enabled: root.currentYear !== 0

            height: year.height; width: height

            contentItem: Label {
                text: "‹"

                font.pixelSize: year.font.pixelSize

                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter

                bottomPadding: font.pixelSize/4

            }

            onClicked: root.currentYear -= 1

        }

        Label {
            id: year

            text: qsTr("Year %1").arg(root.currentYear + 1)

            height: implicitHeight; width: implicitWidth

            font.pixelSize: root.spacing * 2

            verticalAlignment: Text.AlignVCenter
            horizontalAlignment: Text.AlignHCenter

        }

        Button {
            id: next

            enabled: root.currentYear !== 4

            width: previous.width; height: previous.height

            contentItem: Label {
                text: "›"

                font.pixelSize: year.font.pixelSize

                verticalAlignment: Text.AlignVCenter
                horizontalAlignment: Text.AlignHCenter

                bottomPadding: font.pixelSize/4

            }

            onClicked: root.currentYear += 1
        }
    }