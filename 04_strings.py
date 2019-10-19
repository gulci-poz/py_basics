poem = '''bla
bla
bla'''
print(poem)

place_name = "gulci's"

# starting at 0
print(place_name[0])
# last, indexing from the end starts at -1
print(place_name[-1])
# second to last
print(place_name[-2])
# including 0 indexed, excluding 3rd
print(place_name[0:3])
# to the end
print(place_name[0:])
print(place_name[1:])
# from the beginning excluding 3rd
print(place_name[:3])
# every second from all
print(place_name[::2])
# excluding the last one
print(place_name[:-1])
# every second from the last one
print(place_name[-1::-2])

# all and assign = clone
# 0:length is assumed
new_place = place_name[:]
# the same :step is optional
# new_place = place_name[::]
print(new_place)

# splitting and taking the last element of the list
print("johnny bravo".split()[-1])
