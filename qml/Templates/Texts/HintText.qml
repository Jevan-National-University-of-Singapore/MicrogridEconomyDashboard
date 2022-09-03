import QtQuick 2.15
import QtQuick.Controls 2.15

import "../../System"

StandardText {
    id: hint

    opacity: 0.7

    content {

        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignLeft

        font{
            pointSize: FontSettings.hintFontSize
            italic: true
        }
    }


}
