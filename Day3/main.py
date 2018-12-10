from claim import Claim
from fabric import Fabric


def representClaim(claim, fabric):
    for i in range(claim.height):
        for j in range(claim.width):
            fabric.matrix[claim.x + j][claim.y + i] += 1
    
    return fabric


def findOverlap(fabric):
    count = 0
    for i in range(len(fabric.matrix)):
        for j in range(len(fabric.matrix[i])):
            if fabric.matrix[i][j] > 1:
                count += 1

    return count


fab = Fabric(1000, 1000)
claims = []

with open('input.txt') as f:
    for line in f:
        claims.append(Claim(line))

for c in claims:
    representClaim(c, fab)

print(findOverlap(fab))
