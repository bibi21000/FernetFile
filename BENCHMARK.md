# General benchmarks

| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile           | download.html        |          16 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |          16 |        1755 |       2351 |     133.96% |   0.17 |   0.01 |
| FernetFile           | searchindex.js       |          16 |        3859 |       5170 |     133.96% |   0.78 |   0.03 |
| FernetFile           | library.pdf          |          16 |       11336 |      15185 |     133.96% |   7.47 |   0.11 |
| Bz2FernetFile        | download.html        |          16 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |          16 |        1755 |        209 |      11.93% |   0.23 |   0.12 |
| Bz2FernetFile        | searchindex.js       |          16 |        3859 |        825 |      21.37% |   0.37 |   0.11 |
| Bz2FernetFile        | library.pdf          |          16 |       11336 |      14890 |     131.35% |   2.76 |   1.90 |
| LzmaFernetFile       | download.html        |          16 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |          16 |        1755 |        219 |      12.50% |   0.40 |   0.01 |
| LzmaFernetFile       | searchindex.js       |          16 |        3859 |        797 |      20.66% |   1.56 |   0.05 |
| LzmaFernetFile       | library.pdf          |          16 |       11336 |      14759 |     130.20% |   6.97 |   2.15 |
| ZstdFernetFile       | download.html        |          16 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |          16 |        1755 |        324 |      18.49% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |          16 |        3859 |       1183 |      30.66% |   0.04 |   0.02 |
| ZstdFernetFile       | library.pdf          |          16 |       11336 |      14812 |     130.67% |   0.21 |   0.08 |
| FernetFile           | download.html        |         256 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |         256 |        1755 |       2341 |     133.37% |   0.02 |   0.01 |
| FernetFile           | searchindex.js       |         256 |        3859 |       5147 |     133.37% |   0.05 |   0.02 |
| FernetFile           | library.pdf          |         256 |       11336 |      15119 |     133.37% |   0.21 |   0.06 |
| Bz2FernetFile        | download.html        |         256 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |         256 |        1755 |        209 |      11.88% |   0.16 |   0.04 |
| Bz2FernetFile        | searchindex.js       |         256 |        3859 |        821 |      21.28% |   0.28 |   0.13 |
| Bz2FernetFile        | library.pdf          |         256 |       11336 |      14825 |     130.78% |   1.41 |   2.23 |
| LzmaFernetFile       | download.html        |         256 |          11 |          4 |      35.89% |   0.00 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |         256 |        1755 |        218 |      12.44% |   0.37 |   0.02 |
| LzmaFernetFile       | searchindex.js       |         256 |        3859 |        794 |      20.57% |   1.65 |   0.06 |
| LzmaFernetFile       | library.pdf          |         256 |       11336 |      14694 |     129.63% |   4.51 |   1.72 |
| ZstdFernetFile       | download.html        |         256 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |         256 |        1755 |        323 |      18.40% |   0.01 |   0.01 |
| ZstdFernetFile       | searchindex.js       |         256 |        3859 |       1178 |      30.51% |   0.06 |   0.02 |
| ZstdFernetFile       | library.pdf          |         256 |       11336 |      14740 |     130.03% |   0.33 |   0.11 |
| FernetFile           | download.html        |        1024 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |        1024 |        1755 |       2340 |     133.34% |   0.02 |   0.02 |
| FernetFile           | searchindex.js       |        1024 |        3859 |       5146 |     133.34% |   0.06 |   0.04 |
| FernetFile           | library.pdf          |        1024 |       11336 |      15115 |     133.34% |   0.19 |   0.10 |
| Bz2FernetFile        | download.html        |        1024 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |        1024 |        1755 |        209 |      11.88% |   0.18 |   0.05 |
| Bz2FernetFile        | searchindex.js       |        1024 |        3859 |        821 |      21.27% |   0.32 |   0.14 |
| Bz2FernetFile        | library.pdf          |        1024 |       11336 |      14821 |     130.75% |   1.39 |   1.76 |
| LzmaFernetFile       | download.html        |        1024 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |        1024 |        1755 |        218 |      12.44% |   0.36 |   0.01 |
| LzmaFernetFile       | searchindex.js       |        1024 |        3859 |        794 |      20.56% |   1.40 |   0.04 |
| LzmaFernetFile       | library.pdf          |        1024 |       11336 |      14691 |     129.60% |   4.39 |   1.83 |
| ZstdFernetFile       | download.html        |        1024 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |        1024 |        1755 |        323 |      18.40% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |        1024 |        3859 |       1177 |      30.50% |   0.03 |   0.01 |
| ZstdFernetFile       | library.pdf          |        1024 |       11336 |      14736 |     130.00% |   0.14 |   0.09 |
| TarBz2FernetFile     | html,js and pdf      |          16 |       16961 |      15942 |      94.00% |   1.59 |   1.74 |
| TarBz2FernetFile     | html,js and pdf      |         256 |       16961 |      15872 |      93.58% |   1.55 |   2.21 |
| TarBz2FernetFile     | html,js and pdf      |        1024 |       16961 |      15868 |      93.56% |   1.83 |   2.30 |
| TarZstdFernetFile    | html,js and pdf      |          16 |       16961 |      16314 |      96.19% |   0.22 |   0.12 |
| TarZstdFernetFile    | html,js and pdf      |         256 |       16961 |      16240 |      95.75% |   0.19 |   0.13 |
| TarZstdFernetFile    | html,js and pdf      |        1024 |       16961 |      16237 |      95.73% |   0.16 |   0.14 |
| TarLzmaFernetFile    | html,js and pdf      |          16 |       16961 |      15765 |      92.95% |   6.28 |   2.18 |
| TarLzmaFernetFile    | html,js and pdf      |         256 |       16961 |      15692 |      92.52% |   7.09 |   1.97 |
| TarLzmaFernetFile    | html,js and pdf      |        1024 |       16961 |      15688 |      92.50% |   6.35 |   2.04 |


# Benchmarks ZstdFernetFile

Tests with different compression level and workers

| Class                | Data                 | Lvl | Wrks |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|----:|-----:|------------:|-----------:|------------:|-------:|-------:|
| ZstdFernetFile       | genindex-all.html    |   9 |    2 |        1755 |        258 |      14.67% |   0.04 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |   9 |    8 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |   9 |   12 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |    2 |        1755 |        216 |      12.34% |   0.80 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |    8 |        1755 |        216 |      12.34% |   0.93 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |   12 |        1755 |        216 |      12.34% |   0.79 |   0.00 |
| ZstdFernetFile       | searchindex.js       |   9 |    2 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |    8 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |   12 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |    2 |        3859 |        836 |      21.66% |   1.58 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |    8 |        3859 |        836 |      21.66% |   1.54 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |   12 |        3859 |        836 |      21.66% |   1.56 |   0.01 |
| ZstdFernetFile       | library.pdf          |   9 |    2 |       11336 |      14651 |     129.24% |   0.24 |   0.06 |
| ZstdFernetFile       | library.pdf          |   9 |    8 |       11336 |      14651 |     129.24% |   0.23 |   0.06 |
| ZstdFernetFile       | library.pdf          |   9 |   12 |       11336 |      14651 |     129.24% |   0.22 |   0.06 |
| ZstdFernetFile       | library.pdf          |  19 |    2 |       11336 |      14609 |     128.87% |   2.90 |   0.08 |
| ZstdFernetFile       | library.pdf          |  19 |    8 |       11336 |      14609 |     128.87% |   2.63 |   0.06 |
| ZstdFernetFile       | library.pdf          |  19 |   12 |       11336 |      14609 |     128.87% |   3.75 |   0.07 |


# Benchmarks FernetStore with random data

Tests done with autoflush, with or without open_secure.
WT -1, ... are the last add time of files in store
WTime is the total write time. RTime the time spend to read

| Data              | NbDocs | Op sec | Orig size | Crypt size | C Ratio | WTime | Rtime | WT -1 | WT -2 | WT -3 | WT -4 |
|:------------------|-------:|-------:|----------:|-----------:|--------:|------:|------:|------:|------:|------:|------:|
|genindex-all.html  |      5 | None   |      8775 |        324 |       4 |  0.11 |  0.05 |  0.02 |  0.02 |  0.02 |  0.02 |
|genindex-all.html  |      5 | zstd   |      8775 |       1623 |      18 |  0.14 |  0.07 |  0.03 |  0.03 |  0.03 |  0.02 |
|genindex-all.html  |     20 | None   |     35100 |        328 |       1 |  0.46 |  0.13 |  0.03 |  0.03 |  0.03 |  0.03 |
|genindex-all.html  |     20 | zstd   |     35100 |       6493 |      18 |  0.78 |  0.15 |  0.06 |  0.06 |  0.06 |  0.05 |
|searchindex.js     |      5 | None   |     19295 |       5903 |      31 |  0.61 |  0.12 |  0.14 |  0.12 |  0.09 |  0.08 |
|searchindex.js     |      5 | zstd   |     19295 |       5918 |      31 |  0.35 |  0.11 |  0.08 |  0.07 |  0.05 |  0.06 |
|searchindex.js     |     20 | None   |     77181 |      23617 |      31 |  7.11 |  0.49 |  0.57 |  0.58 |  0.55 |  0.53 |
|searchindex.js     |     20 | zstd   |     77181 |      23670 |      31 |  2.76 |  0.56 |  0.21 |  0.21 |  0.19 |  0.19 |
|library.pdf        |      5 | None   |     56679 |      73751 |     130 |  3.32 |  0.50 |  0.81 |  0.65 |  0.49 |  0.32 |
|library.pdf        |      5 | zstd   |     56679 |      74061 |     131 |  3.22 |  0.92 |  0.76 |  0.59 |  0.47 |  0.38 |
|library.pdf        |     20 | None   |    226714 |     295030 |     130 | 40.42 |  2.06 |  3.36 |  3.15 |  3.40 |  2.94 |
|library.pdf        |     20 | zstd   |    226714 |     296249 |     131 | 31.15 |  3.35 |  2.50 |  2.38 |  2.23 |  2.10 |
