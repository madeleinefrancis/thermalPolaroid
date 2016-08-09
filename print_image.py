#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import sys, os
from printer import ThermalPrinter

def resizeimage (im):

    maxW = 384


    width, height = im.size

    height = height + 0.0

    width = width + 0.0

    ratio = (maxW / width)

    newWidth = maxW

    newHeight = int(height * ratio)

    size = newWidth, newHeight

    im.thumbnail(size)

    im.save("thumbnail.png", "PNG")

    return im 


def capture(image):
    serialport = ThermalPrinter.SERIALPORT

    if not os.path.exists(serialport):
        sys.exit("ERROR: Serial port not found at: %s" % serialport)

    p = ThermalPrinter(serialport=serialport)
    i = image
    i = resizeimage(i)
    data = list(i.getdata())
    w, h = i.size
    p.print_bitmap(data, w, h, True)
    p.linefeed(2)




    
