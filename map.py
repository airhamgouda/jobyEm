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



topLeft = [0, 0]
bottomRight = [0, 0]
for i in testMap:
  
  # Top Left XY Coordinates
  if topLeft[0] == (LENGTH - GRIDSIZE):
      topLeft[0] = 0 # Reset X coordinates to 0
      topLeft[1] = topLeft[1] + GRIDSIZE # Adjust Y Coordinates to next row
  topLeft[0] = topLeft[0] + GRIDSIZE


  # Bottom Right XY Coordinates
  bottomRight = [(topLeft[0] + GRIDSIZE), (topLeft[1] + GRIDSIZE)]

  

  if i == 0:
    print('Grass')
    print(topLeft)
    print(bottomRight)
  if i == 1:
    print('Wall')
    print(topLeft)
    print(bottomRight)
