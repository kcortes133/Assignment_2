# Author: Katherina Cortes
# Date: September 29, 2021
# Purpose: Different possible statistical tests for networks and subnetworks

import matplotlib.pyplot as plt
import numpy as np


# edge density defined in the paper as edge count
# bool avgDensity if want avg num of edges/node -> good if networks have diff num of nodes
#   default set to false
# @param network
# @param avgDensity=False
def calcEdgeDensity(network):
    density = 0

    # each edge is represented twice so
    for node in network:
        density += len(network[node])
    density = density/2


    return density


# @param densities
# @displays
def histogram(densities):
    # Plot Histogram on x
    plt.hist(densities)
    plt.gca().set(title='Density Distribution Histogram', ylabel='Density');
    plt.show()
    return


# @param dens1
# @param dens2
def overlappingHistogram(dens1, dens2):

    # Plot Histogram on x
    plt.hist([dens1, dens2])
    plt.gca().set(title='Edge Density Histogram', ylabel='Number of Nodes');
    plt.legend(loc='upper right')
    plt.show()


# @param subNetworks
# @param fullNetwork
# @param loci
def empiricalPVal(lociSubN, coFSubN):
    # use avg density of final population in random trial
    # P value representing fraction of random trials producing final pop of subnetworks
    # with higher avg density than the avg density seen with true loci inputs
    lociDensity = 0
    for subNet in lociSubN:
        # calculate the edge density
        tempLD = calcEdgeDensity(subNet)
        lociDensity += tempLD
    lociDensity = lociDensity/len(lociSubN)

    coFDensities = []
    for coF in coFSubN:
        coFDensities.append(calcEdgeDensity(coF))

    coFDensities = sorted(coFDensities)
    pos = 0
    densPos = 0
    for c in coFDensities:
        if c <=lociDensity:
            p = pos
            densPos = c
        pos +=1

    pval = p/len(coFDensities)
    plt.hist(coFDensities)
    plt.axvline(densPos, color='k', linestyle='dashed', linewidth=1)
    plt.title('Empirical P-Value')
    min_ylim, max_ylim = plt.ylim()
    plt.text(lociDensity, max_ylim*0.9, 'Pval = '+ str(pval))
    plt.show()
    return pval
