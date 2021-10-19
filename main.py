# Author: Katherina Cortes
# Date: September 29, 2021
# Purpose: Take a tab delimited .gmz file of gene sets, a given tab-delimited STRING file
#   create a sub network of the gene interactions from the input file using the STRING file
#   get statistical significance

import argparse, logging
import networkCreation, fileParsing, statistics

# arguments:
#   - input file
#   - STRING file
#   - number of bins for cof network default=128
#   - number of networks to run
#   - fixed or quantile


parser = argparse.ArgumentParser(description='Get the statistical significance of the connection of genes vs random '
                                             'genes.')
parser.add_argument('genesFile', metavar='genes', type=str, default='Input.gmt.txt',
                    help='the input file of genes')
parser.add_argument('--interactionsFile', metavar='gene_interactions', type=str, default='STRING.txt',
                    help='the input file of gene interactions')
parser.add_argument('--numBins', type=int, default=128, help='the number of bins to separate edge densities into')
parser.add_argument('--numSubnetworks', type=int, default=5000, help='the number of subnetworks to make')

args = parser.parse_args()
print(args)

def main():
    #inputF = 'input.gmt.txt'
    #stringF = 'STRING.txt'

    # read in networks
    lociLists = fileParsing.readInput(args.genesFile)
    interactions = fileParsing.makeInteractionNetwork(args.interactionsFile)
    network = fileParsing.makeNetwork(lociLists, interactions)

    # make loci subnetworks
    lociSubN = networkCreation.makeLociSubnetworks(args.numSubnetworks, network, lociLists)

    numBins = args.numBins
    # make bins for coFunctional subnetwork creation
    qNetworkBins = networkCreation.makeQuantileBins(interactions, numBins)
    # fNetworkBins = makeFixedBins(interactions, numBins)

    # make coFunctional random subnetworks
    coFSubnetworks = networkCreation.makeCoFSubnetworks(interactions, qNetworkBins, lociSubN)

    # calculate the pvalue
    # probability edges using cof distribution is greater than avg of loci edged divided by # of random networks
    pval = statistics.empiricalPVal(lociSubN, coFSubnetworks)

    # make a graph showing the edge density distributions
    coFDensities = []
    for network in coFSubnetworks:
        coFDensities.append(statistics.calcEdgeDensity(network))

    lociDensities = []
    for network in lociSubN:
        lociDensities.append(statistics.calcEdgeDensity(network))

    statistics.overlappingHistogram(coFDensities, lociDensities)

    print('P-val : ', pval)

main()