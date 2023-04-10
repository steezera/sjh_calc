# get two integer parameters
# return sum
def plus(x, y):
    return x+y
def gob(x, y):
    return x*y
def na(x, y):
    return x/y
# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: start")
        check = int(input())
        if check == 1:
            print("First Number")
            x = int(input())
            print("Second Number")
            y = int(input())
            z = int(input("더하기 : 1번\n곱셈 : 2번\n나누기 : 3번 "))
            if z == 1:
                print("answer : ", plus(x,y))
            if z == 2:
                print("answer : ", gob(x,y))
            if z == 3:
                print("answer : ", na(x,y))
        elif check > 1:
            print("Unsupported")
        else:
            print("Thank you")

if __name__ == "__main__":
    main()
