import numpy as np

def cm_to_dataset(C, random_seed=0):
    """
    It takes a confusion matrix C as numpy array and returns corresponding random binary y_true and y_pred.
    With C:  
    C{0, 0} = TN 
    C{1, 0} = FN
    c{1, 1} = TP
    c{0, 1} = FP
    
    :param C: confusion matrix as
    :param random_seed: 
    :return: y_true, y_pred
    """
    np.random.permutation(random_seed)
    n_tot = C.sum()
    permutation = np.random.permutation(n_tot)
    tn, fp, fn, tp  = C.ravel()
    labels = [0, 1]

    # generate y_true
    y_t = np.array([1]*tp +[1]*fn + [0]*tn +[0]*fp)
    y_p = np.array([1]*tp +[0]*fn + [0]*tn +[1]*fp)
    y_true = [y_t[i] for i in permutation]
    y_pred = [y_p[i] for i in permutation]
    return np.array(y_true), np.array(y_pred)