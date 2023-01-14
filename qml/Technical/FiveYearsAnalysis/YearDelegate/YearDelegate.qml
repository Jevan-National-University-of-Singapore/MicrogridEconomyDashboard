import QtQuick
import QtQuick.Controls.Material

import "Tables/HourSection"
import "Tables/TotalChargeSupplySection"
import "Tables/DcChargerDemandSection"
import "Tables/StatusSection"

Item {
    id: root

    height: contentHeight

    property alias tables: tables

    Column {
        id: tables
        HourSection {
            id: hourSection

            height: contentHeight
            width: root.width// - label.font.pixelSize
        }

        TotalChargeSupplySection {
            id: totalChargeSupplySection

            height: contentHeight
            width: hourSection.width

            syncView: hourSection
            syncDirection: Qt.Horizontal
        }

        DcChargerDemandSection {
            id: dcChargerDemandSection

            height: contentHeight
            width: hourSection.width

            syncView: hourSection
            syncDirection: Qt.Horizontal
        }

        StatusSection {
            id: statusSection

            height: contentHeight
            width: hourSection.width

            syncView: hourSection
            syncDirection: Qt.Horizontal
        }

    }



}

