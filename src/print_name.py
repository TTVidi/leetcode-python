if __name__ == '__main__':
    ok = True
    while ok:
        name = input('please input your name : ')
        if len(name) >= 5:
            print("your name is too long!")
        else:
            print('hello ,', name)
            break
