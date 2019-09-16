import sys
import KMeansClustering as kmeans
import InputReader
import Terrain
from Node import Node
import NodeUtils
import SimulatedAnnealing as sa
from time import time


def main(input_file):
    offices_list = list()
    customers_list = list()

    input_data = InputReader.read(input_file)
    customers_list = input_data.customers_list

    office_index = 0
    for y in range(len(input_data.map)):
        for x in range(len(input_data.map[0])):
            if (input_data.map[y][x] > 0) and (input_data.map[y][x] < Terrain.cost_mountains):
                office = Node(office_index, x, y, input_data.map[y][x])

                offices_list.append(office)
                office_index += 1

    # dist_matrix = NodeUtils.distance_matrix(offices_list, customers_list)

    data_points = list()
    for c in customers_list:
        data_points.append([c.x, c.y])

    kmeans_time = time()
    initial_sol = gen_initial_solution(data_points, offices_list, customers_list, input_data.num_max_offices)
    # print(str(compute_initial_sol_value(initial_sol, dist_matrix, customers_list)))

    kmeans_time = time() - kmeans_time

    solution = list()
    for sol in initial_sol:
        solution.append(sol.office.index)

    [sol, cost, built_offices, sa_time] = sa.simulated_annealing(solution, offices_list, customers_list, verbose=False)
    sa.print_sol(sol, cost, built_offices)
    print("total time (s): " + str(kmeans_time + sa_time))


def gen_initial_solution(data_points, offices, customers, n_offices):
    tot_iteration = 100
    [cluster_label, new_centroids] = k_means(data_points, n_offices, tot_iteration)

    new_solution = list()
    clusters = list()

    for i in range(len(new_centroids)):
        clusters.append(list())

    for label in cluster_label:
        clusters[label[0]].append(label)

    office = None
    for cluster in clusters:
        customers_id = list()
        for elem in cluster:
            cust = NodeUtils.closest_node(Node(None, elem[1][0], elem[1][1], None), customers)
            customers_id.append(cust.index)
            office = NodeUtils.closest_node(Node(None, elem[2][0], elem[2][1], None), offices)

        office_sol = InitialSolution()
        office_sol.office = office
        office_sol.customers_id = customers_id

        new_solution.append(office_sol)

    return new_solution


def k_means(data_points, n_centroids, tot_iteration=100):
    centroids = kmeans.create_centroids(data_points, n_centroids)
    [cluster_label, new_centroids] = kmeans.iterate_k_means(data_points, centroids, tot_iteration)
    # kmeans.print_label_data([cluster_label, new_centroids])

    return [cluster_label, new_centroids]

# def compute_initial_sol_value(solution, dist_mat, customers):
#     tot_dist = 0
#     tot_reward = 0
#     for s in solution:
#         for c in s.customers_id:
#             tot_dist += dist_mat[s.office.index][c] + s.office.value
#             tot_reward += customers[c].value
#
#     return tot_reward - int(tot_dist)


class InitialSolution:
    def __init__(self):
        self.office = None
        self.customers_id = list()


if __name__ == '__main__':
    main(sys.argv[1])
