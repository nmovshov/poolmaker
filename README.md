POOLMAKER - A tool for planning a fencing tournament
====================================================

Usage:

    python poolmaker.py input_file.csv
    python poolmaker.py --help

or if your python is in a standrd location you can `chmod u+x poolmaker.py`
run as an executable:

    ./poolmaker.py input_file.csv

### Notes on implementation
I implemented `toolmaker.py` as a command-line tool, i.e., meant to be invoked
from the shell rather than imported into another python program. It's still
possible to `import poolmaker` of course, but if this is the desired usage I would
recommend renaming `_main()` into something more meaningful and putting a
docstring.

There are three basic tasks for `poolmaker` to handle.

1. Reading and sorting in the competitors list.
   I use the `csv` module from the standard library to read in the file. Minor
   issues (e.g. extra whitespaces, blank lines) are not a problem, but in general
   I assume a valid file exists with read permissions and the correct format. A
   failed read for any reason displays the same warning message (including the
   expected format) and re-raises the exception.

   Sorting fencers by rank is easy enough if we are allowed to assume a valid code
   in the rank system. (A 2-digit year code can be sorted lexicographically
   without converting to a number.)

2. Dealing fencers into pools of equivalent difficulty.
   One way to handle this is to sort fencers by rank and then continuously deal
   the strongest remaining fencer to the weakest remaining pool, until all are
   accounted for.

   To determine the pool sizes we "factor" the number of fencers, N, into products
   of 6 and 7, or 7 and 8, or 5 and 6. There _might_ be an elegant mathemtical
   trick to factoring N on two arbitrary integers, L and M, but it's easy enough
   to search the integers 1 through N/L for a solution. The solution is certainly
   not unique in and the implementation in `poolmaker._lmfactor(N, L, M)` does not
   have a preference between, e.g., pool sizes of 6 or 7. For example, for N=42,
   the choice of six pools of seven fencers versus seven pools of six fencers
   depends on the order of arguments.

   The exact distribution into pools will also depend on the unspecified order of
   pool sizes, e.g. (6, 7) versus (7, 6). But the variation in pool "strength"
   would be minimal.

3. Swap fencers to avoid club-conflicts.
   I put a place-holder method and I may come back to this in the future.

### Examples, tests
