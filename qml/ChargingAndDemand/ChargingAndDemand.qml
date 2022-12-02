import QtQuick
import QtQuick.Controls.Material

import "../Templates"

ScrollView {
    id: root


    UsersPerHourChart {
        id: usersPerHourChart

        anchors {
            horizontalCenter: parent.horizontalCenter

            top: parent.top
        }
    }

    Column{
        id: inputs

        anchors {
            top: usersPerHourChart.bottom
            topMargin: numberOfUsersPerDay.height

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