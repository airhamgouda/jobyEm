testMap = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
           0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
           0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
           0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
           0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
           0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
           0, 1, 0, 0, 0, 0, 0, 0, 1, 0,
           0, 1, 1, 1, 0, 0, 1, 1, 1, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]


GRIDSIZE = 10
LENGTH = len(testMap)

WIDTH = int(LENGTH / GRIDSIZE)
HEIGHT = int(LENGTH / GRIDSIZE)



topLeft = (0, 0)
bottomRight = (0, 0)
for i in testMap:
  


  if i == 0:
    print('Grass')
    print(topLeft)
    print(bottomRight)
  if i == 1:
    print('Wall')
