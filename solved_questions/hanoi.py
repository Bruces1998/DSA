def movetop(tower1, tower2):
    disk = tower1.pop()
    tower2.append(disk)

def moveDisk(n, origin, dest, buffer):
    if n <= 0:
        return
    moveDisk(n - 1, origin, buffer, dest)
    movetop(origin, dest)
    moveDisk(n - 1, buffer, dest, origin)


source = [6, 5, 4, 3, 2, 1]
dest = []
buff = []
a = moveDisk(6,source ,dest, buff)
print(source, dest, buff)
