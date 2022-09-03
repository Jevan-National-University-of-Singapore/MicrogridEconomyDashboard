/****************************************************************************
**
**     Copyright (c)  2022  JAVERN GOH.
** Permission is granted to copy, distribute and/or modify this document
** under the terms of the GNU Free Documentation License, Version 1.3
** or any later version published by the Free Software Foundation;
** with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
** A copy of the license is included in the section entitled "GNU
** Free Documentation License".
**
** Contact: javerngoh@gmail.com
**
****************************************************************************/

pragma Singleton

import QtQuick 2.15

Item {
    id: system

    //images used by the application system (primarily for system icons, not for database)

    // generate new directory for new set of captured images from a toolbox
    // captured images format: toolboxInventory/X_YYMMDD_HHMM_AIM01_employeeID
    function newDateTimeString(){
        return String(Qt.formatDateTime(new Date(), "yyMMdd_hhmm"))
    }

    //Permissions
    property var permissionsNameList: [
        "android.permission.READ_EXTERNAL_STORAGE",
        "android.permission.WRITE_EXTERNAL_STORAGE"
    ]


}
