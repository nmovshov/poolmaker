#---------------------------------------------------------------------------------
# POOLMAKER - a utility for dividing fencers into equal-difficulty pools
#
# Bugs and questions to: Naor Movshovitz (nmovshov@gmail.com)
#---------------------------------------------------------------------------------
from __future__ import division
import sys
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

    # Sort competitors by rank (NOTE: assumes correct rank code: '[A-Z]YY')
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
    pool_sizes = ps[0]*[fs[0]] + ps[1]*[fs[1]]
    pools = [[] for _ in pool_sizes]

    # Distribute fencers into pools
    _fill_pools(fencers, pools, pool_sizes)

    # Write output and return
    output = _fmt_output(fencers, pools)
    cout(output)
    return

def _fill_pools(fencers, pools, pool_sizes):
    next_pool = 0
    next_dir = +1
    t_fencers = list(fencers); t_fencers.reverse() # tmp list to pop into pools
    while len(t_fencers) > 0:
        if len(pools[next_pool]) < pool_sizes[next_pool]:
            pools[next_pool].append(t_fencers.pop())
        next_pool += next_dir
        if next_pool == -1 or next_pool == len(pools):
            next_dir *= -1
            next_pool += next_dir
    return

def _fmt_output(fencers, pools):
    out = "Competitor list\n"
    for f in fencers:
        out += "{1:22s}{0:22s}{2:22s}{3[0]:8s}".format(*f)
        out += "{}\n".format(f[3][1:])

    out += "\n\n"
    out += "Pool list\n"
    for k in range(len(pools)):
        out += "--)------- Pool # {} -------(-- ({})\n".format(k+1, len(pools[k]))
        for f in pools[k]:
            out += "{1:22s}{0:22s}{2:22s}{3[0]:8s}".format(*f)
            out += "{}\n".format(f[3][1:])
        out += "\n"
    return out

def _PCL():

    parser = argparse.ArgumentParser(
        description="POOLMAKER - plan a fencing tournament",
        epilog="WARNING: this is a toy problem, not a real tool.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('competitors_file', help="csv file containing list of " +
        "competitors with ratings and club affiliation.")
    parser.add_argument('-O','--output-file', help="Specify output to file " +
        "instead of to stdout.",
        default=None)
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
