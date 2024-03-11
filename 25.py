
def get_divisors(n):
  divisors = []
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n // i)
  return sorted(divisors)


number = 124521450
divisors = get_divisors(number)
print("Делители числа", number, ":", divisors)
