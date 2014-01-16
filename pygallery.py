""" A gallery script for pyblosxom

QUIK HOWTO

1. Create the following templates (with your flavor suffix) pygallery_index,
pygallery_thumbs, pygallery_image. The following template variables are
availible:

* pygallery_index
   - $body : contains the list of galleries

* pygallery_thumbs
   - $title :  contains the thumb group name (if any)
   - $body : contains the list of thumbs

* pygallery_image
   - $title: file name
   - $image_url: the url to the image
   - $next: the url to the next image
   - $prev: the url to the previus image
   - $summary: a little text you have written

2. The following variables must be set in your pybloxsom config.py file:

py["pygallery_dirpath"] = "/home/myaccount/www/gallery" #file system
py["pygallery_url"] = "http://myurl.com/gallery" #URL

The pygallery_dirpath configuration variable must point on a place in the
file system that can be read from your web server. The variable
pygallery_dirpath points to the root of your galleries.  This root must
contain one directory (one gallery) at least, however it can contain several
directories (many galleries). Every gallery directory must contain one
directory that is called thumbs (the small images) and one that is called
images (the big images). 

pygallery_dirpath must be set to point to the root url of your galleries.

3. Create your first three galleries (summer2005, newyear2005 and summer2006)!
For example:

   mkdir /home/myaccount/www/gallery
   mkdir /home/myaccount/www/gallery/summer2005 
   mkdir /home/myaccount/www/gallery/summer2005/thumbs
   mkdir /home/myaccount/www/gallery/summer2005/images
   mkdir /home/myaccount/www/gallery/newyear2005
   mkdir /home/myaccount/www/gallery/newyear2005/thumbs
   mkdir /home/myaccount/www/gallery/newyear2005/images
   mkdir /home/myaccount/www/gallery/summer2006 
   mkdir /home/myaccount/www/gallery/summer2006/thumbs
   mkdir /home/myaccount/www/gallery/summer2006/images
   

Then copy your big pictures to the new image directories and the thumbs to
the thumbs directories. OBSERVE.!!  the thumbs and the images must have
matching names. So if you have a picture called mycomputer.jpg in the image
directory, you must have a  mycomputer.jpg in the thumbs directory.

4. Test your gallery! For example :

   http://myurl.com/gallery/cgi-bin/pyblosxom.cgi/pygallery/index

Observe that you must write pygallery in the end of the the url. 

5. pygallery has 3 levels. The first level is the galleries list, The second
level is the thumbs section and the third level is the big image. What if
you do not like for example the look of the gallery list items or that there
are 5 thumbs on a row and that yo want a to use HTML table tags in the
beginning and the end of a thumb row? Well then you should read the
CONFIGURATION OPTIONS section. 

6. In the default gallery list the name used for each gallery is the
directory names you gave them (for example summer2005) and does not contain
any summary text and other fun stuff. However this is fixed by placing an
index.cfg file in those galleries you need them in. This is described in the
chapter INDEX.CFG section.

7. If you want to sort your items in the galleries list add the file dirlist.cfg
to your root of your galleries. Type in the directory names in the order you
want them to be listed, separated with new lines and you have a new order. If
you have a dirlist.cfg file ,only directories listed in the file will show up in
the galleries list. Here is an example:

   touch /home/myaccount/www/gallery/dirlist.cfg
   echo "summer2005" >> /home/myaccount/www/gallery/dirlist.cfg
   echo "newyear2005" >> /home/myaccount/www/gallery/dirlist.cfg

If you have the directories summer2005, newyear2005 and summer2006 the above
example would mean that you only show gallery summer2005 and newyear2005 in the
list and in that order.

8. The thumbs are not the only things that can be grouped! You can also group
galleries in the dirlist.cfg (you need to add one more template to use this called
pygallery_group). To do that you just put a label enclosed with brackets before the
directory names that are in the same group like this:

[Family]
summer2005
newyear2005
[Parties]
lanparty1
lanparty2
bithday2005

It is possible to use ordinary index and grouped index at the same time because the
use of different url paths. For example:

* Ordinary index: http://myurl.com/gallery/cgi-bin/pyblosxom.cgi/pygallery/index
* Grouped index: http://myurl.com/gallery/cgi-bin/pyblosxom.cgi/pygallery/groups

In the ordinary index case the groups are ignored but the order of the galleries are
still taken in consideration.

The url to the ordinary index ends with index in the url and the grouped index ends
with groups in the utl. To only view the galleries in a group the url must end with
the word group and the name of the group:

* http://myurl.com/gallery/cgi-bin/pyblosxom.cgi/pygallery/group/Family

Observe the difference between the url containing groups (the group index) and group
(the group).

* pygallery_index
   - $body : contains the list of galleries
   - $grp_name: contains the name of the group
   - $grp_url:  contains the url to the group

The template pygallery_group have two additional template variables than
pygallery_index. It has been designed with flexibility in mind. For example if you
only want to list the names of the groups and the url to the groups, skip the  $body
template variable. If you want to list all groups and images then you probably do not
need the  $grp_url variable (even if it is possible).

9. If you are interested in more customizing keep on reading.

CONFIGURATION OPTIONS
These are the configuration options for pyblosxom config.py

* pygallery_dirpath
   - Already covered

* pygallery_url
   - Already covered

* pygallery_use_grp
   - You can group thumbs in a gallery with a index.cfg (True/False).
   - Default: False
   
* pygallery_thumb_row_len
   - How many thumbs will be on a row. 
   - Default: 5
   
* pygallery_index_item
   - How do you want the HTML of an item in the gallery list to look like.
   - Default: <a href="$gal_dir_relurl">$gal_dirname</a><br />
   - Variables:
      $gal_dirname: The name of the gallery
      $gal_summary: Text (from index.cfg)
      $gal_dir_relurl: The url to the gallery
      $gal_thumb: A thumb images name (from index.cfg)
      
* pygallery_thumb_rbegin
   - How do you want your thumb row to begin. 
   - Default: <!-- row begin -->
   
* pygallery_thumb_rend
   - How do you want your thumb row to end. 
   - Default: <!-- row end --> <br />
   
* pygallery_thumb_item
   - How do you want the HTML of a thumb to look like.
   - Default: <a href="$gal_thumb_imgurl">
              <img style="border-style: none;" src="$gal_thumb_url"
                   alt="$gal_thumb_filename"/>
              </a>&nbsp
   - Variables:
      $gal_thumb_filename: The name of the file
      $gal_thumb_url: The url to the thumb
      $gal_thumb_imgurl: The url to the big picture
      
* pygallery_thumb_item_grp
   - When the gallery ends with a row where the number of thumbs is less
     than pygallery_thumb_row_len you maybe want to replace the empty spot
     with HTLM table tags or another picture.
   - Default: <img style="border-style: none;"
                   src="$gal_thumb_url" alt="$gal_thumb_filename"/>&nbsp
   - Variables:
      $gal_thumb_filename: The name of the file
      $gal_thumb_url: The url to the group thumb. This image must be placed
                      in the gallery root (pygallery_dirpath) and have the
                      same name (+ the format suffix) as the thumb group it
                      will appear in (a group is defined in the index.cfg).
                      This can be used even if no groups are used but then
                      the image msut have the name thumbs (+ the format
                      suffix).
                      
* pygallery_default_index_thumb
   - A image used in the gallery list when no one is found in a index.cfg.
     The image must be placed in the gallery root (pygallery_dirpath).

INDEX.CFG 
The config.py options are used to customize all the galleries globally. If
you want to customize things in a gallery you must use the index.cfg file. A
index.cfg file is placed in any gallery (for example one in summer2005 and
one in newyear2005). The data format follows RFC822:
 
	http://www.faqs.org/rfcs/rfc822.html 

Here is an example that uses all the options of the index.cfg

[index]
name: The fun summer 2005
summary: Here we have a gallery with allot of sun and sand
thumb: picture2.jpg

[grouplinks]
picture1.jpg: landscape
picture2.jpg: portrait
picture3.jpg: portrait
picture4.jpg: landscape

[text]
picture1.jpg: Carl is skydiving
picture2.jpg: Oscar is playing mini golf 
picture3.jpg: Oscar throws the golf club
picture4.jpg: Carl laugh at Oscar

Lets explain the file. The tags [index], [grouplinks], [text] must exist in
the file. Lets begin with the [index] part. The name variable contains the
value that will be put in the $gal_dirname variable. The summary variable
contains the value that will be put in the $gal_summary variable. The thumb
variable contains the value that will be put in the $gal_thumb variable.
$gal_dirname, $gal_summary and $gal_thumb are used in the config.py option
pygallery_index_item.

The [grouplinks] tag contains file names of thumb files in the thumbs
directory of a gallery. The after the : char is the group name. In the
example above yo got two groups. When a new group name appear in a index.cfg
file it is automatically added to the gallery that the index.cfg file
belongs to. I actually made this functionality because i wanted to separate
landscape oriented and portrait oriented in to two groups. I hate mixing
them! 

The [text] tag contains file names of files in a images directory and the
corresponding text that will be shown with the picture.

There is also a program that copies an resizes images, creates thumbs and
creates index.cfg files. One interesting feature is that it creates groups
in the index.cfg file. It uses the orientation (landscape and portrait) of
the picture and size to create groups. This program is called apethumbgen.py
and is available from http://www.codeape.org/blog/static/download



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

Revisions:
0.1  - (3 April, 2006) Created.
1.0  - (1 October, 2006) Finished =)
1.01 - (8 October, 2006) Fixed html bug in defult data
1.2  - (15 Februari, 2007) Added a way to sort the galleries list (dirlist.cfg).
2.0  - (13 November, 2007) Added the group functionality and fixed a ton of bugs
2.01 - (13 November, 2007) Found a last minute index out of bound bug
"""

__author__ = "Oscar Norander - oscar-no at codeape dot org"
__version__ = "2.01"
__url__ = "http://www.codeape.org/blog/static/download"
__description__ = "A gallery"

import os 
from ConfigParser import *
from Pyblosxom import tools, entries

__TRIGGER__ = "pygallery"
__TRIGGER_INDEX__ = "index"
__TRIGGER_GROUP_S__ = "groups"
__TRIGGER_GROUP__ = "group"

__CFG_FLAVDIR__ = "flavourdir"
__CFG_BASE_URL__ = "base_url"

#Stuff in config.py
__CFG_DIRPATH__ = "pygallery_dirpath" #The root of the gallery (on the file system)
__CFG_URL__ = "pygallery_url" #the url root of the galleies images
__CFG_USE_GRP_SORT__ = "pygallery_use_grp" #Sorting everything by group
__CFG_THUMBS_ROW_LEN__ = "pygallery_thumb_row_len" #how many thumbs in a row before next row
__CFG_INDEX_ITEM__ = "pygallery_index_item" #HTML for the gallery list
__CFG_THUMB_RBEGIN__ = "pygallery_thumb_rbegin" #HTML for the beginging of the thumb rows
__CFG_THUMB_REND__ = "pygallery_thumb_rend" #HTML for the end of the thumb rows
__CFG_THUMB_ITEM__ = "pygallery_thumb_item" #thumb HTML
__CFG_THUMB_ITEM_GRP__ = "pygallery_thumb_item_grp" #thumb group fil out HTML
__CFG_DEFAULT_INDEX_THUMB__ = "pygallery_default_index_thumb" #a safty image =)

#variables for __CFG_THUMB_ITEM__
__VALKEY_THUMB_FNAME__ = "gal_thumb_filename"
__VALKEY_THUMB_URL__ = "gal_thumb_url"
__VALKEY_THUMB_IMGURL__ = "gal_thumb_imgurl"

#variables for __CFG_INDEX_ITEM__
__VALKEY_INDEX_DIR__ = "gal_dirname"
__VALKEY_INDEX_SUM__ = "gal_summary"
__VALKEY_INDEX_RELURL__ = "gal_dir_relurl"
__VALKEY_INDEX_THUMB__ = "gal_thumb"

#data for diffrent places
__DATA_FLAV__ = "flavour"
__DATA_DIR_THUMBS__ = "thumbs"
__DATA_DIR_IMAGES__ = "images"
__DATA_CFG_FNAME__ = "index.cfg"
__DATA_INDEX_FNAME__ = "dirlist.cfg"
__DATA_FORM_INDEX__ = "pygallery_index"
__DATA_FORM_GROUP__ = "pygallery_group"
__DATA_FORM_THUMBS__ = "pygallery_thumbs"
__DATA_FORM_IMAGE__ = "pygallery_image"
__DATA_DEF_INDEX__ = '<a href="$gal_dir_relurl">$gal_dirname</a><br />'
__DATA_DEF_THUMB_RBEGIN__ = "<!-- row begin -->"
__DATA_DEF_THUMB_REND__ = "<!-- row end --> <br />"
__DATA_DEF_THUMB_ITEM__ = '<a href="$gal_thumb_imgurl"><img style="border-style: none;" src="$gal_thumb_url" alt="$gal_thumb_filename"/></a>&nbsp;'
__DATA_DEF_THUMB_ITEM_GRP__ = '<img style="border-style: none;" src="$gal_thumb_url" alt="$gal_thumb_filename"/>&nbsp;'

#data entry field names
__ENTRY_F_TITLE__ = "title"
__ENTRY_F_TEMPL__ = "template_name"
__ENTRY_F_IMGURL__ = "image_url"
__ENTRY_F_NEXT__ = "next"
__ENTRY_F_PREV__ = "prev"
__ENTRY_F_SUM__ = "summary"
__ENTRY_F_GRP__ = "grp_name"
__ENTRY_F_GRPURL__ = "grp_url"

#variables in index.cfg __DATA_CFG_FNAME__
__INDEX_SECT_INDEX__ = "index"
__INDEX_OPT_NAME__ = "name"
__INDEX_OPT_SUM__ = "summary"
__INDEX_OPT_THUMB__ = "thumb"

#parts in index.cfg __DATA_CFG_FNAME__
__INDEX_SECT_GROUP__ = "grouplinks"
__INDEX_SECT_TEXT__ = "text"

#parts in dirlist.cfg __DATA_INDEX_FNAME__
__INDEX_SECT_GROUPREL__ = "groups"



def verify_installation(req):
    config = req.getConfiguration()

    retval = 1

    if not config.has_key(__CFG_DIRPATH__) :
        print "- '" + __CFG_DIRPATH__ + "' is not set for pygallery in config.py!"
        retval = 0
    elif not os.path.isdir(config[__CFG_DIRPATH__]):
        print "- Path '" + config[__CFG_DIRPATH__] + "' do not exist!"
        retval = 0
        
    if not config.has_key(__CFG_URL__) :
        print "- '" + __CFG_URL__ + "' is not set for pygallery in config.py!"
        retval = 0
        
    return retval

#I simply want that slash in the end of the path.
def fix_local_path(path):
    if not path.endswith("/"):
        path = path + "/"
    return path.replace("/", os.sep)

#uncached read of index.cfg
def uncached_cfg_read(cfg, adir, section, option, default) :
    lpath  = fix_local_path(cfg[__CFG_DIRPATH__])+adir+"/"+__DATA_CFG_FNAME__
    if not os.path.isfile(lpath) :
        return default
    
    lconfig = SafeConfigParser()
    lconfig.readfp(open(lpath))

    if not lconfig.has_section(section) :
        return default
    elif not lconfig.has_option(section, option):
        return default
    else:
        return lconfig.get(section, option)

#cached read of index.cfg
def cached_cfg_read(gconfig, cfg, adir, section, option, default) :
    if gconfig == None :
        lpath  = fix_local_path(cfg[__CFG_DIRPATH__])+adir+"/"+__DATA_CFG_FNAME__
        if not os.path.isfile(lpath) :
            return default
    
        gconfig = SafeConfigParser()
        gconfig.readfp(open(lpath))

    if not gconfig.has_section(section) :
        return default
    elif not gconfig.has_option(section, option):
        return default
    else:
        return gconfig.get(section, option)

#A default thing to do if nothing works
def nopics(req) :
    entry = entries.base.EntryBase(req)
    entry[__ENTRY_F_TITLE__] = "No pictures found!"
    entry.setData("Soon maybe?");
    return [entry]

#A default thing to do if nothing works
def cfg_error(req, file, estr) :
    entry = entries.base.EntryBase(req)
    entry[__ENTRY_F_TITLE__] = "PROBLEM WITH YOUR "+file
    entry.setData("Something is wrong with "+file \
                  + "<br /> Check pygallery.py documentation. <br />" \
                  + "Exception: " + estr);
    return [entry]

#resolv if there is a group picture and its format
#kind of uggly but it works
def get_group_pic(cfg, grp):
    pygal_url = cfg.get(__CFG_URL__ , "")

    if(os.path.isfile(cfg[__CFG_DIRPATH__] + "/" + grp +".png")):
        return pygal_url + "/" + grp +".png"
    elif(os.path.isfile(cfg[__CFG_DIRPATH__] + "/" + grp +".gif")):
        return pygal_url + "/" + grp +".gif"
    elif(os.path.isfile(cfg[__CFG_DIRPATH__] + "/" + grp +".jpg")):
        return pygal_url + "/" + grp +".jpg"
    elif(os.path.isfile(cfg[__CFG_DIRPATH__] + "/" + grp +".jpeg")):
        return pygal_url + "/" + grp +".jpg"
    elif(os.path.isfile(cfg[__CFG_DIRPATH__] + "/" + grp +".PNG")):
        return pygal_url + "/" + grp +".PNG"
    elif(os.path.isfile(cfg[__CFG_DIRPATH__] + "/" + grp +".GIF")):
        return pygal_url + "/" + grp +".GIF"
    elif(os.path.isfile(cfg[__CFG_DIRPATH__] + "/" + grp +".JPG")):
        return pygal_url + "/" + grp +".JPG"
    elif(os.path.isfile(cfg[__CFG_DIRPATH__] + "/" + grp +".JPEG")):
        return pygal_url + "/" + grp +".JPEG"
    else:
        return "group pic not entered"

def list_thumbs(cfg, req, apath, adir) :    
    #Create the path to the thumb directory
    ltmp_path = fix_local_path(cfg[__CFG_DIRPATH__]) + adir + "/" +__DATA_DIR_THUMBS__
    
    if not os.path.isdir(ltmp_path) :
        return nopics(req)
    
    tmp_list = os.listdir(ltmp_path)
    thumbs = []
    #We only want image files from the thumb directory
    for item in tmp_list :
        if item.endswith(".jpeg") \
               or item.endswith(".jpg") \
               or item.endswith(".png") \
               or item.endswith(".gif") \
               or item.endswith(".JPEG") \
               or item.endswith(".JPG") \
               or item.endswith(".PNG") \
               or item.endswith(".GIF") :  
            thumbs.append(item)

    if len(thumbs) == 0 :
        return nopics(req)

    #get the configuration for the thumbs
    use_sort = cfg.get(__CFG_USE_GRP_SORT__, False)
    row_len = cfg.get(__CFG_THUMBS_ROW_LEN__, 5)
    pygal_url = cfg.get(__CFG_URL__ , "")
    baseurl = cfg.get(__CFG_BASE_URL__, "")

    if len(pygal_url) > 0 :
        pygal_url = fix_local_path(pygal_url)

    #get the HTML templates for each item
    tag_row_begin = cfg.get(__CFG_THUMB_RBEGIN__ , __DATA_DEF_THUMB_RBEGIN__)
    tag_row_end = cfg.get(__CFG_THUMB_REND__ , __DATA_DEF_THUMB_REND__)
    tag_thumb_item = cfg.get(__CFG_THUMB_ITEM__ , __DATA_DEF_THUMB_ITEM__)

    #create a directory that will be used as environment for variable substitution
    thumb_val = {}
    thumb_val[__VALKEY_THUMB_FNAME__] = ""
    thumb_val[__VALKEY_THUMB_URL__] = ""
    thumb_val[__VALKEY_THUMB_IMGURL__] = ""
    
    data_dic = {}
    i = 0
    mycache = None
    
    #create the HTML for the thumbs
    for item in thumbs :
        #find out group belonging (begin)
        key = "thumbs" #default if no group is used
        try:
            if use_sort :
                key = cached_cfg_read(mycache, cfg, adir, __INDEX_SECT_GROUP__, item, "")
        except (NoSectionError \
            , DuplicateSectionError \
            , NoOptionError \
            , InterpolationError \
            , InterpolationDepthError \
            , InterpolationSyntaxError \
            , ParsingError \
            ,MissingSectionHeaderError), e:
            return cfg_error(req, __DATA_INDEX_FNAME__, repr(e))

        if data_dic.has_key(key) == 0 :
            data_dic[key] = (0,"")
            i = 0
        else:
            i = data_dic[key][0]
        #find out group belonging (end)

        #if it is a new row
        data_str = ""
        if i == 0 :
            data_str = data_str + tag_row_begin

        #fill environment variable substitution
        thumb_val[__VALKEY_THUMB_FNAME__] = item
        thumb_val[__VALKEY_THUMB_URL__] = pygal_url + adir + "/" + __DATA_DIR_THUMBS__ + "/" + item
        thumb_val[__VALKEY_THUMB_IMGURL__] = baseurl + "/" + __TRIGGER__ + "/" + adir + "/" + __DATA_DIR_IMAGES__ + "/" + item

        #do variable substitution
        tmp_item = tools.parse(req, "iso-8859-1",thumb_val, tag_thumb_item)
        data_str = data_str + tmp_item

        if i == (row_len - 1):
            #before a new row
            data_str = data_str + tag_row_end + "\n"
            i = 0
        else:
            i += 1

        #put the thumb in the right group
        data_dic[key] = (i, (data_dic[key][1] + data_str))

    groups = []
    tag_thumb_item = cfg.get(__CFG_THUMB_ITEM_GRP__ , __DATA_DEF_THUMB_ITEM_GRP__)
    #create the HTML for the last row filling (for even out rows)
    for grp in data_dic.keys() :
        i = ((data_dic[grp])[0]) 
        data_str = ((data_dic[grp])[1])
        if (i < row_len) and (i != 0):
            thumb_val = {}
            thumb_val[__VALKEY_THUMB_URL__] = get_group_pic(cfg, grp)
            tmp_item = tools.parse(req, "iso-8859-1",thumb_val, tag_thumb_item)
            for fake in xrange(0, row_len - i):
                data_str = data_str + tmp_item
            data_str = data_str + tag_row_end

        
        entry = entries.base.EntryBase(req)
        entry[__ENTRY_F_TITLE__] = grp
        entry[__ENTRY_F_TEMPL__] = __DATA_FORM_THUMBS__
        entry.setData(data_str)
        groups.append(entry)
        
    return groups

def show_image(cfg, req, adir, aimg) :
    ltmp_path = fix_local_path(cfg[__CFG_DIRPATH__]) + adir + "/" +__DATA_DIR_THUMBS__
    
    if not os.path.isdir(ltmp_path) :
        return nopics(req)
   
    tmp_list = os.listdir(ltmp_path)
    thumbs = []
    #create a list so that you know which is prev and next
    for item in tmp_list :
        if item.endswith(".jpeg") \
               or item.endswith(".jpg") \
               or item.endswith(".png") \
               or item.endswith(".gif") \
               or item.endswith(".JPEG") \
               or item.endswith(".JPG") \
               or item.endswith(".PNG") \
               or item.endswith(".GIF") :
            thumbs.append(item)

    if len(thumbs) == 0 :
        return nopics(req)

    found = False
    i = 0
    #find the image that is displayed
    while (i < len(thumbs)) and not(found) :
        if thumbs[i] == aimg :
            found = True
        else :
            i += 1

    if not found :
        return []

    #if displayed picture is the last one set ther next image
    #to be the first image
    n = i + 1
    if n >= len(thumbs) :
        n = 0

    #if displayed picture is the first one set ther previus image
    #to be the last image
    p = i - 1
    if p < 0 :
        p = len(thumbs) - 1

    pygal_url = cfg.get(__CFG_URL__ , "")
    baseurl = cfg.get(__CFG_BASE_URL__, "")
                
    entry = entries.base.EntryBase(req)
    entry[__ENTRY_F_TITLE__] = aimg
    entry[__ENTRY_F_IMGURL__] = pygal_url +"/"+ adir + "/" + __DATA_DIR_IMAGES__ + "/" + aimg
    entry[__ENTRY_F_NEXT__] = baseurl + "/" + __TRIGGER__ + "/" + adir + "/" + __DATA_DIR_IMAGES__ + "/" + thumbs[n]
    entry[__ENTRY_F_PREV__] = baseurl + "/" + __TRIGGER__ + "/" + adir + "/" + __DATA_DIR_IMAGES__ + "/" + thumbs[p]
    try:
        entry[__ENTRY_F_SUM__] = uncached_cfg_read(cfg, adir, __INDEX_SECT_TEXT__, aimg, "")
    except (NoSectionError \
        , DuplicateSectionError \
        , NoOptionError \
        , InterpolationError \
        , InterpolationDepthError \
        , InterpolationSyntaxError \
        , ParsingError \
        ,MissingSectionHeaderError), e:
        return cfg_error(req, __DATA_INDEX_FNAME__, repr(e))
    entry[__ENTRY_F_TEMPL__] = __DATA_FORM_IMAGE__
    entry.setData("")
    return [entry]

def cb_filelist(args):
    req = args["request"]

    pyhttp = req.getHttp()
    data = req.getData()
    config = req.getConfiguration()

    baseurl = config.get(__CFG_BASE_URL__, "")

    path_info = pyhttp["PATH_INFO"]
    if not path_info.startswith("/" + __TRIGGER__ + "/") : 
        return
        
    gall_dir = config[__CFG_DIRPATH__]
    if not gall_dir :
        return
    
    gall_dir = fix_local_path(gall_dir)
    dir_tmp = []
    grp_order = []
    grp_tmp = {}
    grp_name = ""

    cblpath = gall_dir+__DATA_INDEX_FNAME__
    if (os.path.isfile(cblpath)):
        #if a file for sorting files exists do this
        f = open(cblpath)
        try:
            for line in f:
                line = line.replace("\n", "")
                line = line.strip();
                if len(line) > 1 :
                    if (line[0] == "[") and (line[len(line) - 1] == "]") :
                        grp_name = line[1:len(line) - 1]
                        if grp_name != "":
                            grp_order.append(grp_name)
                            grp_tmp[grp_name] = []
                    elif line != "" :
                        dir_tmp.append(line)
                        if(grp_name != ""):
                            grp_tmp[grp_name].append(line)
                elif line != "" :
                    dir_tmp.append(line)
                    if(grp_name != ""):
                        grp_tmp[grp_name].append(line)
        finally:
            f.close()
    else:
        #no sorting
        dir_tmp = os.listdir(gall_dir)
        
    if len(dir_tmp) == 0:
        return nopics(req)

    if path_info.startswith("/" + __TRIGGER__ + "/" + __TRIGGER_INDEX__):
        #the gallery index/list
        itemformat = config.get(__CFG_INDEX_ITEM__, __DATA_DEF_INDEX__)
        pygal_url = config.get(__CFG_URL__ , "")
        def_thumb = config.get(__CFG_DEFAULT_INDEX_THUMB__, __CFG_DEFAULT_INDEX_THUMB__+" not set")

        index_val = {}
        index_val[__VALKEY_INDEX_DIR__] = ""
        index_val[__VALKEY_INDEX_SUM__] = ""
        index_val[__VALKEY_INDEX_RELURL__] = ""
        index_val[__VALKEY_INDEX_THUMB__] = ""
        dir_list = ""
        for item in dir_tmp :
            tmp_path = str(gall_dir + item)
            if os.path.isdir(tmp_path) :
                mychace = None          
                try:
                    index_val[__VALKEY_INDEX_DIR__] = cached_cfg_read(mychace ,config ,item, __INDEX_SECT_INDEX__, __INDEX_OPT_NAME__, item)
                    index_val[__VALKEY_INDEX_SUM__] = cached_cfg_read(mychace ,config ,item, __INDEX_SECT_INDEX__, __INDEX_OPT_SUM__, "")
                    index_val[__VALKEY_INDEX_RELURL__] = baseurl+"/" + __TRIGGER__ + "/" + item
                    one_thumb = cached_cfg_read(mychace, config, item, __INDEX_SECT_INDEX__, __INDEX_OPT_THUMB__, "")
                except (NoSectionError \
                    , DuplicateSectionError \
                    , NoOptionError \
                    , InterpolationError \
                    , InterpolationDepthError \
                    , InterpolationSyntaxError \
                    , ParsingError \
                    ,MissingSectionHeaderError), e:
                    return cfg_error(req, __DATA_INDEX_FNAME__, repr(e))
                if one_thumb == "" :
                    index_val[__VALKEY_INDEX_THUMB__] = pygal_url + "/" + def_thumb
                else :
                    index_val[__VALKEY_INDEX_THUMB__] = pygal_url + "/" + item + "/" + __DATA_DIR_THUMBS__ + "/" + one_thumb
                                                    
                str_item = tools.parse(req, "iso-8859-1", index_val, itemformat);
                dir_list = dir_list + str_item + "\n"
                mychace = None

        entry = entries.base.EntryBase(req)
        entry[__ENTRY_F_TEMPL__] = __DATA_FORM_INDEX__
        entry.setData(str(dir_list));
        return [entry]
    elif path_info == ("/" + __TRIGGER__ + "/" + __TRIGGER_GROUP_S__):    
        if(len(grp_tmp) > 0):
            itemformat = config.get(__CFG_INDEX_ITEM__, __DATA_DEF_INDEX__)
            pygal_url = config.get(__CFG_URL__ , "")
            def_thumb = config.get(__CFG_DEFAULT_INDEX_THUMB__, __CFG_DEFAULT_INDEX_THUMB__+" not set")

            elist = []
            grp_name = ""
            for grp_name in grp_order :
                gals = grp_tmp[grp_name]
                index_val = {}
                index_val[__VALKEY_INDEX_DIR__] = ""
                index_val[__VALKEY_INDEX_SUM__] = ""
                index_val[__VALKEY_INDEX_RELURL__] = ""
                index_val[__VALKEY_INDEX_THUMB__] = ""
                dir_list = ""
                for item in gals :
                    tmp_path = str(gall_dir + item)
                    if os.path.isdir(tmp_path) :
                        mychace = None                
                        try:
                            index_val[__VALKEY_INDEX_DIR__] = cached_cfg_read(mychace ,config ,item, __INDEX_SECT_INDEX__, __INDEX_OPT_NAME__, item)
                            index_val[__VALKEY_INDEX_SUM__] = cached_cfg_read(mychace ,config ,item, __INDEX_SECT_INDEX__, __INDEX_OPT_SUM__, "")
                            index_val[__VALKEY_INDEX_RELURL__] = baseurl+"/" + __TRIGGER__ + "/" + item
                            one_thumb = cached_cfg_read(mychace, config, item, __INDEX_SECT_INDEX__, __INDEX_OPT_THUMB__, "")
                        except (NoSectionError \
                            , DuplicateSectionError \
                            , NoOptionError \
                            , InterpolationError \
                            , InterpolationDepthError \
                            , InterpolationSyntaxError \
                            , ParsingError \
                            ,MissingSectionHeaderError), e:
                            return cfg_error(req, __DATA_INDEX_FNAME__, repr(e))
                        if one_thumb == "" :
                            index_val[__VALKEY_INDEX_THUMB__] = pygal_url + "/" + def_thumb
                        else :
                            index_val[__VALKEY_INDEX_THUMB__] = pygal_url + "/" + item + "/" + __DATA_DIR_THUMBS__ + "/" + one_thumb
                                                    
                        str_item = tools.parse(req, "iso-8859-1", index_val, itemformat);
                        dir_list = dir_list + str_item + "\n"
                        mychace = None
                entry = entries.base.EntryBase(req)
                entry[__ENTRY_F_TEMPL__] = __DATA_FORM_GROUP__
                entry[__ENTRY_F_GRP__] = grp_name
                entry[__ENTRY_F_GRPURL__] = baseurl+"/" + __TRIGGER__ + "/" + __TRIGGER_GROUP__ + "/" + grp_name.replace(" ","%20")
                entry.setData(str(dir_list));
                elist.append(entry)

            return elist
        else:
            return nopics(req)
    elif path_info.startswith("/" + __TRIGGER__ + "/" + __TRIGGER_GROUP__ + "/"):
        itemformat = config.get(__CFG_INDEX_ITEM__, __DATA_DEF_INDEX__)
        pygal_url = config.get(__CFG_URL__ , "")
        def_thumb = config.get(__CFG_DEFAULT_INDEX_THUMB__, __CFG_DEFAULT_INDEX_THUMB__+" not set")

        index_val = {}
        index_val[__VALKEY_INDEX_DIR__] = ""
        index_val[__VALKEY_INDEX_SUM__] = ""
        index_val[__VALKEY_INDEX_RELURL__] = ""
        index_val[__VALKEY_INDEX_THUMB__] = ""
        dir_list = ""
        grp_name = path_info[len("/" + __TRIGGER__ + "/" + __TRIGGER_GROUP__ + "/") : len(path_info)]
        gals = grp_tmp[grp_name]
        for item in gals :
            tmp_path = str(gall_dir + item)
            if os.path.isdir(tmp_path) :
                mychace = None             
                try:
                    index_val[__VALKEY_INDEX_DIR__] = cached_cfg_read(mychace ,config ,item, __INDEX_SECT_INDEX__, __INDEX_OPT_NAME__, item)
                    index_val[__VALKEY_INDEX_SUM__] = cached_cfg_read(mychace ,config ,item, __INDEX_SECT_INDEX__, __INDEX_OPT_SUM__, "")
                    index_val[__VALKEY_INDEX_RELURL__] = baseurl+"/" + __TRIGGER__ + "/" + item
                    one_thumb = cached_cfg_read(mychace, config, item, __INDEX_SECT_INDEX__, __INDEX_OPT_THUMB__, "")
                except (NoSectionError \
                    , DuplicateSectionError \
                    , NoOptionError \
                    , InterpolationError \
                    , InterpolationDepthError \
                    , InterpolationSyntaxError \
                    , ParsingError \
                    ,MissingSectionHeaderError), e:
                    return cfg_error(req, __DATA_INDEX_FNAME__, repr(e))
                if one_thumb == "" :
                    index_val[__VALKEY_INDEX_THUMB__] = pygal_url + "/" + def_thumb
                else :
                    index_val[__VALKEY_INDEX_THUMB__] = pygal_url + "/" + item + "/" + __DATA_DIR_THUMBS__ + "/" + one_thumb
                                                    
                str_item = tools.parse(req, "iso-8859-1", index_val, itemformat);
                dir_list = dir_list + str_item + "\n"
                mychace = None

        entry = entries.base.EntryBase(req)
        entry[__ENTRY_F_TEMPL__] = __DATA_FORM_INDEX__
        entry.setData(str(dir_list));
        return [entry]
    else:
        notrigger_info = path_info[len("/" + __TRIGGER__ + "/") : len(path_info)]
        test_path = gall_dir + notrigger_info
        if os.path.isdir(test_path):
            #list thumbs
            dir_name = os.path.split(test_path)[1]
            return list_thumbs(config, req, gall_dir, dir_name)
        elif os.path.isdir(myrsplit(test_path)) :
            #Uses flav
            #list thumbs
            dir_name = os.path.split(myrsplit(test_path))[1]
            return list_thumbs(config, req, gall_dir, dir_name)
        elif os.path.isfile(test_path) :
            #Show picture and next and prev
            tmp_pair = os.path.split(notrigger_info)
            fname = tmp_pair[1]
            dir_name = tmp_pair[0]
            dir_name = dir_name.split("/", 1)[0]
            return show_image(config, req, dir_name, fname)
        elif os.path.isfile(myrsplit(test_path)) :    
            #Uses flav
            #Show picture and next and prev
            tmp_pair = os.path.split(myrsplit(test_path))
            fname = tmp_pair[1]
            tmp_pair = os.path.split(notrigger_info)
            dir_name = tmp_pair[0]
            dir_name = dir_name.split("/", 1)[0]
            return show_image(config, req, dir_name, fname)
        else :
            return

#to make it work with python older than 2.4
def myrsplit(astr):
    i = 0
    i = len(astr) - 1
    found = False
    while (i >= 0) and (not found) :
        if astr[i] == ".":
            found = True
        else:
            i -= 1
            
    if found:
        newstr = astr[0:i]
        return newstr
    else:
        return astr
