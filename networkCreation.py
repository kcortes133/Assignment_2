# Author: Katherina Cortes
# Date: September 29, 2021
# Purpose: Create subnetworks and full network from FA loci genes and STRING database


# @param fullNetwork
# @param numNetworks
# @returns subnetworks
def makeLociSubnetworks(numNetworks, fullNetwork):
    subNetworks = []
    for i in range(numNetworks):
        createSubnetwork(fullNetwork)
    return subNetworks


# @param fullNetwork
# @returns subNetwork
def createSubnetwork(fullNetwork):
    subNetwork = {}
    # //TODO
    # pick
    return subNetwork


# @param
# @return
def makecoFBins(fullNetwork):
    fullNetworkBins = []
    # //TODO
    return fullNetworkBins


# create a subnetwork of the cofunctional network
# where nodes have similar density to nodes in the loci sub network
# @param
# @param
# @return
def makeCoFSubnetworks(fullNetworkBins, lociSubN):
    # //TODO
    return
