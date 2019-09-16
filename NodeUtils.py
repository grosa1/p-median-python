from scipy.spatial import distance
import math


def closest_node(node, nodes):
    p_node = (node.x, node.y)
    p_nodes = list()
    for n in nodes:
        p_nodes.append([n.x, n.y])

    closest_index = distance.cdist([p_node], p_nodes).argmin()

    return nodes[closest_index]


def distance_matrix(nodes_x, nodes_y):
    d_matrix = [[0 for x in range(len(nodes_y))] for y in range(len(nodes_x))]
    for i in range(len(nodes_x)):
        for j in range(len(nodes_y)):
            d_matrix[i][j] = euclidean_dist(nodes_x[i], nodes_y[j])

    return d_matrix


def euclidean_dist(node1, node2):
    return math.sqrt(((node1.x-node2.x)**2) + ((node1.y-node2.y)**2))
