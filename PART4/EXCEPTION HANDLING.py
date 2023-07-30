b=0

try:
    a=30/b
    print(a)
    print("try completed")
except ZeroDivisionError:
    print("can't divided by 0")

print("program finished")

