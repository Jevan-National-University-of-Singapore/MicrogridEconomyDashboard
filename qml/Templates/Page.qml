import QtQuick
import QtQuick.Controls.Material

ScrollView {
    id: root

    contentHeight: page.height + root.bottomMargin
    contentWidth: page.width

    property real bottomMargin: 0

    default property alias data: page.data

    Item {
        id: page

        height: childrenRect.height
        width: childrenRect.width
    }
}