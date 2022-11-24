#!/usr/bin/env python3

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import argparse
from scipy import stats

argparser = argparse.ArgumentParser(description = '')
argparser.add_argument('-i1', metavar = 'name', dest = 'in_file1', type = str, required = True, help = 'Regenie Input to Mahattan plot')
argparser.add_argument('-T1', metavar = 'name', dest = 'in_file_Title1', type = str, required = True, help = 'Title of Manhattan plot/Subtitle of Miami plot')
argparser.add_argument('-i1', metavar = 'name', dest = 'in_file_Title2', type = str, required = False, help = 'Subtitle of Miami plot')
argparser.add_argument('-T2', metavar = 'name', dest = 'in_file2', type = str, required = False, help = 'Regenie Second Input to Miami plot.')
argparser.add_argument('-T', metavar = 'name', dest = 'args.trait', type = str, required = True, help = 'Name of the trait space = \'_\' | base Name of output ')


plt.rcParams.update({'font.size': 18})

def manhattan(Fig, file,inverted,title):
	df= pd.read_table(file, header=0,sep="\s+",low_memory=False,usecols=['CHROM','LOG10P'])
	df=df[df['LOG10P']!='TEST_FAIL']
	df['minuslog10pvalue'] = df['LOG10P'].astype(float)
	df.loc[df.minuslog10pvalue>11,'minuslog10pvalue'] = 11
	df["chromosome"]=df["CHROM"]
	df=df[~df.chromosome.isin(["Y"])]
	df.chromosome = df.chromosome.astype('category')
	df.chromosome = df.chromosome.cat.set_categories([ i for i in set(df.chromosome)], ordered=True)
	df = df.sort_values('chromosome')
	df['ind'] = range(len(df))
	df_grouped = df.groupby('chromosome')
	ax = Fig
	colors = ['black','gray']
	x_labels = []
	x_labels_pos = []
	for num, (name, group) in enumerate(df_grouped):
		group.plot(kind='scatter', x='ind', y='minuslog10pvalue',color=colors[num % len(colors)], s=9,ax=ax)
		x_labels.append(name)
		x_labels_pos.append((group['ind'].iloc[-1] - (group['ind'].iloc[-1] - group['ind'].iloc[0])/2))
	ax.set_xticks(x_labels_pos)
	ax.set_xticklabels(x_labels)
	# set axis limits
	ax.set_xlabel('Chromosome')
	ax.set_ylabel('-'+r'$\log_{10}$' +'(P-value)')
	ax.set_xlim([0, len(df)])
	ax.set_ylim([0, 12])
	if inverted :
		ax.invert_yaxis()
		ax.xaxis.tick_top()
		ax.xaxis.set_label_position('top')
		ax.title.set_text(title)
	else :
		ax.title.set_text(title)
	ax.axhline(y=7.30102999566 , color='r', linestyle='-')
  ax.title.set_text(title)
  
if __name__ == '__main__':
	args = argparser.parse_args()
	print('1')
  trait=args.trait
  if args.in_file2 is not None:
    fig, axs = plt.subplots(2, 1, constrained_layout=True,figsize=(32,15))
    manhattan(axs[0],args.in_file1,False, args.in_file_Title1)
	  manhattan(axs[1],args.in_file2,True, args.in_file_Title2)
	  plt.suptitle(Trait.replace('_',' '),fontsize=12)
	  fig.savefig(Trait + 'Miami.png', dpi=300)
  if args.in_file2 is None:
    fig, axs = plt.subplots(2, 1, constrained_layout=True,figsize=(32,8))
    manhattan(axs[0],args.in_file1,False, args.in_file_Title1)
    fig.savefig(Trait + 'manhattan.png', dpi=300)
