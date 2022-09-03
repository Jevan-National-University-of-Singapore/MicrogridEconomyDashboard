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

QtObject {

    //System
    property string rootColor: "black"


    //Surfaces
    property string surfaceColor: "#272727"
    property string accentColor: "white"
    
    //dialog
    property string dialogColor: "#474747"
    property string dialogHeaderColor: "#232323"
    property string dialogFooterColor: "#232323"
    property string dialogInputSurfaceColor: "#121212"

    property string boxColor: "#121212"
    property string headerColor: "#232323"

    property string boundingBorderColor: "white"

    //status
    property string warningColor: "red"
    property string validColor: "#1de9b6"

    //Buttons
    property string buttonColor: "#272727"
    property string buttonPressedColor: "#171717"
    property string dialogButtonColor: "#121212"

    //text
    property string textColor: "white"
    property string headerTextColor: "lightsteelblue"
    property string buttonTextColor: "white"

    property string warningTextColor: "red"

    //targets
    property string boundingBoxColor: "red"

}
