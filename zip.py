letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]

# We use the below syntex of the builtin function "zip"
new_list = (list(zip(letters, numbers)))
print(new_list)

# We can also unzip a list of tupels using the sintex below.
let, num = zip(*new_list)
print(let)
print(num)

#zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables. For example, printing
for letter, number in zip(letters, numbers):
    print("{}:{}".format(letter, number))
