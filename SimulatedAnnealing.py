import random as r
from Node import Node
from math import exp
import NodeUtils
from time import time


def simulated_annealing(sol, offices, customers, verbose=True):
    start_time = time()

    old_cost, built_offices = evaluate_sol(sol, offices, customers)
    if verbose:
        print_sol(sol, old_cost, built_offices)

    sol_built_offices = 0
    temp = 1.0
    temp_min = 0.00001
    alpha = 0.9
    while temp > temp_min:
        i = 1
        while i <= 100:
            new_sol = get_rand_neighbor2(sol, offices)
            new_cost, built_offices = evaluate_sol(new_sol, offices, customers)
            ap = acceptance_probability(old_cost, new_cost, temp)
            if ap > r.random():
                sol = new_sol
                old_cost = new_cost
                sol_built_offices = built_offices
                if verbose:
                    print_sol(new_sol, new_cost, built_offices)
            i += 1
        temp = temp * alpha

    elapsed_time = time() - start_time

    return sol, old_cost, sol_built_offices, elapsed_time


def get_rand_neighbor(sol, offices, area=10):
    swap_id = r.randrange(len(sol))
    new_x = offices[swap_id].x + r.uniform(-area, area)
    new_y = offices[swap_id].y + r.uniform(-area, area)

    new_office = NodeUtils.closest_node(Node(None, new_x, new_y, None), offices)
    sol[swap_id] = new_office.index

    return sol


def get_rand_neighbor2(sol, offices):
    to_swap_id = r.randrange(len(sol))

    new_id = r.randrange(len(offices))
    sol[to_swap_id] = new_id

    return sol


def evaluate_sol(offices_id, offices, customers):
    tot_dist = 0
    tot_reward = 0

    offices_sol = list()
    for index in offices_id:
        offices_sol.append(offices[index])

    built_offices = list()
    for customer in customers:
        office = NodeUtils.closest_node(customer, offices_sol)
        tot_dist += NodeUtils.euclidean_dist(office, customer) + offices[index].value
        tot_reward += customer.value

        if office not in built_offices:
            built_offices.append(office)

    return tot_reward - int(tot_dist), len(built_offices)


def acceptance_probability(old_cost, new_cost, T):
    try:
        return exp((new_cost - old_cost) / T)
    except OverflowError:
        return float('inf')


def print_sol(solution, cost, built_offices):
    print('### SOLUTION ###')
    print('cost: ' + str(cost))
    print(*solution)
    print("built offices: " + str(built_offices))
    print()


