### Challenge 1: What is the difference between expected value and mean?

The expected value can be thought of as the Hypotheses of some action and the mean is the actual outcome. 

In a well balanced experiment and after n tries the outcome will get closer and closer be the expected value. 

For example drawing a dice there is always a chance of 1/6 for each value.

So the the expected value will be: 
$$
(1×(1÷6))+(2×(1÷6))+(3×(1÷6))+(4×(1÷6))+(5×(1÷6))+(6×(1÷6)) = 3.5
$$


Using the code from the previous exercise we can easily create a simulation:

```
def mean_dice_roll(n):
    return pd.DataFrame([randint(1,6) for i in range(n)]).mean()
```

mean for 10 throws = 3.7
mean for 100 throws = 3.58
mean for 1000 throws = 3.516
mean for 10000 throws = 3.513
mean for 100000 throws = 3.50652

As we can see the average is getting closer and closer to the expected value of 3.5