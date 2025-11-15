exp1 = 5 > 10 # false exp
exp2 = 5 < 10 # true exp

# and - If Both True
print("and case: ", exp1 and exp2)

# or - If Anyone True
print("or case: ", exp1 or exp2)

# not - Reverses the result
# Returns False if result is True and vice-versa

print("not exp1 case: ", not exp1) # Gives True
print("not exp2 case: ", not exp2) # Gives False

print("not exp1 case: ", not (exp1)) # Gives True
print("not exp2 case: ", not (exp2)) # Gives False