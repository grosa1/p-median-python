import sys
import KMeansClustering as kmeans
import InputReader
import Terrain
import Node
import math
import OfficeSolution


solution = list()
offices_list = list()
customers_list = list()


def main(input_file):
    input_data = InputReader.read(input_file)
    customers_list = input_data.customers_list

    office_index = 0
    for y in len(input_data.map):
        for x in len(input_data.map[0]):
            if (input_data.map[x][y] > 0) and (input_data.map[x][y] != Terrain.cost_mountains):
                office = Node()
                office.index = office_index
                office.x = x
                office.y = y
                office.value = input_data.map[x][y]
                offices_list.append(office)
                office_index += 1

    dist_matrix = distance_matrix(offices_list, customers_list)
    initial_sol = gen_initial_solution()


def distance_matrix(nodes_x, nodes_y):
    d_matrix = [[0 for x in range(len(nodes_x))] for y in range(len(nodes_y))]
    for i in range(nodes_x):
        for j in range(nodes_y):
            d_matrix[i][j] = euclidean_dist(offices_list[i], customers_list[j])

    return d_matrix


def euclidean_dist(node1, node2):
    return math.sqrt(((node1.x-node2.x)**2) + ((node1.y-node2.y)**2))


def gen_initial_solution(data_points, n_offices, map):
    tot_iteration = 100
    [cluster_label, new_centroids] = k_means(data_points, n_offices, tot_iteration)

    solution = list()
    for i in range(len(new_centroids)):
        office_sol = OfficeSolution()
        office_sol.office = 0
        solution.append()



def k_means(data_points, n_centroids, tot_iteration=100):
    centroids = kmeans.create_centroids(data_points, n_centroids)
    [cluster_label, new_centroids] = kmeans.iterate_k_means(data_points, centroids, tot_iteration)
    # kmeans.print_label_data([cluster_label, new_centroids])

    return [cluster_label, new_centroids]


if __name__ == '__main__':
    main(sys.argv[1])