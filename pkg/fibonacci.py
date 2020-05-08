class Fibonacci:
  def __init__(self, title="fibonacci"): 
  #title="fibonacci" 타이틀로 다른게 들어오면 다른걸 쓰고 타이틀이 안넘어오면 피보나치를 타이틀에 넣어라
    self.title = title

  def fib(n):
    a, b = 0, 1
    while a < n:
      print(a, end=' ')
      a, b = b, a+b
    print()

  def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
      result.append(a)
      a, b = b, a+b
    return result

