#!/usr/bin/env python

from astropy.table import Table
import glob
import re

files = glob.glob('Field*.fits');
CID = 1
for fname in files:
    res = re.match('Field-(\d+)-(\w+)(-E[0-9]+)?\.fits', fname)
    fnum = res.group(1)
    fltr = res.group(2)

    t = Table().read(fname)
    nsources = len(t)
    
    print "{0},{1},{2},{3},{4},{5}".format(CID,1,fnum,fname,fltr,nsources)

        

