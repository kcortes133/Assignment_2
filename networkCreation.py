# Author: Katherina Cortes
# Date: September 29, 2021
# Purpose: Create subnetworks and full network from FA loci genes and STRING database

import random
import fileParsing

# @param fullNetwork
# @param numNetworks
# @returns subnetworks
def makeLociSubnetworks(numNetworks, fullNetwork, lociLists):
    subNetworks = []
    for i in range(numNetworks):
        #subNetworks.append(createSubnetwork(fullNetwork, lociLists))
        if createSubnetwork(fullNetwork, lociLists):
            return

    return subNetworks


# @param fullNetwork
# @returns subNetwork
def createSubnetwork(fullNetwork, lociLists):
    subNetwork = {}
    hasEdges = False
    # for loci in network:
    # pick gene randomly
    # get all connections
    for loci in lociLists:
        randGene = random.choice(list(loci))
        subNetwork[randGene] = {}
    print('------------')
    print(subNetwork)

    # get edges
    for gene1 in subNetwork:
        print(gene1)
        # connect nodes with edges
        #if len(fullNetwork[gene1]) > 0:
        #    print(fullNetwork[gene1])
        print(fullNetwork[gene1])
        for gene2 in fullNetwork[gene1]:
            if gene2 in subNetwork:
                weight = fullNetwork[gene1][gene2]
                subNetwork[gene1][gene2] = weight
                print(gene1, ' : ', gene2)
                hasEdges = True

    #return subNetwork
    print(subNetwork)
    return hasEdges

# @param
# @return
def makecoFBins(fullNetwork, numBins):
    fullNetworkBins = []
    # //TODO
    # dict should be node: num Edges
    # sort dict by values
    # 128 bins like in paper -> equally spaced

    return fullNetworkBins


# create a subnetwork of the cofunctional network
# where nodes have similar density to nodes in the loci sub network
# @param
# @param
# @return
def makeCoFSubnetworks(fullNetworkBins, lociSubN):
    # //TODO
    # for each node in lociSubN
    #   pick node from networkBins where numEdges is similar for both
    # make edges between picked nodes
    return


lociLists = fileParsing.readInput('Input.gmt.txt')
interactions = fileParsing.makeInteractionNetwork('STRING.txt')
network = fileParsing.makeNetwork(lociLists, interactions)
#createSubnetwork(network, lociLists)
makeLociSubnetworks(100, network, lociLists)