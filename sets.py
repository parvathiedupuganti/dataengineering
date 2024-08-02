lucky_draws = set()
print(type(lucky_draws),lucky_draws)

lucky_draws_o = {14,18,35,37,67,55,40,18,37}
lucky_draws_s = {11,18,35,36,66,55,43}
lucky_draws_s.add(4)
lucky_draws_s.discard(43)

print("online draws", lucky_draws_o,len(lucky_draws_o))
print("shop draws",lucky_draws_s)
"""
for draw in lucky_draws_o:
    print(draw)
"""

print("union ",lucky_draws_o | lucky_draws_s)
print("intersect", lucky_draws_o & lucky_draws_s)
print("differenct between online - shopping", lucky_draws_o - lucky_draws_s)
print("differenct between shopping - online", lucky_draws_s - lucky_draws_o)

set1 = {1,3,5}
set2 = {5,1,3}
print(set1==set2) # returns true irrespective of its position in the set if both sets are having common values




