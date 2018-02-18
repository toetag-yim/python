import filecmp
results1 = filecmp.cmp('test1.txt', 'test2.txt') 
results2 = filecmp.cmp('test1.txt', 'test3.txt')
print(results1)
print(results2)

test1='hello world'
test2='hello country'

if test1 == test1:
    print('passed')
if test1 == test2:
    print('passed')
else:
   print('failed')
