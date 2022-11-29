import "../../../Templates"
import "../../../Templates/Separators"
import "SubSections"

Section {
    id: root

    section: "Operating Expenditure"

    OperatingExpenditureItems {
        id: operatingExpenditureItems
    }

    VerticalSeparator {
        id: operatingExpenditureItemsSeparator

        anchors {
            left: operatingExpenditureItems.right
            leftMargin: operatingExpenditureItems.label.font.pixelSize

            verticalCenter: operatingExpenditureItems.verticalCenter
        }

        length: operatingExpenditureItems.height - operatingExpenditureItems.label.font.pixelSize
    }


    FixedOAndM {
        id: fixedOAndM

        anchors {
            left: operatingExpenditureItemsSeparator.right
            leftMargin: fixedOAndM.label.font.pixelSize
        }
    }

}