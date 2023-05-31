#python3

def parallel_processing(n, m, data):
    output = []
    time = [0]*n
    #inicializejam laika sarakstu ar tik daudz nullem cik thread count

    for i in range(m): # iterējam i+1 lidz vienads ar job count
        thread = time.index(min(time)) # paņemam vismazāko laika elementu no laika saraksta
        counter = time[thread] # inicializejam start vertibu nemot laika saraksta atrasto mazako elementu
        time[thread] += int(data[i]) # pievienojam pie veca laika saraksta mazaka elementa
        output.append((thread, counter))
        # vienkarsi pievienojam tuple output sarakstam izvadei

    return output
    # izvadam output

def main():
    # n,m = map(int, input().split())
    text = input().split()
    # n = thread count
    # m = job count
    n=text[0]
    m=text[1]
    # data = list(map(int, input().split()))
    data = input().split()

    result = parallel_processing(int(n),int(m),data)

    for thread, counter in result:
        print(thread, counter)



if __name__ == "__main__":
    main()