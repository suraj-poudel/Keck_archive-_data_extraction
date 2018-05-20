#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 18:11:14 2018

@author: surajpoudel
"""

from astropy.io import fits
hdulist = fits.open('HI.fits')
hdulist.info()
for i in range(10):
   list=(data['WAVE'][i],data['FX'][i],data['VAR'][i])
   x=list[0]
   y=list[1]
   z=list[2]
   from astropy.io import ascii
   ascii.write([x,y,z], 'order_hi'+str(i)+'.txt', names=['wave', 'flux','var'], overwrite=True)