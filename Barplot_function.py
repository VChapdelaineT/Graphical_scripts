#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import argparse

argparser = argparse.ArgumentParser(description = '')
argparser.add_argument('-i', metavar = 'name', dest = 'in_file1', type = str, required = True, help = 'Input file (separator tab\space)')
argparser.add_argument('-on', metavar = 'name', dest = 'on', type = str, required = True, help = 'Column in to create category.')
argparser.add_argument('-cat', metavar = 'name', dest = 'cat', type = str, required = True, help = 'Column to be Categorized.')
argparser.add_argument('-s', metavar = 'name', dest = 'sep', type = float, required = True, nargs='+', help = 'delimiters')
argparser.add_argument('-l', metavar = 'name', dest = 'low_include', type = bool, required = True, help = 'delimiters')
argparser.add_argument('-o', metavar = 'name', dest = 'out', type = str, required = True, help = 'Outfile base name.')

def addlabels(fig,x,y):
    for j in range(len(x)):
        fig.text(j,y[j],str(y[j]),ha='center')

if __name__ == '__main__':
	args = argparser.parse_args()
  dfo=pd.read_csv(args.in_file1, sep = "\s+", low_memory=False, names=[args.on,args.cat])
  binned=pd.cut(dfo[args.on], args.sep , include_lowest =args.low_include)
  labels=[]
  sums=[]
  for i in range(0,len(a[0].categories)-1):
    sums.append((a[0]==a[0].categories[i]).sum())
    labels.append(a[0].categories[i])
  fig, ax1 = plt.subplots(figsize=(15, 15))
  ax1.boxplot(sums,labels=labels)
  addlabels(ax1,sums,sums)
  fig.savefig(args.out + '.png', dpi=300)
  


        

