#!/usr/bin/python3

import sys
import csv

def get_interset(seta, setb):
    interset = []
    for a in seta:
        if a in setb:
            interset.append(a)
    return interset

if len(sys.argv) != 2:
    print("Usage: python3 venn.py filepath!")
    exit(-1)

fd = open(sys.argv[1])
reader = csv.reader(fd, delimiter=',')
set_list = []
is_init = True
names = None
nset = 0
for item in reader:
    if is_init:
        nset = len(item)
        print("nset: {}".format(nset))
        print("first item (names):")
        for v in item:
            print(v)
        names = item
        if nset > 3:
            print("Error: cannot support more than 3 sets: {}!".format(nset))
            exit(-1)
        for i in range(nset):
            set_list.append([])
        is_init = False
    else:
        for i in range(nset):
            if item[i] != '':
                set_list[i].append(item[i])
for i in range(len(set_list)):
    set_list[i] = set(set_list[i])
fd.close()

fd = open("venn.csv", "w")
writer = csv.writer(fd, delimiter=',')
if nset == 2:
    rowname = "{}&{}".format(names[0], names[1])
    writer.writerow(rowname)
    interset_ab = get_interset(set_list[0], set_list[1])
    for v in interset_ab:
        writer.writerow(v)
elif nset == 3:
    rowname = ["{}&{}".format(names[0], names[1]), \
            "{}&{}".format(names[0], names[2]), \
            "{}&{}".format(names[1], names[2]), \
            "{}&{}&{}".format(names[0], names[1], names[2])]
    writer.writerow(rowname)
    interset_ab = get_interset(set_list[0], set_list[1])
    interset_ac = get_interset(set_list[0], set_list[2])
    interset_bc = get_interset(set_list[1], set_list[2])
    interset_abc = get_interset(interset_ab, set_list[2])
    nrow = max([len(interset_ab), len(interset_ac), len(interset_bc), len(interset_abc)])
    for i in range(nrow):
        tmprow = ["", "", "", ""]
        if i < len(interset_ab):
            tmprow[0] = interset_ab[i]
        if i < len(interset_ac):
            tmprow[1] = interset_ac[i]
        if i < len(interset_bc):
            tmprow[2] = interset_bc[i]
        if i < len(interset_abc):
            tmprow[3] = interset_abc[i]
        writer.writerow(tmprow)
else:
    print("Error: cannot support more than 3 sets: {}!".format(nset))
fd.close()

import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn3

fig, ax = plt.subplots(figsize=(8,4))
if nset == 2:
    venn2(set_list, set_labels=names, alpha=0.6, normalize_to=2.0)
elif nset == 3:
    venn3(set_list, set_labels=names, alpha=0.6, normalize_to=2.0)
else:
    print("Error: cannot support more than 3 sets: {}!".format(nset))
fig.savefig("./venn.pdf", dpi=600)
