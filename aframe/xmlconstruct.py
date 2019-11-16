#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from bs4 import Comment
from cameraspecs import cam_settngs
from aframe import Aframe

_cam = self.cbCameras

soup = bs("<framelines></framelines>", "xml")

cam_mu = bs(f"<b><!--Frameline definition for {self.cbCameras.currentText()}--></b>")
cam_cmt = soup.b.string
type(cam_cmt)

soup.framelines.append(soup.new_tag("camera"))
fl = soup.framelines
fl.camera.append(soup.new_tag("type"))
fl.camera.type.string = self.cbCameras.currentText()
fl.camera.append(soup.new_tag("sensor"))
fl.camera.type.string = self.cbCameras.currentText()
fl.camera.append(soup.new_tag("aspect"))
fl.camera.type.string = self.cbCameras.currentText()
fl.camera.append(soup.new_tag("hres"))
fl.camera.type.string = self.cbCameras.currentText()
fl.camera.append(soup.new_tag("vres"))
fl.camera.type.string = self.cbCameras.currentText()
