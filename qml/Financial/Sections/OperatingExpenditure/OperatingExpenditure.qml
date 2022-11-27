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
            leftMargin: operatingExpenditureItems.width/8
            verticalCenter: operatingExpenditureItems.verticalCenter
        }

        length: operatingExpenditureItems.height/1.2
    }


    FixedOAndM {
        id: fixedOAndM

        anchors {
            left: operatingExpenditureItemsSeparator.right
            leftMargin: fixedOAndM.width/8
        }
    }

}