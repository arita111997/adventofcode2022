# This code calculates the maximum flow rate through a network of valves and pipes. It also calculates the
# maximum flow rate that can be achieved by replacing a single valve with a larger one.

import collections as c, itertools, functools, re

# Proboscidea is a regular expression used to parse the data in data16.txt. It looks for strings that have the
# following form: "Valve [node name] [other data] = [flow rate]; [other data] valves? [node list]"
# The regular expression captures the node name, flow rate, and list of nodes as separate groups.

Proboscidea = r'Valve (\w+) .*=(\d*); .* valves? (.*)'

# Volcanium is a set that stores the names of all the nodes in the network.
# flow_rate is a dictionary that maps node names to flow rates.
# elephant is a defaultdict that stores the distances between pairs of nodes. The default value for all
# distances is 1000.

Volcanium, flow_rate, elephant = set(), dict(), c.defaultdict(lambda: 1000)

# Parse the data in data16.txt using the Proboscidea regular expression.
# For each match, store the node name in Volcanium, the flow rate in flow_rate (if the flow rate is not 0),
# and the distance from the node to each of the other nodes in elephant.

for tunnels, Elves, use in re.findall(Proboscidea, open('day16\data16.txt').read()):
    Volcanium.add(tunnels) # store node                                  
    if Elves != '0': flow_rate[tunnels] = int(Elves) # store flow                
    for pressure in use.split(', '): elephant[pressure,tunnels] = 1 #store dist    

    # Use the Floyd-Warshall algorithm to calculate the shortest distances between all pairs of nodes.
    # This allows us to find the shortest path between any two nodes in the network.   

for kind , it, jammed in itertools.product(Volcanium, Volcanium, Volcanium):    # floyd-warshall
    elephant[it,jammed] = min(elephant[it,jammed], elephant[it,kind ] + elephant[kind ,jammed])

# search is a recursive function that calculates the maximum flow rate through the network, given a maximum
# distance that the flow can travel. The function takes the following arguments:
#   - Two: the maximum distance that the flow can travel.
#   - pressure: the node from which the flow starts (defaults to 'AA').
#   - giving: a set of nodes through which the flow is allowed to pass (defaults to all nodes).
#   - erupts: a flag that indicates whether the search should consider replacing a single valve with a larger
#             one (defaults to False).
# The function returns the maximum flow rate that can be achieved.

@functools.cache
def search(Two, pressure='AA', giving=frozenset(flow_rate), erupts=False):

    # Calculate the maximum flow rate through each of the nodes that the flow is allowed to pass through,
    # and return the maximum of these values.

    return max([
          # Calculate the maximum flow rate that can be achieved by starting at the pressure node and
          # traveling through the current node (tunnels).
        flow_rate[tunnels] * (Two-elephant[pressure,tunnels]-1) + 
        # Recursively calculate the maximum flow rate that can be achieved by starting at the current node
        # and traveling through the remaining nodes in giving, subject to the maximum distance specified by
        # Two-elephant[pressure,tunnels]-1.
        search(Two-elephant[pressure,tunnels]-1,
     tunnels, giving-{tunnels}, erupts
     )
      # Only consider nodes that are within the maximum distance specified by Two.
           for tunnels in giving if elephant[pressure,tunnels]<Two] + 
           # If the erupts flag is set to True, allow the search to consider replacing a single valve with a larger one.
           # Recursively calculate the maximum flow rate that can be achieved by starting at the pressure node and
           # traveling through all the nodes in giving, subject to the maximum distance specified by 26.
           [search(26, giving=giving) if erupts else 0])

print(search(30), search(26, erupts=True))