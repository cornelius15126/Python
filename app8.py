try:
    x = int(input('enter an integer: '))
    print(x)
except:
    print('something went wrong')
else:
    print('nothing went wrong')
finally:
    print('try except finish')