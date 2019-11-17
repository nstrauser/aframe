from camerasettings import Cameras
from cameraspecs import cb_ratios_l, cb_ratios_r


class Framelines(Cameras):

    def __init__(self, rec_w, rec_h):
        Cameras().__init__()
        self.rec_w = rec_w
        self.rec_h = rec_h

    def fl_pushbutton_event(self):
        print('fl_pushbutton_event')

        self.ratio_text = {"A": (self.leRatioFLALeft, self.leRatioFLARight,),
                      "B": (self.leRatioFLBLeft, self.leRatioFLBRight,),
                      "C": (self.leRatioFLCLeft, self.leRatioFLCRight,)
                      }
        self.ratio_frame = {"A": self.fCenterRatioA,
                       "B": self.fCenterRatioB,
                       "C": self.fCenterRatioC
                       }

        if self.pbFLA.isChecked() == True:
            self.lActiveFL.setStyleSheet('color: rgb(252,52,73);')
            self.lActiveFL.setText('FL: A')
            return "A"

        elif self.pbFLB.isChecked() == True:
            self.lActiveFL.setStyleSheet('color: rgb(0,130,241);')
            self.lActiveFL.setText('FL: B')
            return "B"

        elif self.pbFLC.isChecked() == True:
            self.lActiveFL.setStyleSheet('color: rgb(255,255,0);')
            self.lActiveFL.setText('FL: C')
            return "C"

    def calc_aspect_ratio(self, ratio=''):
        print('calc_aspect_ratio')
        fl_letter = Framelines.fl_pushbutton_event(self)
        show_ratio = {"A": self.fCenterRatioA.show(),
                      "B": self.fCenterRatioB.show(),
                      "C": self.fCenterRatioC.show()}
        s = ratio.split(':')
        rec_wh = Cameras.get_rec_width_height(self)
        rec_w = int(rec_wh[0])
        rec_h = int(rec_wh[1])
        rec_ratio = rec_w / rec_h
        ratio_l = float(s[0])
        ratio_r = float(s[1])
        ratio_lr = ratio_l / ratio_r


    def fl_ratio_event(self, ratio, fl=None):
        rec_wh = Cameras.camera_stats(self)
        rec_w = int(rec_wh[2])
        rec_h = int(rec_wh[3])
        fl_letter = Framelines.fl_pushbutton_event(self)
        self.ratio_frame[fl].show()
        if ratio == "none":
            self.ratio_frame[fl].hide()

        elif ratio == "Custom":
            if self.ratio_text[fl][0].text() in cb_ratios_l:
                return self.ratio_text[fl][0].clear(), \
                       self.ratio_text[fl][1].clear()

            else:
                Framelines.custom_ratio(
                rec_w, rec_h, fl=Framelines.fl_pushbutton_event())

        elif ratio == "1.33:1" or ratio == "1.78:1":
            if ratio == "1.33:1":
                return self.ratio_text[fl][0].setText("1.3333"),\
                       self.ratio_text[fl][1].setText("1"),\
                       "1.3333", "1"

            elif ratio == "1.78:1":
                return self.ratio_text[fl][0].setText("1.7777"), \
                       self.ratio_text[fl][1].setText("1"), \
                       "1.7777", "1"

        else:
            s = ratio.split(":")
            r_left = s[0]
            r_right = s[1]
            return self.ratio_text[fl][0].setText(r_left), \
                   self.ratio_text[fl][1].setText(r_right), \
                   r_left, r_right

    def custom_ratio(self, rec_w, rec_h, fl=""):
        if ratio_l == "" or ratio_r == "":
            pass

        elif ratio_l in cb_ratios_l:
            self.cbRatioFL.setCurrentText('Custom')


    def calc_aspect_ratio(self, ratio_l, ratio_r, fl=None):
        sqze = float(self.cbSqueeze.currentText())
        rec_wh = self.lRecordingArea.text()
        rec_split = rec_wh.split()
        rec_w = int(rec_split[0])
        rec_h = int(rec_split[2])

        if ratio_l in cb_ratios_l or ratio_r in cb_ratios_r:
            pass
        else:
            self.cbRatioFL.setCurrentText("Custom")

        if (rec_w / rec_h) == ((float(ratio_l) / float(ratio_r)) / sqze): # REC RATIO = FL RATIO
            print("rec ratio == fl ratio")

        elif (rec_w / rec_h) > ((float(ratio_l) / float(ratio_r)) / sqze):
            fl_w = rec_h * ((float(ratio_l) / float(ratio_r)) / sqze)
            print(f"{round(fl_w)} x {rec_w}")
            print("rec ratio > fl ratio")

        elif (rec_w / rec_h) < ((float(ratio_l) / float(ratio_r)) / sqze):
            fl_h = rec_w / ((float(ratio_l) / float(ratio_r)) / sqze)
            print(f"{rec_w} x {round(fl_h)}")
            print("rec ratio < fl ratio")
        print(ratio_l, ratio_r, fl, sqze)


    def fl_scaling_event(self):
        print('fl_scaling_event')

    def fl_center_marker_event(self):
        print('fl_center_marker_event')

    def fl_style_event(self):
        print('fl_style_event')

    def fl_style_len_event(self):
        print('fl_style_len_event')
        s_len = self.cbStyleLenFL.currentText()

    def fl_shading_sel(self):
        print('fl_shading_event')
        s = self.cbShadingFL.currentText()
        sha = int(s[0:-1]) / 100
        print(str(sha))

    def fl_line_width(self):
        print('fl_line_width')
        l = self.cbLineWidthFL.currentText()
        l_width = l.split()
        return l_width[0]

    def fl_align_marker(self):
        print('fl_align_marker')
        align_mkr = self.cbAlignFL.currentText()
        if align_mkr == 'Frameline A':
            pass
        elif align_mkr == 'Frameline B':
            pass
        elif align_mkr == 'Frameline C':
            pass
        else:
            pass
