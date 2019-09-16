import Node
import Terrain


class InputData():
    def __init__(self):
        self.num_max_offices = None
        self.num_customers = None
        self.customers_list = list()
        self.map_n = None
        self.map_m = None
        self.map = None

    @staticmethod
    def read(input_file):
        input_data = InputData()
        with open(input_file, "r") as in_file:
            header = in_file.readline().split()
            input_data.map_m = header[1]
            input_data.map_n = header[0]
            input_data.num_customers = header[2]
            input_data.num_max_offices = header[3]

            for i in range(0, input_data.num_customers):
                row = in_file.readline().split()
                customer = Node()
                customer.index = i
                customer.x = row[0]
                customer.y = row[1]
                customer.value = row[2]
                input_data.customers_list.append(customer)

            input_data.map = [[0 for x in range(input_data.map_n)] for y in range(input_data.map_m)]
            for i in range(0, input_data.map_m):
                row = in_file.readline().split()
                for j in range(0, input_data.map_n):
                    input_data.map[i][j] = Terrain.get_cost(row[j])

            for node in input_data.customers_list:
                input_data.map[node.x][node.y] = -1

        return input_data




