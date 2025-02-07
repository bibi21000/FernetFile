# Benchmarks

| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile           | download.html        |          16 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |          16 |        1755 |       2351 |     133.96% |   0.20 |   0.02 |
| FernetFile           | searchindex.js       |          16 |        3859 |       5170 |     133.96% |   0.60 |   0.03 |
| FernetFile           | library.pdf          |          16 |       11336 |      15185 |     133.96% |   4.59 |   0.07 |
| Bz2FernetFile        | download.html        |          16 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |          16 |        1755 |        209 |      11.93% |   0.15 |   0.03 |
| Bz2FernetFile        | searchindex.js       |          16 |        3859 |        825 |      21.37% |   0.27 |   0.09 |
| Bz2FernetFile        | library.pdf          |          16 |       11336 |      14890 |     131.35% |   2.27 |   1.61 |
| LzmaFernetFile       | download.html        |          16 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |          16 |        1755 |        219 |      12.50% |   0.37 |   0.01 |
| LzmaFernetFile       | searchindex.js       |          16 |        3859 |        797 |      20.66% |   1.40 |   0.04 |
| LzmaFernetFile       | library.pdf          |          16 |       11336 |      14759 |     130.20% |   5.43 |   1.59 |
| FernetFile           | download.html        |          16 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |          16 |        1755 |        324 |      18.49% |   0.01 |   0.00 |
| FernetFile           | searchindex.js       |          16 |        3859 |       1183 |      30.66% |   0.03 |   0.02 |
| FernetFile           | library.pdf          |          16 |       11336 |      14812 |     130.67% |   0.18 |   0.08 |
| FernetFile           | download.html        |         256 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |         256 |        1755 |       2341 |     133.37% |   0.01 |   0.01 |
| FernetFile           | searchindex.js       |         256 |        3859 |       5147 |     133.37% |   0.04 |   0.02 |
| FernetFile           | library.pdf          |         256 |       11336 |      15119 |     133.37% |   0.17 |   0.05 |
| Bz2FernetFile        | download.html        |         256 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |         256 |        1755 |        209 |      11.88% |   0.15 |   0.04 |
| Bz2FernetFile        | searchindex.js       |         256 |        3859 |        821 |      21.28% |   0.27 |   0.09 |
| Bz2FernetFile        | library.pdf          |         256 |       11336 |      14825 |     130.78% |   1.24 |   1.46 |
| LzmaFernetFile       | download.html        |         256 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |         256 |        1755 |        218 |      12.44% |   0.36 |   0.01 |
| LzmaFernetFile       | searchindex.js       |         256 |        3859 |        794 |      20.57% |   1.37 |   0.04 |
| LzmaFernetFile       | library.pdf          |         256 |       11336 |      14694 |     129.63% |   4.30 |   1.77 |
| FernetFile           | download.html        |         256 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |         256 |        1755 |        323 |      18.40% |   0.01 |   0.00 |
| FernetFile           | searchindex.js       |         256 |        3859 |       1178 |      30.51% |   0.04 |   0.02 |
| FernetFile           | library.pdf          |         256 |       11336 |      14740 |     130.03% |   0.17 |   0.07 |
| FernetFile           | download.html        |        1024 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |        1024 |        1755 |       2340 |     133.34% |   0.01 |   0.01 |
| FernetFile           | searchindex.js       |        1024 |        3859 |       5146 |     133.34% |   0.04 |   0.03 |
| FernetFile           | library.pdf          |        1024 |       11336 |      15115 |     133.34% |   0.14 |   0.09 |
| Bz2FernetFile        | download.html        |        1024 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |        1024 |        1755 |        209 |      11.88% |   0.19 |   0.06 |
| Bz2FernetFile        | searchindex.js       |        1024 |        3859 |        821 |      21.27% |   0.31 |   0.13 |
| Bz2FernetFile        | library.pdf          |        1024 |       11336 |      14821 |     130.75% |   1.38 |   1.75 |
| LzmaFernetFile       | download.html        |        1024 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |        1024 |        1755 |        218 |      12.44% |   0.40 |   0.01 |
| LzmaFernetFile       | searchindex.js       |        1024 |        3859 |        794 |      20.56% |   1.51 |   0.04 |
| LzmaFernetFile       | library.pdf          |        1024 |       11336 |      14691 |     129.60% |   4.28 |   1.57 |
| FernetFile           | download.html        |        1024 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |        1024 |        1755 |        323 |      18.40% |   0.01 |   0.00 |
| FernetFile           | searchindex.js       |        1024 |        3859 |       1177 |      30.50% |   0.03 |   0.01 |
| FernetFile           | library.pdf          |        1024 |       11336 |      14736 |     130.00% |   0.12 |   0.07 |
| TarBz2FernetFile     | html,js and pdf      |          16 |       16961 |      15942 |      94.00% |   1.72 |   2.19 |
| TarBz2FernetFile     | html,js and pdf      |         256 |       16961 |      15872 |      93.58% |   1.56 |   1.83 |
| TarBz2FernetFile     | html,js and pdf      |        1024 |       16961 |      15868 |      93.56% |   1.54 |   1.81 |
| TarZstdFernetFile    | html,js and pdf      |          16 |       16961 |      16314 |      96.19% |   0.20 |   0.12 |
| TarZstdFernetFile    | html,js and pdf      |         256 |       16961 |      16240 |      95.75% |   0.14 |   0.11 |
| TarZstdFernetFile    | html,js and pdf      |        1024 |       16961 |      16237 |      95.73% |   0.14 |   0.13 |
| TarLzmaFernetFile    | html,js and pdf      |          16 |       16961 |      15765 |      92.95% |   6.20 |   1.86 |
| TarLzmaFernetFile    | html,js and pdf      |         256 |       16961 |      15691 |      92.52% |   7.24 |   1.93 |
| TarLzmaFernetFile    | html,js and pdf      |        1024 |       16961 |      15688 |      92.50% |   6.15 |   1.71 |


# Benchmarks ZstdFernetFile

| Class                | Data                 | Lvl | Wrks |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|----:|-----:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile           | genindex-all.html    |   9 |    2 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| FernetFile           | genindex-all.html    |   9 |    4 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| FernetFile           | genindex-all.html    |   9 |    8 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| FernetFile           | genindex-all.html    |  19 |    2 |        1755 |        216 |      12.34% |   0.78 |   0.00 |
| FernetFile           | genindex-all.html    |  19 |    4 |        1755 |        216 |      12.34% |   0.78 |   0.00 |
| FernetFile           | genindex-all.html    |  19 |    8 |        1755 |        216 |      12.34% |   0.78 |   0.00 |
| FernetFile           | searchindex.js       |   9 |    2 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| FernetFile           | searchindex.js       |   9 |    4 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| FernetFile           | searchindex.js       |   9 |    8 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| FernetFile           | searchindex.js       |  19 |    2 |        3859 |        836 |      21.66% |   1.53 |   0.01 |
| FernetFile           | searchindex.js       |  19 |    4 |        3859 |        836 |      21.66% |   1.53 |   0.01 |
| FernetFile           | searchindex.js       |  19 |    8 |        3859 |        836 |      21.66% |   1.55 |   0.01 |
| FernetFile           | library.pdf          |   9 |    2 |       11336 |      14651 |     129.24% |   0.20 |   0.06 |
| FernetFile           | library.pdf          |   9 |    4 |       11336 |      14651 |     129.24% |   0.19 |   0.06 |
| FernetFile           | library.pdf          |   9 |    8 |       11336 |      14651 |     129.24% |   0.21 |   0.05 |
| FernetFile           | library.pdf          |  19 |    2 |       11336 |      14609 |     128.87% |   2.57 |   0.06 |
| FernetFile           | library.pdf          |  19 |    4 |       11336 |      14609 |     128.87% |   2.59 |   0.06 |
| FernetFile           | library.pdf          |  19 |    8 |       11336 |      14609 |     128.87% |   2.60 |   0.06 |
