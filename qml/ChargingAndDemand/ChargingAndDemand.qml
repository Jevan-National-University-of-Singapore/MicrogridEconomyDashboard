import QtQuick
import QtQuick.Controls.Material

import "Year"
import "../Templates"

ScrollView {
    id: root

    YearSelector {
        id: yearSelector

        anchors {
            top: parent.top
            topMargin: spacing

            horizontalCenter: parent.horizontalCenter
        }

        spacing: additionalNumberOfUsersPerYear.input.font.pixelSize
    }

    SwipeView{
        id: years

        height: root.height - yearSelector.height * 5
        width: root.width

        currentIndex: yearSelector.currentYear

        anchors {
            horizontalCenter: parent.horizontalCenter

            top: yearSelector.bottom
            topMargin: yearSelector.spacing
        }

        Year {
            id: year0

            currentYear: 0    
        }

        Year {
            id: year1

            currentYear: 1
        }

        Year {
            id: year2

            currentYear: 2    
        }

        Year {
            id: year3

            currentYear: 3
        }

        Year {
            id: year4

            currentYear: 4
        }



    }

    LabelledInput {
        id: additionalNumberOfUsersPerYear

        anchors {
            top: years.bottom

            left: parent.left
            leftMargin: font.pixelSize * 8
        }

        label: "additional number of users per year"

        inputText: Scenario.chargingAndDemand.additionalNumberOfUsersPerYear

        input.onEditingFinished: Scenario.chargingAndDemand.additionalNumberOfUsersPerYear = additionalNumberOfUsersPerYear.inputText
    }
}