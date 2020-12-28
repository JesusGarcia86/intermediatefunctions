import random

def randint(min=0, max=100):
  num = random.random() * (max-min) + min
  return round(num)

print(randint())
print(randint(max=50))
print(randint(min=50))
print(randint(min=50, max=500))

