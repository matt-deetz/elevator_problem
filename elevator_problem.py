
from bisect import bisect_right

def elevator_problem(start, floors):
    top = max(floors)
    bottom = min(floors)
    unique_floors = sorted(set(f for f in floors if f != start))
    visited = []
    x = bisect_right(unique_floors, start)
    
    
    if abs(start - bottom) < abs(top - start):
        cost = (abs(start - bottom) + abs(top - bottom)) * 10
        visited = unique_floors[:x][::-1] + unique_floors[x:]
    else:
        cost = (abs(top - start) + abs(top - bottom)) * 10
        visited = unique_floors[x:] + unique_floors[:x][::-1]
        
    return (visited, cost)



if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Elevator problem solver")
    parser.add_argument("--start", type=int, required=True, help="Starting floor")
    parser.add_argument("--floor", type=str, required=True, help="Comma-separated list of floors to visit")
    args = parser.parse_args()

    floors = [int(f) for f in args.floor.split(",")]
    visited, cost = elevator_problem(args.start, floors)
    floors_str = ",".join(str(f) for f in visited)
    print(f"{cost} {floors_str}")

