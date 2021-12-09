def moveTop(tower1, tower2):
    disk = tower1.pop()
    tower2.append(disk)

def moveDisk(n, source, destination, extra):
    if n<=0:
        return

    moveDisk(n-1, source, extra, destination)
    moveTop(source, destination)
    moveDisk(n-1, extra, destination, source)


source = [6, 5, 4, 3, 2, 1]
dest = []
buff = []
moveDisk(6,source ,dest, buff)
print(source, dest, buff)