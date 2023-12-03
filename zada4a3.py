WorkDays = int(input())
Mb = float(input())
money = 0

for i in range(1, WorkDays + 1):
    if i % 2 == 0:
        zaplata = 100
        money += zaplata
    else:
        zaplata = 150
        money += zaplata
    if i % 5 == 0:
        if i % 2 == 0:
            zaplata = 0.2 * 100
            money += zaplata
        else:
            zaplata = 0.2 * 150
            money += zaplata
    money -= 10

if money >= Mb:
    money_left = money - Mb
    print(f"Yes, I finally bought my dream bike, and I had money {money_left} leva left")
elif money < Mb:
    needed_money = Mb - money 
    print(f"I did not manage to buy my dream bike, I need {needed_money} leva more")

