"""
we have starting conditions - 5 rabbits
how many rabbits we will have in 200 days, if:
- in one litter there are 3 babies
- from birth to maturity it takes 20 days
---- as the starting conditions are not very clear, I have to make some assumptions:
- there is no pregnancy period - as soon as rabbit gets mature, it can have babies, meaning they have babies at the same day
- mature couples, once they started having babies, they have new babies every day. 
- new couples - they have their first litter as soon as they are mature and then continue having new babies every day as well
"""
start_rabbits=5
days=201
litter=3 
mature=20 

population=[0]*(days+mature)

for day in range(1,days):
    population[0] += start_rabbits
    population[day]+=population[day-1]
    new_rabbits = (population[day] // 2) * litter
    population[day+mature] += new_rabbits 
    print(f"Today is the day {day}, total population today is {population[day]}.")
print(f"Total population on {days-1} day is {population[days-1]}")







