import re
from collections import defaultdict

def input():
    """
    Reads a file containing a list of tuples of 3 numbers and returns the tuples.
    The input file is expected to be in the format: x y z x y z ...
    """
    with open(r'adventofcode\day18\data18.txt') as f:
        return zip(*[iter(map(int, re.findall(r"\d+", f.read())))]*3)

def generator(x, y, z):
    """
    Yields the six faces of a cube.
    The coordinate system used is such that (x, y, z) is the bottom-left corner of the cube.
    The faces are generated as follows:
        - (x, y, z, x+1, y+1, z)
        - (x, y, z, x+1, y, z+1)
        - (x, y, z, x, y+1, z+1)
        - (x+1, y, z, x+1, y+1, z+1)
        - (x, y+1, z, x+1, y+1, z+1)
        - (x, y, z+1, x+1, y+1, z+1)
    """
    
    yield (x, y, z, x+1, y+1, z)
    yield (x, y, z, x+1, y, z+1)
    yield (x, y, z, x, y+1, z+1)
    yield (x+1, y, z, x+1, y+1, z+1)
    yield (x, y+1, z, x+1, y+1, z+1)
    yield (x, y, z+1, x+1, y+1, z+1)

def todayfaces():
    """
    Returns a set of faces that are only used once in the input data.
    This is determined by iterating through the input cubes, generating the faces for each cube,
    and counting the number of times each face appears in the input.
    """
    faces = defaultdict(int)
    for cube in input():
        for face in generator(*cube):
            faces[face] += 1
    return set(face for face in faces if faces[face] == 1)

def fill(faces):
    """
    Finds the water volume by simulating the filling of a 3D space with water.
    The simulation starts at the bottom-left corner of the space (x=-1, y=-1, z=-1) and
    fills the space with water by expanding outward until it reaches a face in the input set.
    The input set represents the faces of the cubes that are not submerged in water.
    """
    x, y, z, width, height, depth = -1, -1, -1, 23, 23, 23

    cubes = set()
    wet = set()
    floo = [(x, y, z)]

    while floo:
        flood = floo.pop()
        if flood not in cubes:
            if flood[0] >= -1 and flood[0] <= width and flood[1] >= -1 and flood[1] <= height and flood[2] >= -1 and flood[2] <= depth:
                # and flood[0] <= width and flood[1] >= -1 and flood[1] <= height and flood[2] >= -1 and flood[2] <= depth:
                cubes.add(flood)
                d = iter([(0, 0, -1), (0, -1, 0), (-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)])
                for face in generator(*flood):
                    delta = next(d)
                    if face in faces:
                        wet.add(face)
                    else:
                        floo.append(tuple([flood[i] + delta[i] for i in range(3)]))
    return wet
# Set of faces that are only used once in the input data
faces = todayfaces()

# Print the number of faces that are only used once and the volume of the water
print("Part 1:", len(faces))
print("Part 2:", len(fill(faces)))