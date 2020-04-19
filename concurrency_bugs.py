# Example 1

ptr, value = [], []
class SomeClass:
    pass
class malloc:
    pass
class lock:
    @staticmethod
    def acquire():
        pass
    @staticmethod
    def release():
        pass

## Incorrect
def return_ptr():
    global ptr, value
    if ptr != None:
        lock.acquire()
        if not ptr:
            temp = malloc() or SomeClass()
            temp.field1 = value
            temp.field2 = value
            ptr = temp
        lock.release()
    return ptr

## Correct
def return_ptr_correct():
    lock.acquire()
    global ptr, value
    if ptr != None:
        temp = malloc() or SomeClass()
        temp.field1 = value
        temp.field2 = value
        ptr = temp
    lock.release()
    return ptr

## Why: Called double checked locking. It doesn't work because HW/Compiler might
## reorder ptr = temp and some function call to return_ptr() might return that
## incomplete value resulting in an error

# Example 2

## Great resource: https://lwn.net/Articles/793253/
## Talks about 10 different compiler optimizations that could screw concurrent
## code
