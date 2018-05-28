#!/usr/local/bin/python3
import collections
import heapq

def find_cheapest_flight(n, flights, src, dst, K):
    PriceDest = collections.namedtuple('PriceDest', ('price', 'dest'))
    Node = collections.namedtuple('Node', ('price', 'name', 'stops'))

    available_flights = collections.defaultdict(list)
    for f in flights:
        available_flights[f[0]].append(PriceDest(f[2], f[1]))

    min_heap = []
    heapq.heappush(min_heap, Node(0, src, 0))

    while min_heap:
        node = heapq.heappop(min_heap)

        if node.name == dst:
            return node.price

        if node.stops > K: #stops exhausted, can't proceed further from this node
            continue

        #proceed further to next nodes
        for f in available_flights[node.name]:
            heapq.heappush(min_heap, Node(node.price + f.price, f.dest, node.stops + 1))

    return -1 # no route found



    # def find_cheapest_flight_helper(stop, price_so_far, num_pending):
    #     if stop == dst:
    #         return price_so_far

    #     if num_pending < 0: # stops exhausted, no routes found
    #         return -1

    #     for flight in sorted(available_flights[stop]):
    #         final_price = find_cheapest_flight_helper(flight.dest, price_so_far + flight.price, num_pending - 1)
    #         if final_price > 0:
    #             return final_price
    #     return -1 # no routes found


    # return find_cheapest_flight_helper(src, 0, K)



if __name__ == '__main__':
    print('Find cheapest flight from src -> dest with atmost k stops')
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    print(find_cheapest_flight(n, flights, 0, 2, 1))
    print(find_cheapest_flight(n, flights, 0, 2, 0))
    n = 5
    flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
    print(find_cheapest_flight(n, flights, 2, 1, 1))
