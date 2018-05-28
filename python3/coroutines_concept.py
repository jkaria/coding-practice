#!/usr/local/bin/python3
from collections import namedtuple


Query = namedtuple('Query', ('y', 'x'))
Transition = namedtuple('Transition', ('y', 'x', 'state'))
TICK = object()
ALIVE = "*"
EMPTY = "-"


class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width  = width
        self.rows   = []
        for _ in range(height):
            self.rows.append([EMPTY] * self.width)

    def __str__(self):
        res = "\n"
        for r in self.rows:
            res += "".join(r) + "\n"
        return res

    def assign(self, y, x, value):
        self.rows[y % self.height][x % self.width] = value

    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]


def game_logic(state, neighbours_alive):
    """ Document game logic in words
    """
    if state == ALIVE:
        if neighbours_alive < 2:
            return EMPTY # To few -> DIE
        elif neighbours_alive > 3:
            return EMPTY # To many -> DIE
    else:
        if neighbours_alive == 3:
            return ALIVE # Regnerate
    return state


def count_neighbours(y, x):
    """Counts # of neighbours in ALIVE state"""
    n_ = yield Query(y+1, x)
    ne = yield Query(y+1, x+1)
    _e = yield Query(y, x+1)
    se = yield Query(y-1, x+1)
    s_ = yield Query(y-1, x)
    sw = yield Query(y-1, x-1)
    _w = yield Query(y, x-1)
    nw = yield Query(y+1, x-1)
    neighbour_states = [n_, ne, _e, se, s_, sw, _w, nw]
    count = 0
    for state in neighbour_states:
        if state == ALIVE:
            count += 1
    return count


def step_cell(y, x):
    state = yield Query(y, x)
    neighbours = yield from count_neighbours(y, x)
    next_state = game_logic(state, neighbours)
    yield Transition(y, x, next_state)

def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK


def live_a_generation(grid, sim):
    next_grid = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else: # cell transition complete, assign result in new grid
            next_grid.assign(item.y, item.x, item.state)
            item = next(sim) # sim.send('abc')
                             # BOTH works since yield Transition value is not used
    return next_grid


class GridJoiner(object):
    def __init__(self):
        self.grids = []

    def add_grid(self, grid):
        self.grids.append(grid)

    def __str__(self):
        res = ""
        header_str = ""
        rows_str = []
        for idx, grid in enumerate(self.grids):
            if idx > 0:
                header_str += "|"
            header_str += "{:^{:d}d}".format(idx, grid.width)
            for h_idx, r in enumerate(grid.rows):
                if idx == 0: # first grid
                    rows_str.append("".join(r))
                else:
                    rows_str[h_idx] += "|" + "".join(r)

        res += header_str
        for r_str in rows_str:
            res += "\n" + r_str

        return res


if __name__ == "__main__":
    print("Implemeting game of life using coroutines!")
    grid = Grid(5, 9)
    simulator = simulate(grid.height, grid.width)
    grid.assign(0, 3, ALIVE)
    grid.assign(1, 4, ALIVE)
    grid.assign(2, 2, ALIVE)
    grid.assign(2, 3, ALIVE)
    grid.assign(2, 4, ALIVE)
    grid_joiner = GridJoiner()

    for _ in range(5):
        grid_joiner.add_grid(grid)
        grid = live_a_generation(grid, simulator)

    print(grid_joiner)
