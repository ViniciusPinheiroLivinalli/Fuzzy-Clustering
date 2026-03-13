# Input: data_points (X), number of clusters (C), fuzziness coefficient (m), convergence threshold (epsilon)
# Output: cluster centers (c), membership matrix (U)
initialize U randomly such that for each data point i: sum(U[i][j] for j in 1...C) = 1
repeat:
    # Step 1: Compute cluster centers
    for each cluster j:
        numerator = sum( (U[i][j] ** m) * X[i] for i in range(N) )
        denominator = sum( U[i][j] ** m for i in range(N) )
        c[j] = numerator / denominator
    # Step 2: Update membership values
    for each data point i:
        for each cluster j:
            sum_term = 0
            for each cluster k:
                ratio = norm(X[i] - c[j]) / norm(X[i] - c[k])
                sum_term += (ratio) ** (2 / (m - 1))
            U[i][j] = 1 / sum_term
    # Check convergence: if change in U is less than epsilon, break
until convergence
return c, U
