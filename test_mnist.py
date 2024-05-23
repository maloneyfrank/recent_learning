from sklearn.datasets import fetch_openml
from network import Network
 
import numpy as np

mnist = fetch_openml('mnist_784')

print(f"Shape of mnist input data: {np.shape(mnist.data)}")
print(f"Shape of mnist target data: {np.shape(mnist.target)}")

mnist.data = mnist.data/255

#
def data_wrapper(data, target):
    training_cut = 50000
    validation_cut = 60000
    
    tr_d, va_d, te_d = ((data[:training_cut], target[:training_cut]),
                        (data[training_cut: validation_cut], target[training_cut:validation_cut]),
                        (data[validation_cut:], target[validation_cut:]))
    
    training_inputs = [np.reshape(x, (784,1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_data = zip(validation_inputs, va_d[1])
    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])
    return (list(training_data), list(validation_data), list(test_data))
      
      
def vectorized_result(j):
    """Return a 10-dimensional unit vector with a 1.0 in the jth
          position and zeroes elsewhere.  This is used to convert a digit
          (0...9) into a corresponding desired output from the neural
          network."""
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e


training_data, validation_data, test_data = data_wrapper(mnist.data.to_numpy(), mnist.target.to_numpy().astype(int) )

print(training_data[0])


net = Network([784,30,10])
net.SGD(training_data, 30, 10, 3, test_data=test_data)
