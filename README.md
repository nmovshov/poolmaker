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
1. Simplest case. Comparing with provided case, the two pools are identical except
   for the placement of the weakest fencer (placed last) due to unspecified pool
   order (pool #1(6) pool #2(7) or vice versa).

      [nmovshov@clyde ~/poolmaker]$ python poolmaker.py MEshort.csv
      Competitor List
      Keith                LICHTEN                 EBFG                    A       15
      Alexandre            RACHTCHININE            FAIRFAX FENCERS CLUB    A       15
      Mehmet               TEPEDELENLIOGLU         EBFG                    A       15
      David                HITCHCOCK               OLYMPIA F. C.           A       15
      Sergey               SUPONYA                 MEDEO F.C.              A       15
      Halim                ALJIBURY                NO FEAR                 A       14
      Velizar              ILIEV                   OLYMPIANFC              A       14
      Tomas                STRAKA                  SSC                     A       12
      Daniel               KROGH                   NWFC                    B       15
      Kenneth              HAGAN                   LOUISVLLE F.C.          B       14
      Alfred               ROEBUCK                 NO FEAR                 B       13
      John                 KISSINGFORD             NO FEAR                 C       15
      Aaron                PAGE                    METRO TACOMA            C       15


      Pool List
      --)------- Pool # 1 -------(-- (6)
      Keith                LICHTEN                 EBFG                    A       15
      David                HITCHCOCK               OLYMPIA F. C.           A       15
      Sergey               SUPONYA                 MEDEO F.C.              A       15
      Tomas                STRAKA                  SSC                     A       12
      Daniel               KROGH                   NWFC                    B       15
      John                 KISSINGFORD             NO FEAR                 C       15

      --)------- Pool # 2 -------(-- (7)
      Alexandre            RACHTCHININE            FAIRFAX FENCERS CLUB    A       15
      Mehmet               TEPEDELENLIOGLU         EBFG                    A       15
      Halim                ALJIBURY                NO FEAR                 A       14
      Velizar              ILIEV                   OLYMPIANFC              A       14
      Kenneth              HAGAN                   LOUISVLLE F.C.          B       14
      Alfred               ROEBUCK                 NO FEAR                 B       13
      Aaron                PAGE                    METRO TACOMA            C       15

2. More complete list. Competitor list handled correctly. Pool distrobution is
   similar to provided output except for the fencers swapped to avoid club
   conflicts. (Not yet implemented.)

      [nmovshov@clyde ~/poolmaker]$ python poolmaker.py MEentries.csv
      Competitor List
      Keith                LICHTEN                 EBFG                    A       15
      Alexandre            RACHTCHININE            FAIRFAX FENCERS CLUB    A       15
      Mehmet               TEPEDELENLIOGLU         EBFG                    A       15
      David                HITCHCOCK               OLYMPIA F. C.           A       15
      Sergey               SUPONYA                 MEDEO F.C.              A       15
      Tracy                COLWELL                 CARDINAL                A       15
      Alexander            TUROFF                  FISHKILL / CANDLE       A       15
      Halim                ALJIBURY                NO FEAR                 A       14
      Velizar              ILIEV                   OLYMPIANFC / USMPENT    A       14
      Kashi                WAY                     DCFC                    A       14
      Joseph               DEUCHER                 TOURFC                  A       14
      Alberto              FELIX                                           A       14
      Creston              BAILEY                  NO FEAR                 A       14
      Tomas                STRAKA                  WCFA                    A       12
      Daniel               KROGH                   NWFC                    B       15
      Andrew               DAVIS                   EBFG                    B       15
      Joseph               HARRINGTON                                      B       15
      Kenneth              HAGAN                   LOUISVLLE F.C.          B       14
      Michael              LOPARCO                 ALLIANCE F.A.           B       14
      Manuel               CORRALES                                        B       14
      Alfred               ROEBUCK                 NO FEAR                 B       13
      Steven               FIALKOWSKI              EBFG                    B       13
      Christopher          GETSLA                  CABRAOTSL               B       11
      John                 KISSINGFORD             DFC                     C       15
      Aaron                PAGE                    METRO TACOMA            C       15
      Phil                 AJAYI                   PFFC                    C       15
      Marc                 UNGER                   TFCSANJOSE              C       14
      John                 COMES                   W.F.A.                  C       14
      Lewis                WADSWORTH IV            BSF                     C       13
      David                ST. GEORGE              IL F.C.                 C       13
      Marc                 KURITZ                  NO FEAR                 C       13
      David                NEMAZIE                 SALISBURY               C       12
      Robert               THOMAS Jr.              CFFA                    C       11
      Jansen               HU                      LAIFC                   D       14
      Onno                 VAN EIKEMA HOMMES       OLYMPIA F. C.           D       14
      Robert               HARRIS                  OLYMPIA F. C.           E       15
      Paul                 FLY                     SAS                     E       14
      Cesar                COLLANTES               EBFG                    E       14
      Gregory              PEISTRUP                F.A. - NV               E       13
      Michael              MRAK                    MEDEO F.C.              U
      Stephen              LEE                                             U
      Oronde               GORDON                  EBFG                    U
      Arejas               UZGIRIS                 WESTBFC                 U
      Sean                 FLETCHER                EBFG                    U
      Sushil               TYAGI                   LAIFC                   U
      Matthias             ROSCHKE                 DECESARE                U
      Scott                DOUDRICK                FORTUNE                 U
      Brian                FERGUSON                TFCSANJOSE / FORTUNE    U


      Pool List
      --)------- Pool # 1 -------(-- (6)
      Keith                LICHTEN                 EBFG                    A       15
      Andrew               DAVIS                   EBFG                    B       15
      Joseph               HARRINGTON                                      B       15
      David                NEMAZIE                 SALISBURY               C       12
      Robert               THOMAS Jr.              CFFA                    C       11
      Brian                FERGUSON                TFCSANJOSE / FORTUNE    U

      --)------- Pool # 2 -------(-- (6)
      Alexandre            RACHTCHININE            FAIRFAX FENCERS CLUB    A       15
      Daniel               KROGH                   NWFC                    B       15
      Kenneth              HAGAN                   LOUISVLLE F.C.          B       14
      Marc                 KURITZ                  NO FEAR                 C       13
      Jansen               HU                      LAIFC                   D       14
      Scott                DOUDRICK                FORTUNE                 U

      --)------- Pool # 3 -------(-- (6)
      Mehmet               TEPEDELENLIOGLU         EBFG                    A       15
      Tomas                STRAKA                  WCFA                    A       12
      Michael              LOPARCO                 ALLIANCE F.A.           B       14
      David                ST. GEORGE              IL F.C.                 C       13
      Onno                 VAN EIKEMA HOMMES       OLYMPIA F. C.           D       14
      Matthias             ROSCHKE                 DECESARE                U

      --)------- Pool # 4 -------(-- (6)
      David                HITCHCOCK               OLYMPIA F. C.           A       15
      Creston              BAILEY                  NO FEAR                 A       14
      Manuel               CORRALES                                        B       14
      Lewis                WADSWORTH IV            BSF                     C       13
      Robert               HARRIS                  OLYMPIA F. C.           E       15
      Sushil               TYAGI                   LAIFC                   U

      --)------- Pool # 5 -------(-- (6)
      Sergey               SUPONYA                 MEDEO F.C.              A       15
      Alberto              FELIX                                           A       14
      Alfred               ROEBUCK                 NO FEAR                 B       13
      John                 COMES                   W.F.A.                  C       14
      Paul                 FLY                     SAS                     E       14
      Sean                 FLETCHER                EBFG                    U

      --)------- Pool # 6 -------(-- (6)
      Tracy                COLWELL                 CARDINAL                A       15
      Joseph               DEUCHER                 TOURFC                  A       14
      Steven               FIALKOWSKI              EBFG                    B       13
      Marc                 UNGER                   TFCSANJOSE              C       14
      Cesar                COLLANTES               EBFG                    E       14
      Arejas               UZGIRIS                 WESTBFC                 U

      --)------- Pool # 7 -------(-- (6)
      Alexander            TUROFF                  FISHKILL / CANDLE       A       15
      Kashi                WAY                     DCFC                    A       14
      Christopher          GETSLA                  CABRAOTSL               B       11
      Phil                 AJAYI                   PFFC                    C       15
      Gregory              PEISTRUP                F.A. - NV               E       13
      Oronde               GORDON                  EBFG                    U

      --)------- Pool # 8 -------(-- (6)
      Halim                ALJIBURY                NO FEAR                 A       14
      Velizar              ILIEV                   OLYMPIANFC / USMPENT    A       14
      John                 KISSINGFORD             DFC                     C       15
      Aaron                PAGE                    METRO TACOMA            C       15
      Michael              MRAK                    MEDEO F.C.              U
      Stephen              LEE                                             U

3. Case with lots of club conflicts. Again competitors list and pool sizes match
   the provided output, but a lot more conflicts lead to one or two fencer
   differences in many pools.

      [nmovshov@clyde ~/poolmaker]$ python poolmaker.py MEconflicts.csv
      Competitor List
      Keith                LICHTEN                 EBFG                    A       15
      Alexandre            RACHTCHININE            NO FEAR                 A       15
      Mehmet               TEPEDELENLIOGLU         EBFG                    A       15
      David                HITCHCOCK               NO FEAR                 A       15
      Sergey               SUPONYA                 MEDEO F.C.              A       15
      Tracy                COLWELL                 EBFG                    A       15
      Alexander            TUROFF                  FISHKILL / CANDLE       A       15
      Halim                ALJIBURY                NO FEAR                 A       14
      Velizar              ILIEV                   OLYMPIANFC / USMPENT    A       14
      Kashi                WAY                     EBFG                    A       14
      Joseph               DEUCHER                                         A       14
      Alberto              FELIX                                           A       14
      Tomas                STRAKA                                          A       12
      Daniel               KROGH                   EBFG                    B       15
      Andrew               DAVIS                   EBFG                    B       15
      Joseph               HARRINGTON              NO FEAR                 B       15
      Kenneth              HAGAN                   LOUISVLLE F.C.          B       14
      Michael              LOPARCO                                         B       14
      Alfred               ROEBUCK                 NO FEAR                 B       13
      John                 KISSINGFORD             NO FEAR                 C       15
      Aaron                PAGE                    METRO TACOMA            C       15
      David                NEMAZIE                 EBFG                    C       12
      Jansen               HU                                              D       14
      Michael              MRAK                    MEDEO F.C.              U


      Pool List
      --)------- Pool # 1 -------(-- (6)
      Keith                LICHTEN                 EBFG                    A       15
      Halim                ALJIBURY                NO FEAR                 A       14
      Velizar              ILIEV                   OLYMPIANFC / USMPENT    A       14
      Joseph               HARRINGTON              NO FEAR                 B       15
      Kenneth              HAGAN                   LOUISVLLE F.C.          B       14
      Michael              MRAK                    MEDEO F.C.              U

      --)------- Pool # 2 -------(-- (6)
      Alexandre            RACHTCHININE            NO FEAR                 A       15
      Alexander            TUROFF                  FISHKILL / CANDLE       A       15
      Kashi                WAY                     EBFG                    A       14
      Andrew               DAVIS                   EBFG                    B       15
      Michael              LOPARCO                                         B       14
      Jansen               HU                                              D       14

      --)------- Pool # 3 -------(-- (6)
      Mehmet               TEPEDELENLIOGLU         EBFG                    A       15
      Tracy                COLWELL                 EBFG                    A       15
      Joseph               DEUCHER                                         A       14
      Daniel               KROGH                   EBFG                    B       15
      Alfred               ROEBUCK                 NO FEAR                 B       13
      David                NEMAZIE                 EBFG                    C       12

      --)------- Pool # 4 -------(-- (6)
      David                HITCHCOCK               NO FEAR                 A       15
      Sergey               SUPONYA                 MEDEO F.C.              A       15
      Alberto              FELIX                                           A       14
      Tomas                STRAKA                                          A       12
      John                 KISSINGFORD             NO FEAR                 C       15
      Aaron                PAGE                    METRO TACOMA            C       15
