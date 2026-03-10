

test_cases = [
    {
        "description": "All floors above start - single sweep up",
        "start": 2,
        "floors": [5, 8, 10, 3],
        "expected_order": [3, 5, 8, 10],
        "expected_time": 80
    },
    {
        "description": "All floors below start - single sweep down",
        "start": 10,
        "floors": [7, 4, 1, 6],
        "expected_order": [7, 6, 4, 1],
        "expected_time": 90
    },
    {
        "description": "Mixed floors, up sweep is cheaper",
        "start": 5,
        "floors": [6, 7, 8, 3],
        "expected_order": [3, 6, 7, 8],
        "expected_time": 70
    },
    {
        "description": "Mixed floors, down sweep is cheaper",
        "start": 5,
        "floors": [2, 1, 3, 7],
        "expected_order": [7, 3, 2, 1],
        "expected_time": 80
    },
    {
        "description": "Single floor above",
        "start": 4,
        "floors": [9],
        "expected_order": [9],
        "expected_time": 50
    },
    {
        "description": "Single floor below",
        "start": 8,
        "floors": [3],
        "expected_order": [3],
        "expected_time": 50
    },
    {
        "description": "Floors already in optimal order given as input",
        "start": 1,
        "floors": [3, 5, 7, 9],
        "expected_order": [3, 5, 7, 9],
        "expected_time": 80
    },
    {
        "description": "Duplicate floors in input",
        "start": 5,
        "floors": [8, 8, 3, 3],
        "expected_order": [3, 8],
        "expected_time": 70
    },
    {
        "description": "Floor in list matches starting floor",
        "start": 5,
        "floors": [5, 8, 2],
        "expected_order": [8, 2],
        "expected_time": 90
    },
    {
        "description": "Large spread of floors",
        "start": 50,
        "floors": [1, 25, 75, 100],
        "expected_order": [25, 1, 75, 100],
        "expected_time": 1480
    },
]

for i, tc in enumerate(test_cases):
    order, time = elevator_problem(tc["start"], tc["floors"])
    
    passed_time = time == tc["expected_time"]
    passed_order = order == tc["expected_order"]
    
    status = "PASS" if passed_time and passed_order else "FAIL"
    print(f"Test {i+1} [{status}]: {tc['description']}")
    
    if not passed_order:
        print(f"  Order   → expected {tc['expected_order']}, got {order}")
    if not passed_time:
        print(f"  Time    → expected {tc['expected_time']}, got {time}")

