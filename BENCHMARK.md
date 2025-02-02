# Benchmarks

| Class            | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:-----------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile       | download.html        |          16 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile       | genindex-all.html    |          16 |        1755 |       2351 |     133.96% |   0.18 |   0.01 |
| FernetFile       | searchindex.js       |          16 |        3859 |       5169 |     133.96% |   0.76 |   0.03 |
| FernetFile       | library.pdf          |          16 |       11330 |      15178 |     133.96% |   6.90 |   0.09 |
| Bz2FernetFile    | download.html        |          16 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile    | genindex-all.html    |          16 |        1755 |        209 |      11.93% |   0.15 |   0.03 |
| Bz2FernetFile    | searchindex.js       |          16 |        3859 |        824 |      21.36% |   0.26 |   0.09 |
| Bz2FernetFile    | library.pdf          |          16 |       11330 |      14887 |     131.40% |   2.24 |   0.69 |
| ZstdFernetFile   | download.html        |          16 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile   | genindex-all.html    |          16 |        1755 |        324 |      18.49% |   0.01 |   0.00 |
| ZstdFernetFile   | searchindex.js       |          16 |        3859 |       1183 |      30.67% |   0.03 |   0.01 |
| ZstdFernetFile   | library.pdf          |          16 |       11330 |      14823 |     130.83% |   0.17 |   0.08 |
| FernetFile       | download.html        |         256 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile       | genindex-all.html    |         256 |        1755 |       2341 |     133.37% |   0.02 |   0.01 |
| FernetFile       | searchindex.js       |         256 |        3859 |       5146 |     133.37% |   0.04 |   0.02 |
| FernetFile       | library.pdf          |         256 |       11330 |      15111 |     133.37% |   0.17 |   0.07 |
| Bz2FernetFile    | download.html        |         256 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile    | genindex-all.html    |         256 |        1755 |        209 |      11.88% |   0.15 |   0.04 |
| Bz2FernetFile    | searchindex.js       |         256 |        3859 |        821 |      21.27% |   0.27 |   0.12 |
| Bz2FernetFile    | library.pdf          |         256 |       11330 |      14822 |     130.82% |   1.79 |   0.83 |
| ZstdFernetFile   | download.html        |         256 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile   | genindex-all.html    |         256 |        1755 |        323 |      18.41% |   0.01 |   0.00 |
| ZstdFernetFile   | searchindex.js       |         256 |        3859 |       1178 |      30.53% |   0.03 |   0.01 |
| ZstdFernetFile   | library.pdf          |         256 |       11330 |      14754 |     130.22% |   0.16 |   0.07 |
| FernetFile       | download.html        |        1024 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile       | genindex-all.html    |        1024 |        1755 |       2340 |     133.34% |   0.02 |   0.02 |
| FernetFile       | searchindex.js       |        1024 |        3859 |       5145 |     133.34% |   0.03 |   0.04 |
| FernetFile       | library.pdf          |        1024 |       11330 |      15108 |     133.34% |   0.12 |   0.14 |
| Bz2FernetFile    | download.html        |        1024 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile    | genindex-all.html    |        1024 |        1755 |        209 |      11.88% |   0.16 |   0.04 |
| Bz2FernetFile    | searchindex.js       |        1024 |        3859 |        820 |      21.26% |   0.28 |   0.10 |
| Bz2FernetFile    | library.pdf          |        1024 |       11330 |      14819 |     130.79% |   1.23 |   0.91 |
| ZstdFernetFile   | download.html        |        1024 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile   | genindex-all.html    |        1024 |        1755 |        323 |      18.41% |   0.01 |   0.00 |
| ZstdFernetFile   | searchindex.js       |        1024 |        3859 |       1178 |      30.53% |   0.03 |   0.01 |
| ZstdFernetFile   | library.pdf          |        1024 |       11330 |      14754 |     130.22% |   0.16 |   0.07 |
| TarBz2FernetFile | html,js and pdf      |          16 |       16955 |      15940 |      94.02% |   1.61 |   1.08 |
| TarBz2FernetFile | html,js and pdf      |         256 |       16955 |      15870 |      93.60% |   1.55 |   1.01 |
| TarBz2FernetFile | html,js and pdf      |        1024 |       16955 |      15867 |      93.58% |   1.55 |   1.09 |
