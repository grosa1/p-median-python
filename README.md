# p-median-python

This repository contains a Python-based implementation designed for the [Reply Code Challenge 2019](https://challenges.reply.com/challenges/coding/standard-code-challenge/detail/). The project focuses on solving a variation of the p-median problem, a classic location-allocation challenge in combinatorial optimization.

## Problem Overview

The p-median problem involves selecting p facilities from a set of candidate locations to minimize the total weighted distance between demand points and their nearest selected facility. In this repository, we tackle a specific instance of this problem experimenting with different optimization algorithms (KMeans and SimluatedAnnealing).


## Getting Started

Clone the repo:
```
git clone https://github.com/grosa1/p-median-python.git
```

Install dependencies:
```
pip install -r requirements.txt
```

Run the solver:
```
python run.py <data-file.csv>
```
