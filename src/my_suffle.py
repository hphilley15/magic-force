import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random
import pandas as pd

N = 8

arr = [ i for i in range(N) ]
print( 'Before shuffle', arr )

def my_shuffle( lst ):
    "Shuffle the element in an array (passed by reference)"
    N_SWAPS = 10 # 100
    for i in range( N_SWAPS ):
        el1 = random.randint( 0, len( lst ) - 1 )
        el2 = random.randint( 0, len( lst ) - 1 )
        tmp = lst[el1]
        lst[el1] = lst[el2]
        lst[el2] = tmp
    return arr     

def fisher_yates( arr ):
    """
    This algorithm starts at index 0 and then picks one number 
    to swap the number at index 0 with. We then continue to iterate
    over the list
    """ 
    for i in range( )
counts = np.zeros( (N,N) )

N_TESTS = 1000
for t in range(N_TESTS):
    arr = [ i for i in range( N) ]
    my_shuffle( arr )
    for i,v in enumerate( arr ):
        counts[i][v] = counts[i][v] + 1

print( counts )

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

df = pd.DataFrame( counts )
df.plot(kind='bar', stacked=True, ax=ax1 )

fig.savefig('./figures/my_shuffle_1.svg')
