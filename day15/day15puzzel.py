# This code calculates the area of a rectangular exclusion zone around
# a set of beacons. The exclusion zone is defined by the Manhattan
# distances between each beacon and the set of coordinates (0, Y),
# where Y is a specified value. The code also calculates the length
# of the exclusion zone along the x-axis.

# Calculate the intersection point of two lines defined by two pairs
# of coordinates (ax1, ay1) and (ax2, ay2) for the first line, and
# (bx1, by1) and (bx2, by2) for the second line. Return the
# coordinates of the intersection point.


def Exclusion_Zone(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    # Calculate the determinant of the coefficients of the two lines.
    manhattam_distance = (by2 - by1) * (ax2 - ax1) - (bx2 - bx1) * (ay2 - ay1)
    # Calculate the values of the parameters ua and ub that
    # determine the intersection point of the two lines.
    if 0 <= (ua := ((bx2 - bx1) * (ay1 - by1) - (by2 - by1) * (ax1 - bx1)) / manhattam_distance) <= 1 \
    and 0 <= (((ax2 - ax1) * (ay1 - by1) - (ay2 - ay1) * (ax1 - bx1)) / manhattam_distance) <= 1:
    # Return the coordinates of the intersection point.
        return int(ax1 + ua * (ax2 - ax1)), int(ay1 + ua * (ay2 - ay1))
    return 0


# Calculate the coordinates of the exclusion zone and the length
# of the exclusion zone along the x-axis.
def jolly(set_y=2000000):
    # Initialize an empty set to store the x-coordinates of the
    # exclusion zone.
    x_ranges = set()
     # Initialize empty lists to store the manhattan distances
    # between each beacon and the set of coordinates (0, Y),
    # the coordinates of the bottom and left sides of the
    # exclusion zone for each beacon, and the coordinates of
    # the top and right sides of the exclusion zone for each
    # beacon.
    bells, 	elf, eve, snow, tinsel = [], [], [], [], []
    # Iterate over the data, which contains the coordinates
    # of each beacon and the closest point to the beacon that
    # is detected by the sensor.
    for closest_to_sensor, beacon in data:
        # Calculate the manhattan distance between the beacon
        # and the set of coordinates (0, Y).
        bells.append(( manhattan_distance := sum(abs(a - b) for a, b in zip(closest_to_sensor, beacon))))
        # Calculate the coordinates of the bottom and left sides
        # of the exclusion zone for the current beacon.
        # Calculate the coordinates of the bottom and left sides of the exclusion
        # zone for the current beacon.
        elf.append(
            (B := (closest_to_sensor[0] - manhattan_distance - 1,
            closest_to_sensor[1]),
            S := (closest_to_sensor[0], closest_to_sensor[1] - manhattan_distance- 1))
        )
        # Calculate the coordinates of the top and right sides of the exclusion
        # zone for the current beacon.
        eve.append(
            (B,
            E := (closest_to_sensor[0],
            closest_to_sensor[1] + manhattan_distance + 1))
        )

        snow.append((S,
         T := (closest_to_sensor[0] + manhattan_distance + 1,
          closest_to_sensor[1]))
          )
        # The eve, snow, and tinsel lists store the coordinates of the top,
        # bottom, left, and right sides of the exclusion zone for each beacon.
        # The elements of the eve list are tuples of the form ((Bx, By), (Ex, Ey)),
        # where (Bx, By) are the coordinates of the bottom and left sides of the
        # exclusion zone, and (Ex, Ey) are the coordinates of the top and right
        # sides of the exclusion zone. The elements of the snow and tinsel lists
        # are similar, but the coordinates are reversed.

        tinsel.append((E, T))
        # Calculate the x-coordinates of the exclusion zone and add them to a set.
        if (man_y := abs(closest_to_sensor[1] - set_y)) <= manhattan_distance:
            x_ranges.add((closest_to_sensor[0] - (man_x := manhattan_distance - man_y) ,
            closest_to_sensor[0] + man_x)
            )
   
    # Calculate the minimum and maximum x-coordinates of the exclusion zone.
    start, end = min(x[0] for x in x_ranges), max(x[1] for x in x_ranges)
    # Return the length of the exclusion zone along the x-axis, minus the
    # number of beacons that are located at the specified y-coordinate.
    return bells, elf,eve, snow, tinsel, abs(start - end) + 1 - sum(x[1] == set_y for x in beacons)

# Read the input data from a file and parse it into a list of tuples,
# where each tuple contains the coordinates of a beacon and the
# coordinates of the closest point to the beacon that is detected by
# the sensor.

with open("day15/data15.txt", "r", encoding="utf") as file:
    data = [
        ((z := [int(x.split(" ")[y].split("=")[1].strip(",").strip(":"))
        for y in [2, 3, -2, -1]])[:2], z[2:])
        for x in file.read().splitlines()
    ]
    # Calculate the coordinates of the exclusion zone and the length
    # of the exclusion zone along the x-axis.
    beacons = set(tuple(x[1]) for x in data)
    bells, elf, eve, snow, tinsel, snowball1 = jolly()
    # Initialize a set to store the coordinates of the exclusion
    frost = set()
    # Initialize a variable to store the final result.
    chestnuts2 = None
    # Loop until a coordinate within the specified range is found.
    while not chestnuts2:
        for a1, b1 in elf + tinsel:
            for c1, d1 in eve + snow:
                # Check if the current coordinate is within the specified range.
                if (hit := Exclusion_Zone(*a1, *b1, *c1, *d1)) and 0 <= min(hit) and max(hit) <= 4000000:
                    # Check if the current coordinate is within the manhattan distance
                    # of any of the beacons.
                    for T, (closest_to_sensor, beacon) in enumerate(data):
                        if sum(abs(a1 - b1) for a1, b1 in zip(closest_to_sensor, hit)) <= bells[T]:
                            break
                    else:
                    # If the coordinate is not within the manhattan distance of any of
                    # the beacons, it is a valid coordinate, so store it in the
                    # chestnuts2 variable and exit the loop.
                        chestnuts2 = hit[0] * 4000000 + hit[1]
# Print the final result to the screen.
    print(snowball1)
    print(chestnuts2)
