import QtQuick 2.15

import Templates 1.0
import Assets 1.0 as Assets

StandardImage{
    id: fullImage

    image {
        source: Assets.Drawer.capturedImagePath
        autoTransform: true
    }
}

