#!/usr/bin/env python

'''
Randomize a pyramid.
'''

import sys
import numpy as np


def main(args):
    '''Generate random pyramid sample to standard output.'''

    size, threshold, seed = parse_args(args)
    if seed is not None:
        np.random.seed(seed)

    result = generate(size, threshold)

    # Output as a CSV grid of 1's and 0's.
    np.savetxt(sys.stdout.buffer, result, delimiter=',', fmt='%1d')


def generate(size, threshold):
    '''Generate size*size sampled pyramid of 0s and 1s.'''

    # Rise linearly from 0.0 at each end to 1.0 in the center.
    triangle = np.linspace(0, 1, (size+1)/2)
    triangle = np.concatenate((triangle, triangle[-2::-1]))

    # Multiply two of those at right angles to make a pyramid.
    pyramid = np.outer(triangle, triangle)

    # Pyramid determines probability that a cell is full or empty.
    result = (threshold * np.random.random((size, size))) < pyramid
    result = result.astype(int)

    return result

def parse_args(args):
    '''Parse command-line arguments.'''

    # Sanity check.
    if not (1 <= len(args) <= 3):
        fail('Usage: generate-data.py size [threshold] [seed]')
        sys.exit(1)

    # To keep things simple, insist on an odd-sized grid.
    size = int(args[0])
    if (size < 0) or (size % 2 != 1):
        fail('size must be positive and odd')
        sys.exit(1)

    # Check filling threshold.
    threshold = 0.5
    if len(args) > 1:
        threshold = float(args[1])
        if not (0.0 <= threshold <= 1.0):
            fail('threshold must be between 0.0 and 1.0')
            sys.exit(1)

    # Seed the random number generator.
    seed = None
    if len(args) > 2:
        seed = int(args[2])

    return size, threshold, seed


def fail(msg):
    '''Report a problem and exit.'''
    print(msg, file=sys.stderr)
    sys.exit(1)


if __name__ == '__main__':
    main(sys.argv[1:])
