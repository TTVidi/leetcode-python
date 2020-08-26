if __name__ == '__main__':
    file = "C://Users//tangtao02//Desktop//算法/1/1.txt"
    case = "C://Users//tangtao02//Desktop//算法/1/case.txt"
    result = "C://Users//tangtao02//Desktop//算法/1/result.txt"
    fp = open(file)
    c = open(case, 'w+')
    r = open(result, 'w+')

    cr = []
    rr = []
    s = fp.readlines()
    idx = 0
    for i in s:
        idx += 1
        if idx % 3 == 1:
            cr.append(i)
        elif idx % 3 == 2:
            rr.append(i)

    c.writelines(cr)
    r.writelines(rr)
    c.close()
    r.close()
    fp.close()
