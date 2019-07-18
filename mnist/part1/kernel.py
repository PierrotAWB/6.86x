import numpy as np

### Functions for you to fill in ###



def polynomial_kernel(X, Y, c, p):
    """
        Compute the polynomial kernel between two matrices X and Y::
            K(x, y) = (<x, y> + c)^p
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            c - a coefficient to trade off high-order and low-order terms (scalar)
            p - the degree of the polynomial kernel

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    def K(s, t, c, p): 
        return (sum(s * t) + c) ** p
    
    n = np.shape(X)[0]
    m = np.shape(Y)[0]

    kernel_matrix = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            kernel_matrix[i][j] = K(X[i], Y[j], c, p)
    
    return kernel_matrix
    
    raise NotImplementedError



def rbf_kernel(X, Y, gamma):
    """
        Compute the Gaussian RBF kernel between two matrices X and Y::
            K(x, y) = exp(-gamma ||x-y||^2)
        for each pair of rows x in X and y in Y.

        Args:
            X - (n, d) NumPy array (n datapoints each with d features)
            Y - (m, d) NumPy array (m datapoints each with d features)
            gamma - the gamma parameter of gaussian function (scalar)

        Returns:
            kernel_matrix - (n, m) Numpy array containing the kernel matrix
    """
    def K(s, t, gamma): 
        return np.exp(-gamma * np.linalg.norm(s - t) ** 2) 
    
    n = np.shape(X)[0]
    m = np.shape(Y)[0]

    kernel_matrix = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            kernel_matrix[i][j] = K(X[i], Y[j], gamma)
    
    return kernel_matrix
    raise NotImplementedError

