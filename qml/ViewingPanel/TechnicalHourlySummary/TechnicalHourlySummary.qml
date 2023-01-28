import QtQuick
import QtQuick.Controls.Material
import QtQuick.Layouts

import "../../Templates" as Templates

import "HourSection"
import "TotalChargeSupplySection"
import "DcChargerDemandSection"
import "StatusSection"



Templates.Page{
    id: root

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