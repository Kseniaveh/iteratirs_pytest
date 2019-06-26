def fib1(el):
  """Вычисление ряда чисел Фибоначчи рекурсией. 
      Вызов функции самой себя
  """
  if el > 1:
    return fib1(el-1) + fib1(el-2)
  return el

def ryadFib1(value):
    list=[]
    for i in range(value):
        list.append(fib1(i))
    return list

def fib2():
    """
    Итератор - генератор
    """
    a, b = 0, 1
    while True:            # Первая итерация
      yield a              # yield 0 => начинаем с нуля
      a, b = b, a + b      # a теперь = 1, b будет также 1, (0 + 1)
      
def ryadFib2(value):
    list=[]
    for index, fib_num in zip(range(value), fib2()):
        list.append(fib_num)        
    return list    
