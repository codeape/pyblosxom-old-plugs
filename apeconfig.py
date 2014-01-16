# -*- coding: iso-8859-1 -*-

apethumbgen_cfg.side = 700.0
apethumbgen_cfg.th_side = 150.0

import Image, ImageDraw, ImageFont

ttf_path  = "/usr/share/fonts/truetype/freefont/FreeSans.ttf"
ttf_size = 12
framesize = (ttf_size + 5) * 2

def oscars_image_hook(self, img) :
    frame = Image.new("RGB",(img.size[0]+framesize,img.size[1]+framesize), (255,255,255))
    area =  ImageDraw.Draw(frame)
    area.rectangle([0,0,frame.size[0]-1,frame.size[1]-1], fill=None, outline=(0,0,0))
    mfont = ImageFont.truetype(ttf_path, ttf_size)
    msgtxt = u"Copyright 2006 \u00A9 You" 
    area.text((3,3), msgtxt, font=mfont, fill=(0,0,0))
    frame.paste(img, (framesize/2,framesize/2))
    return frame

apethumbgen_cfg.after_resize_image_hook = oscars_image_hook
