# we know tuples are immutable but we can update

sports = ("football", "cricket", "badminton", "hockey", "hadudu")
print("Before update tuple:", sports)
# sports[0] = "kabadi"
# print(sports[0])    # hold an error, because we can't change it directly
print("--------------------------------")

# for updating tuples, first converted to a list
newSports = list(sports)    # converted to a list
print("converting to list:",newSports)
print("--------------------------------")

#now we can update a list
newSports[0] = "kabadi"
newSports[-1]= "chess"
print("After Update list:",newSports)
print("--------------------------------")

# list > tuple
sports = tuple(newSports)
print("After update tuple:", sports)
print("--------------------------------")

# Add, remove objects> operation on list
newSports.append("Race")
newSports.append("WWE")
newSports.remove("cricket")
newSports.remove("badminton")

# again update to get the updated values
sports = tuple(newSports)
print("Final tuple:", sports)