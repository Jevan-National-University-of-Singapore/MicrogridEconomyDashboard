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
    id: defaultFontSettings

    //font sizes
    property int fontSize: 32
    property int largeFontSize: 40
    property int smallFontSize: 28
    property int hintFontSize: 24

    property int headerFontSize: 28
    property int detailFontSize: 20

    property int menuHeaderFontSize: 34
    property int menuListFontSize: 30

    property int toolboxFontSize: 28
    property int currentDrawerFontSize: 28
    property int nonCurrentDrawerFontSize: 16

    property int warningDialogHeaderFontSize: 26

    property int previewFontSize: 24
    property int previewDetailFontSize: 20

    //font family
    property string fontFamily: "Helvetica Neue"


}
