import numpy as np

from exact_cover.io import DTYPE_FOR_ARRAY

# one specific problem that I had trouble with
# originally based on solving the trivial problem
# of arranging 2 identical triminos on a 3x3 board

#    +--+
#    |  |
# +--+--+
# |  |  |
# +--+--+

# +--+--+--+
# |xx|  |xx|
# +--+--+--+
# |  |  |  |
# +--+--+--+
# |xx|  |  |
# +--+--+--+

# this problem has 2 solutions
# (5, 13) and (6, 12)
def small_trimino_problem():
    to_cover = [
        [1, 0, 0, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 0, 0],  # <- 5
        [1, 0, 0, 0, 0, 1, 1, 1],  # <- 6
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 0, 0],  # <- 12
        [0, 1, 0, 0, 0, 1, 1, 1],  # <- 13
    ]
    return dict(
        data=np.array(to_cover, dtype=DTYPE_FOR_ARRAY),
        solution1=[5, 13],
        solution_count=2,
    )

def small_trimino_problem_from_file():
    return dict(
        data=np.load("tests/files/small_trimino_problem.npy"),
        solution1=[5, 13],
        solution_count=2,
    )

# https://en.wikipedia.org/wiki/Exact_cover#Detailed_example
def detailed_wikipedia_problem():
    sets = [
        {1, 4, 7},
        {1, 4},         # <- 1
        {4, 5, 7},
        {3, 5, 6},      # <- 3
        {2, 3, 6, 7},
        {2, 7},         # <- 5
    ]
    return dict(
        data=np.array(
            [[1 if i in s else 0 for i in range(1, 8)] for s in sets], 
            dtype=DTYPE_FOR_ARRAY),
        solution1=[1, 3, 5],
        solution_count=1,
    )
