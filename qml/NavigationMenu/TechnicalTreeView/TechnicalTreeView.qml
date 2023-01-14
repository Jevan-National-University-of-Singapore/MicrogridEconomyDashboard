import QtQuick
import QtQuick.Layouts
import QtQuick.Controls.Material

import "../Delegates"

Item {
    id: root
    property alias solarPowerGeneration: solarPowerGeneration

    Column{
        id: subTreeViews

        height: contentHeight; width: contentWidth

        SolarPowerGenerationTreeView {
            id: solarPowerGeneration
            height: implicitHeight; width: implicitWidth
        }

    }
}