sym_mountains = "#"
sym_water = "~"
sym_traffic_jam = "*"
sym_dirt = "+"
sym_railway_level_crossing = "X"
sym_standard_terrain = "_"
sym_highway = "H"
sym_railway = "T"

cost_mountains = 2000
cost_water = 800
cost_traffic_jam = 200
cost_dirt = 150
cost_railway_level_crossing = 120
cost_standard_terrain = 100
cost_highway = 70
cost_railway = 50
cost_default = cost_mountains


def get_cost(sym):
    switcher = {
        cost_mountains: sym_mountains,
        cost_water: sym_water,
        cost_traffic_jam: sym_traffic_jam,
        cost_dirt: sym_dirt,
        cost_railway_level_crossing: sym_railway_level_crossing,
        cost_standard_terrain: sym_standard_terrain,
        cost_highway: sym_highway,
        cost_railway: sym_railway
    }

    return switcher.get(sym, None)


def get_sym(cost):
    switcher = {
        sym_mountains: cost_mountains,
        sym_water: cost_water,
        sym_traffic_jam: cost_traffic_jam,
        sym_dirt: cost_dirt,
        sym_railway_level_crossing: cost_railway_level_crossing,
        sym_standard_terrain: cost_standard_terrain,
        sym_highway: cost_highway,
        sym_railway: cost_railway
    }

    return switcher.get(cost, None)
