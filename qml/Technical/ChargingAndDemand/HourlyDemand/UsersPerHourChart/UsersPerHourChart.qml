import QtQuick
import QtQuick.Controls.Material

import "../../../../Templates"

Item {
    id: root

    property int currentYear: 0

    height: contentItem.height
    width: contentItem.width

    UsersPerHourChartPlot {
        id: usersPerHourChart

        currentYear: root.currentYear

        anchors {
            horizontalCenter: parent.horizontalCenter

            top: parent.top
        }
    }


    LabelledText {
        id: numberOfUsersPerDay

        labelText: "number of users per day"

        text: Scenario.years[Scenario.currentYearIndex].technical.chargingAndDemand.demand.numberOfUsersPerDay

        anchors {
            top: usersPerHourChart.bottom
            topMargin: numberOfUsersPerDay.height

            left: usersPerHourChart.left
        }
    }


    


}