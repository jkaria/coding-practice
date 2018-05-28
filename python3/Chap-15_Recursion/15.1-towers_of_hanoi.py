#!/usr/local/bin/python3


def compute_tower_of_hanoi(num_rings):
    print("num rings ->", num_rings)

    def compute_transitions(rings, from_peg, to_peg, free_peg):
        if len(rings) == 0:
            return

        #move n-1 rings to free peg
        compute_transitions(rings[0:-1], from_peg, free_peg, to_peg)
        print('moving ring {} from {} -> to {}'.format(rings[-1], from_peg, to_peg))
        compute_transitions(rings[0:-1], free_peg, to_peg, from_peg)

    rings = list(range(num_rings))
    compute_transitions(rings, 'peg_1', 'peg_2', 'peg_3')

if __name__ == '__main__':
    print('The two towers of Hanoi problem')

    compute_tower_of_hanoi(1)
    compute_tower_of_hanoi(3)
    # compute_tower_of_hanoi(5)
