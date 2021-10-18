# Statistical Significance of Genetic Functional Networks Using Edge Density 

## Goal
Compute the statistical significance of a population of subnetworks from a 
set of FA loci compared to the STRING database. 

## Install
scipy

## Usage
#### Python Usage
```python
import operator
from functools import reduce
import scipy
```
#### Command Line Usage
```commandline
$ python main.py Input.gmt.txt STRING.txt 
$ python main.py yourInputFile.gmt.txt
```

## Input
1. Input.gmt
- disjoint gene sets
- tab-delimited file Input.gmt
- First two columns describe row of gene set
- format: (https://software.broadinstitute.org/cancer/software/gsea/wiki/index.php/Data_formats/)
2. STRING.txt
- STRING database of known and predicted protein-protein interactions
- tab-delimited
- each line represents an edge in network between two genes
- weighted by strength of functional similarity

## Output
p values for subnetworks