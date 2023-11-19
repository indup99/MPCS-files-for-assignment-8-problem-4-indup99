# Indumathi Prakash

import stats
import random_numbers

"""calling the stats module and hardcoding 100 random numbers"""

def main():
    num_lst = random_numbers.generate(100,True)
    #printing all the results
    print(f"mean: {stats.mean(num_lst)}")
    print(f"median: {stats.median(num_lst)}")
    print(f"mode: {stats.mode(num_lst)}")
    print(f"variance: {stats.variance(num_lst)}")
    print(f"standard deviation: {stats.standard_deviation(num_lst)}")

if __name__ == "__main__":
    main()