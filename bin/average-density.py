#!/usr/bin/env python

'''Calculate average density of a set of data files.'''

import sys
import numpy as np
from matplotlib import pyplot as plt

def main(visualize, args):
    '''Read files and produce grid of filling probability.'''

    total = None
    for filename in args:
        current = np.loadtxt(filename, delimiter=',')
        if total is None:
            total = current
        else:
            total += current

    total /= len(args)

    if visualize:
        plt.imshow(total)
        plt.show()
    else:
        np.savetxt(sys.stdout.buffer, total, delimiter=',', fmt='%1.3f')


if __name__ == '__main__':
    if sys.argv[1] == '-p':
        visualize, filenames = True, sys.argv[2:]
    else:
        visualize, filenames = False, sys.argv[1:]
    main(visualize, filenames)
