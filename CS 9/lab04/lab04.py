from Stack import Stack

def solveMaze(maze, startX, startY):
    s = Stack()
    maze[startX][startY]= 1
    step = 2
    s.push((startX,startY))

    while not s.isEmpty():
        p = s.peek()
        x=p[0]
        y=p[1]
        
        if maze[x-1][y] == 'G':
            return True
        if maze[x-1][y] == ' ':
            maze[x-1][y] = step
            step+=1

            s.push((x-1,y))
            continue

        if maze[x][y-1] == 'G':
            return True
        if maze[x][y-1] == ' ':
            maze[x][y-1] = step
            step+=1

            s.push((x,y-1))
            continue

        if maze[x+1][y] == 'G':
            return True
        if maze[x+1][y] == ' ':
            maze[x+1][y] = step
            step+=1

            s.push((x+1,y))
            continue
        
        if maze[x][y+1] == 'G':
            return True
        if maze[x][y+1] == ' ':
            maze[x][y+1] = step
            step+=1

            s.push((x,y+1))
            continue

        else:
            s.pop()
            if s.isEmpty():
                return False
        
