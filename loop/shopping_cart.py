# condition- we should buy serially in our budget
items_price =[10,20,30,50,100,500,1000,2000,5000]
budget = 500
count = 0
for custom_price in items_price:
    budget = budget - custom_price
    if(budget<0):
        break
    count = count+1
    print(count)
print("Total items bought:", count)
