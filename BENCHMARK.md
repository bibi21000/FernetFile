# Benchmarks FernetStore

Tests done with autoflush, with or without open_secure.

WT -1, ... are the last store.add time in store

WTime is the total write time. RTime the time spent to read

| Data              | NbDocs | Op sec | Orig size | Crypt size | C Ratio | WTime | Rtime | WT -1 | WT -2 | WT -3 | WT -4 |
|:------------------|-------:|-------:|----------:|-----------:|--------:|------:|------:|------:|------:|------:|------:|
|genindex-all.html  |      5 | None   |      8775 |        324 |    3.70 |  0.09 |  0.03 |  0.02 |  0.01 |  0.01 |  0.01 |
|genindex-all.html  |      5 | zstd   |      8775 |       1623 |   18.50 |  0.10 |  0.04 |  0.02 |  0.02 |  0.02 |  0.02 |
|genindex-all.html  |      5 | frnt   |      8775 |      11762 |  134.04 |  0.53 |  0.13 |  0.12 |  0.10 |  0.09 |  0.07 |
|genindex-all.html  |     20 | None   |     35100 |        328 |    0.93 |  0.51 |  0.13 |  0.03 |  0.04 |  0.05 |  0.03 |
|genindex-all.html  |     20 | zstd   |     35100 |       6493 |   18.50 |  0.83 |  0.17 |  0.07 |  0.07 |  0.06 |  0.06 |
|genindex-all.html  |     20 | frnt   |     35100 |      47047 |  134.04 |  5.11 |  0.54 |  0.55 |  0.42 |  0.39 |  0.34 |
|searchindex.js     |      5 | None   |     19295 |       5903 |   30.59 |  0.78 |  0.12 |  0.18 |  0.16 |  0.12 |  0.08 |
|searchindex.js     |      5 | zstd   |     19295 |       5917 |   30.67 |  0.34 |  0.15 |  0.08 |  0.07 |  0.06 |  0.05 |
|searchindex.js     |      5 | frnt   |     19295 |      25857 |  134.01 |  1.39 |  0.27 |  0.30 |  0.26 |  0.23 |  0.18 |
|searchindex.js     |     20 | None   |     77181 |      23615 |   30.60 |  7.56 |  0.51 |  0.63 |  0.57 |  0.55 |  0.51 |
|searchindex.js     |     20 | zstd   |     77181 |      23670 |   30.67 |  2.84 |  0.47 |  0.24 |  0.21 |  0.20 |  0.19 |
|searchindex.js     |     20 | frnt   |     77181 |     103430 |  134.01 | 12.02 |  1.11 |  0.96 |  0.93 |  0.84 |  0.89 |
|library.pdf        |      5 | None   |     56679 |      73751 |  130.12 |  3.96 |  0.64 |  1.04 |  0.84 |  0.56 |  0.41 |
|library.pdf        |      5 | zstd   |     56679 |      74061 |  130.67 |  3.78 |  0.92 |  0.80 |  0.68 |  0.56 |  0.45 |
|library.pdf        |      5 | frnt   |     56679 |      75948 |  134.00 |  6.19 |  0.96 |  1.29 |  1.13 |  0.98 |  0.78 |
|library.pdf        |     20 | None   |    226714 |     295030 |  130.13 | 42.93 |  2.01 |  3.88 |  3.51 |  3.15 |  3.91 |
|library.pdf        |     20 | zstd   |    226714 |     296249 |  130.67 | 38.25 |  3.60 |  2.73 |  2.84 |  2.95 |  2.79 |
|library.pdf        |     20 | frnt   |    226714 |     303792 |  134.00 | 43.47 |  3.48 |  3.38 |  3.09 |  3.37 |  2.82 |


# Benchmarks ZstdFernetFile

Tests with different compression level and workers

| Class                | Data                 | Lvl | Wrks |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|----:|-----:|------------:|-----------:|------------:|-------:|-------:|
| ZstdFernetFile       | genindex-all.html    |   9 |    2 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |   9 |    8 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |   9 |   12 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |    2 |        1755 |        216 |      12.34% |   0.84 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |    8 |        1755 |        216 |      12.34% |   0.80 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |   12 |        1755 |        216 |      12.34% |   0.81 |   0.00 |
| ZstdFernetFile       | searchindex.js       |   9 |    2 |        3859 |        964 |      24.97% |   0.10 |   0.02 |
| ZstdFernetFile       | searchindex.js       |   9 |    8 |        3859 |        964 |      24.97% |   0.11 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |   12 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |    2 |        3859 |        836 |      21.66% |   1.71 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |    8 |        3859 |        836 |      21.66% |   1.70 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |   12 |        3859 |        836 |      21.66% |   1.62 |   0.01 |
| ZstdFernetFile       | library.pdf          |   9 |    2 |       11336 |      14651 |     129.24% |   0.26 |   0.06 |
| ZstdFernetFile       | library.pdf          |   9 |    8 |       11336 |      14651 |     129.24% |   0.23 |   0.05 |
| ZstdFernetFile       | library.pdf          |   9 |   12 |       11336 |      14651 |     129.24% |   0.22 |   0.06 |
| ZstdFernetFile       | library.pdf          |  19 |    2 |       11336 |      14609 |     128.87% |   2.84 |   0.06 |
| ZstdFernetFile       | library.pdf          |  19 |    8 |       11336 |      14609 |     128.87% |   2.87 |   0.09 |
| ZstdFernetFile       | library.pdf          |  19 |   12 |       11336 |      14609 |     128.87% |   2.87 |   0.11 |


# General benchmarks

| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile           | download.html        |          16 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |          16 |        1755 |       2351 |     133.96% |   0.13 |   0.01 |
| FernetFile           | searchindex.js       |          16 |        3859 |       5170 |     133.96% |   0.42 |   0.02 |
| FernetFile           | library.pdf          |          16 |       11336 |      15185 |     133.96% |   2.17 |   0.07 |
| Bz2FernetFile        | download.html        |          16 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |          16 |        1755 |        209 |      11.93% |   0.20 |   0.13 |
| Bz2FernetFile        | searchindex.js       |          16 |        3859 |        825 |      21.37% |   0.29 |   0.10 |
| Bz2FernetFile        | library.pdf          |          16 |       11336 |      14890 |     131.35% |   2.54 |   1.89 |
| LzmaFernetFile       | download.html        |          16 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |          16 |        1755 |        219 |      12.50% |   0.37 |   0.01 |
| LzmaFernetFile       | searchindex.js       |          16 |        3859 |        797 |      20.66% |   1.50 |   0.04 |
| LzmaFernetFile       | library.pdf          |          16 |       11336 |      14759 |     130.20% |   6.49 |   1.98 |
| ZstdFernetFile       | download.html        |          16 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |          16 |        1755 |        324 |      18.49% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |          16 |        3859 |       1183 |      30.66% |   0.04 |   0.01 |
| ZstdFernetFile       | library.pdf          |          16 |       11336 |      14812 |     130.67% |   0.18 |   0.08 |
| FernetFile           | download.html        |         256 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |         256 |        1755 |       2341 |     133.37% |   0.01 |   0.01 |
| FernetFile           | searchindex.js       |         256 |        3859 |       5147 |     133.37% |   0.04 |   0.02 |
| FernetFile           | library.pdf          |         256 |       11336 |      15119 |     133.37% |   0.21 |   0.06 |
| Bz2FernetFile        | download.html        |         256 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |         256 |        1755 |        209 |      11.88% |   0.16 |   0.04 |
| Bz2FernetFile        | searchindex.js       |         256 |        3859 |        821 |      21.28% |   0.28 |   0.12 |
| Bz2FernetFile        | library.pdf          |         256 |       11336 |      14825 |     130.78% |   1.33 |   1.99 |
| LzmaFernetFile       | download.html        |         256 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |         256 |        1755 |        218 |      12.44% |   0.39 |   0.01 |
| LzmaFernetFile       | searchindex.js       |         256 |        3859 |        794 |      20.57% |   1.45 |   0.05 |
| LzmaFernetFile       | library.pdf          |         256 |       11336 |      14694 |     129.63% |   4.76 |   2.43 |
| ZstdFernetFile       | download.html        |         256 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |         256 |        1755 |        323 |      18.40% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |         256 |        3859 |       1178 |      30.51% |   0.04 |   0.01 |
| ZstdFernetFile       | library.pdf          |         256 |       11336 |      14740 |     130.03% |   0.16 |   0.07 |
| FernetFile           | download.html        |        1024 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |        1024 |        1755 |       2340 |     133.34% |   0.01 |   0.01 |
| FernetFile           | searchindex.js       |        1024 |        3859 |       5146 |     133.34% |   0.04 |   0.02 |
| FernetFile           | library.pdf          |        1024 |       11336 |      15115 |     133.34% |   0.14 |   0.08 |
| Bz2FernetFile        | download.html        |        1024 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |        1024 |        1755 |        209 |      11.88% |   0.22 |   0.10 |
| Bz2FernetFile        | searchindex.js       |        1024 |        3859 |        821 |      21.27% |   0.28 |   0.09 |
| Bz2FernetFile        | library.pdf          |        1024 |       11336 |      14821 |     130.75% |   1.18 |   2.05 |
| LzmaFernetFile       | download.html        |        1024 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |        1024 |        1755 |        218 |      12.44% |   0.38 |   0.01 |
| LzmaFernetFile       | searchindex.js       |        1024 |        3859 |        794 |      20.56% |   1.50 |   0.04 |
| LzmaFernetFile       | library.pdf          |        1024 |       11336 |      14691 |     129.60% |   4.53 |   1.85 |
| ZstdFernetFile       | download.html        |        1024 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |        1024 |        1755 |        323 |      18.40% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |        1024 |        3859 |       1177 |      30.50% |   0.03 |   0.02 |
| ZstdFernetFile       | library.pdf          |        1024 |       11336 |      14736 |     130.00% |   0.13 |   0.09 |
| TarBz2FernetFile     | html,js and pdf      |          16 |       16961 |      15942 |      94.00% |   1.67 |   1.95 |
| TarBz2FernetFile     | html,js and pdf      |         256 |       16961 |      15872 |      93.58% |   1.66 |   2.50 |
| TarBz2FernetFile     | html,js and pdf      |        1024 |       16961 |      15868 |      93.56% |   1.78 |   2.49 |
| TarZstdFernetFile    | html,js and pdf      |          16 |       16961 |      16314 |      96.19% |   0.25 |   0.12 |
| TarZstdFernetFile    | html,js and pdf      |         256 |       16961 |      16240 |      95.75% |   0.20 |   0.12 |
| TarZstdFernetFile    | html,js and pdf      |        1024 |       16961 |      16237 |      95.73% |   0.17 |   0.14 |
| TarLzmaFernetFile    | html,js and pdf      |          16 |       16961 |      15765 |      92.95% |   7.46 |   2.36 |
| TarLzmaFernetFile    | html,js and pdf      |         256 |       16961 |      15692 |      92.52% |   6.66 |   2.16 |
| TarLzmaFernetFile    | html,js and pdf      |        1024 |       16961 |      15688 |      92.50% |   6.76 |   2.09 |
