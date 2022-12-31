import QtQuick
import QtQuick.Controls.Material

import "../../Templates"

Item {
    id: root

    property int currentYear: 0

    height: contentItem.height
    width: contentItem.width

    UsersPerHourChart {
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

        text: Scenario.chargingAndDemand.years[root.currentYear].numberOfUsersPerDay

        anchors {
            top: usersPerHourChart.bottom
            topMargin: numberOfUsersPerDay.height

            left: usersPerHourChart.left
        }
    }


    


}