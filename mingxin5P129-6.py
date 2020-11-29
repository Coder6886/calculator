for a in range(1,11):
    for b in range(1,11):
        if b != a:
            for c in range(1,11):
                if c != b and c != a:
                    for d in range(1,11):
                        if d != c and d != b and d != a:
                            for e in range(1,11):
                                if e != d and e != c and e != b and e != a:
                                    for f in range(1,11):
                                        if f != e and f != d and f != c and f != b and f != a:
                                            for g in range(1,11):
                                                if g != f and g != e and g != d and g != c and g != b and g != a:
                                                    for h in range(1,11):
                                                        if h != g and h != f and h != e and h != d and h != c and h != b and h != a:
                                                            for i in range(1,11):
                                                                if i != h and i != g and i != f and i != e and i != d and i != c and i != b and i != a:
                                                                    for j in range(1,11):
                                                                        if j != i and j != h and j != g and j != f and j != e and j != d and j != c and j != b and j != a:
                                                                            if a + b == c + d and  c+d == e + f and  e + f == g + h and h + j + d == g + h and h + j +d  == f + i + b:
                                                                                print ("a:"+str(a) + " b:"+str(b)+" c:"+str(c)+" d:"+str(d)+" e:"+str(e)+" f:"+str(f)+" g:"+str(g)+" h:"+str(h)+" i:"+str(i)+" j:"+str(j) + " numadd:" + str(a+b))
