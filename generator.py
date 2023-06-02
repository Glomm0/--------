import random

con = "|"
start = "("
end = ")"


def getSign():
    return random.randint(0, 1)

def addCon(formula, n):
    var = ["x" + str(i) for i in range(1, n+1)]
    var1 = ["-x" + str(i) for i in range(1, n+1)]
    var.extend(var1)
    func = formula + ","
    freq = dict.fromkeys(var, 0)
    cons = formula.replace(",", " ").replace("(", " ").replace(")", " ").split(" ")

    for c in cons:
        if len(c) > 0:
            vars = c.split("|")
            for v in vars:
                freq.update([(v, freq.get(v) + 1)])
    
    func += start
        

    k = 0
    t = 0
    s = []
    for i in range(n*2):
        s.append(random.randint(1, 2*n * (n-1) * (n-2)))

    freq = sorted(freq.items(), key=lambda x:x[1])

    freq = dict(freq)

    t = list(freq.items())[0][1]

    v1 = list(freq.items())[0][0]

    func += v1 + "|"

    t += 1

    freq.update([(v1, t)])

    exclude = []
    
    ex1, ex2 = 0, 0

    

    ex1 = var.index(v1)

    if ex1 <= (n*2 - 1) / 2:
        ex2 = ex1 + n
    else:
        ex2 = ex1 - n
    

    exclude.append(var[ex1])
    exclude.append(var[ex2])

    

    e1 = s[k]
    e2 = s[k+1]
    k += 2

    t_temp = t + 2
    b = []

    for key in freq.keys():
        if key not in exclude and key not in exclude and freq.get(key) <= t:
            b.append(key)

    while len(b) == 0:
        t_temp += 1
        for key in freq.keys():
            if key not in exclude and key not in exclude and freq.get(key) <= t:
                b.append(key)

    v2 = b[e1 % len(b)]

    func += v2 + "|"

    ex1 = var.index(v2)

    if ex1 <= (n*2 - 1) / 2:
        ex2 = ex1 + n
    else:
        ex2 = ex1 - n
    

    exclude.append(var[ex1])
    exclude.append(var[ex2])

    
    t_temp = t + 2

    b = []

    for key in freq.keys():
        if key not in exclude and key not in exclude and freq.get(key) <= t:
            b.append(key)

    while len(b) == 0:
        t_temp += 1
        for key in freq.keys():
            if key not in exclude and key not in exclude and freq.get(key) <= t:
                b.append(key)

    v3 = b[e2 % len(b)]
    func += v3 + end


    return(func)


def generateKNF(n):
    var = ["x" + str(i) for i in range(1, n+1)]
    var1 = ["-x" + str(i) for i in range(1, n+1)]
    var.extend(var1)
    func = ""
    freq = dict.fromkeys(var, 0)


    for c in range(n):
        func += start
        

        k = 0
        t = 0
        s = []
        for i in range(n*2):
            s.append(random.randint(1, 2*n * (n-1) * (n-2)))

        freq = sorted(freq.items(), key=lambda x:x[1])

        freq = dict(freq)

        t = list(freq.items())[0][1]

        v1 = list(freq.items())[0][0]

        func += v1 + "|"

        t += 1

        freq.update([(v1, t)])

        exclude = []
        
        ex1, ex2 = 0, 0

        

        ex1 = var.index(v1)

        if ex1 <= (n*2 - 1) / 2:
            ex2 = ex1 + n
        else:
            ex2 = ex1 - n
        

        exclude.append(var[ex1])
        exclude.append(var[ex2])

        

        e1 = s[k]
        e2 = s[k+1]
        k += 2

        t_temp = t + 2
        b = []

        for key in freq.keys():
            if key not in exclude and key not in exclude and freq.get(key) <= t:
                b.append(key)

        while len(b) == 0:
            t_temp += 1
            for key in freq.keys():
                if key not in exclude and key not in exclude and freq.get(key) <= t:
                    b.append(key)

        v2 = b[e1 % len(b)]

        func += v2 + "|"

        ex1 = var.index(v2)

        if ex1 <= (n*2 - 1) / 2:
            ex2 = ex1 + n
        else:
            ex2 = ex1 - n
        

        exclude.append(var[ex1])
        exclude.append(var[ex2])

        
        t_temp = t + 2

        b = []

        for key in freq.keys():
            if key not in exclude and key not in exclude and freq.get(key) <= t:
                b.append(key)

        while len(b) == 0:
            t_temp += 1
            for key in freq.keys():
                if key not in exclude and key not in exclude and freq.get(key) <= t:
                    b.append(key)

        v3 = b[e2 % len(b)]
        func += v3 + end + ","


    return(func[:-1:])

    # for i in range(len(var)):
    #     pos = []
    #     ind = set()
    #     ind.add(i)
    #     if getSign():
    #         pos.append(var[i])
    #     else:
    #         pos.append("-" + var[i])

    #     for p in range(2):
    #         j = random.randint(0, n-1)
    #         while(j in ind):
    #             j = random.randint(0, n-1)

    #         ind.add(j)
    #         if getSign():
    #             pos.append(var[j])
    #         else:
    #             pos.append("-" + var[j])

    #     func += start + pos[0] + "|" + pos[1] + "|" + pos[2] + end + ","
    # return func[:-1:]
    

f = "(x1|x8|-x5),(x2|x9|x4),(x3|x7|-x9),(x4|-x3|-x5),(x5|-x1|x9),(x6|x3|x4),(x7|x2|-x4),(x8|x7|-x2),(x9|-x5|x8),(x10|x5|x7)"
addCon("(x1|x8|-x5),(x2|x9|x4),(x3|x7|-x9),(x4|-x3|-x5),(x5|-x1|x9),(x6|x3|x4),(x7|x2|-x4),(x8|x7|-x2),(x9|-x5|x8),(x10|x5|x7)", 10)
# generateKNF(5)