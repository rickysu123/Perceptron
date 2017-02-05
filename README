Ricky Su
rsu4@u.rochester.edu
CSC446
Homework 2

Implement perceptron for the adult income dataset using Python. Data available in /u/cs246/data/adult. Experiment with performance as a function of learning rate.

************ Files *********
parse.py => parses the data files to create vectors of 0’s and 1’s. Since the longest vector in the datasets is 123, I make vectors of length 123 for each line in the data file given as the parameter. This is used to parse the train, dev, and test datasets. Each line will be transformed into something that looks like: [0, 0, 1, …, 0, 1, 0, 0], with a length of 123. The true class of each vector is converted. Classes of -1 are encoded as 0, and classes of +1 are encoded as 1. This number is added to the beginning of the vector, to make all vectors a length of 124. This is because we can easily remove it when multiplying by the weight vectors, since x_0 is 1 anyways, and w_0 (the bias) can be removed to change.

Perceptron.py => file that contains the algorithm. There are five functions here: train_weights(), get_sign(), perceptron(), get_plot() and main(). The function train_weights() is basically the algorithm. The perceptron() function calls train_weights() and finds the accuracy based on the testing file that is given. I use the dev set here to clean up the training set. Function get_sign() returns 0 or 1 based on the estimated class. main() puts it all together. I kept the best accuracy that I found on the dev set as the default, which was 6 training loops with a learning rate of 0.31. The get_plot() function was for me to test accuracies based on different training loops and learning rates. As this function will take a long time to run, I kept the accuracies, which is in the file accuracies.csv.

plot.py => uses matplotlib to plot the many different accuracies that I experimented with. There are 2 plots. The first shows all the different combinations, while the second plot zooms into the part where the accuracies start differing more.

accuracies.csv => a csv file that contains a bunch of different accuracies achieved. There are 6 rows here, depicting the number of training loops. Each element in a list depicts the learning rate used, starting from -0.4 to 0.4 in steps of 0.01. Therefore, each list should be a length of 81. I use these numbers to make a plot to show the changing of accuracies. 

first.png => first plot of the accuracies

second.png -> second plot of the accuracies 


************ Algorithm *****
We start in Perceptron.py. Looking through the datasets, I found that the longest vector will be of length 123, as stated above in parse.py. 

In train_weights() I begin with a weight vector of size 123 of all 0’s (line 34), then inserting another 0, the bias, into the beginning of the vector, now of length 124. I then create a list called all_weights to keep track of the weights throughout each run through of the training set. The temp variable was used to track the amount of difference between the old weights and the new weights, but I realized that this doesn’t really matter since it doesn’t directly affect the accuracy in the end. I just kept it for convenience anyways. You can see that the print statements used to check the differences are commented out (lines 49 & 50).
 
So when running through the training data, I keep track of the true class (line 39), and then calculate the estimated class by calling the function get_sign(). This just uses numpy to do vector multiplication between the weights and the current vector datapoint. This returns our estimated class, whether it is 0 if < 0.0, or 1 if >= 0.0. Back to the train_weights() function now, we find the difference between the true and estimated class. If guessed correctly, there will be a 0 difference, and hence, we can continue onto the next iteration without update (lines 43 & 44). Otherwise, update the weights. This works by updating the bias (w_0) first, since all the information is just in the learning rate and the difference. And then looping through the rest of the weight vector, we update against the line. Here, we could have used numpy’s vector multiplication, but I think it’s more readable with the for loop. Either one works. The numpy line to do this is commented out (line 48). Appending each new weight vector to all_weights, we can keep track of the different weight vectors for testing for accuracies later. However, for this project’s convenience, I return the weight vector from the last run through of the training set.

Now that we have the weights, function perceptron() will test the weights against whatever test data is given in the parameters. I used the dev set for all testing. It loops through the dev set, and records sensitivity and specificity for the accuracy, and then returns it.

The main() function takes as parameters: the test file, the learning rate, and the number of times to train the weight vector. The function parses the training data, runs train_weights() to train and get the weights, runs perceptron() for the accuracy, and prints the accuracy to the console.

At the bottom of the Perceptron.py file, you can see that the files are loaded and parsed here, then the main() is called.
************ Instructions ***

Place all datasets in the same directory as the given files.

To run the program, just run the Perceptron.py file. At the bottom of the file, there is a print statement using the main function, which prints the accuracy output from the main function. The first parameter is the test file you would like to use. I left it as the dev_data. Second parameter is learning rate, and the third parameter is the number of times to loop through the training set to train the weights. You can change the parameters around to see different accuracies!

To see the plots be generated, run the plot.py program. However, I tried running this on the cycle machine, but I don’t think it has matplotlib installed, or one of the modules that I use, which is either pandas, numpy, or matplotlib. So I included the plots anyways just in case!

************ Results *******
I tried a large number of learning rates as well as the number of times to train the data. For the learning rates, I went from -0.4 to 0.4 by steps of 0.01, along with training the weights up to 6 times. This was done with a double nested for loop. I had tried different biases besides 0, but they all immediately were worse, so I did not include changing the bias. I found that changing the bias to anything besides 0 negatively affected the accuracy. I kept a dictionary mapping the learning rate and training number, to the accuracy. All testing was done on the dev set. 

The highest accuracy that I achieved was 82.975%, using a bias of 0, 0.31 learning rate, and 6 loops of training. This setup is left in the program, but it can be changed from the call to the main() function. Plots are included for the different accuracies achieved.

************ Your interpretation **** (Attention: important!)

Your understanding of the results, for instance, "from the above results, learning rate is very important that a learning rate from XX to XX yields the best result, and that a learning rate larger than XX yields a significant drop of the performance"

As we can see from the plots shown, the results vary differently based on many attributes of the algorithm, specifically when training the weights. Many factors like the bias, the learning rate, and how many times you train the weights matter. When changing the bias away from my default of 0, I found that the accuracies decrease and get worse. Thus, I kept the bias as 0. 

The number of times that the weights were trained on the training set also changed the accuracies. Doing this, as we said in class, the accuracy fluctuates around a certain interval, and since the data in the training set aren’t linearly separable, the algorithm will never converge. Hence, we have to eventually stop at some point otherwise we will overfit the weights to our training data, losing accuracy on test sets.

The idea of perceptron is very closely related to regressions, in the idea that it finds a line that will try to accurately estimate a future class value. I experimented mostly with changing the learning rate, which changed the accuracies . I found that positive learning rates have better accuracies as compared to negative learning rates. I’m not too sure why this would happen, but the best accuracy that I found was inherently positive. 

************ References ************
http://aass.oru.se/~lilien/ml/seminars/2007_02_01b-Janecek-Perceptron.pdf
http://web.engr.oregonstate.edu/~xfern/classes/cs534/notes/perceptron-4-11.pdf