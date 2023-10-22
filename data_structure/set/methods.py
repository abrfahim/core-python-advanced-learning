
name= {"abrar", "sonet", "rakib", "santo"}
print("primary set:", name)
# add
name.add("yahiya")
print("After add:",name)

# remove
name.remove("abrar")
print("After remove:",name)

# discard - same as remove
name.discard("santo")
print("After discard:",name)

# we can add mutable properties to the set, but we don't add immutable
# so tuple can be added,but list can't be added

