#---------------------------------------------------------------------------------
# POOLMAKER - a utility for dividing fencers into equal-difficulty pools
#
# Bugs and questions to: Naor Movshovitz (nmovshov@gmail.com)
#---------------------------------------------------------------------------------
from __future__ import division
import sys, os, shutil
import math
import argparse
import csv
cout = sys.stdout.write
cerr = sys.stderr.write

def _main():

    # Parse command line arguments
    args = _PCL()

    # Load competitors list
    try:
        with open(args.competitors_file, 'rb') as f:
            fencers = []
            reader = csv.reader(f, delimiter=args.delimiter)
            for row in reader:
                assert(len(row)==4)
                fencers.append(row)
    except:
        print("Error while reading competitors list.")
        print("Check that the file exists and has the correct format:")
        print("  LAST,  first,  club, rating")
        print
        raise

    # Determine pool sizes
    print(fencers)
    pass

    # Finalize and return
    return

def _PCL():

    parser = argparse.ArgumentParser(
        description="POOLMAKER - plan a fencing tournament",
        epilog="WARNING: this is a toy problem, not a real tool.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('competitors_file', help="csv file containing list of " +
        "competitors with ratings and club affiliation.")
    parser.add_argument('-O','--output-file', help="Specify output to file " +
        "instead of to stdout.")
    parser.add_argument('-d','--delimiter',
        help="single-character column delimiter used in input file if " +
             "non-standard. (Note: may need to be double-quoted.)",
        choices=['t','s',',',';',' ','/'],
        default=',')

    args = parser.parse_args()

    if args.delimiter is 't':
        args.delimiter = '\t'
    if args.delimiter is 's':
        args.delimiter = ' '

    return args

def _lmfactor(N, L, M):
    # Return factorization of positive integer into two arbitrary positive integers.

    assert(N > 0)
    for k in range(int(math.ceil((N - M)/L) + 2)):
        j = (N - k*L)/M
        if j >= 0 and (int(j) - j) == 0:
            return (k, j)
    return None

if __name__ == "__main__":
    _main()
    pass
