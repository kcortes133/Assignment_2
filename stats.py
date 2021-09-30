# Author: Katherina Cortes
# Date: September 29, 2021
# Purpose: Different possible statistical tests for networks and subnetworks


# edge density defined in the paper as edge count
# bool avgDensity if want avg num of edges/node -> good if networks have diff num of nodes
#   default set to false
def calcEdgeDensity(network, avgDensity=False):
    density = 0

    # each edge is represented twice so
    for node in network:
        density += len(node)
    density = density/2

    if avgDensity:
        density = density/len(network)

    return density


# @param subNetworks
# @param fullNetwork
# @param loci
def empiricalPVal(subNetworks, fullNetwork, loci):
    # //TODO
    # use avg density of final population in random trial
    # P value representing fraction of random trials producing final pop of subnetworks
    # with higher avg density than the avg density seen with true loci inputs
    return
