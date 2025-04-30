import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        """
        {
        'mean': [axis1, axis2, flattened],
        'variance': [axis1, axis2, flattened],
        'standard deviation': [axis1, axis2, flattened],
        'max': [axis1, axis2, flattened],
        'min': [axis1, axis2, flattened],
        'sum': [axis1, axis2, flattened]
        }
        """
        matrixOf3 = np.array(list).reshape(3,3)

        mean = [matrixOf3.mean(axis=0).tolist(), matrixOf3.mean(axis=1).tolist(), matrixOf3.flatten().mean()]
        variance = [matrixOf3.var(axis=0).tolist(), matrixOf3.var(axis=1).tolist(), matrixOf3.flatten().var()]
        standard = [matrixOf3.std(axis=0).tolist(), matrixOf3.std(axis=1).tolist(), matrixOf3.flatten().std()]
        max1 = [matrixOf3.max(axis=0).tolist(), matrixOf3.max(axis=1).tolist(), matrixOf3.flatten().max()]
        min1 = [matrixOf3.min(axis=0).tolist(), matrixOf3.min(axis=1).tolist(), matrixOf3.flatten().min()]
        sum1 = [matrixOf3.sum(axis=0).tolist(), matrixOf3.sum(axis=1).tolist(), matrixOf3.flatten().sum()]

        calculations = {
            "mean": mean,
            "variance": variance,
            "standard deviation": standard,
            "max": max1,
            "min": min1,
            "sum": sum1,
        }
        return calculations