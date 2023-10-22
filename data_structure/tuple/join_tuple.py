sports = ("football", "cricket", "badminton", "hockey", "hadudu")
player = ("Ronaldo", "Messing","Milar", "khabi","Arnold")

merge = sports + player
print(merge)
print("--------------------------------")

# how to sort a tuple
odd = (1,3,5,7,9)
even = (2,4,6,8,10)
num = odd + even

# tuple>list
convert = list(num)
convert.sort(reverse=True)

#list>tuple
num = tuple(convert)
print(num)
