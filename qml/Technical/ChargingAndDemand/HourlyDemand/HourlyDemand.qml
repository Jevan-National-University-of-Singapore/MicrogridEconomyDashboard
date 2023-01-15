import QtQuick
import QtQuick.Controls.Material

import "UsersPerHourChart"
import "../../../Templates" as Templates

Templates.Page {
    id: root

    contentHeight: childrenRect.height
    contentWidth: childrenRect.width
    

    UsersPerHourChart {
        id: usersPerHourChart

        anchors {
            horizontalCenter: parent.horizontalCenter

            top: parent.top
            topMargin: Qt.application.font.pixelSize
        }
    }



    Templates.LabelledInput {
        id: additionalNumberOfUsersPerYear

        anchors {
            top: usersPerHourChart.bottom

            left: parent.left
            leftMargin: Qt.application.font.pixelSize
        }

        label: "additional number of users per year"

        inputText: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.additionalNumberOfUsersPerYear

        input.onEditingFinished: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.additionalNumberOfUsersPerYear = additionalNumberOfUsersPerYear.inputText
    }

}