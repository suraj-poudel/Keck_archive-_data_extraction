#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 18:11:14 2018

@author: surajpoudel
"""
#Open file
from astropy.io import fits
import sys
fn='a.fits'
#fn = 'r0117.fits'
if len(sys.argv) == 2:
    fn=(sys.argv[1])
hdulist = fits.open(fn)
hdulist.info()
#hdu = hdulist[0]
#hdu.header

#reading tables
import matplotlib as plt
import numpy as np
from astropy.table import Table
data1 = fits.getdata(fn)
t = Table(data1)

#print column names
print t.colnames
#no. of rows
print len(t)
#print a specific row
#print t[0]
#print a specific column
#print t['FWHM']
print t

#getting data
data = fits.getdata(fn)

#print data
print data[1]['WAVE'],data[1]['FX']
for i in range(10):
 x=data[i]['WAVE']
 y=data[i]['FX']
 z=data[i]['VAR']
#writing in txt file
 from astropy.io import ascii
 ascii.write([x,y,z], 'order_esi'+str(i)+'.txt', names=['wave', 'flux','var'], overwrite=True)
#"file_" + str(i) + ".dat"
