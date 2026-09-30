count = 1
total = 0

# BUG: Added missing colon ':' to fix SyntaxError, and changed '<' to '<=' so 5 is included in the loop total.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Converted integer 'total' to string using str(total) to fix TypeError when concatenating with text.
print("Sum of 1 to 5 is: " + str(total))
