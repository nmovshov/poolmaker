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
                row = [k.strip() for k in row]
                fencers.append(row)
    except:
        print("Error while reading competitors list.")
        print("Check that the file exists and has the correct format:")
        print("  LAST,  first,  club, rating")
        print
        raise

    # Sort competitors by rank
    rkey = lambda f: f[-1]
    rcmp = lambda x,y: -2*cmp(x[0],y[0]) + 1*cmp(x[1:],y[1:])
    fencers.sort(key=rkey, cmp=rcmp, reverse=True)

    # Determine pool sizes
    N = len(fencers)
    fs = (6,7)
    ps = _lmfactor(N,6,7)
    if ps is None:
        fs = (7,8)
        ps = _lmfactor(N,7,8)
    if ps is None:
        fs = (5,6)
        ps = _lmfactor(N,5,6)
    if ps is None:
        raise Exception
    pools = ps[0]*[fs[0]] + ps[1]*[fs[1]]

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
    if N%L == 0:
        return (int(N/L), 0)
    if N%M == 0:
        return (0, int(N/M))
    for k in range(int(math.ceil((N - M)/L) + 2)):
        j = (N - k*L)/M
        if j >= 0 and (int(j) - j) == 0:
            return (k, int(j))
    return None

if __name__ == "__main__":
    _main()
    pass
