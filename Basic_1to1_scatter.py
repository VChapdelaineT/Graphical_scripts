#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import argparse


argparser = argparse.ArgumentParser(description = '')
argparser.add_argument('-i', metavar = 'name', dest = 'in_file1', type = str, required = True, help = 'Input file (separator tab\space)')
argparser.add_argument('-X', metavar = 'name', dest = 'X', type = str, required = True, help = 'Column name axis X.')
argparser.add_argument('-Y', metavar = 'name', dest = 'Y', type = str, required = True, help = 'Column name axis Y.')
argparser.add_argument('-out', metavar = 'name', dest = 'out', type = str, required = True, help = 'Outfile base name')

if __name__ == '__main__':
	args = argparser.parse_args()
  dfo=pd.read_csv(args.in_file1, sep = "\s+", low_memory=False, usecols=[args.X,args.Y])
  plt.rcParams.update({'font.size': 20})
  fig, ax1 = plt.subplots(figsize=(20, 20))
  ax1.scatter(df[args.X],df[args.Y],edgecolors='black', s=30, facecolor="None")
  ax1.set_ylabel(args.labely)
  ax1.set_xlabel(args.labelx)
  ax1.set_aspect('equal', 'box')
  line=ax1.axline((0, 0), slope=1, color="red", linestyle=(0, (5, 5)), label = '1:1')
  ax1.legend(handles=[line])
  ax1.grid()
  plt.tight_layout()
  plt.savefig(args.out+".png")
