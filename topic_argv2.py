#! /usr/bin/python
# -*- coding: utf-8 -*-

"""Module Intro: main mod of current package

This Module is used as main file for  package
"""

#main
import sys

#print sys.argv[0], sys.argv[1],sys.argv[2],
def main(var0=0, var1=0, var2=0):
    print "from main", var0, var1, var2

if __name__ == "__main__":
    #mtd1: sys.exit(main(sys.argv[1], sys.argv[2]))
    #mtd2: in calling env(not here) use os.system("python main 2 3")
    #      as if calling from outside python interpreter
    main()