# Benchmarks

| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile           | download.html        |          16 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |          16 |        1755 |       2351 |     133.96% |   0.12 |   0.01 |
| FernetFile           | searchindex.js       |          16 |        3859 |       5170 |     133.96% |   0.48 |   0.02 |
| FernetFile           | library.pdf          |          16 |       11336 |      15185 |     133.96% |   4.16 |   0.07 |
| Bz2FernetFile        | download.html        |          16 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |          16 |        1755 |        209 |      11.93% |   0.17 |   0.05 |
| Bz2FernetFile        | searchindex.js       |          16 |        3859 |        825 |      21.37% |   0.28 |   0.10 |
| Bz2FernetFile        | library.pdf          |          16 |       11336 |      14890 |     131.35% |   2.31 |   1.62 |
| LzmaFernetFile       | download.html        |          16 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |          16 |        1755 |        219 |      12.50% |   0.39 |   0.01 |
| LzmaFernetFile       | searchindex.js       |          16 |        3859 |        797 |      20.66% |   1.39 |   0.04 |
| LzmaFernetFile       | library.pdf          |          16 |       11336 |      14759 |     130.20% |   5.51 |   1.62 |
| ZstdFernetFile       | download.html        |          16 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |          16 |        1755 |        324 |      18.49% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |          16 |        3859 |       1183 |      30.66% |   0.04 |   0.01 |
| ZstdFernetFile       | library.pdf          |          16 |       11336 |      14812 |     130.67% |   0.17 |   0.07 |
| FernetFile           | download.html        |         256 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |         256 |        1755 |       2341 |     133.37% |   0.01 |   0.01 |
| FernetFile           | searchindex.js       |         256 |        3859 |       5147 |     133.37% |   0.04 |   0.02 |
| FernetFile           | library.pdf          |         256 |       11336 |      15119 |     133.37% |   0.18 |   0.05 |
| Bz2FernetFile        | download.html        |         256 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |         256 |        1755 |        209 |      11.88% |   0.16 |   0.04 |
| Bz2FernetFile        | searchindex.js       |         256 |        3859 |        821 |      21.28% |   0.26 |   0.09 |
| Bz2FernetFile        | library.pdf          |         256 |       11336 |      14825 |     130.78% |   1.29 |   1.49 |
| LzmaFernetFile       | download.html        |         256 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |         256 |        1755 |        218 |      12.44% |   0.36 |   0.01 |
| LzmaFernetFile       | searchindex.js       |         256 |        3859 |        794 |      20.57% |   1.41 |   0.04 |
| LzmaFernetFile       | library.pdf          |         256 |       11336 |      14694 |     129.63% |   4.46 |   1.53 |
| ZstdFernetFile       | download.html        |         256 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |         256 |        1755 |        323 |      18.40% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |         256 |        3859 |       1178 |      30.51% |   0.03 |   0.01 |
| ZstdFernetFile       | library.pdf          |         256 |       11336 |      14740 |     130.03% |   0.13 |   0.06 |
| FernetFile           | download.html        |        1024 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |        1024 |        1755 |       2340 |     133.34% |   0.01 |   0.01 |
| FernetFile           | searchindex.js       |        1024 |        3859 |       5146 |     133.34% |   0.04 |   0.03 |
| FernetFile           | library.pdf          |        1024 |       11336 |      15115 |     133.34% |   0.12 |   0.08 |
| Bz2FernetFile        | download.html        |        1024 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |        1024 |        1755 |        209 |      11.88% |   0.17 |   0.04 |
| Bz2FernetFile        | searchindex.js       |        1024 |        3859 |        821 |      21.27% |   0.26 |   0.09 |
| Bz2FernetFile        | library.pdf          |        1024 |       11336 |      14821 |     130.75% |   1.21 |   1.47 |
| LzmaFernetFile       | download.html        |        1024 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |        1024 |        1755 |        218 |      12.44% |   0.36 |   0.01 |
| LzmaFernetFile       | searchindex.js       |        1024 |        3859 |        794 |      20.56% |   1.45 |   0.04 |
| LzmaFernetFile       | library.pdf          |        1024 |       11336 |      14691 |     129.60% |   4.36 |   1.50 |
| ZstdFernetFile       | download.html        |        1024 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |        1024 |        1755 |        323 |      18.40% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |        1024 |        3859 |       1177 |      30.50% |   0.02 |   0.01 |
| ZstdFernetFile       | library.pdf          |        1024 |       11336 |      14736 |     130.00% |   0.12 |   0.08 |
| TarBz2FernetFile     | html,js and pdf      |          16 |       16961 |      15942 |      94.00% |   1.56 |   2.10 |
| TarBz2FernetFile     | html,js and pdf      |         256 |       16961 |      15872 |      93.58% |   1.52 |   1.85 |
| TarBz2FernetFile     | html,js and pdf      |        1024 |       16961 |      15868 |      93.56% |   1.51 |   1.81 |
| TarZstdFernetFile    | html,js and pdf      |          16 |       16961 |      16314 |      96.19% |   0.20 |   0.12 |
| TarZstdFernetFile    | html,js and pdf      |         256 |       16961 |      16240 |      95.75% |   0.15 |   0.12 |
| TarZstdFernetFile    | html,js and pdf      |        1024 |       16961 |      16237 |      95.73% |   0.15 |   0.14 |
| TarLzmaFernetFile    | html,js and pdf      |          16 |       16961 |      15765 |      92.95% |   6.42 |   1.90 |
| TarLzmaFernetFile    | html,js and pdf      |         256 |       16961 |      15692 |      92.52% |   6.22 |   2.08 |
| TarLzmaFernetFile    | html,js and pdf      |        1024 |       16961 |      15688 |      92.50% |   6.15 |   1.78 |


# Benchmarks ZstdFernetFile

| Class                | Data                 | Lvl | Wrks |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|----:|-----:|------------:|-----------:|------------:|-------:|-------:|
| ZstdFernetFile       | genindex-all.html    |   9 |    2 |        1755 |        258 |      14.67% |   0.04 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |   9 |    8 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |   9 |   12 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |    2 |        1755 |        216 |      12.34% |   0.78 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |    8 |        1755 |        216 |      12.34% |   0.78 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |   12 |        1755 |        216 |      12.34% |   0.77 |   0.00 |
| ZstdFernetFile       | searchindex.js       |   9 |    2 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |    8 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |   12 |        3859 |        964 |      24.97% |   0.08 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |    2 |        3859 |        836 |      21.66% |   1.52 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |    8 |        3859 |        836 |      21.66% |   1.52 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |   12 |        3859 |        836 |      21.66% |   1.58 |   0.01 |
| ZstdFernetFile       | library.pdf          |   9 |    2 |       11336 |      14651 |     129.24% |   0.22 |   0.05 |
| ZstdFernetFile       | library.pdf          |   9 |    8 |       11336 |      14651 |     129.24% |   0.20 |   0.06 |
| ZstdFernetFile       | library.pdf          |   9 |   12 |       11336 |      14651 |     129.24% |   0.21 |   0.06 |
| ZstdFernetFile       | library.pdf          |  19 |    2 |       11336 |      14609 |     128.87% |   2.56 |   0.06 |
| ZstdFernetFile       | library.pdf          |  19 |    8 |       11336 |      14609 |     128.87% |   2.60 |   0.06 |
| ZstdFernetFile       | library.pdf          |  19 |   12 |       11336 |      14609 |     128.87% |   2.60 |   0.06 |
