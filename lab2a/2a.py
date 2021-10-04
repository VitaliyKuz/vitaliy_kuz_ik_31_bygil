
print("First constant", False)
print("Second constant", __debug__)
print("Third constant", None)
print(10, f"є рівним {bin(10)}")
print(10, f"є рівним {hex(10)}")
x = "Password"
print(x, f"є рівним {len(x)}")

print("y" if 34 / 2 == 17 else "n")
for i in range(0, 10):
    print(i)
if 54 + 2 == 56:
    print("It`s 56")
else:
    print("how")
x = "Hello"
try:
    print("Що буде якщо", 4.3 + x, "?")
except Exception as e:
    print(e)
finally:
    print("Wow")
with open('2aa.txt', 'r+') as f:
    f.write('Hello')
    for line in f:
        print(list(line))
str_fun = lambda a, b: f' if {a} i will {b}'
print(str_fun('it rains', 'stay at home'))
print("я розумiю лямбди як функції в один рядок ")
