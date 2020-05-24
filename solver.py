# location, taxi-targets, bus-targets, subway-targets, boat-target
def get_possible_stations(city, station, ticket):
    # this collects all possible stations
    possible_stations = []

    # if not black ticket
    if ticket != 4:
        # every possible next station
        for possible_station in city[station][ticket]:
            # gets appended to the result
            possible_stations.append(possible_station)
    
    # black ticket
    else:
        # every possible ticket, including black
        for ticket in [1, 2, 3, 4]:
            # every possible next station
            for possible_station in city[station][ticket]:
                # if it is not already in the list
                if not possible_station in possible_stations:
                    # gets appended to the result
                    possible_stations.append(possible_station)
    
    # clean the result
    possible_stations.sort()

    # return all possible stations
    return possible_stations

def solve(city, station, tickets):
    # for an unknown start station
    if station == 0:
        # allow all stations in the city
        result = [n+1 for n in range(len(city)-1)]
    else:
        # first the result is the starting station
        result = [station]

    # for every ticket that Mister X used
    for ticket in tickets:
        # copy the last results
        last_result = result.copy()
        # clear the new result list
        result = []
        # for every station in the results of the last ticket
        for station in last_result:
            # get possible next stations
            next_result = get_possible_stations(city, station, ticket)
            # and append them
            for next_station in next_result:
                # if they dont already exist
                if not next_station in result:
                    # to the new result list
                    result.append(next_station)
    
    # sort the result
    result.sort()

    # finally, return the last results
    return result


if __name__ == "__main__":
    print("Please execute MisterXSolver.py as main")