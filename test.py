from redblacktree import *

T = Tree()
for i in range(1, 16):
    T.insert(i)

print('Raiz: ', T.getRoot().getData())
print('\n')
print('Em ordem:')
T.inOrderTreeWalk(T.getRoot())
print('\n')

a = T.search(8)
print(a.getData())
print(type(a))
T.delete(a)

print('Em ordem:')
T.inOrderTreeWalk(T.getRoot())
print('\n')
