#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

"""A simple but powerfull image resizer and thumb generator

This is a very simple but powerful script that uses Python Imaging Library
(PIL). The scripts creates two directories (images and thumbs). One
directory for the resized big pictures and one for the thumbs (but keeping
the original pictures where they where found). The program has the following
command line options:

apethumbgen.py <options> dirname

-c  string   configuration file
-sl int      size of longest side (default 640)
-s  int      size of shortest side (overrides longest)
-tl int      size of longest side (thumb, default 64)
-t  int      size of shortest side (thumb, overrides longest)
-n           DO NOT generate index.cfg file for pygallery.py

Normal usage is is simple. Just type: apethumbgen.py <option> dirname.
However, the script can only work on one source directory at a time. 

For example apethumbgen.py -sl 700 -tl 100 images/

If the program is used often you can write a configuration file. In the
configuration file you have the following variables to play with:

* apethumbgen_cfg.side                    (the same as -sl)
* apethumbgen_cfg.side_short              (the same as -s)
* apethumbgen_cfg.th_side                 (the same as -tl)
* apethumbgen_cfg.th_side_short           (the same as -t)
* apethumbgen_cfg.create_index            (the same as -c)
* apethumbgen_cfg.after_resize_image_hook (see bellow)
* apethumbgen_cfg.after_resize_thumb_hook (see bellow)

The hooks are a bit special. These can point to functions that do some extra
formating on the picture after it has bee resized but before the picture is
saved to disk. There is one hook for the big pictures and one for the
thumbs. A hook function MUST ALLWAYS:

* return a Image object.
* have 2 arguments (no more no less)

An example of a config file can look like this (lets call it my.cfg).


#FILE BEGIN
apethumbgen_cfg.side = 640.0
apethumbgen_cfg.th_side = 100.0
import Image, ImageDraw, ImageFont
ttf_path = "/usr/share/fonts/truetype/ttf-dejavu/DejaVuSansCondensed.ttf"
ttf_size = 14 framesize = (ttf_size + 5) * 2
def image_hook(self, img) :
    area = ImageDraw.Draw(img)
    mfont = ImageFont.truetype(ttf_path, ttf_size)
    msgtxt = u"Copyright \u00A9 2006 Oscar Norlander"
    area.text((5,5), msgtxt, font=mfont)
    return img
apethumbgen_cfg.after_resize_image_hook = image_hook
#EOF


In this case the image_hook function prints a text in the upper left corner
before the image is saved to disk. The config file is actually a python
program that is called from apethumbgen.py. So if you can hack python
the sky is the limit.

Lets test the configuration file:
apethumbgen.py -c my.cfg mysrcdir

ToDo
- Make checks of types when using config file
- Make a install part with distutils (if needed)


Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Copyright 2006 Oscar Norlander

AUTHOR: Oscar Norander - oscar-no at codeape dot org

Revisions:
1.0  - (1 Oktober, 2006) Created.
"""

import os, sys
from PIL import Image, ImageDraw

_imagesdir = "./images"
_thumbsdir = "./thumbs"

# This class is used for configuration data
# both internaly and externaly
class apethumbgen_cfg:
    side = 640
    side_short = None
    th_side = 64
    th_side_short = None
    create_index = True
    after_resize_image_hook = None
    after_resize_thumb_hook = None

def _print_help():
    print """apethumbgen.py <options> dirname
    
    -c  string   configuration file
    -sl int      size of longest side (default 640)
    -s  int      size of shortest side (overrides longest)
    -tl int      size of longest side (thumb, default 64)
    -t  int      size of shortest side (thumb, overrides longest)
    -n           DO NOT generate index.cfg file for pygallery.py
    """

def _is_int(val):
    if val.isdigit():
        return int(val)
    else:
        print val + " is not a integer \n"
        _print_help()
        sys.exit(0)

def _save_image(fname, img, big_w, big_h, th_w, th_h):
    print fname + " sizes " + "[" + str(big_w) + "," + str(big_h) + "][" + str(th_w) + "," + str(th_h)+ "]"
    big = img.resize((big_w, big_h), Image.ANTIALIAS)
    thmb = img.resize((th_w, th_h), Image.ANTIALIAS)

    #hook big image
    if apethumbgen_cfg.after_resize_image_hook != None :
        linst = apethumbgen_cfg()
        big = apethumbgen_cfg.after_resize_image_hook(linst,big)

    #hook thumb  
    if apethumbgen_cfg.after_resize_thumb_hook != None :
        linst = apethumbgen_cfg()
        thmb = apethumbgen_cfg.after_resize_thumb_hook(linst,thmb)

    big.save(_imagesdir+"/"+fname)
    thmb.save(_thumbsdir+"/"+fname)

def _handle_item(pdir, fname):
    try:
        im = Image.open(pdir + fname)
    except:
        print pdir + fname + " not a image file (Ignoring file)"
        return ""
    im.load()
    
    bw = 0.00
    bh = 0.00
    tw = 0.00
    th = 0.00
    
    if im.getbbox()[2] > im.getbbox()[3]: #landscape
        if apethumbgen_cfg.side_short != None : #short side big
            bw = float(im.getbbox()[2])/(float(im.getbbox()[3])/float(apethumbgen_cfg.side_short))
            bh = apethumbgen_cfg.side_short
        else: #long side big
            bw = apethumbgen_cfg.side
            bh = float(im.getbbox()[3])/(float(im.getbbox()[2])/float(apethumbgen_cfg.side))

        if apethumbgen_cfg.th_side_short != None : #short side thumb
            tw = float(im.getbbox()[2])/(float(im.getbbox()[3])/float(apethumbgen_cfg.th_side_short))
            th = apethumbgen_cfg.th_side_short
        else: #long side thumb
            tw = apethumbgen_cfg.th_side
            th = float(im.getbbox()[3])/(float(im.getbbox()[2])/float(apethumbgen_cfg.th_side))
    else: #portrait
        if apethumbgen_cfg.side_short != None : #short side big
            bw = apethumbgen_cfg.side_short
            bh = float(im.getbbox()[3])/(float(im.getbbox()[2])/float(apethumbgen_cfg.side_short))
        else: #long side big
            bw = float(im.getbbox()[2])/(float(im.getbbox()[3])/float(apethumbgen_cfg.side))
            bh = apethumbgen_cfg.side

        if apethumbgen_cfg.th_side_short != None : #short side thumb
            tw = apethumbgen_cfg.th_side_short
            th = float(im.getbbox()[3])/(float(im.getbbox()[2])/float(apethumbgen_cfg.th_side_short))
        else: #long side big
            tw = float(im.getbbox()[2])/(float(im.getbbox()[3])/float(apethumbgen_cfg.th_side))
            th = apethumbgen_cfg.th_side
            
    _save_image(fname, im , int(bw), int(bh), int(tw), int(th))
    return str(int(bw)) + "x" + str(int(bh))

def _start():
    i = 1
    flags = True
    while (i < len(sys.argv)) & (flags == True) :
        argtmp = sys.argv[i]
    
        if(argtmp == "-c"):
            i += 1
            if (os.path.isfile(sys.argv[i])):
                execfile(sys.argv[i], globals())
            else:
                _print_help()
                sys.exit(0)
        elif (argtmp == "-sl"):
            i += 1
            apethumbgen_cfg.side =_is_int(sys.argv[i])
        elif (argtmp == "-s"):
            i += 1
            apethumbgen_cfg.side_short = _is_int(sys.argv[i])
        elif (argtmp == "-tl"):
            i += 1
            apethumbgen_cfg.th_side = _is_int(sys.argv[i])
        elif (argtmp == "-t"):
            i += 1
            apethumbgen_cfg.th_side_short = _is_int(sys.argv[i])
        elif (argtmp == "-n"):
            apethumbgen_cfg.create_index = False
        elif (argtmp == "-h"):
            _print_help()
            sys.exit(0)
        else:
            flags = False
    
        if flags :
            i += 1
        
    if flags :
        print "No dir to compute"
        sys.exit(0)

    if i != (len(sys.argv) - 1):
        print "This script can only handle one directory at a time"
        sys.exit(0)
    
    if not(os.path.isdir(sys.argv[i])):
        print sys.argv[i] + " is not a directory"
        sys.exit(0)

    dirpath = sys.argv[i]

    if not os.path.isdir(_imagesdir):
        os.mkdir(_imagesdir)

    if not os.path.isdir(_thumbsdir):   
        os.mkdir(_thumbsdir)

    filelist = os.listdir(sys.argv[i])

    grp_list = "" #for index.cfg
    txt_list = "" #for index.cfg
    for imgfile in filelist :
        txt_list = txt_list + "#" + imgfile + ": \n" 
        grp = _handle_item(os.path.normpath(dirpath) + "/", imgfile)
        grp_list = grp_list + "#" + str(imgfile) + ": " + str(grp) + "\n" 

    #generating index.cfg
    if(apethumbgen_cfg.create_index):       
        cfgfile = open("index.cfg", "w+")
        cfgfile.write("[index] \n")
        cfgfile.write("name: A name \n")
        cfgfile.write("summary: A story \n")
        cfgfile.write("#thumb:  \n")
        cfgfile.write("\n")
        cfgfile.write("[grouplinks] \n")
        cfgfile.write(grp_list)
        cfgfile.write("\n")
        cfgfile.write("[text]\n")
        cfgfile.write(txt_list)

if __name__ == "__main__":
    _start()
