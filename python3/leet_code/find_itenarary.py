#!/usr/local/bin/python3
import collections
import heapq


def findItinerary(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    tickets.sort()
    flights = collections.defaultdict(list)
    for t in tickets:
        # heapq.heappush(flights[t[0]], t[1])
        flights[t[0]].append(t[1])

    # print(flights)

    route = []

    def visit(airport):
        if airport in flights:
            while flights[airport]:
                visit(flights[airport].pop())
            route.append(airport)
    visit('JFK')

    # while True:
    #     if route[-1] not in flights or flights[route[-1]] == []:
    #         break

    #     route.append(heapq.heappop(flights[route[-1]]))

    return route


if __name__ == '__main__':
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    print('findItenarary:', findItinerary(tickets))
    tickets = [["JFK","ATL"],["ATL","JFK"]]
    print('findItenarary:', findItinerary(tickets))
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    print('findItenarary:', findItinerary(tickets))
