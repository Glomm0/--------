import random

con = "|"
start = "("
end = ")"


def getSign():
    return random.randint(0, 1)


def generateKNF(n):
    var = ["x" + str(i) for i in range(1, n+1)]
    func = ""
    for i in range(len(var)):
        pos = []
        ind = set()
        ind.add(i)
        if getSign():
            pos.append(var[i])
        else:
            pos.append("-" + var[i])

        for p in range(2):
            j = random.randint(0, n-1)
            while(j in ind):
                j = random.randint(0, n-1)

            ind.add(j)
            if getSign():
                pos.append(var[j])
            else:
                pos.append("-" + var[j])

        func += start + pos[0] + "|" + pos[1] + "|" + pos[2] + end + ","
    return func[:-1:]

    