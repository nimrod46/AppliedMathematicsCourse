def normip(v, p):
    """
    function to compute the natural norm of an input vector.
    Inputs: v - a numpy array (n dim vector)
    Outputs: natural norm of v
    """
    return sum(map(lambda x: abs(x) ** p, v)) ** (1 / p)
