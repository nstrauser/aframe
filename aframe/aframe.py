#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PySide2.QtWidgets import QMainWindow, QLabel, QApplication
from PySide2.QtCore import QRect, QCoreApplication, Qt
from PySide2.QtGui import QPixmap,QIntValidator, QDoubleValidator
from ui_loader import load_ui
from camerasettings import Cameras
from framelinesettings import Framelines


class Aframe(QMainWindow, Framelines, Cameras):

    def __init__(self, parent: object = None) -> object:
        QMainWindow.__init__(self, parent)
        load_ui('aframe.ui', self)

        self.cam    = self.cbCameras.currentText()
        self.sensor = self.cbSensor.currentText()
        self.reso   = self.cbReso.currentText()
        self.formt  = self.cbFormat.currentText()

        self.cbCameras.currentIndexChanged.connect(
            lambda: Aframe.default_main_gui(self))

        self.cbSensor.currentIndexChanged.connect(
            lambda: Cameras.sensor_cb_event(self,
            cam=self.cbCameras.currentText(),
            sensor=self.cbSensor.currentText(),
            reso=self.cbReso.currentText(),
            formt=self.cbFormat.currentText()))

        self.cbReso.currentIndexChanged.connect(
            lambda: Cameras.reso_cb_event(self))

        self.cbFormat.currentIndexChanged.connect(
            lambda: Cameras.formt_cb_event(self,
            cam=self.cbCameras.currentText(),
            sensor=self.cbSensor.currentText(),
            reso=self.cbReso.currentText(),
            formt=self.cbFormat.currentText()))

        self.logo = QLabel(self.centralwidget)
        self.logo.setGeometry(QRect(155, 230, 791, 321))
        self.logo.setPixmap(QPixmap("images/aframe_logo.png"))
        self.logo.setObjectName("logo")

        self.dbl_validatorFLA = QDoubleValidator()
        self.leRatioFLALeft.setValidator(self.dbl_validatorFLA)
        self.leRatioFLALeft.setMaxLength(6)

        self.dbl_validatorFLB = QDoubleValidator()
        self.leRatioFLBLeft.setValidator(self.dbl_validatorFLB)
        self.leRatioFLBLeft.setMaxLength(6)

        self.dbl_validatorFLC = QDoubleValidator()
        self.leRatioFLCLeft.setValidator(self.dbl_validatorFLC)
        self.leRatioFLCLeft.setMaxLength(6)

        # ------------ Frameline Events -------------->>>
        self.pbFLA.clicked.connect(
            lambda: Framelines.fl_pushbutton_event(self))

        self.pbFLB.clicked.connect(
            lambda: Framelines.fl_pushbutton_event(self))

        self.pbFLC.clicked.connect(
            lambda: Framelines.fl_pushbutton_event(self))

        self.cbRatioFL.currentIndexChanged.connect(
            lambda: Framelines.fl_ratio_event(
        self, self.cbRatioFL.currentText(),
        fl=Framelines.fl_pushbutton_event(self)))

        self.leScalingFL.textEdited.connect(
            lambda: Framelines.fl_scaling_event(self))

        self.cbCenterMarkerFL.currentIndexChanged.connect(
            lambda: Framelines.fl_center_marker_event(self))

        self.cbStyleFL.currentIndexChanged.connect(
            lambda: Framelines.fl_style_event(self))

        self.cbStyleLenFL.currentIndexChanged.connect(
            lambda: Framelines.fl_style_len_event(self))

        self.cbShadingFL.currentIndexChanged.connect(
            lambda: Framelines.fl_shading_event(self))


    def splash_gui(self):
        return self.logo.show(), self.fCameraSettings.hide(),\
               self.fCenterRatioA.hide(), self.fCenterRatioB.hide(),\
               self.fCenterRatioC.hide(), self.fFrameline.hide(),\
               self.fShading.hide(),self.lFramelineContainer.hide(),\
               self.fRecordingArea.hide(), self.lFLA.hide(), self.lFLB.hide(),\
               self.lFLC.hide(), self.fOffset.hide(), self.fFLStats.hide(),\
               self.fCenterRatioA.hide(), self.fCenterRatioB.hide(),\
               self.fCenterRatioC.hide()

    def default_main_gui(self):
        return self.logo.hide(), self.fCameraSettings.show(),\
               self.fFrameline.show(), self.fShading.hide(),\
               self.lFramelineContainer.show(), self.fRecordingArea.show(),\
               self.lRecordingAreaBG.resize(620, 349), self.lRecordingAreaBG.move(50, 28),\
               self.fOffset.show(), self.fFLStats.show(), self.lFLAText.hide(),\
               self.lFLAScaleText.hide() ,self.lFLBText.hide(), self.lFLBScaleText.hide(),\
               self.lFLCText.hide(), self.lFLCScaleText.hide(), self.fCenterRatioA.hide(),\
               self.fCenterRatioB.hide(), self.fCenterRatioC.hide(),\
               self.pbFLA.setChecked(True), Cameras.camera_defaults(self)

if __name__ == '__main__':
    import sys
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    w = Aframe()
    w.show()
    w.splash_gui()
    sys.exit(app.exec_())
