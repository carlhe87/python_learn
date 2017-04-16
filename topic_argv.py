#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: 

This Module is used for erro proof argv setting
    report on argv state
    pass given argv to main()
"""

from sys import argv
from os.path import exists


PATH_PY_FILE = "C:/Users/Carl W He/Documents/Python/Scripts"



#main
def main(n):
    print "Hello!",
    print "argv parameter:", n
    
    
#accept argv 
from sys import argv
ARGV_NUM = 2 #expected argv number
try:
    main(argv[1])
    print "execute main() with argv1"
except Exception:
    argv_num = len(argv)
    print "Report: argv expected: {}, actual {}".format(ARGV_NUM,argv_num)
    print "skip main()"
finally:
    print "argv =", argv
    