#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Generate path and make empty files

The mod is used for generating path
also used as templated file generation

Feature: 
    assume ~/temp/temp.py (with template)
    
"""
import rabbit
import mod_const

PATH_PY_FILE = mod_const.PATH_PY_FILE
TMPL_PY = mod_const.TEMPLATE_PY

def make_file(sub_folder="temp", filename="temp", filetype="py", content=TMPL_PY):
    """create empty file, auto rename upon name conflict, fill with py2 mod template"""
    #construct path from other info
    directory = os.path.join(PATH_PY_FILE, sub_folder)
    path = os.path.join(directory, ".".join((filename, filetype)))
    
    #If directory not exist, make directory
    if not os.path.exists(directory):
        print "Directory not exist, create directory!"
        os.makedirs(directory)
    else: pass

    #if file not exist, create empty file
    if not os.path.exists(path):
        print "File created: {}".format(".".join((filename, filetype)))
        with open(path,"a") as f: f.write(content)
        return path
    #if file exists, rename and create new empty file
    else:    
        filenum = ""
        i = 1 
        while 1:     
            tmp_name = "{}{}.{}".format(filename, filenum, filetype)
            tmp = os.path.join(directory, tmp_name)
            if not os.path.exists(tmp):
                path = tmp
                print "File name exists, rename as {}".format(tmp_name)
                break
            else:
                filenum = "_{}".format(i)
                i += 1 
        with open(path,"a") as f: f.write(content)
        return path