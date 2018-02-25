# 2.1
# Normal 1
numbers = range(10)
size = len(numbers)
evens = []

i = 0
while i<size:
    if i%2 == 0:
        evens.append(i)
    i += 1

print evens

# Advance 1
print [i for i in range(10) if i%2 == 0]

# Normal 2
i = 0
seq = ["one", "two", "three"]

for element in seq:
    seq[i] = "%d: %s" % (i,seq[i])
    i += 1

print seq

# Advance 2
seq = ["one", "two", "three"]
for i, element in enumerate(seq):
    seq[i] = "%d: %s" % (i, seq[i])

print seq

# Advance 2_2
def _treatment(pos, element):
    return "%d: %s" %(pos, element)

seq = ["one", "two", "three"]
print [_treatment(i,el) for i,el in enumerate(seq)]

#--------------------------------------------------#
print '-'*40
##

# Advance 3

i = iter('abc')

# print i.next()


# New iter
class MyIterator(object):
    def __init__(self, step):
        self.step = step

    def next(self):
        """Return the next element"""
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """Return the iterator itself"""
        return self


for el in MyIterator(4):
    print el

print '*'*20
## Advance 4
def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

fib = fibonacci()

for i in range(4):
    print fib.next()

print [fib.next() for i in range(4)]


## Advance 5
def power(values):
    for value in values:
        print "powering %s" % value
        yield value

def adder(values):
    for value in values:
        print "adding to %s" % value
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2

elements = [1, 4, 7, 9, 12, 19]

res = adder(power(elements))

for i in range(len(elements)):
    res.next()

def psychologist():
    print "Please tell me your problems"
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print "Don't ask yourself too much questions"
            elif "good" in answer:
                