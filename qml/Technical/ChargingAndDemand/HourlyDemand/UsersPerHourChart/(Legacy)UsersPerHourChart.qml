import QtQuick
import QtQuick.Controls.Material

import "../../third_parties/ChartJs2QML/Chart.js" as Chart
import "../../third_parties/ChartJs2QML/"

import "../Templates"

Card {
    id: surface

	property alias chart: canvasBars

	Connections {
		id: updateChart

		target: Scenario.chargingAndDemand

		function onUsersPerHourChanged(){
			canvasBars.chartData.datasets[0].data = Scenario.chargingAndDemand.usersPerHour
			canvasBars.animateToNewData()
		}
	}

    Chart {
		id: canvasBars
		chartType: "bar"

		// anchors.fill: surface
		anchors.centerIn: surface
		height: surface.height/1.1
		width: surface.width/1.1

		chartData: { return {
				labels: [
					'00:00',
					'01:00',
					'02:00',
					'03:00',
					'04:00',
					'05:00',
					'06:00',
					'07:00',
					'08:00',
					'09:00',
					'10:00',
					'11:00',
					'12:00',
					'13:00',
					'14:00',
					'15:00',
					'16:00',
					'17:00',
					'18:00',
					'19:00',
					'20:00',
					'21:00',
					'22:00',
					'23:00'
				],
				datasets: [{
					backgroundColor: Material.color(Material.Green).toString(),
					data: Scenario.chargingAndDemand.usersPerHour
				}]
			}

		}

		chartOptions: { return {
				maintainAspectRatio: false,
				title: {
					display: true,
					text: 'Users Per Hour',
					fontColor: Material.foreground.toString(),
					fontSize: 24
				},
				tooltips: {
					mode: 'index',
					intersect: false
				},
				legend: {
					display: false
				},
				scales: {
					xAxes: [{
						gridLines: {
							color: 'rgba(255,255,255, 0.2)',
						},
						scaleLabel: {
							display: true,
							labelString: 'time/hr',
							fontSize: 18
						}
					}],
					yAxes: [{
						gridLines: {
							color: 'rgba(255,255,255, 0.2)',
						},
						scaleLabel: {
							display: true,
							labelString: 'number of users',
							fontSize: 18
						},
						ticks: {
							// max: 2,
							stepSize: 1
						}
					}]
				},
				responsive: true,
			}
		}
	}
    // Component.onCompleted: Chart.defaults.global.defaultFontColor = "#ff0000"
}
