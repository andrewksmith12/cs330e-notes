from math import sqrt
from functools import reduce

def RMSE_for(vals1, vals2):
    val = 0
    div = len(vals1)
    if div > 0:
        for i in range(0,len(vals1)):
            tempval = vals1[i] - vals2[i]
            val += tempval**2
        val = sqrt(val/div)
        return val
    return 0

def rmse_zip_for(vals1,vals2):
    zipped = zip(vals1,vals2)
    val = 0
    count = 0
    for a in zipped:
        val+= (a[0]-a[1])**2
        count += 1
    return sqrt(val/count)



def rmse_zip(vals1, vals2):
    zipped = zip(vals1,vals2)
    val = 0
    count = 0
    try:
        while True:
            a = next(zipped)
            val += (a[0]-a[1])**2
            count += 1
    except StopIteration:
        val = sqrt(val/count)
        pass
    return val 




def rmse_zip_reduce (a, p) :
    z = zip(a, p)
    v = reduce(lambda starter, object : starter + (object[0] - object[1]) ** 2, z, 0)
    return sqrt(v / len(a))