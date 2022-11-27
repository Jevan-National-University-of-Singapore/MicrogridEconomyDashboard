import QtQuick
import QtQuick.Controls.Material

import "../Templates"

Item {
    id: root
    // onVisibleChanged: {
    //     if (visible){
    //         usersPerHourChart.chart.animateToNewData()
    //     }
    // }

    UsersPerHourChart {
        id: usersPerHourChart

        height: root.height/1.5
        width: root.width/1.8

        anchors {
            horizontalCenter: root.horizontalCenter

            top: root.top
            topMargin: height/20
        }
    }

    Column{
        id: inputs

        anchors {
            top: usersPerHourChart.bottom
            topMargin: usersPerHourChart.anchors.topMargin

            left: usersPerHourChart.left
        }

        LabelledInput {
            id: numberOfUsersPerDay

            label: "number of users per day"

            inputText: Scenario.chargingAndDemand.numberOfUsersPerDay

            input.onEditingFinished: Scenario.chargingAndDemand.numberOfUsersPerDay = numberOfUsersPerDay.inputText
        }

        LabelledInput {
            id: additionalNumberOfUsersPerYear

            label: "additional number of users per year"

            inputText: Scenario.chargingAndDemand.additionalNumberOfUsersPerYear

            input.onEditingFinished: Scenario.chargingAndDemand.additionalNumberOfUsersPerYear = additionalNumberOfUsersPerYear.inputText
        }
    }


}