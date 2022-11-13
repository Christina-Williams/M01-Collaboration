
#7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
things= ['mozzarella', 'cinderella','salmonella' ]
#7.5 Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
things[1] = 'Cinderella'
print("After capitlizing cinderella:", things)
#7.6 Make the cheesy element of things all uppercase and then print the list.
things[0] = 'MOZZARELLA'
print("After capitlizing mozzarella:", things)
#7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.
del things[2]
print("After deleting the item :", things)
#9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].
def good(Harry , Ron, Hermione):
    return {'Harry': Harry, 'Ron': Ron, 'Hermione': Hermione}
print(good)
#9.2 Define a generator function called get_odds() that returns the odd numbers from range(10). Use a for loop to find and print the third value returned.

def get_odds(numbers, odds):
    if len(numbers) == 0:
        return
    v = numbers.pop()
    if v % 2 == 1:
        odds.append(v)
    get_odds(numbers, odds)
odds = []
numbers = [1,2,3,4,5,6,7,8,9,10]
get_odds(numbers,odds)
print (odds)
