#!/usr/bin/python

import sys
import os
import tarfile


cps_list = [] # Initialize array to hold CPS samples
r_total = 0 # Variable to total CPS samples
avg_cps = 0 # Variable to hold average of CPS samples

# Get name of tech support file
infile = raw_input("Tech support file (copy/paste here): ")



ts_file = tarfile.open(infile,'r:gz')

# List CPS stats from the tech support file
for tar_info in ts_file:
    if (tar_info.isdir() or tar_info.issym()):
        continue
    f = ts_file.extractfile(tar_info)
    for line in f:
        if "connection establish rate" in line:
            cps = line[40:]
            cps = ''.join(cps.split())
            cps = cps[:-3]
            cps_list.append(cps)

# Compute the average CPS

for datapoint in range(len(cps_list)):
    r_total += int(cps_list[datapoint])

avg_cps = r_total / len(cps_list)
print "Your average connection rate is: %i" % avg_cps
