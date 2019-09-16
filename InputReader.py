from Node import Node
import Terrain


class InputData():
    def __init__(self):
        self.num_max_offices = None
        self.num_customers = None
        self.customers_list = list()
        self.map_n = None
        self.map_m = None
        self.map = None


def read(input_file):
    input_data = InputData()
    with open(input_file, "r") as in_file:
        header = in_file.readline().strip().split()
        input_data.map_m = int(header[1])
        input_data.map_n = int(header[0])
        input_data.num_customers = int(header[2])
        input_data.num_max_offices = int(header[3])

        input_data.customers_list = list()
        for i in range(0, input_data.num_customers):
            line = in_file.readline().strip().split()
            customer = Node(i, int(line[0]), int(line[1]), int(line[2]))
            input_data.customers_list.append(customer)

        input_data.map = [[0 for x in range(input_data.map_n)] for y in range(input_data.map_m)]
        for i in range(input_data.map_m):
            line = in_file.readline().strip()
            j = 0
            for char in line:
                input_data.map[i][j] = Terrain.get_cost(char)
                j += 1

        for node in input_data.customers_list:
            input_data.map[node.y][node.x] = -1

    return input_data




