# MMR: Maximal Marginal Relevance
[![Build Status](https://travis-ci.org/stepgazaille/mmr.svg?branch=master)](https://travis-ci.org/stepgazaille/mmr)


A naive implementation of MMR in Python 3.

## Installation
Requires Python >= 3.5.
```
cd mmr
pip install --upgrade pip

# Normal installation:
pip install .

# Editable installation:
pip install -e .
``` 

## Running tests
Use the following command to run unit tests:
``` 
python -m unittest
```

## Developpement corpus
A developpement corpus built using articles from [The Guardian](https://www.theguardian.com/international) is provided for development and testing.

## References
Original papers of baseline algorithms:
- **MMR**: Carbonell, J. & Goldstein, J. (1998). [The Use of MMR, Diversity-based Reranking for Reordering Documents and Producing Summaries](https://dl.acm.org/citation.cfm?id=291025). *Proceedings of he 21st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval* (pp. 335–336). New York, NY, USA : ACM.
