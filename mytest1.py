import fibonachi as fib
import fibonachiIterators as fibIter

def test_ryadFib1():
    assert fib.ryadFib1(4)==[0, 1, 1, 2]
    assert len(fib.ryadFib1(4))==4    
    
def test_ryadFib2():
    assert fib.ryadFib2(4)==[0, 1, 1, 2]
    assert len(fib.ryadFib2(5))==5
    
def test_ryadFibIterators():
    assert fibIter.ryadFibIterators(0,4)==[1, 1, 2, 3]
    assert len(fibIter.ryadFibIterators(0,4))==4
    
