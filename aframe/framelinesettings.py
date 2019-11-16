from camerasettings import Cameras


class Framelines(Cameras):
    def __init__(self, rec_w, rec_h):
        Cameras().__init__()
        self.rec_w = rec_w
        self.rec_h = rec_h

    def fl_pushbutton_event(self):
        print('fl_pushbutton_event')
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
        fl_letter = Framelines.fl_pushbutton_event(self)
        show_ratio = {"A": self.fCenterRatioA.show(),
                      "B": self.fCenterRatioB.show(),
                      "C": self.fCenterRatioC.show()}
        print('calc_aspect_ratio')
        s = ratio.split(':')
        rec_wh = Cameras.get_rec_width_height(self)
        rec_w = int(rec_wh[0])
        rec_h = int(rec_wh[1])
        rec_ratio = rec_w / rec_h
        ratio_l = float(s[0])
        ratio_r = float(s[1])
        ratio_lr = ratio_l / ratio_r
        if ratio_l == 1.33:
            pass

        elif ratio_l == 1.78:
            pass

    def fl_ratio_event(self, ratio, fl=''):
        sqze = float(self.cbSqueeze.currentText())
        rec_wh = Cameras.camera_stats(self)
        rec_w = int(rec_wh[2])
        rec_h = int(rec_wh[3])
        fl_letter = Framelines.fl_pushbutton_event(self)
        ratio_text = {"A": (self.leRatioFLALeft,
                            self.leRatioFLARight,),
                      "B": (self.leRatioFLBLeft,
                            self.leRatioFLBRight,),
                      "C": (self.leRatioFLCLeft,
                            self.leRatioFLCRight,)
                      }
        ratio_frame = {"A": self.fCenterRatioA,
                       "B": self.fCenterRatioB,
                       "C": self.fCenterRatioC
                       }
        ratio_l = float(ratio_text[fl_letter][0].text())
        ratio_r = float(ratio_text[fl_letter][1].text())

        if ratio == 'none':
            hide_ratio[fl_letter]

        if ratio == 'Custom':
            if ratio_text[fl_letter][0].text() == "0.00" or ratio_text[fl_letter][1].text() == "0":
                pass
            else:
                print(fl_ratio = (rec_w / sqze) / (ratio_l / ratio_r))

        s = ratio.split(':')
        r_left = s[0]
        r_right = s[1]

        if ratio == "1.33:1":
            ratio_frame[fl_letter].show()
            l = ratio_text[fl_letter][0]
            r = ratio_text[fl_letter][1]
            return l.setText("1.3333"), r.setText("1")

        elif ratio == "1.78:1":
            ratio_frame[fl_letter].show()
            l = ratio_text[fl_letter][0]
            r = ratio_text[fl_letter][1]
            return l.setText("1.7777"), r.setText("1")

        else:
            self.leRatioFLALeft.setText(r_left)
            self.leRatioFLARight.setText(r_right)

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
