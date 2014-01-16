"""A guestbook script for pyblosxom

This is a simple guestbook (and my first pyblosxom hack). These
are the features:
  - To post to the guestbook, the user must enter a name and a
    message or else the guestbook entry will not be saved. The
    other fields are not mandatory and don't need to be entered.

  - The guestbook have protection against double posts due to
    reloading of browsers etc.

  - There are two ways to reach the guestbook:
    1).../guestbook/index 2).../guestbook/all (for example
    http://www.codeape.org/cgi-bin/pyblosxom.cgi/guestbook/index
    or http://www.codeape.org/blog/guestbook/index). The index
    link shows the number of entires that is given in the
    config.py (ex. py['num_entries'] = 5) for the blog. The all
    link shows all entries.

  - The message part is striped from all HTML.

  - The message part do not allow the @ character (less spam).

  - The guestbook give feedback about user faults.

  - The guest book has a anti bot spam feature (captcha =
    completely automated public Turing test to tell computers
    and humans apart)

Quick and dirty how-to:
1. Putt pyguest.py in your plug-in directory

2. Add pyguest to your py['load_plug-ins'] property and check that
   your py['base_url'] is set correctly.

3. Add a new property called "guestbookdir" to your config.py.
   This property must point on a directory where you want to keep
   you guestbook entries. Example:

     #A absolute paht to a directory that is NOT reachable from
     #an URL
     py["guestbookdir"] = "/home/myuser/pydata/gb-entries"

   Remember to chmod and chgrp this directory so that the script has
   read, write and execute permissions to it. Example: Apache runs
   as www-data user and group. To make pyguest work on an Apache
   server, you need to set the group of the directory you keep your
   guestbook entries in to www-data (chgrp www-data mydir). You must
   also give the www-data group read write and execute permissions
   on that directory (chmod 775 mydir). 
   
4. Add a file in your datadir (where you have all your templates)
   that is called pyguest_item.flav (exchange flav with the name of
   a real flavor). Now edit that file and make a nice layout for you
   guestbook items. You have some new template variables that you
   can use: $posted_email (the email address in the entry) $posted_url
   (the url in the entry)

5. In your header or footer template add the variable $pyguest_form
   where you want the submit form to show up. The submit form will
   only be shown when the index or all links are executed. The
   pyguest.py plug-in is equipped with it's own form but it is
   recomended that you do you own becuse the builtin form is a bit
   ugly and do not work with the antispam feature. You need to set
   the base_url also to use it. Next step (6) explains how to build
   your own form.
   
6. If you want to fix your own submit form just add a file in your
   datadir that is called pyguest_form.flav (exchange flav with the
   name of a real flavor). Make a nice form that contains at least
   the input fields aname and amsg (the other two are aurl and aemail).
   To get the double posts protection to work you must add this hidden
   field to your form:
   
     <input type="hidden" name="atime" value="$posted_date" />.
   
   To give feedback to the user you can add the variable $gb_msg to
   the template. So, if a user forgets to fill in the name the user
   will be notified about this with a message.

   If you want the captcha to work some more things need to be added to
   this form. But that will be handled later on in this how-to.

   If you want something to copy and paste from, look bellow (There is
   a variable in this plug-in called __BUILTIN_FORM__ that is
   interesting).

7. The captcha functionality requires Python Imaging Library (PIL):

     http://www.pythonware.com/products/pil/

   If you want to enable the captcha functionality you must follow this
   step. However, I would first get pyguest to work without captcha add
   then add it. To use captcha add the following configuration variables
   to your config.py : 

     #guestbookdir_gen = where to generate pictures (absolute directory
     #path that also can be reached by an url)
     py["guestbookdir_gen"] = "/home/myuser/www/gens"  

     #guestbookdir_www = url to generated pictures
     py["guestbookdir_www"] = "http://192.168.0.10/~myuser/gens/" 

     #guestbook_ttf_path = absolute path to a true type font of your
     #choice
     py["guestbook_ttf_path"] = ""

     #guestbook_ttf_size = font size 
     py["guestbook_ttf_size"] = 14

     #guestbook_txt_len  = key length
     py["guestbook_txt_len"] = 10

     #guestbook_colour_bg  = background color (rgb) 
     py["guestbook_colour_bg"] = (000,000,000)

     #guestbook_colour_txt = text color (rgb)
     py["guestbook_colour_txt"] = (255,255,255)

   Then you need to add something like this to your pyguest_form.flav :

     Generated key (for antispam):
     <img src="$gens_path" alt="Key is missing" />  
     <br />
     Rewrite Generated key:
     <input style="width: 93px; font-size: 16px"
     type="text" name="agens" value="" /> 
     <input type="hidden" name="aimg" value="$gens_img" />

   The img tag contains the $gens_path variable. The $gens_path variable
   contains the url to the key image. The first input tag is the field where
   the user will rewrite the generated key and it must be named agens. The
   second input field (must be a hidden field) that must be called aimg and
   contains the $gens_img again. The hidden field is used for the
   validation.

8. Run pyblosxom.cgi from the shell (not the browser) to verify that you
   have all configuration variables set.
   
   Now you are ready to test your guestbook! With the ../guestbook/index
   or/and  ../guestbook/all links. For example:
   http://www.someurlorip.org/cgi-bin/pyblosxom.cgi/guestbook/index
   http://www.someurlorip.org/cgi-bin/pyblosxom.cgi/guestbook/all
   or with flav. :
   http://www.someurlorip.org/cgi-bin/pyblosxom.cgi/guestbook/index.myflav
   http://www.someurlorip.org/cgi-bin/pyblosxom.cgi/guestbook/all.myflav
   (replace www.someurlorip.com with your site =) ).

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

Copyright 2004 Oscar Norlander

Revisions:
1.0  - (23 Oktober, 2004) Created.
1.1  - (27 Oktober, 2004) Added better template variables support
       for the pyguest_form template. Also, now striping HTML from
       all posted data.
1.2  - (22 December, 2004) Documentation updates.
1.3  - (10 August, 2005) Added base_url template variable to
       pyguest_form. Documentation updates.
2.0  - (26 March, 2006) Added anti spam bot stuff (captcha = completely
       automated public Turing test to tell computers and humans apart)
       and @ char filtering. Added documentation.
2.05 - (27 March, 2006) Documentation updates (PIL).
2.06 - (2 April, 2006) Fixed flavour bugs. Documentation updates.
2.07 - (12 April, 2006) Minor documentation updates.
2.08 - (31 May, 2007) Removed trace printout
2.09 - (6 Oct, 2007) Fixed a python 2.5 issue regarding sorting lists.
"""

__author__ = "Oscar Norander - oscar-no at codeape dot org"
__version__ = "2.09"
__url__ = "http://www.codeape.org/blog/static/download"
__description__ = "A guestbook"

import os, os.path, string, md5
import random, sys, time
from Pyblosxom.tools import Stripper
import Pyblosxom.tools
from Pyblosxom.entries.fileentry import FileEntry
from datetime import datetime
import random

__DATA_FLAV__ = "flavour"
__DATA_PDATE__ = "posted_date"
__DATA_GENSIMG__ = "gens_img"
__DATA_GENSPATH__ = "gens_path"
__DATA_URL__ = "base_url"
__DATA_FRM__ = "pyguest_form"
__DATA_DATADIR__ = "root_datadir"
__DATA_MSG__ = "gb_msg"

__CFG_GEN_TPATH__ = "guestbook_ttf_path" 
__CFG_GEN_TSIZE__ = "guestbook_ttf_size"
__CFG_GEN_KLEN__ = "guestbook_txt_len"
__CFG_GEN_BG__ = "guestbook_colour_bg"
__CFG_GEN_FG__ = "guestbook_colour_txt"
__CFG_DATADIR__ = "datadir"
__CFG_BASEURL__ = "base_url"
__CFG_NO_ENTRIES__ = "num_entries"
__CFG_FLAVDIR__ = "flavourdir"
__PROP_DIR__ = "guestbookdir"
__TRIGGER__ = "guestbook"
__GEN_DIR__= "guestbookdir_gen"
__GEN_WWW__= "guestbookdir_www"
__FORM_TEMPLATE__ = "pyguest_form"
__BUILTIN_FORM__ = \
"""
<br />
<b>The fields name and message are mandatory.</b>
<br />&nbsp;                        
<form action="$base_url/guestbook/index" method="post">
   Name: <br /><input type="text" name="aname" value="" /><br />
   Email:<br /><input type="text" name="aemail" value="" /><br />
   URL:<br /><input type="text" name="aurl" value="http://" /><br />
   Message:<br />
   <textarea name="amsg" rows="4" cols="20"></textarea><br />
   <input type="hidden" name="atime" value="$posted_date" />
   <input type="submit" value="Submit" />
   <!-- $gens_path  -->
   <br />
   $gb_msg
   <br />
</form> \n
"""

def verify_installation(req):
    config = req.getConfiguration()

    retval = 1

    #Checks if config.py has a property "guestbookdir". "guestbookdir"
    #describes the path where the guestbook entries are stored. A check
    #to see if the path is valid is also executed.
    if not config.has_key(__PROP_DIR__) :
        print "'- guestbookdir' property is not set in the config file."
        retval = 0
    elif not os.path.isdir(config[__PROP_DIR__]):
        print "- Path '" + config[__PROP_DIR__] + "' for entries do not exist."
        retval = 0

    if config.has_key(__GEN_DIR__) or \
    config.has_key(__GEN_WWW__) or \
    config.has_key(__CFG_GEN_TPATH__) or \
    config.has_key(__CFG_GEN_TSIZE__) or \
    config.has_key(__CFG_GEN_KLEN__) or \
    config.has_key(__CFG_GEN_BG__) or \
    config.has_key(__CFG_GEN_FG__) :
        if not os.path.isdir(config[__GEN_DIR__]) :
            print "- Path '" + config[__GEN_DIR__] + "' for ANTI SPAM  do not exist."
            retval = 0
        else :
            print "- Using ANTI SPAM!"
            
        if not config.has_key(__GEN_WWW__) :
            print "- ANTI SPAM misses the " + __GEN_WWW__ + " URL!"
            retval = 0
            
        if not config.has_key(__CFG_GEN_TPATH__) :
            print "- ANTI SPAM misses the " +__CFG_GEN_TPATH__+ " config variable"
            retval = 0

        if not config.has_key(__CFG_GEN_TSIZE__) :
            print "- ANTI SPAM misses the " +__CFG_GEN_TSIZE__+ " config variable"
            retval = 0

        if not config.has_key(__CFG_GEN_KLEN__) :
            print "- ANTI SPAM misses the " +__CFG_GEN_KLEN__+ " config variable"
            retval = 0

        if not config.has_key(__CFG_GEN_BG__) :
            print "- ANTI SPAM misses the " +__CFG_GEN_BG__+ " config variable"
            retval = 0

        if not config.has_key(__CFG_GEN_FG__) :
            print "- ANTI SPAM misses the " +__CFG_GEN_FG__+ " config variable"
            retval = 0

    return retval

#I simply want that slash in the end of the path.
def fix_local_path(path):
    if not path.endswith("/"):
        path = path + "/"
    return path.replace("/", os.sep)

def createMd5Png(mtext, cfg):
    import Image, ImageDraw, ImageFont #pil
    
    ttf_path = cfg[__CFG_GEN_TPATH__]
    ttf_size = cfg[__CFG_GEN_TSIZE__]
    colour_bg = cfg[__CFG_GEN_BG__]
    colour_txt = cfg[__CFG_GEN_FG__]
    output_dir = fix_local_path(cfg[__GEN_DIR__])
    
    mfont = None
    dummy = Image.new("RGB",(1,1))
    drawdummy = ImageDraw.Draw(dummy)  

    mfont = ImageFont.truetype(ttf_path, ttf_size)
    txt_size =  drawdummy.textsize(mtext, font=mfont)
    txt_size = (txt_size[0] + 4, txt_size[1] + 4)
    im = Image.new("RGB", txt_size, colour_bg)
    
    draw = ImageDraw.Draw(im)
    draw.text((2,2), mtext, font=mfont, fill=colour_txt)

    file_name = md5.new(mtext).hexdigest() + ".png"
    file_path = output_dir + file_name;
    
    im.save(file_path)
    return file_name

def fetchPicName(cfg):
    tmp_path = fix_local_path(cfg[__GEN_DIR__])
    tmp_list = os.listdir(tmp_path)
    tmp_len = len(tmp_list)
    if tmp_len >= 50 :
        for fname in tmp_list :
            os.remove(tmp_path+fname)
    elif tmp_len > 0 :
        for fname in tmp_list :
            fstat = os.stat(tmp_path+fname)
            if time.localtime(fstat.st_mtime + 600) < time.localtime() :
                os.remove(tmp_path+fname)
    
    txt_len = cfg[__CFG_GEN_KLEN__]
    a = ""
    for i in xrange(0, txt_len - 1):
        a = a + "%s" % (random.randint(0, 9))        
    return createMd5Png(a, cfg);

#Load the template for the form used to commit data and stores it in
#variable $pyguest_form
def cb_prepare(args):
    req = args["request"]
    
    pyhttp = req.getHttp()
    data = req.getData()
    config = req.getConfiguration()

    #Checks if this is a valid path for this action.
    if (not pyhttp["PATH_INFO"].startswith("/" + __TRIGGER__ + "/index")) \
           and (not pyhttp["PATH_INFO"].startswith("/" + __TRIGGER__ + "/all")) :
        return

    datadir = config[__CFG_DATADIR__]
    if not datadir :
        return
    datadir = fix_local_path(datadir)

    if config.has_key(__CFG_FLAVDIR__) :
        flpath = config[__CFG_FLAVDIR__]
        flpath = fix_local_path(flpath)
    else:
        flpath = datadir

    #Loads the user specified form template 
    flavour = os.path.split(pyhttp["PATH_INFO"])[1]
    dott_index = flavour.find(".")
    if dott_index == -1 :
        flavour = data[__DATA_FLAV__]
    else:
        flavour = flavour.split(".")[1]
        Pyblosxom.renderers.blosxom.get_flavour_from_dir(flpath,flavour)
        data[__DATA_FLAV__] = flavour

    filename = flpath+__FORM_TEMPLATE__+"."+flavour
    #data["debugprint"] = filename

    #the date used for the dubleposthingy
    data[__DATA_PDATE__] =  str(datetime.today()).replace(" ","_")

    #fixing anti spam stuff (if we use it)     
    if config.has_key(__GEN_DIR__) :
        data[__DATA_GENSIMG__] = fetchPicName(config)
        data[__DATA_GENSPATH__] = config[__GEN_WWW__]+data[__DATA_GENSIMG__]
    else :
        data[__DATA_GENSIMG__] = ""
        data[__DATA_GENSPATH__] = ""
    
    if  config[__CFG_BASEURL__] :
        data[__DATA_URL__] = config[__CFG_BASEURL__]

    #If no user specified form tamplate exists load the default one
    if not os.path.isfile(filename) :
        formdata = __BUILTIN_FORM__
    else :
        formdata = open(filename).read()

    #if template variables exists they are set in the template
    formdata = Pyblosxom.tools.parse(req, "iso-8859-1", data, formdata)

    #adds the from as a variable
    data[__DATA_FRM__] = formdata 

#Creates a unique string by using the current date and time together
#with a md5 checksum on the data that will be stored
#It can operate with a given time string
def unique_filename(astr, adate = None):
    if not adate :
        return string.replace(str(datetime.today()), " ","_")+"_"+str(md5.new(astr).hexdigest())+".pg"
    else :
        return adate+"_"+str(md5.new(astr).hexdigest())+".pg"
        
def already_posted(astr, adate, apath):
    return os.path.isfile(apath+adate+"_"+str(md5.new(astr).hexdigest())+".pg")

def HTMLStrip(str):
    LStrpr = Stripper()
    LStrpr.feed(str)
    return LStrpr.gettext()
        
def save_post(ahttp, path, data, cfg):
    form = ahttp["form"]

    #Check so that we have minimal data
    if not form.getvalue("aname") :
        data[__DATA_MSG__] = "Your name is missing"
        return
    elif not form.getvalue("amsg") :
        data[__DATA_MSG__] = "You have not left a message"
        return

    if cfg.has_key(__GEN_DIR__) :
        tmp_md = form.getvalue("agens")
        tmp_mg = form.getvalue("aimg")
        if (tmp_md != None) and (tmp_mg != None):
            mygen = str(md5.new(tmp_md).hexdigest() + ".png")
            if tmp_mg != mygen :
                data[__DATA_MSG__] = "Wrong key"
                if os.path.isfile(str(fix_local_path(cfg[__GEN_DIR__]) + tmp_mg)) :
                    os.remove(str(fix_local_path(cfg[__GEN_DIR__]) + tmp_mg))
                return

            if not os.path.isfile(str(fix_local_path(cfg[__GEN_DIR__]) + tmp_mg)) :
                data[__DATA_MSG__] = "Session timed out. Try a new key"
                return
            else :
                os.remove(str(fix_local_path(cfg[__GEN_DIR__]) + tmp_mg))
        else :
            data[__DATA_MSG__] = "Wrong code"
            return

    
    #Prepare data for saving it to file
    
    txt = ""
    txt = txt + HTMLStrip(form.getvalue("aname").replace("\n", " ")) + "\n"
    if  form.getvalue("aemail") :
        txt = txt + HTMLStrip(form.getvalue("aemail").replace("\n", " ")) + "\n"
    else :
        txt = txt + "\n"
    if form.getvalue("aurl") :
        if (form.getvalue("aurl") == "http://") or (form.getvalue("aurl") == "") :
            txt = txt + "\n"
        else :
            txt = txt + HTMLStrip(form.getvalue("aurl").replace("\n", " ")) + "\n"
    else :
        txt = txt + "\n"

    if form.getvalue("amsg").find("@") != -1 :
        data[__DATA_MSG__] = "The message contains an @ char. Will not post this."
        return
    txt = txt + HTMLStrip(form.getvalue("amsg").replace("\n", " ")) + "\n"

    #If the submit form has a input with name atime set, checks are done
    #to see if entry is already posted. If post exists entry will not get
    #posted
    strdate = form.getvalue("atime")
    if strdate :
        if already_posted(txt, strdate, path):
            return
        else :
            lfile = open(path+unique_filename(txt, strdate), "w+")
            lfile.write(txt)
            lfile.close         
    else :
        lfile = open(path+unique_filename(txt), "w+")
        lfile.write(txt)
        lfile.close

def cmp_datefloat_cmp(item1, item2):
    return int(item2[0] - item1[0])

def cb_filelist(args):
    req = args["request"]

    pyhttp = req.getHttp()
    data = req.getData()
    config = req.getConfiguration()

    if (pyhttp["PATH_INFO"].startswith("/" + __TRIGGER__ + "/index")) : 
        ShowAll = False
    elif (pyhttp["PATH_INFO"].startswith("/" + __TRIGGER__ + "/all")) :
        ShowAll = True
    else :
        return

    gb_dir = config[__PROP_DIR__]
    if not gb_dir :
        return
    gb_dir = fix_local_path(gb_dir)
    

    if pyhttp["REQUEST_METHOD"] == "POST":
        save_post(pyhttp, gb_dir, data, config) 

    data[__DATA_DATADIR__] = gb_dir
    tmp_list = os.listdir(gb_dir)

    files_list = []
    for itm in tmp_list :
        tmp_tupple = os.stat(gb_dir+itm).st_mtime, itm
        files_list.append(tmp_tupple)
    files_list.sort(cmp_datefloat_cmp)

    if ShowAll == True :
        config[__CFG_NO_ENTRIES__] = len(files_list)
    else :
        del files_list[config[__CFG_NO_ENTRIES__]:len(files_list)]    

    entrylist = []
    for itm in files_list :
        filename = gb_dir+itm[1]
        fe = FileEntry(req, filename, gb_dir)
        entrylist.append(fe)

    if len(entrylist) == 0 :
        entry = Pyblosxom.entries.base.generate_entry(
            req,
            {"title" : "It works!" },
            "This message will disappear after first entry in guestbook",
            None)
        entrylist.append(entry)
    
    return entrylist

#Parser for the .pg file format
def parse(filename, request):
    entryData = {}
    lfile = open(filename, "r").read().split("\n")
    entryData["title"] = lfile[0]
    entryData["posted_email"] = lfile[1]
    entryData["posted_url"] = lfile[2]
    entryData['body'] = lfile[3]
    entryData["template_name"] = "pyguest_item"
    return entryData

def cb_entryparser(entryparsingdict):
    entryparsingdict['pg'] = parse
    return entryparsingdict
