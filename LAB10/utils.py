def read_test_case1_from_txt(filename = "LAB10\Testcase_Q1.txt"):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # Read the value of K from the first line
        K = int(lines[0].strip())

        # Read and process the adjacency matrix
        adjacency_matrix = []
        for line in lines[1:]:
            row = [int(num) for num in line.strip().split()]
            adjacency_matrix.append(row)

        return K, adjacency_matrix

def read_test_case2_from_txt(filename = "LAB10\Testcase_Q2.txt"):
    with open(filename, "r") as f:
        data = f.read()

    # Parse the input data
    lines = data.strip().split("\n")
    n = len(lines)  # Assuming the size of the matrix is equal to the number of lines
    adj_matrix = [[int(x) for x in line.split()] for line in lines]

    return n, adj_matrix

def read_test_case3_from_txt(filename = "LAB10\Testcase_Q3.txt"):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Read the number of clauses
    m = int(lines[0].strip())

    # Read each clause
    clauses = []
    for i in range(1, m + 1):
        # Split the line into literals and convert them to integers
        literals = list(map(int, lines[i].strip().split()))
        clauses.append(literals)

    return m, clauses

if __name__ == "__main__":
    import numpy as np
    print("-" * 50)
    print("Test Case 1:")
    K, adjacency_matrix = read_test_case1_from_txt()
    print(f"K: {K}")
    print(f"Adjacency Matrix:\n{np.array(adjacency_matrix)}")
    
    print("-" * 50)
    print("Test Case 2:")
    n, adjacency_matrix = read_test_case2_from_txt()
    print(f"n: {n}")
    print(f"Adjacency Matrix:\n{np.array(adjacency_matrix)}")
    
    print("-" * 50)
    print("Test Case 3:")
    m, clauses = read_test_case3_from_txt()
    print(f"m: {m}")
    print(f"Clauses: {clauses}")
    
    print("-" * 50)
    