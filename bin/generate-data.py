#!/usr/bin/env python

'''
Randomize a pyramid.
'''

import sys
import numpy as np


def main(args):

    # To keep things simple, insist on an odd-sized grid.
    size = int(args[0])
    assert size % 2 == 1, 'Size must be odd'

    # Rise linearly from 0.0 at each end to 1.0 in the center.
    saw = 2 * (0.5 - abs((np.linspace(0, size, size) / size) - 0.5))

    # Now multiply two of those at right angles to make a pyramid.
    pyr_x = np.zeros((size, size))
    pyr_x[:, :] = saw
    pyr_y = np.zeros((size, size))
    pyr_y[:, :] = saw
    pyr_y = pyr_y.T
    pyr = pyr_x * pyr_y

    # Pyramid is the probability a cell is full or empty.
    samples = 0.5 * np.random.random((size, size))
    result = samples < pyr

    # Output as a CSV grid of 1's and 0's.
    result = result.astype(int)
    np.savetxt(sys.stdout.buffer, result, delimiter=',', fmt='%1d')


if __name__ == '__main__':
    main(sys.argv[1:])
