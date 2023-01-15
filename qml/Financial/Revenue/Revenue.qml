import QtQuick.Layouts

import "../../../Templates"
import "../../../Templates/Separators"
import "SubSections"


Section {
    id: root

    section: "Revenue"

    ColumnLayout {
        id: column1

        spacing: fiveYearLifetime.label.font.pixelSize

        FiveYearLifetime {
            id: fiveYearLifetime
        }

        HorizontalSeparator {
            id: fiveYearLifetimeSeparator

            Layout.alignment: Qt.AlignCenter

            length: fiveYearLifetime.width - column1.spacing
        }

        PerAnnum {
            id: perAnnum
        }

    }

    VerticalSeparator {
        id: column1Separator

        anchors {
            left: column1.right
            leftMargin: column1.spacing

            verticalCenter: column1.verticalCenter
        }

        length: column1.height - column1.spacing
    }

    TariffAssumption {
        id: tariffAssumption 

        anchors {
            left: column1Separator.right
            leftMargin: tariffAssumption.label.font.pixelSize
        }

    }

}