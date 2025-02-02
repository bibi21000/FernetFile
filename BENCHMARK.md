# Benchmarks

| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile           | download.html        |          16 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |          16 |        1753 |       2348 |     133.96% |   0.11 |   0.01 |
| FernetFile           | searchindex.js       |          16 |        3855 |       5164 |     133.96% |   0.47 |   0.03 |
| FernetFile           | library.pdf          |          16 |       11330 |      15178 |     133.96% |   6.86 |   0.08 |
| Bz2FernetFile        | download.html        |          16 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |          16 |        1753 |        209 |      11.92% |   0.15 |   0.04 |
| Bz2FernetFile        | searchindex.js       |          16 |        3855 |        824 |      21.37% |   0.27 |   0.09 |
| Bz2FernetFile        | library.pdf          |          16 |       11330 |      14887 |     131.40% |   2.30 |   0.68 |
| ZstdFernetFile       | download.html        |          16 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |          16 |        1753 |        324 |      18.49% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |          16 |        3855 |       1182 |      30.67% |   0.03 |   0.01 |
| ZstdFernetFile       | library.pdf          |          16 |       11330 |      14823 |     130.83% |   0.17 |   0.08 |
| FernetFile           | download.html        |         256 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |         256 |        1753 |       2338 |     133.37% |   0.02 |   0.01 |
| FernetFile           | searchindex.js       |         256 |        3855 |       5142 |     133.37% |   0.05 |   0.02 |
| FernetFile           | library.pdf          |         256 |       11330 |      15111 |     133.37% |   0.18 |   0.07 |
| Bz2FernetFile        | download.html        |         256 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |         256 |        1753 |        208 |      11.87% |   0.15 |   0.05 |
| Bz2FernetFile        | searchindex.js       |         256 |        3855 |        820 |      21.27% |   0.27 |   0.09 |
| Bz2FernetFile        | library.pdf          |         256 |       11330 |      14822 |     130.82% |   1.21 |   0.68 |
| ZstdFernetFile       | download.html        |         256 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |         256 |        1753 |        323 |      18.41% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |         256 |        3855 |       1177 |      30.53% |   0.03 |   0.01 |
| ZstdFernetFile       | library.pdf          |         256 |       11330 |      14754 |     130.22% |   0.16 |   0.07 |
| FernetFile           | download.html        |        1024 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |        1024 |        1753 |       2337 |     133.34% |   0.02 |   0.02 |
| FernetFile           | searchindex.js       |        1024 |        3855 |       5141 |     133.34% |   0.03 |   0.04 |
| FernetFile           | library.pdf          |        1024 |       11330 |      15108 |     133.34% |   0.11 |   0.12 |
| Bz2FernetFile        | download.html        |        1024 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |        1024 |        1753 |        208 |      11.87% |   0.16 |   0.04 |
| Bz2FernetFile        | searchindex.js       |        1024 |        3855 |        820 |      21.27% |   0.26 |   0.09 |
| Bz2FernetFile        | library.pdf          |        1024 |       11330 |      14819 |     130.79% |   1.16 |   0.81 |
| ZstdFernetFile       | download.html        |        1024 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |        1024 |        1753 |        323 |      18.41% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |        1024 |        3855 |       1177 |      30.53% |   0.03 |   0.01 |
| ZstdFernetFile       | library.pdf          |        1024 |       11330 |      14754 |     130.22% |   0.14 |   0.07 |
| TarBz2FernetFile     | html,js and pdf      |          16 |       16949 |      15939 |      94.04% |   2.05 |   1.01 |
| TarBz2FernetFile     | html,js and pdf      |         256 |       16949 |      15869 |      93.63% |   1.53 |   0.99 |
| TarBz2FernetFile     | html,js and pdf      |        1024 |       16949 |      15865 |      93.61% |   1.54 |   1.07 |
| TarZstdFernetFile    | html,js and pdf      |          16 |       16949 |      16317 |      96.27% |   0.22 |   0.13 |
| TarZstdFernetFile    | html,js and pdf      |         256 |       16949 |      16249 |      95.87% |   0.20 |   0.12 |
| TarZstdFernetFile    | html,js and pdf      |        1024 |       16949 |      16249 |      95.87% |   0.20 |   0.13 |
