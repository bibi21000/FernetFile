# Benchmarks

| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile           | download.html        |          16 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |          16 |        1755 |       2351 |     133.96% |   0.12 |   0.01 |
| FernetFile           | searchindex.js       |          16 |        3859 |       5170 |     133.96% |   0.48 |   0.02 |
| FernetFile           | library.pdf          |          16 |       11336 |      15185 |     133.96% |   4.17 |   0.07 |
| Bz2FernetFile        | download.html        |          16 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |          16 |        1755 |        209 |      11.93% |   0.15 |   0.04 |
| Bz2FernetFile        | searchindex.js       |          16 |        3859 |        825 |      21.37% |   0.27 |   0.10 |
| Bz2FernetFile        | library.pdf          |          16 |       11336 |      14890 |     131.35% |   2.35 |   1.67 |
| LzmaFernetFile       | download.html        |          16 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |          16 |        1755 |        219 |      12.50% |   0.37 |   0.01 |
| LzmaFernetFile       | searchindex.js       |          16 |        3859 |        797 |      20.66% |   1.41 |   0.04 |
| LzmaFernetFile       | library.pdf          |          16 |       11336 |      14759 |     130.20% |   5.69 |   1.94 |
| ZstdFernetFile       | download.html        |          16 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |          16 |        1755 |        324 |      18.49% |   0.02 |   0.01 |
| ZstdFernetFile       | searchindex.js       |          16 |        3859 |       1183 |      30.66% |   0.07 |   0.02 |
| ZstdFernetFile       | library.pdf          |          16 |       11336 |      14812 |     130.67% |   0.31 |   0.14 |
| FernetFile           | download.html        |         256 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |         256 |        1755 |       2341 |     133.37% |   0.02 |   0.02 |
| FernetFile           | searchindex.js       |         256 |        3859 |       5147 |     133.37% |   0.05 |   0.03 |
| FernetFile           | library.pdf          |         256 |       11336 |      15119 |     133.37% |   0.26 |   0.06 |
| Bz2FernetFile        | download.html        |         256 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |         256 |        1755 |        209 |      11.88% |   0.21 |   0.08 |
| Bz2FernetFile        | searchindex.js       |         256 |        3859 |        821 |      21.28% |   0.30 |   0.11 |
| Bz2FernetFile        | library.pdf          |         256 |       11336 |      14825 |     130.78% |   1.38 |   2.02 |
| LzmaFernetFile       | download.html        |         256 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |         256 |        1755 |        218 |      12.44% |   0.37 |   0.01 |
| LzmaFernetFile       | searchindex.js       |         256 |        3859 |        794 |      20.57% |   1.41 |   0.04 |
| LzmaFernetFile       | library.pdf          |         256 |       11336 |      14694 |     129.63% |   4.29 |   1.56 |
| ZstdFernetFile       | download.html        |         256 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |         256 |        1755 |        323 |      18.40% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |         256 |        3859 |       1178 |      30.51% |   0.03 |   0.01 |
| ZstdFernetFile       | library.pdf          |         256 |       11336 |      14740 |     130.03% |   0.13 |   0.06 |
| FernetFile           | download.html        |        1024 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |        1024 |        1755 |       2340 |     133.34% |   0.01 |   0.01 |
| FernetFile           | searchindex.js       |        1024 |        3859 |       5146 |     133.34% |   0.03 |   0.02 |
| FernetFile           | library.pdf          |        1024 |       11336 |      15115 |     133.34% |   0.12 |   0.08 |
| Bz2FernetFile        | download.html        |        1024 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |        1024 |        1755 |        209 |      11.88% |   0.16 |   0.04 |
| Bz2FernetFile        | searchindex.js       |        1024 |        3859 |        821 |      21.27% |   0.26 |   0.10 |
| Bz2FernetFile        | library.pdf          |        1024 |       11336 |      14821 |     130.75% |   1.17 |   1.58 |
| LzmaFernetFile       | download.html        |        1024 |          11 |          4 |      35.89% |   0.00 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |        1024 |        1755 |        218 |      12.44% |   0.37 |   0.01 |
| LzmaFernetFile       | searchindex.js       |        1024 |        3859 |        794 |      20.56% |   1.40 |   0.04 |
| LzmaFernetFile       | library.pdf          |        1024 |       11336 |      14691 |     129.60% |   4.26 |   1.56 |
| ZstdFernetFile       | download.html        |        1024 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |        1024 |        1755 |        323 |      18.40% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |        1024 |        3859 |       1177 |      30.50% |   0.03 |   0.01 |
| ZstdFernetFile       | library.pdf          |        1024 |       11336 |      14736 |     130.00% |   0.12 |   0.08 |
| TarBz2FernetFile     | html,js and pdf      |          16 |       16961 |      15942 |      94.00% |   1.60 |   1.65 |
| TarBz2FernetFile     | html,js and pdf      |         256 |       16961 |      15872 |      93.58% |   1.55 |   1.95 |
| TarBz2FernetFile     | html,js and pdf      |        1024 |       16961 |      15868 |      93.56% |   1.62 |   2.03 |
| TarZstdFernetFile    | html,js and pdf      |          16 |       16961 |      16314 |      96.19% |   0.38 |   0.16 |
| TarZstdFernetFile    | html,js and pdf      |         256 |       16961 |      16240 |      95.75% |   0.26 |   0.12 |
| TarZstdFernetFile    | html,js and pdf      |        1024 |       16961 |      16237 |      95.73% |   0.21 |   0.17 |
| TarLzmaFernetFile    | html,js and pdf      |          16 |       16961 |      15764 |      92.95% |   6.95 |   1.94 |
| TarLzmaFernetFile    | html,js and pdf      |         256 |       16961 |      15691 |      92.51% |   6.13 |   1.78 |
| TarLzmaFernetFile    | html,js and pdf      |        1024 |       16961 |      15688 |      92.49% |   6.22 |   1.82 |
