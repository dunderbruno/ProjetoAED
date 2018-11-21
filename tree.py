"""Tree."""


def inorderTreeWalk(x):
    """Plots the tree in order."""
    if x != None:
        inorderTreeWalk(left(x))
        print(key(x))
        inorderTreeWalk(righy(x))


def treeSearch(x, k):
    """Recursive search in the tree."""
    if x == None or key(x) == k:
        return key(x)
    if k < key(x):
        return treeSearch(left(x), k)
    else:
        return treeSearch(right(x), k)


def iterativeTreeSearch(x, k):
    """Iterative search in the tree."""
    while x != None and k != key(x):
        if x < key(x):
            x = left(x)
        else:
            x = right(x)
    return x


def treeMinimum(x):
    """Returns the tree minimum."""
    while left(x) != None:
        x = left(x)
    return x


def treeMaximum(x):
    """Returns the tree maximum."""
    while right(x) != None:
        x = right(x)
    return x


def treeSuccessor(x):
    """Return the successor of x."""
    if right(x) != None:
        return treeMinimum(right(x))
    y = p(x)
    while y != None and x == right(y):
        x = y
        y = p(y)
    return y