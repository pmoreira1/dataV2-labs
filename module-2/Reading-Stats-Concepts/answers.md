### Challenge 1: What is the difference between expected value and mean?

The expected value can be thought of as the Hypotheses of some action and the mean is the actual outcome. 

In a well balanced experiment and after n tries the outcome will get closer and closer be the expected value. 

For example drawing a dice there is always a chance of 1/6 for each value.

So the the expected value will be: 

(1×(1÷6))+(2×(1÷6))+(3×(1÷6))+(4×(1÷6))+(5×(1÷6))+(6×(1÷6)) = 3.5


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

### Challenge 2: What is the "problem" in science with p-values?

This article helped me a lot: https://towardsdatascience.com/a-case-study-of-the-p-value-f0d708861334

Recall that the correct interpretation of a p-value is

> **Assuming that your null is true, a p-value quantifies the probability of seeing a data point at or beyond your current observation**.

Basically, you calculate a 95% confidence interval of where you expect your data to be.

This is the "problem" with the p-value, there is a 5% interval where your data is not 'valid' but this can be 'easily' changed by doing studies with higher confidence levels and of course lower p-values. 

This will generate more meaningful results and less chance to the "'no difference’ between two groups because the difference was ‘statistically non-significant’"

### Challenge 3: Applying testing to a specific case: A/B testing.

After reading the articles I have to say... I wouldn't change anything. I know that it's a bit vague but all the information in the articles justifies the decisions taken, event the basecamp.com article.

I this case I don't think there would be a way to predict the impact of not having the sign in form in the main page only after doing they actually found the mistake. Of course the time it took to fix the error is a completely different subject which could've been done faster, but there always room for improvement, no matter what.

