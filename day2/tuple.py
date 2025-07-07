tuple_of_days = ("mon","tues","wed","thurs","fri")
list_of_days = ["mon","tues","wed","thurs","fri"]
#print(tuple_of_days[2])
#print(list_of_days[2])

list_of_days[2] = "wednesday"
print(list_of_days)
# tuple_of_days[2] = "wednesday" -----> tuples are immutable we can't change their values as they store values in a hash so it can't be
# changed plus their size is less as compared to list