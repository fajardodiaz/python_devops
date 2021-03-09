thinkers = ['Plato','PlayDo','Gumby']
while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as e:
        print("We tried to pop too many thinkers")
        print(e)
        break