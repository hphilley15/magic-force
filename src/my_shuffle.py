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
    N_SWAPS = 8 # 100
    for i in range( N_SWAPS ):
        el1 = random.randint( 0, len( lst ) - 1 )
        el2 = random.randint( 0, len( lst ) - 1 )
        tmp = lst[el1]
        lst[el1] = lst[el2]
        lst[el2] = tmp
    return arr     

def fisher_yates( lst ):
    """
    This algorithm starts at index 0 and then picks one number 
    to swap the number at index 0 with. We then continue to iterate
    over the list.
    Efficient algorithm since it is O(n)
    """ 
    for i in range( len( lst ) - 1, 0, -1 ):
        j = random.randint( 0, N-1 ) # Buggy version
        j = random.randint( 0, i ) # Correct version
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp

def run_test( shuffle, N = 8, N_TESTS = 1000 ):
    counts = np.zeros( (N,N) )    
    for t in range(N_TESTS):
        arr = [ i for i in range( N) ]
        shuffle( arr )
        for i,v in enumerate( arr ):
            counts[i][v] = counts[i][v] + 1
    return pd.DataFrame( counts )

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

df = run_test( my_shuffle, N = 8, N_TESTS = 1000 )

df.plot(kind='bar', stacked=True, ax=ax1 )

fig.savefig('./figures/my_shuffle_8.svg')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

df = run_test( fisher_yates, N = 8, N_TESTS = 1000 )
df.plot(kind='bar', stacked=True, ax=ax1 )

fig.savefig('./figures/my_shuffle_fisher_yates_buggy.svg')
