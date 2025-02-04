graph = {'start': {'a': 6, 'b' : 2}, 'a': {'finish': 1}, 'b':{'a':3, 'finish':5}, 'finish':{}}

infinity= float("inf")

costs = {'a': 6, 'b' : 2, 'finish': infinity}

parents= {'a':'start', 'b':'start', 'finish': None}
proceessed = []
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs: 
        cost = costs[node]
        if cost< lowest_cost and node not in proceessed
        lowest_cost = cost
        lowest_cost_node = node
    return lowest_cost_node