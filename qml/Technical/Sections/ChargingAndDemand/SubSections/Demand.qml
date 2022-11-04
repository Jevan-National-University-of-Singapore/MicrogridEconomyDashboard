import "../../../../Templates"


SubSection {
    id: root

    subsection: "Demand"

    LabelledInput {
        id: numberOfUsersPerDay

        label: "Number of Users / day"
    }

    LabelledInput {
        id: numberOfUsersPerYear

        label: "Number of Users / year"
    }

    LabelledInput {
        id: socAtEntry

        label: "SoC at entry"
    }

    LabelledInput {
        id: socLimit

        label: "SoC limit"
    }

    LabelledInput {
        id: socToBeCharged

        label: "SoC to be charged"
    }

    LabelledInput {
        id: totalWaitingTime

        label: "Total waiting time"
    }

    LabelledInput {
        id: actualUsersServed

        label: "Actual Users served  / day"
    }

    LabelledInput {
        id: actaulEnergyServed

        label: "Actual energy served / day"
    }

}
