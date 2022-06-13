n = 50
def frontback(n):
    for i in range(1,n+1):
        if i % 15 == 0:
            print("Frontend Backend")
            continue
        elif i % 3 == 0:
            print("Frontend")
            continue
        elif i % 5 == 0:
            print("Backend")
            continue
        # print(fizzbuzz)
        return n 