import QtQuick
import QtCharts
import QtQuick.Controls.Material

// import "../../third_parties/ChartJs2QML/Chart.js" as Chart
// import "../../third_parties/ChartJs2QML/"

import "../Templates"

Card {
    id: surface

	property alias chart: chart

	height: chart.height + surface.radius
	width: chart.width + xAxisTicks.elementWidth + surface.radius

	ChartView {
		id: chart

		title: "Users Per Hour"
		titleColor: Material.foreground
		titleFont {pixelSize: 24}

		anchors {
			top: surface.top

			left: yAxisLabel.left
			leftMargin: yAxisLabel.width-yAxisLabel.font.pixelSize*2
		}
		height: titleFont.pixelSize * 25
		width: height * 2.5

		legend.alignment: Qt.AlignBottom
		backgroundColor: "transparent"
		antialiasing: true
		legend.visible: false

		animationOptions: ChartView.AllAnimations
		

		BarSeries {
			id: barSeries

			function opacity(color, opacity){
				var new_color = Qt.color(color)
				new_color.a = opacity
				return new_color
			}

			BarSet { 
				values: Scenario.chargingAndDemand.usersPerHour 
				color: parent.Material.accent
				borderColor: parent.Material.foreground
			}

			axisX: BarCategoryAxis { 
				id: axisX
				property real opacity: 0.3

				categories: [
					'00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00',
					'12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00'
				]
				labelsColor: "transparent"
				gridLineColor: barSeries.opacity(parent.Material.foreground, axisX.opacity)

			}

			axisY: ValueAxis {
				id: axisY

				property real opacity: 0.3

				min: 0
				max: 1
				tickCount: 2
				labelsColor: parent.Material.foreground
				gridLineColor: barSeries.opacity(parent.Material.foreground, axisX.opacity)
			}
		}
	}

	XAxis {
		id: xAxisTicks
		spacing: (chart.width - (this.elementWidth*25))/25.5

		anchors {
			bottom: xAxisLabel.top
		
			left: chart.left
			leftMargin: this.elementWidth

			horizontalCenter: chart.horizontalCenter
		}
		width: implicitWidth

	}

	Label {
		id: xAxisLabel

		anchors {
			bottom: surface.bottom
			bottomMargin: surface.radius

			horizontalCenter: chart.horizontalCenter
		}

		text: "Time"
		font.pixelSize: 16
	}

	Label {
		id: yAxisLabel

		anchors {
			left: surface.left
			leftMargin: surface.radius

			verticalCenter: chart.verticalCenter
		}

		horizontalAlignment: Text.AlignHCenter

		text: "Number\nof\nUsers"
		font.pixelSize: 16
	}
}
