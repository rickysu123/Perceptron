import parser
import numpy as np
import copy
import sys

    
''' calculates our predicted class for the row given in the parameters
    returns 1 or 0 as our guess

    parameters are the weights in np.array form, and the list of the line
        weights are in np.array form already for faster testing purposes
        
    The first elements of the line and the weights are
        the true class, and bias, respectively. When calculating our estimated
        class, we remove these elements from the matrix multiplication.
        
    When getting our estimate, we add the output of the matrix multiplcation
        to the bias that was initially removed. This sum is what we would get
        to determine our guess for the class
    '''
def get_sign(weights, line):
    bias = weights[0]           # keep track of bias
    # remove class from the line, and bias from weights when calculating
    bias += sum(np.array(line[1:])*weights[1:]) # vector multiplication
    return 1 if bias >= 0.0 else 0



''' trains the weights
    parameters are the training data in list form, learning rate,
        and number of times to run through training data
    returns the last weight vector '''
def train_weights(train_data, learning_rate, train_number):
    weight_length = len(train_data[0])
    weights = [0] * weight_length
    all_weights = []
    temp = copy.copy(weights)
    for time in range(train_number):  # loop for number of times to train
        for line in train_data: # [0.2, 0.4, ..., 1]
            true_class = line[0]
            array_weights = np.array(weights)
            estimated_class = get_sign(array_weights, line)   # guessed class
            difference = true_class - estimated_class  # diff btw true and guess
            if difference == 0:     # if guessed correctly, move on; no change
                continue
            weights[0] = weights[0] + learning_rate*difference  # change bias
            for i in range(len(weights)-1):
                weights[i+1] = weights[i+1] + learning_rate*difference*line[i+1]
            # weights[1:] = list(array_weights[1:] + learning_rate*difference*np.array(line[1:]))
        #print "difference in weights"
        #print sum(np.array(weights)-np.array(temp))
        temp = copy.copy(weights)
        all_weights.append(temp)
    return weights



''' Perceptron Algorithm.
    parameters are the dataset to test, and the weights
    returns the accuracy '''
def perceptron(test_data, weights):
    right = 0
    wrong = 0
    weights = np.array(weights)
    for line in test_data:
        true_class = line[0]
        estimated_class = get_sign(weights, line)
        if estimated_class == true_class:
            right += 1
        else:
            wrong += 1
    accuracy = float(right)/float((right+wrong))
    return accuracy


''' generates the accuracies based on up to 6 loops of training, with
        learning rates varying from -0.4 to 0.4 with steps of 0.01
    returns a dictionary of accuracies, with keys as the training loop,
        and values as a list of accuracies with different learning rates based
        on position
    sample output with learning rates of -0.4 to 0.4 with steps of 0.01
        and one loop through training data:
        1 [0.233125, 0.233125, 0.233125, 0.233125, 0.233125, 0.233125,
        0.233125, 0.233125, 0.233125, 0.233125, 0.233125, 0.233125, 0.233125,
        0.233125, 0.233125, 0.233125, 0.233125, 0.233125, 0.233125, 0.233125,
        0.233125, 0.233125, 0.233125, 0.233125, 0.233125, 0.233125, 0.233125,
        0.233125, 0.233125, 0.233125, 0.233125, 0.233125, 0.233125, 0.233125,
        0.233125, 0.233125, 0.233125, 0.233125, 0.233125, 0.233125, 0.791,
        0.791, 0.791, 0.791, 0.791, 0.757, 0.785625, 0.821, 0.78975, 0.772,
        0.807875, 0.74575, 0.7915, 0.812125, 0.800125, 0.749125, 0.826,
        0.816625, 0.8095, 0.78325, 0.77175, 0.778, 0.8145, 0.69775, 0.79875,
        0.814125, 0.808, 0.793125, 0.7185, 0.806, 0.731625, 0.786375, 0.796625,
        0.805125, 0.806625, 0.802, 0.8075, 0.805875, 0.789375, 0.80775, 0.733]
        '''
        
def get_plot():
    lrs = np.arange(-0.4, 0.41, 0.01)
    train_num = 7

    accs = {}  # holds key(training number) to
                    # value(list of accuacies based on learning rate)

    lrs = np.arange(-0.4, 0.41, 0.01)

    for train_loop in range(1, train_num):
        temp = []
        for lr in lrs:
            weights = train_weights(train_data, lr, train_loop)
            acc = perceptron(dev_data, weights)
            temp.append(copy.copy(acc))
        accs[train_loop] = temp
    return accs



''' main program
    parameters are the learning rate,
        and the number of times to train the data
    '''
def main():#test_data, learning_rate, train_num):
        # load datasets
    file_train = "a7a.train"
    file_test = sys.argv[1]
    # file_test = "a7a.dev"

    # parse datasets
    train_data = parser.parse(file_train)
    test_data = parser.parse(file_test)

    # get weight array
    
    learning_rate = 0.31
    train_num = 6

    print "Training..."
    weights = train_weights(train_data, learning_rate, train_num)
    
    print "Weights are trained " + str(train_num) + " times, with a learning rate of " \
          + str(learning_rate)
    print "Testing..."
    print "Tested on " + str(file_test) + ", accuracy is " + \
          str(perceptron(test_data, weights)*100) + "%"


if __name__ == '__main__':
    main()
