>>> import numpy as np
>>> D = pd.DataFrame(np.random.randn(6, 5))  # 产生6*5随机矩阵
>>> D.skew
<bound method DataFrame.skew of           0         1         2         3         4
0 -0.356658 -0.818474  1.125020 -0.208365 -1.607690
1 -0.560716 -0.583416  0.284881  2.065659  1.450251
2 -0.439740 -0.076382  1.610470 -0.293204 -0.578135
3 -0.707996 -1.516558 -0.625572 -0.921570  0.954067
4 -0.597216 -0.789598  0.079266 -0.555804  0.489331
5 -1.142762  0.273842 -0.807341 -0.556441  0.563081>
>>> D.kurt()
0    2.493467
1   -0.017757
2   -1.362232
3    4.953506
4    0.095280
dtype: float64
>>> D.skew()
0   -1.439143
1   -0.078273
2    0.331625
3    2.151766
4   -0.895982
dtype: float64
>>> D.describe()
              0         1         2         3         4
count  6.000000  6.000000  6.000000  6.000000  6.000000
mean  -0.634181 -0.585098  0.277787 -0.078287  0.211818
std    0.277738  0.626175  0.951511  1.079573  1.115319
min   -1.142762 -1.516558 -0.807341 -0.921570 -1.607690
25%   -0.680301 -0.811255 -0.449363 -0.556281 -0.311268
50%   -0.578966 -0.686507  0.182073 -0.424504  0.526206
75%   -0.469984 -0.203140  0.914985 -0.229575  0.856321
max   -0.356658  0.273842  1.610470  2.065659  1.450251
>>> D
          0         1         2         3         4
0 -0.356658 -0.818474  1.125020 -0.208365 -1.607690
1 -0.560716 -0.583416  0.284881  2.065659  1.450251
2 -0.439740 -0.076382  1.610470 -0.293204 -0.578135
3 -0.707996 -1.516558 -0.625572 -0.921570  0.954067
4 -0.597216 -0.789598  0.079266 -0.555804  0.489331
5 -1.142762  0.273842 -0.807341 -0.556441  0.563081


>>> D = pd.DataFrame(np.random.randn(6, 7))  # 产生6*7随机矩阵
>>> D
          0         1         2         3         4         5         6
0 -1.759516 -1.743953 -1.090860  0.293944  0.687187 -1.889391 -1.619245
1  0.465130 -0.026138  0.932866 -1.633194  0.640675  1.709452  2.755673
2  2.186606  0.443182 -1.649103  2.105980 -1.018612  0.305463  0.550834
3 -0.907343 -1.249021 -0.471538 -0.077566 -0.376112  0.528098 -0.008216
4  1.252573 -0.441288 -0.888943 -1.318685  0.002452  0.647620 -0.210767
5 -0.301911 -0.285576 -1.315104  0.041760 -1.307782 -0.470426 -0.957000
>>> D.skew()    # 每一列的偏度
0    0.139059
1   -0.511227
2    1.496014
3    0.675910
4   -0.164221
5   -0.749963
6    1.130479
dtype: float64
>>> D.kurt()    # 每一列的峰度
0   -0.903254
1   -0.767919
2    2.546004
3    0.720280
4   -1.825752
5    1.194014
6    1.849835
dtype: float64
