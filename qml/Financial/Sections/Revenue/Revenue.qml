import QtQuick.Layouts

import "../../../Templates"
import "../../../Templates/Separators"
import "SubSections"


Section {
    id: root

    section: "Revenue"

    ColumnLayout {
        id: column1

        spacing: root.height/40

        FiveYearLifetime {
            id: fiveYearLifetime
        }

        HorizontalSeparator {
            id: fiveYearLifetimeSeparator

            Layout.alignment: Qt.AlignCenter
            Layout.preferredWidth: 200
        }

        PerAnnum {
            id: perAnnum
        }

    }

    VerticalSeparator {
        id: column1Separator

        anchors {
            left: column1.right
            leftMargin: column1.width/4

            verticalCenter: column1.verticalCenter
        }

        length: column1.height/1.2
    }

    TariffAssumption {
        id: tariffAssumption 

        anchors {
            left: column1Separator.right
            leftMargin: column1.width/20
        }

    }

}