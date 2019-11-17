from cameraspecs import cam_defaults, cam_settngs


class Cameras:
    def __init__(self, sen_w, sen_h, rec_w, rec_h):
        super().__init__()
        self.cam = self.cbCameras.currentText()
        self.sensor = self.cbSensor.currentText()
        self.reso = self.cbReso.currentText()
        self.formt = self.cbFormat.currentText()
        self.sen_w = sen_w
        self.sen_h = sen_h
        self.rec_w = rec_w
        self.rec_h = rec_h

    def sensor_cb_event(self, cam='', sensor='', reso='', formt=''):
        setting = f"{cam} {sensor} {reso} {formt}"
        setting_sensor = f"{cam} {sensor} {formt}"

        if setting_sensor in cam_settngs:
            self.cbReso.clear()
            self.cbReso.blockSignals(True)
            self.cbReso.addItems(cam_settngs[setting_sensor][2])
            self.cbReso.blockSignals(True)
            print('camerasettings.py: l.24 worked')

        elif setting in cam_settngs:
            self.cbReso.clear()
            self.cbReso.blockSignals(True)
            self.cbReso.addItems(cam_settngs[setting][2])
            self.cbReso.blockSignals(True)
            print('camerasettings.py: l.31 worked')
        else:
            print('sensor_cb_event: Error!')

        Cameras.camera_stats(self)

    def reso_cb_event(self):
        Cameras.camera_stats(self)

    def formt_cb_event(self, cam=None, sensor=None,
                       reso=None, formt=None
                       ):
        if cam is None:
            cam = [str]
        print('formt_cb_event')
        print(cam)
        if cam == 'ALEXA Mini' or cam == 'Amira' or cam == 'ALEXA Mini LF':
            new_reso = f"{cam} {formt}"
            self.cbReso.blockSignals(True)
            self.cbReso.clear()
            self.cbReso.addItems(cam_settngs[new_reso])
            if cam == 'ALEXA Mini' or cam == 'Amira' and formt == "Apple ProRes":
                self.cbReso.setCurrentText('HD')
            print('format changed: ALEXA Mini, Amira: apple prores')

        elif cam == 'ALEXA Classic' or cam == 'ALEXA XT' or cam == 'ALEXA SXT' or cam == 'ALEXA LF' or cam == 'ALEXA 65':
            setting = f"{cam} {sensor} {reso} {formt}"
            setting_sensor = f"{cam} {sensor} {formt}"
            print('formt_cb_event: classic, xt, sxt, lf, 65')
            if setting in cam_settngs:
                print('worked')

            elif setting_sensor in cam_settngs:
                self.cbReso.clear()
                self.cbReso.blockSignals(True)
                self.cbReso.addItems(cam_settngs[setting_sensor][2])
                self.cbReso.blockSignals(True)
                print('formt_cb_changed: Classic, XT, SXT, LF, 65')

        elif cam == 'ALEXA Classic':
            self.cbFormat.blockSignals(True)
            self.cbFormat.clear()
            self.cbFormat.addItem('Apple ProRes')
            print('format changed: Alexa classic')

        Cameras.camera_stats(self)

    def lens_squeeze_event(self):
        cam = self.cbCameras.currentText()
        sensor = self.cbSensor.currentText()
        reso = self.cbReso.currentText()
        formt = self.cbFormat.currentText()
        has_sensor = f"{cam} {sensor} {reso} {formt}"
        no_sensor = f"{cam} {reso} {formt}"

        if cam == "ALEXA Classic" or cam == "ALEXA SXT" or cam == "ALEXA Mini LF" or cam == "ALEXA LF" or cam == "ALEXA 65":
            return self.cbSqueeze.blockSignals(True), \
                   self.cbSqueeze.clear(),\
                   self.cbSqueeze.addItems(cam_defaults[f'{cam} squeeze']), \
                   self.cbSqueeze.blockSignals(False)

        elif cam == "ALEXA XT":
            if has_sensor in cam_settngs == cam_settngs['ALEXA XT 6:5 (4:3 Cropped) 2.6K ARRIRAW']:
                return self.cbSqueeze.blockSignals(True), \
                       self.cbSqueeze.clear(), \
                       self.cbSqueeze.addItems(cam_settngs['ALEXA XT 6:5 (4:3 Cropped) 2.6K ARRIRAW'][3]), \
                       self.cbSqueeze.blockSignals(False)
            else:
                return self.cbSqueeze.blockSignals(True), \
                       self.cbSqueeze.clear(), \
                       self.cbSqueeze.addItems(cam_defaults['ALEXA XT squeeze']), \
                       self.cbSqueeze.blockSignals(False)

        elif cam == "ALEXA Mini":
            self.cbSqueeze.blockSignals(True)
            self.cbSqueeze.clear()
            self.cbSqueeze.addItems(cam_settngs[no_sensor][2])
            self.cbSqueeze.blockSignals(False)

        elif cam == "Amira":
            if self.cbFormat.currentText() == "Apple ProRes":
                self.cbSqueeze.blockSignals(True)
                self.cbSqueeze.clear()
                self.cbSqueeze.addItems(cam_settngs['Amira Apple ProRes'])
                self.cbSqueeze.blockSignals(False)


            elif self.cbFormat.currentText() == "ARRIRAW":
                self.cbSqueeze.blockSignals(True)
                self.cbSqueeze.clear()
                self.cbSqueeze.addItems(cam_settngs['Amira ARRIRAW'])
                self.cbSqueeze.blockSignals(False)

    def camera_stats(self):
        cam = self.cbCameras.currentText()
        sensor = self.cbSensor.currentText()
        reso = self.cbReso.currentText()
        formt = self.cbFormat.currentText()
        no_sensor_settng = f'{cam} {reso} {formt}'
        has_sensor_settng = f'{cam} {sensor} {reso} {formt}'
        self.lCamera.setText(cam)
        print('camera_stats')

        if cam == 'ALEXA Mini' or cam == 'Amira' or cam == 'ALEXA Mini LF':
            if no_sensor_settng in cam_settngs:
                self.sen_w = cam_settngs[no_sensor_settng][0][0]
                self.sen_h = cam_settngs[no_sensor_settng][0][1]
                self.rec_w = cam_settngs[no_sensor_settng][0][2]
                self.rec_h = cam_settngs[no_sensor_settng][0][3]
                self.lActiveSensorArea.setText(f'{self.rec_w} x {self.rec_h} px')
                self.lRecordingArea.setText(f'{self.rec_w} x {self.rec_h} px')
                print('no sensor setting: worked')
                return self.sen_w, self.sen_h, self.rec_w, self.rec_h, \
                       Cameras.calc_mm(self, self.rec_w, self.rec_h),\
                       Cameras.calc_inch(self), print('camera stats: mini, amira, mini lf')

            elif no_sensor_settng is not cam_settngs:
                pass
            else:
                print('camera stats: mini amira mini lf: error!')

        elif cam == 'ALEXA Classic' or cam == 'ALEXA XT' or cam == 'ALEXA SXT' or cam == 'ALEXA LF' or cam == 'ALEXA 65':
            if has_sensor_settng in cam_settngs:
                self.sen_w = cam_settngs[has_sensor_settng][0][0]
                self.sen_h = cam_settngs[has_sensor_settng][0][1]
                self.rec_w = cam_settngs[has_sensor_settng][0][2]
                self.rec_h = cam_settngs[has_sensor_settng][0][3]
                self.lActiveSensorArea.setText(f'{self.sen_w} x {self.sen_h} px')
                self.lRecordingArea.setText(f'{self.rec_w} x {self.rec_h} px')

                return self.sen_w, self.sen_h, self.rec_w, self.rec_h, \
                       Cameras.calc_mm(self, self.rec_w, self.rec_h),\
                       Cameras.calc_inch(self), print('camera stats: classic, xt, sxt, lf, 65')

            else:
                print('camera stats: classic, xt, sxt, lf, 65: error! ')

    def camera_defaults(self):
        cam = self.cbCameras.currentText()
        block = Cameras.block_sigs(self)
        unblock = Cameras.unblock_sigs(self)
        defaults = f"{cam} defaults"
        sqze = f"{cam} squeeze"
        if cam == 'ALEXA Classic' or cam == 'ALEXA XT' or cam == 'ALEXA SXT' or cam == 'ALEXA LF' or cam == 'ALEXA 65':
            self.cbSensor.show()
            self.lSensor.show()
            self.cbFormat.move(180, 40)
            self.lFormat.move(180, 10)
            print('cam settings default')

            if cam == 'ALEXA Classic':
                Cameras.block_sigs(self)
                self.cbSensor.addItems(cam_defaults[defaults][0])
                self.cbReso.addItems(cam_defaults[defaults][1])
                self.cbFormat.addItem('Apple ProRes')
                self.cbSqueeze.addItems(cam_defaults[sqze])
                Cameras.unblock_sigs(self)
                print('cam settings defaults: classic')

            elif cam == 'ALEXA XT':
                Cameras.block_sigs(self)
                self.cbSensor.addItems(cam_defaults[defaults][0])
                self.cbReso.addItems(cam_defaults[defaults][1])
                self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
                self.cbSqueeze.addItems(cam_defaults[sqze])
                Cameras.unblock_sigs(self)
                print('XT')

            elif cam == 'ALEXA SXT':
                Cameras.block_sigs(self)
                self.cbSensor.addItems(cam_defaults[defaults][0])
                self.cbReso.addItems(cam_defaults[defaults][1])
                self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
                self.cbFormat.setCurrentText('ARRIRAW')
                self.cbSqueeze.addItems(cam_defaults[sqze])
                Cameras.unblock_sigs(self)
                print('SXT')

            elif cam == 'ALEXA LF':
                Cameras.block_sigs(self)
                self.cbSensor.addItems(cam_defaults[defaults][0])
                self.cbSensor.setCurrentText(cam_defaults[defaults][0][0])
                self.cbReso.addItem('4K UHD')
                self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
                self.cbFormat.setCurrentText('ARRIRAW')
                self.cbSqueeze.addItems(cam_defaults[sqze])
                Cameras.unblock_sigs(self)
                print('LF')

            elif cam == 'ALEXA 65':
                Cameras.block_sigs(self)
                self.cbSensor.addItems(cam_defaults[defaults])
                self.cbSensor.setCurrentText('Open Gate')
                self.cbReso.addItem('6560 x 3100')
                self.cbFormat.addItem('ARRIRAW')
                self.cbSqueeze.addItems(cam_defaults[sqze])
                Cameras.unblock_sigs(self)
                print('65 ', cam_settngs['ALEXA 65 Open Gate 6560 x 3100 ARRIRAW'][1][0])
        # ---------------------------------------------------------------------------
        elif cam == 'ALEXA Mini' or cam == 'Amira' or cam == 'ALEXA Mini LF':
            print('default mini amira mini lf')
            self.cbSensor.hide()
            self.lSensor.hide()
            self.cbFormat.move(0, 40)
            self.lFormat.move(0, 10)

            if cam == 'ALEXA Mini':
                Cameras.block_sigs(self)
                self.cbReso.addItems(cam_defaults['ALEXA Mini defaults'])
                self.cbReso.setCurrentText('HD')
                self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
                self.cbSqueeze.addItems(cam_defaults[sqze])
                Cameras.unblock_sigs(self)
                print('Mini')

            elif cam == 'Amira':
                Cameras.block_sigs(self)
                self.cbReso.addItems(cam_defaults['Amira defaults'])
                self.cbReso.setCurrentText('HD')
                self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
                self.cbSqueeze.addItems(cam_defaults[sqze])
                Cameras.unblock_sigs(self)
                print('Amira')

            elif cam == 'ALEXA Mini LF':
                Cameras.block_sigs(self)
                self.cbReso.addItems(cam_defaults['ALEXA Mini LF defaults'])
                self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
                self.cbFormat.setCurrentText('ARRIRAW')
                self.cbSqueeze.addItems(cam_defaults[sqze])
                Cameras.unblock_sigs(self)
                print('Mini LF')
        print('now run camera stats')
        Cameras.camera_stats(self)

    def get_rec_width_height(self):
        with_sensor = cam_settngs[f"{self.cam} {self.sensor} {self.reso} {self.formt}"]
        no_sensor = cam_settngs[f"{self.cam} {self.reso} {self.formt} "]
        if with_sensor in cam_settngs:
            return cam_settngs[with_sensor][0][2],\
                   cam_settngs[with_sensor][0][3]

        elif no_sensor in cam_settngs:
            return cam_settngs[no_sensor][0][2],\
                   cam_settngs[no_sensor][0][3]

    def block_sigs(self):
        self.cbSensor.blockSignals(True)
        self.cbReso.blockSignals(True)
        self.cbFormat.blockSignals(True)
        self.cbSqueeze.blockSignals(True)
        self.cbSensor.clear()
        self.cbReso.clear()
        self.cbFormat.clear()
        self.cbSqueeze.clear()

    def unblock_sigs(self):
        self.cbSensor.blockSignals(False)
        self.cbReso.blockSignals(False)
        self.cbFormat.blockSignals(False)
        self.cbSqueeze.blockSignals(False)
    def calc_inch(self):
        m = self.lActiveSensorMM.text()
        mm = m.split()
        inch_w = round((float(mm[0]) / 25.4), 3)
        inch_h = round((float(mm[2]) / 25.4), 3)
        self.lActiveSensorInch.setText(f'{str(inch_w)} x {str(inch_h)} in')

    def calc_mm(self, rec_w, rec_h):
        print('calc mm')
        mm = 0.00825
        mm_w = round((int(rec_w) * mm), 2)
        mm_h = round((int(rec_h) * mm), 2)
        self.lActiveSensorMM.setText(f'{str(mm_w)} x {str(mm_h)} mm')
