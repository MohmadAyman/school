'''
Created on Oct 2, 2016

@author: farida
'''
from search import romania_map, GraphProblem, breadth_first_tree_search,\
    depth_first_graph_search, iterative_deepening_search,\
    recursive_best_first_search, breadth_first_search, uniform_cost_search,\
    depth_limited_search


print("Romania Locations:")
print("==================")
print(romania_map.locations)

print("Romania Map:")
print("=============")
print(romania_map.dict)

romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)

print("Search Algorithms Results:")
print("==========================")
print(breadth_first_search(romania_problem).solution())
#print(breadth_first_search(romania_problem).path_cost)
print(uniform_cost_search(romania_problem).solution())
#print(uniform_cost_search(romania_problem).path_cost)
print(depth_first_graph_search(romania_problem).solution())
print(depth_first_graph_search(romania_problem).path_cost)





