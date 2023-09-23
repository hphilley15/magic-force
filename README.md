# magic-force
Some experiments in forcing a card selection on a user.

# Shuffle element in an Array

Implement a function my_shuffle that moves the elements in an array into a random order.

``` python
arr = [1,2,3,4]
my_shuffle( arr ) -> [2,4,3,1], [2,3,1,4], ...

def my_shuffle( arr ):
    ...
```

Do not use itertools or similar libraries, but try and implement the suffle by yourself.

# What would define a good shuffle algorithm?

We could implement a version of the various ways that humans shuffle cards, but that does not seem like a useful inspiration.

Instead, we should try and determine what makes a good shuffle algorithm.

To determine if something is a good shuffle, we have to take
the statistics into consideration.
A single test is not enough to be able to give an answer.

We would expect that the probability of an element to end up
in position 1, .. , N being 1/N each.





