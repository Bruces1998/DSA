def fill(canvas, row, col, prev_color, next_color, memo):
    if (row < 0 or col < 0 or row == len(canvas) or col == len(canvas[0]) ):
        return
    if canvas[row][col]==prev_color:
        canvas[row][col] = next_color
        fill(canvas, row - 1, col, prev_color, next_color)
        fill(canvas, row, col - 1, prev_color, next_color)
        fill(canvas, row + 1, col, prev_color, next_color)
        fill(canvas, row, col + 1, prev_color, next_color)

    return

def driver_fill(canvas, row, col, color):
    if row < 0 or col < 0 or row > len(canvas) or col > len(canvas[0]) :
        return False
    memo = {}
    fill(canvas, row, col, canvas[row][col], color, memo)


screen = [[1, 1, 1, 1, 1, 1, 1, 1],  
          [1, 1, 1, 1, 1, 1, 0, 0],  
          [1, 0, 0, 1, 2, 0, 1, 1],  
          [1, 2, 2, 2, 1, 0, 1, 0],  
          [1, 1, 1, 2, 2, 0, 1, 0],  
          [1, 1, 1, 2, 2, 2, 2, 0],  
          [1, 1, 1, 1, 1, 2, 1, 1],  
          [1, 1, 1, 1, 1, 2, 2, 1]] 
  
x = 4
y = 4
newC = 3
driver_fill(screen, x, y, newC)
for i in screen:
    print(i)
