import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random
import pandas as pd


cards = [i for i in range(6) ]

def die_shuffle( cards ):
    tmp_cards = cards.copy()
    out = [-1 for e in tmp_cards ]
    for i in range( len(cards) ):
        dice = random.randint(0,5)
        ind = dice % len(tmp_cards)
        out[i] = tmp_cards[ind]
        del tmp_cards[ind]

        # count = 0
        # ind = 0
        # while( count < dice ):
        #     if tmp_cards[ind] != -1:
        #         count = count + 1
        #     ind = ( ind + 1 ) % len( cards )
        #out[i] = tmp_cards[ind]
        #tmp_cards[ind] = -1
    return out

out = die_shuffle( cards )

def run_test( shuffle, N = 6, N_TESTS = 1000 ):
    counts = np.zeros( (N,N) )    
    for t in range(N_TESTS):
        arr = [ i for i in range( N) ]
        out = shuffle( arr )
        for i,v in enumerate( out ):
            counts[i][v] = counts[i][v] + 1
    return pd.DataFrame( counts )

def run_conditional_test( shuffle, N = 6, N_TESTS = 10000 ):
    conditional_counts = np.zeros( ( N,N,N ) )
    for t in range(N_TESTS):
        arr = [ i for i in range( N) ]
        out = shuffle( arr )
        cond_ind = out[0]

        for i,v in enumerate( out ):
            conditional_counts[cond_ind,i,v] = conditional_counts[cond_ind, i, v ] + 1
    return [ pd.DataFrame( conditional_counts[i] ) for i in range(len(conditional_counts ) ) ]



# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)

# df = run_test( die_shuffle, N = 6, N_TESTS = 1000 )

# df.plot(kind='bar', stacked=True, ax=ax1 )

# fig.savefig('./figures/die_shuffle.svg')

dframes = run_conditional_test( die_shuffle, N = 6, N_TESTS = 10000 )

for i in range(6):

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    dframes[i].plot(kind='bar', stacked=True, ax=ax1 )

    fig.savefig(f'./figures/conditional_{i:03d}_die_shuffle.svg')
