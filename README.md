These are my old and no longer maintained hacks for pyblosxom

pygallery.py
------------
This is a gallery script that has good configuring possibilities. All 
documentation is in the python source file you download. It currently has the
following functionality:

* can manage several galleries (three level design: gallery list, thumbs,
  image)
* every gallery has a simple configuration file (index.cfg) that contain
  gallery name, summery text, image text, grouping images etc.
* common variables are set in config.py
* there are special care has been taken for customizing row and items in the
  gallery list and the thumbs list.
* grouping of both galleries and thumbs
* the index.cfg file can be generated with apethumbgen.py

pyguest.py
----------

This is a guestbook. All documentation is in the python source file you
download. It currently has the following functionality:

* protection against bot spam (captcha, requires Python Imaging Library)
* protection from double posts and empty form fields
* html stripping
* @ char stripping
* guestbook give feedback about user faults (only in english for now)

apethumbgen.py
--------------

This little hack lighten the burden of resizing images and making thumbs for
your web page. Just let it read the directory where your have the original
images and in no time you got resized images in a new directory and thumbs in
another directory. Ok ok it has been done before by others, but this one
supports output to pygallery.py config file format (index.cfg) and it has
hooks for adding your own code (apeconfig.py contain an example). If you want
to know how it works, download the script and type pydoc ./apethumbgen.py
