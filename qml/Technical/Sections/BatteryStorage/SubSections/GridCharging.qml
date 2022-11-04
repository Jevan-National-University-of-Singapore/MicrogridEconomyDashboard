import "../../../../Templates"


SubSection {
    id: root

    subsection: "Grid Charging"

    LabelledInput {
        id: offPeakElectricityRequired

        label: "Off-peak electricity required"
    }

    LabelledInput {
        id: peakElectricityChargedFromGrid

        label: "Peak electricity charged from grid"
    }

    LabelledInput {
        id: gridElectricityRequired

        label: "Grid electricity required / day"
    }

    LabelledInput {
        id: gridDrawLimit

        label: "Grid draw limit"
    }


}