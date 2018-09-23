#---------------------------------------------------------------------------------
# POOLMAKER - a utility for dividing fencers into equal-difficulty pools
#
# Bugs and questions to: Naor Movshovitz (nmovshov@gmail.com)
#---------------------------------------------------------------------------------
import sys, os, shutil
import argparse
cout = sys.stdout.write
cerr = sys.stderr.write

def _main():

    # Parse command line arguments
    args = _PCL()

    # Finalize and return
    return

def _PCL():

    parser = argparse.ArgumentParser(
        description="POOLMAKER " +
        " - Fencing tournament toy problem",
        epilog="WARNING: just a toy problem.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('keys_file', help="file containing list of keys to " +
        "filter on, one per line")
    parser.add_argument('target_file', help="column delimited file containing " +
        "records to be filtered")
    parser.add_argument('-d','--delimiter',
        help="single-character column delimiter used in target file"+
             " (may need to be double-quoted)",
        choices=['t','s',',',';',' ','/'],
        default='t')

    args = parser.parse_args()

    if args.delimiter is 't':
        args.delimiter = '\t'
    if args.delimiter is 's':
        args.delimiter = ' '

    return args

if __name__ == "__main__":
    print "Running POOLMAKER"
    _main()
    pass
