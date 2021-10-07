# Author: Katherina Cortes
# Date: September 29, 2021
# Purpose: Take a tab delimited .gmz file of gene sets, a given tab-delimited STRING file
#   create a sub network of the gene interactions from the input file using the STRING file
#   get statistical significance

import operator
from functools import reduce
import networkCreation, fileParsing, stats

def main():
    inputF = 'input.gmt.txt'
    stringF = 'STRING.txt'

    # read in networks
    lociNetwork = fileParsing.readInput(inputF)
    coFNetwork = fileParsing.makeInteractionNetwork(stringF)

    # create subnetworks  5000 loci, 1000 coF
    networkCreation.createSubnetwork(lociNetwork)


    # calc edge density
    # calc statistical significance

