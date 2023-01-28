import Qt3D.Core
import Qt3D.Render
import Qt3D.Input
import Qt3D.Extras
import QtQuick.Scene3D
import QtQuick.Scene2D
import QtQuick as QQ2
import QtQuick3D as QQ3

Entity {
    id: sceneRoot

    Camera {
        id: camera
        projectionType: CameraLens.PerspectiveProjection
        fieldOfView: 500
        nearPlane : 0.1
        farPlane : 1000.0
        position: Qt.vector3d( 0.0, 0.0, 40.0 )
        upVector: Qt.vector3d( 0.0, 1.0, 0.0 )
        viewCenter: Qt.vector3d( 0.0, 0.0, 0.0 )
    }

    FirstPersonCameraController { camera: camera}

    components: [
        RenderSettings {
            activeFrameGraph: ForwardRenderer {
                camera: camera
                clearColor: "transparent"
            }
        },
        InputSettings { }
    ]

    QQ3.Node {
        y: 0
        x: 5
        z: 40
        // eulerRotation.y: -10
        QQ2.Rectangle {
            anchors.horizontalCenter: parent.horizontalCenter
            color: "orange"
            width: 1000
            height: 1000
            QQ2.Text {
                anchors.centerIn: parent
                id: text
                text: "I'm Suzanne"
                font.pointSize: 14
                color: "black"
            }
        }
    }

    Entity {
        id: solarPanelEntity
        

        SceneLoader {
            id: solarPanelLoader
            source: "file:///" + applicationDirPath + "/resources/SolarPanelsCad/10781_Solar-Panels_V1.obj"
        }
        Transform {
            id: solarPanelTransform
            scale3D: Qt.vector3d(1, 1, 1)
            translation: Qt.vector3d(0, 0, -50)
            // rotation: fromAxisAndAngle(Qt.vector3d(1, 0, 0), 45)
        }

        components: [
            solarPanelLoader,
            solarPanelTransform 
        ]
    }

}