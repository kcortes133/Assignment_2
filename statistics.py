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
def calcEdgeDensity(network, avgDensity=False):
    density = 0

    # each edge is represented twice so
    for node in network:
        density += len(network[node])
    density = density/2

    if avgDensity:
        density = density/len(network)

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
def empiricalPVal(subNetworks, fullNetwork, loci):
    # //TODO
    # use avg density of final population in random trial
    # P value representing fraction of random trials producing final pop of subnetworks
    # with higher avg density than the avg density seen with true loci inputs
    return
