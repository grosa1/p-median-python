import random as r
from Node import Node
from math import exp
import NodeUtils


def simulated_annealing(sol, offices, customers):
    old_cost = evaluate_sol(sol, offices, customers)
    print_sol(sol, old_cost)

    temp = 1.0
    temp_min = 0.00001
    alpha = 0.9
    while temp > temp_min:
        i = 1
        while i <= 100:
            new_sol = get_rand_neighbor(sol, offices)
            new_cost = evaluate_sol(new_sol, offices, customers)
            ap = acceptance_probability(old_cost, new_cost, temp)
            if ap > r.random():
                sol = new_sol
                old_cost = new_cost
                print_sol(new_sol, new_cost)
            i += 1
        temp = temp * alpha

    return sol, old_costgit


def get_rand_neighbor(sol, offices, area=10):
    swap_id = r.randrange(len(sol))
    # new_x = offices[swap_id].x + r.uniform(-area, area)
    # new_y = offices[swap_id].y + r.uniform(-area, area)

    # new_office = NodeUtils.closest_node(Node(None, new_x, new_y, None), offices)
    new_id = r.randrange(len(offices))
    sol[swap_id] = new_id

    return sol


def evaluate_sol(offices_id, offices, customers):
    tot_dist = 0
    tot_reward = 0

    offices_sol = list()
    for index in offices_id:
        offices_sol.append(offices[index])

    for c in customers:
        o = NodeUtils.closest_node(c, offices_sol)
        tot_dist += NodeUtils.euclidean_dist(o, c) + offices[index].value
        tot_reward += c.value

    return tot_reward - int(tot_dist)


def acceptance_probability(old_cost, new_cost, T):
    try:
        return exp((new_cost - old_cost) / T)
    except OverflowError:
        return float('inf')


def print_sol(solution, cost):
    print('### SOLUTION ###')
    print('cost: ' + str(cost))
    print(*solution)
    print()


