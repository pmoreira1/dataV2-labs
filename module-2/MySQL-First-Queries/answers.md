```
**1. What are the different genres?**
Games, Productivity, Weather, Shopping, Reference, Finance, Music, Utilities, Travel, Social Networking, Sports, Business, Health & Fitness, Entertainment, Photo & Video, Navigation, Education, Lifestyle
Food & Drink, News, Book, Medical, Catalogs

**2. Which is the genre with the most apps rated?**
Social Networking

**3. Which is the genre with most apps?**
Games

**4. Which is the one with least?**
Catalogs

**5. Find the top 10 apps most rated.**
Facebook, Instagram, Clash of Clans, Temple Run, Pandora - Music & Radio, Pinterest, Bible, Candy Crush Saga, Spotify Music, Angry Birds

**6. Find the top 10 apps best rated by users.**
Head Soccer, Plants vs. Zombies, Sniper 3D Assassin: Shoot to Kill Gun Game, Geometry Dash Lite, Infinity Blade, Geometry Dash, Domino\s Pizza USA, CSR Racing 2, Pictoword: Fun 2 Pics Guess What\s the Word Trivia, Plants vs. Zombies HD

**7. Take a look at the data you retrieved in question 5. Give some insights.**
All apps are free, but the rating never goes above 4.5. And the most rated app is actually quite low. 3.5 for Facebook.

**8. Take a look at the data you retrieved in question 6. Give some insights.**
The top 10 user_rating contains mostly games and some paid apps.

**9. Now compare the data from questions 5 and 6. What do you see?**
Most rated apps are not present in the top 10 for the best rated apps. Also free apps get more ratings than paid apps.

**10. How could you take the top 3 regarding both user ratings and number of votes?**
Creating a weigthing system. For example using the time an app has been on the app store.

**11. Do people care about the price of an app?** Do some queries, comment why are you doing them and the results you retrieve. What is your conclusion?

Free Apps have more ratings (so probably more downloads as well) - Queries 11a and 11b
Free Apps - 80105208 ratings;
Paid Apps - 12685045 ratings.

Paid Apps have a higher user rating average - Queries 11c and 11d
Free Apps - 3.37;
Paid Apps - 3.7.

The number of Ratings decreases everytime the price goes up - Query 11f. E.G:
```

| price | number_of_apps | rating_count_avg | user_rating_avg |
| ----- | -------------- | ---------------- | --------------- |
| 0     | 4056           | 19750            | 3.4             |
| 0.99  | 728            | 7146             | 3.5             |
| 1.99  | 621            | 3812             | 3.7             |
| 11.99 | 6              | 179              | 2.2             |
| 12.99 | 5              | 278              | 0.9             |

In short I think people care about the price of the apps. Free apps have more ratings (probably more downloads as well) than paid apps. The rating is also higher on the paid apps, which probably means that before paying for and app people actually check if the app meets their needs.

