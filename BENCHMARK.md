# Benchmarks FernetStore

Tests done with autoflush, with or without open_secure.

WT -1, ... are the last store.add time in store

WTime is the total write time. RTime the time spent to read

| Data              | NbDocs | Op sec | Orig size | Crypt size | C Ratio | WTime | Rtime | WT -1 | WT -2 | WT -3 | WT -4 |
|:------------------|-------:|-------:|----------:|-----------:|--------:|------:|------:|------:|------:|------:|------:|
|genindex-all.html  |      5 | None   |      8775 |        324 |    3.70 |  0.09 |  0.03 |  0.01 |  0.01 |  0.01 |  0.01 |
|genindex-all.html  |      5 | zstd   |      8775 |       1623 |   18.50 |  0.10 |  0.04 |  0.02 |  0.02 |  0.02 |  0.01 |
|genindex-all.html  |     20 | None   |     35100 |        328 |    0.93 |  0.42 |  0.14 |  0.03 |  0.03 |  0.03 |  0.02 |
|genindex-all.html  |     20 | zstd   |     35100 |       6493 |   18.50 |  0.80 |  0.15 |  0.06 |  0.06 |  0.06 |  0.05 |
|searchindex.js     |      5 | None   |     19295 |       5903 |   30.59 |  0.61 |  0.13 |  0.15 |  0.12 |  0.09 |  0.06 |
|searchindex.js     |      5 | zstd   |     19295 |       5917 |   30.67 |  0.33 |  0.12 |  0.08 |  0.06 |  0.06 |  0.05 |
|searchindex.js     |     20 | None   |     77181 |      23616 |   30.60 |  7.07 |  0.50 |  0.58 |  0.54 |  0.53 |  0.50 |
|searchindex.js     |     20 | zstd   |     77181 |      23670 |   30.67 |  2.67 |  0.45 |  0.21 |  0.20 |  0.19 |  0.19 |
|library.pdf        |      5 | None   |     56679 |      73751 |  130.12 |  3.68 |  0.61 |  0.84 |  0.61 |  0.46 |  0.31 |
|library.pdf        |      5 | zstd   |     56679 |      74061 |  130.67 |  3.36 |  0.85 |  0.72 |  0.60 |  0.59 |  0.49 |
|library.pdf        |     20 | None   |    226714 |     295030 |  130.13 | 38.21 |  2.03 |  3.83 |  3.65 |  2.89 |  2.67 |
|library.pdf        |     20 | zstd   |    226714 |     296249 |  130.67 | 30.84 |  3.44 |  2.47 |  2.43 |  2.81 |  2.16 |


# Benchmarks ZstdFernetFile

Tests with different compression level and workers

| Class                | Data                 | Lvl | Wrks |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|----:|-----:|------------:|-----------:|------------:|-------:|-------:|
| ZstdFernetFile       | genindex-all.html    |   9 |    2 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |   9 |    8 |        1755 |        258 |      14.67% |   0.04 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |   9 |   12 |        1755 |        258 |      14.67% |   0.03 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |    2 |        1755 |        216 |      12.34% |   0.83 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |    8 |        1755 |        216 |      12.34% |   0.78 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |  19 |   12 |        1755 |        216 |      12.34% |   0.77 |   0.00 |
| ZstdFernetFile       | searchindex.js       |   9 |    2 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |    8 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |   9 |   12 |        3859 |        964 |      24.97% |   0.09 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |    2 |        3859 |        836 |      21.66% |   1.54 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |    8 |        3859 |        836 |      21.66% |   1.55 |   0.01 |
| ZstdFernetFile       | searchindex.js       |  19 |   12 |        3859 |        836 |      21.66% |   1.57 |   0.01 |
| ZstdFernetFile       | library.pdf          |   9 |    2 |       11336 |      14651 |     129.24% |   0.21 |   0.06 |
| ZstdFernetFile       | library.pdf          |   9 |    8 |       11336 |      14651 |     129.24% |   0.23 |   0.05 |
| ZstdFernetFile       | library.pdf          |   9 |   12 |       11336 |      14651 |     129.24% |   0.22 |   0.05 |
| ZstdFernetFile       | library.pdf          |  19 |    2 |       11336 |      14609 |     128.87% |   2.60 |   0.06 |
| ZstdFernetFile       | library.pdf          |  19 |    8 |       11336 |      14609 |     128.87% |   2.59 |   0.06 |
| ZstdFernetFile       | library.pdf          |  19 |   12 |       11336 |      14609 |     128.87% |   2.60 |   0.06 |


# General benchmarks

| Class                | Data                 |  Chunk size |  Orig size  | Crypt size |  Comp ratio | WTime  | Rtime  |
|:---------------------|:---------------------|------------:|------------:|-----------:|------------:|-------:|-------:|
| FernetFile           | download.html        |          16 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |          16 |        1755 |       2351 |     133.96% |   0.06 |   0.01 |
| FernetFile           | searchindex.js       |          16 |        3859 |       5170 |     133.96% |   0.24 |   0.02 |
| FernetFile           | library.pdf          |          16 |       11336 |      15185 |     133.96% |   1.63 |   0.08 |
| Bz2FernetFile        | download.html        |          16 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |          16 |        1755 |        209 |      11.93% |   0.16 |   0.04 |
| Bz2FernetFile        | searchindex.js       |          16 |        3859 |        825 |      21.37% |   0.27 |   0.09 |
| Bz2FernetFile        | library.pdf          |          16 |       11336 |      14890 |     131.35% |   2.42 |   2.83 |
| LzmaFernetFile       | download.html        |          16 |          11 |          4 |      35.89% |   0.02 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |          16 |        1755 |        219 |      12.50% |   0.42 |   0.01 |
| LzmaFernetFile       | searchindex.js       |          16 |        3859 |        797 |      20.66% |   1.43 |   0.04 |
| LzmaFernetFile       | library.pdf          |          16 |       11336 |      14759 |     130.20% |   6.27 |   1.73 |
| ZstdFernetFile       | download.html        |          16 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |          16 |        1755 |        324 |      18.49% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |          16 |        3859 |       1183 |      30.66% |   0.04 |   0.01 |
| ZstdFernetFile       | library.pdf          |          16 |       11336 |      14812 |     130.67% |   0.19 |   0.08 |
| FernetFile           | download.html        |         256 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |         256 |        1755 |       2341 |     133.37% |   0.01 |   0.01 |
| FernetFile           | searchindex.js       |         256 |        3859 |       5147 |     133.37% |   0.04 |   0.02 |
| FernetFile           | library.pdf          |         256 |       11336 |      15119 |     133.37% |   0.19 |   0.05 |
| Bz2FernetFile        | download.html        |         256 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |         256 |        1755 |        209 |      11.88% |   0.16 |   0.04 |
| Bz2FernetFile        | searchindex.js       |         256 |        3859 |        821 |      21.28% |   0.26 |   0.10 |
| Bz2FernetFile        | library.pdf          |         256 |       11336 |      14825 |     130.78% |   1.24 |   1.59 |
| LzmaFernetFile       | download.html        |         256 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |         256 |        1755 |        218 |      12.44% |   0.37 |   0.01 |
| LzmaFernetFile       | searchindex.js       |         256 |        3859 |        794 |      20.57% |   1.40 |   0.04 |
| LzmaFernetFile       | library.pdf          |         256 |       11336 |      14694 |     129.63% |   4.37 |   1.86 |
| ZstdFernetFile       | download.html        |         256 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |         256 |        1755 |        323 |      18.40% |   0.01 |   0.00 |
| ZstdFernetFile       | searchindex.js       |         256 |        3859 |       1178 |      30.51% |   0.03 |   0.01 |
| ZstdFernetFile       | library.pdf          |         256 |       11336 |      14740 |     130.03% |   0.12 |   0.06 |
| FernetFile           | download.html        |        1024 |          11 |         15 |     134.09% |   0.00 |   0.00 |
| FernetFile           | genindex-all.html    |        1024 |        1755 |       2340 |     133.34% |   0.01 |   0.01 |
| FernetFile           | searchindex.js       |        1024 |        3859 |       5146 |     133.34% |   0.03 |   0.03 |
| FernetFile           | library.pdf          |        1024 |       11336 |      15115 |     133.34% |   0.13 |   0.07 |
| Bz2FernetFile        | download.html        |        1024 |          11 |          4 |      39.12% |   0.00 |   0.00 |
| Bz2FernetFile        | genindex-all.html    |        1024 |        1755 |        209 |      11.88% |   0.15 |   0.03 |
| Bz2FernetFile        | searchindex.js       |        1024 |        3859 |        821 |      21.27% |   0.26 |   0.10 |
| Bz2FernetFile        | library.pdf          |        1024 |       11336 |      14821 |     130.75% |   1.18 |   1.65 |
| LzmaFernetFile       | download.html        |        1024 |          11 |          4 |      35.89% |   0.01 |   0.00 |
| LzmaFernetFile       | genindex-all.html    |        1024 |        1755 |        218 |      12.44% |   0.36 |   0.01 |
| LzmaFernetFile       | searchindex.js       |        1024 |        3859 |        794 |      20.56% |   1.38 |   0.04 |
| LzmaFernetFile       | library.pdf          |        1024 |       11336 |      14691 |     129.60% |   5.03 |   1.78 |
| ZstdFernetFile       | download.html        |        1024 |          11 |          4 |      38.55% |   0.00 |   0.00 |
| ZstdFernetFile       | genindex-all.html    |        1024 |        1755 |        323 |      18.40% |   0.01 |   0.01 |
| ZstdFernetFile       | searchindex.js       |        1024 |        3859 |       1177 |      30.50% |   0.03 |   0.02 |
| ZstdFernetFile       | library.pdf          |        1024 |       11336 |      14736 |     130.00% |   0.12 |   0.08 |
| TarBz2FernetFile     | html,js and pdf      |          16 |       16961 |      15942 |      94.00% |   1.61 |   1.72 |
| TarBz2FernetFile     | html,js and pdf      |         256 |       16961 |      15872 |      93.58% |   1.62 |   2.10 |
| TarBz2FernetFile     | html,js and pdf      |        1024 |       16961 |      15868 |      93.56% |   1.54 |   2.14 |
| TarZstdFernetFile    | html,js and pdf      |          16 |       16961 |      16314 |      96.19% |   0.22 |   0.15 |
| TarZstdFernetFile    | html,js and pdf      |         256 |       16961 |      16240 |      95.75% |   0.17 |   0.11 |
| TarZstdFernetFile    | html,js and pdf      |        1024 |       16961 |      16237 |      95.73% |   0.16 |   0.14 |
| TarLzmaFernetFile    | html,js and pdf      |          16 |       16961 |      15765 |      92.95% |   6.22 |   2.19 |
| TarLzmaFernetFile    | html,js and pdf      |         256 |       16961 |      15692 |      92.52% |   6.23 |   2.13 |
| TarLzmaFernetFile    | html,js and pdf      |        1024 |       16961 |      15688 |      92.50% |   7.95 |   2.38 |
