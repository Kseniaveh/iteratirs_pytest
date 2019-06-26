from itertools import islice
class fib:
  """
    Данный класс одновременно является итерируемым объектом (поскольку реализует метод __iter__()) 
     и итератором (поскольку реализует метод __next__())
  """
  def __init__(self):
    self.elem = 0
    self.numb = 1
 
  def __iter__(self):
    """
    Метод __iter__ возвращает экземпляр класса, 
    реализующего протокол итераторов.
    Получаем текущее состояние объекта на каждой итерации
    """
    return self
 
  def __next__(self):
    """
    Метод __next__ возвращает 
    следующий по порядку элемент итератора
    """
    value = self.numb
    self.numb += self.elem
    self.elem = value
    return value


def ryadFibIterators(start,end):
    f = fib() # создаем объект, в котором описываем правила для задачи
    return list(islice(f, start, end))

print(ryadFibIterators(0,4))
