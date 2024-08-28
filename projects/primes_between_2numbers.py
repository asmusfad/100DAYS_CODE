class Primes:
  start = 0
  end = 0
  primes = []

  def __init__(self, a, b):
      self.start = a
      self.end = b

  def getprimes(self):
      for i in range(self.start, self.end):
          for j in range(2, i):
              if i % j == 0:
                  break
          else:
              self.primes.append(i)

      return self.primes

p = Primes(2,50)
print(p.getprimes())