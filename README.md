# elevator_problem
An executable solution to the elevator problem

I chose to optimize floor order using the SCAN algorithm rather than visiting floors in input order, as the goal was to minimize total travel time
Duplicate floors in the input are deduplicated since visiting the same floor twice is unnecessary
If the starting floor appears in the floor list it is ignored since the elevator is already there
When the cost of going up first vs down first is equal, the program defaults to up first
Floor numbers are assumed to be positive integers

To run the program:
python elevator_problem.py --start 12 --floor 2,9,1,32

Expected Output:
560 12,2,9,1,32
