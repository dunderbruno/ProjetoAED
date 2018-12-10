from redblacktree import *

T = Tree()
for i in range(1, 50):
    T.insert(i)

print('Raiz: ', T.getRoot().getData())
print('\n')
print('Em ordem:')
T.inOrderTreeWalk(T.getRoot())
print('\n')

# T.delete(T.getRoot())
print('Pré ordem:')
T.preOrderTreeWalk(T.getRoot())
print('\n')
