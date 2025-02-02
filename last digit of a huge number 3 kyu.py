def last_digit(lst):
    if len(lst) == 0:
        return 1

    elif int(str(lst[0])[-1]) == 1:
        return 1

    res = int(str(lst[-1])[-2:])  # last 2 digits

    for x in range(len(lst) - 1):

        if int(str(lst[-2 - x])[-1]) == 0:
            res = 0 if res != 0 else 1

        if int(str(lst[-2 - x])[-1]) == 1:
            if len(str(lst[-2 - x])) < 2:
                res = 1
            else:
                if int(str(lst[-1 - x])[-2:]) % 4 == 1:
                    res = 21
                else:
                    res = 11

        if int(str(lst[-2 - x])[-1]) == 4:
            res = 4 if int(str(lst[-1 - x])[-1]) % 2 == 1 else 16

        elif int(str(lst[-2 - x])[-1]) == 9:
            res = 9 if int(str(lst[-1 - x])[-1]) % 2 == 1 else 1


        elif int(str(lst[-2 - x])[-1]) == 5:
            res = 25 if int(str(lst[-1 - x])[-2:]) % 2 == 0 else 5

        elif int(str(lst[-2 - x])[-1]) == 6:
            res = 6 if int(str(lst[-1 - x])[-2:]) % 4 == 2 else 36


        elif int(str(lst[-2 - x])[-1]) == 2:
            if lst[-1 - x] == 0:
                res = 1
            else:
                m = res % 4 if 0 < res < 4 else res % 4 + 4
                res = 2 ** m

        elif int(str(lst[-2 - x])[-1]) == 8:
            if lst[-1 - x] == 0:
                res = 1
            else:
                m = res % 4 if 0 < res < 4 else res % 4 + 4
                res = 8 ** m


        elif int(str(lst[-2 - x])[-1]) == 3:
            if lst[-1 - x] == 0:
                res = 1
            else:
                m = res % 4 if 0 < res < 4 else res % 4 + 4
                res = 3 ** m

        elif int(str(lst[-2 - x])[-1]) == 7:
            if lst[-1 - x] == 0:
                res = 1
            else:
                m = res % 4 if 0 < res < 4 else res % 4 + 4
                res = 7 ** m

    return int(str(res)[-1])