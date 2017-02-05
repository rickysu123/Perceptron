import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    df = pd.read_csv("accuracies.csv", header=None)
    one = df.iloc[0]
    two = df.iloc[1]
    three = df.iloc[2]
    four = df.iloc[3]
    five = df.iloc[4]
    six = df.iloc[5]
    
    x = np.arange(-0.4, 0.41, 0.01)
    
    plt.plot(x, one)
    plt.plot(x, two)
    plt.plot(x, three)
    plt.plot(x, four)
    plt.plot(x, five)
    plt.plot(x, six)

    plt.legend(['1 loop', '2 loops', '3 loops', '4 loops', '5 loops', '6 loops']
               , loc='upper left')
    plt.xlabel("Learning Rate")
    plt.ylabel("Accuracy")

    plt.title("Accuracy vs. Learning Rate by Training Loops")
    plt.show()



    # limited axes for better viewing
    plt.plot(x, one)
    plt.plot(x, two)
    plt.plot(x, three)
    plt.plot(x, four)
    plt.plot(x, five)
    plt.plot(x, six)

    plt.axis((-0.1,0.41,0.68,0.84))

    plt.legend(['1 loop', '2 loops', '3 loops', '4 loops', '5 loops', '6 loops']
               , loc='upper left')
    
    plt.xlabel("Learning Rate")
    plt.ylabel("Accuracy")

    plt.title("Accuracy vs. Learning Rate by Training Loops")

    plt.show()
    
main()
