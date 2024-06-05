def calcuatePos(grid, x, y, xp=None, yp=None, xn=None, yn=None, amt=8):
    posLis = []

    try:
        for ind in range(amt + 1):
            # bishop movement conditions
            if xp and yp:
                posLis.append(grid[y + ind][x + ind])
            if xp and yn:
                # check if the index is negative cause it will go to the opposite side of the board
                if y - ind < 0:
                    raise IndexError
                posLis.append(grid[y - ind][x + ind])
            if xn and yp:
                if x - ind < 0:
                    raise IndexError
                posLis.append(grid[y + ind][x - ind])
            if xn and yn:
                if y - ind < 0 or x - ind < 0:
                    raise IndexError
                posLis.append(grid[y - ind][x - ind])
            # rook movement conditions
            if xp and xn is None and yn is None and yp is None:
                posLis.append(grid[y][x + ind])

            if yp and yn is None and xp is None and xn is None:
                posLis.append(grid[y + ind][x])

            if xn and yn is None and yp is None and xp is None:
                posLis.append(grid[y][abs(x - ind)])

            if yn and xn is None and xp is None and yp is None:
                posLis.append(grid[abs(y - ind)][x])

    except IndexError:
        return posLis
    return posLis


# check knight moves its annoying so i made a diffrent function
def calcuatePosSpical(grid, x, y, upr=False, rup=False, rdown=False, downr=False, upl=False, lup=False, ldown=False, downl=False):
    posLis = []
    try:
        if upr:

            if y - 2 < 0:
                raise IndexError
            return grid[y - 2][x + 1]
        if rup:
            if y - 1 < 0:
                raise IndexError
            return grid[y - 1][x + 2]
        if rdown:
            return grid[y + 1][x + 2]
        if downr:
            return grid[y + 2][x + 1]
        if upl:
            if y - 2 < 0 or x - 1 < 0:
                raise IndexError
            return grid[y - 2][x - 1]
        if lup:
            if y - 1 < 0 or x - 2 < 0:
                raise IndexError
            return grid[y - 1][x - 2]
        if ldown:
            if x - 2 < 0:
                raise IndexError
            return grid[y + 1][x - 2]
        if downl:
            if x - 1 < 0:
                raise IndexError
            return grid[y + 2][x - 1]
    except IndexError:
        return posLis
    return posLis


def bishopMove(move, poslist, grid, rank, sq, amtx=8):
    picePos = grid[sq][rank]
    legalMove = []
    nn = []
    np = []
    pn = []
    pp = []
    # checking what move it is set the peice list and opposite peice list
    if move == "w":
        pl = poslist[0]
        opl = poslist[1]
    elif move == "b":
        pl = poslist[1]
        opl = poslist[0]
    # enumrating all the positions possible the bishop can go
    nn = calcuatePos(grid, rank, sq, xn=True, yn=True, amt=amtx)
    np = calcuatePos(grid, rank, sq, xn=True, yp=True, amt=amtx)
    pn = calcuatePos(grid, rank, sq, xp=True, yn=True, amt=amtx)
    pp = calcuatePos(grid, rank, sq, xp=True, yp=True, amt=amtx)
    # conditions to limit teh movement depending on peices in the way etc
    for i in nn:
        if i in pl and i != picePos:
            break
        elif i in opl and i != picePos:
            legalMove.append(i)
            break
        else:
            legalMove.append(i)
    for i in np:
        if i in pl and i != picePos:
            break
        elif i in opl and i != picePos:
            legalMove.append(i)
            break
        else:
            legalMove.append(i)
    for i in pn:
        if i in pl and i != picePos:
            break
        elif i in opl and i != picePos:
            legalMove.append(i)
            break
        else:
            legalMove.append(i)
    for i in pp:
        if i in pl and i != picePos:
            break
        elif i in opl and i != picePos:
            legalMove.append(i)
            break
        else:
            legalMove.append(i)
    dumthing = []
    # removing dupilicates
    [dumthing.append(x) for x in legalMove if x not in dumthing]

    return dumthing


def rookMove(move, poslist, grid, rank, sq, amtx=8):
    picePos = grid[sq][rank]
    legalMove = []
    nn = []
    np = []
    pn = []
    pp = []
    # checking what move it is set the peice list and opposite peice list
    if move == "w":
        pl = poslist[0]
        opl = poslist[1]
    elif move == "b":
        pl = poslist[1]
        opl = poslist[0]
    # enumrating all the positions possible the rook can go
    nn = calcuatePos(grid, rank, sq, yn=True, amt=amtx)
    np = calcuatePos(grid, rank, sq, xn=True, amt=amtx)
    pn = calcuatePos(grid, rank, sq, xp=True, amt=amtx)
    pp = calcuatePos(grid, rank, sq, yp=True, amt=amtx)
    # conditions to limit teh movement depending on peices in the way etc
    for i in nn:
        if i in pl and i != picePos:
            break
        elif i in opl and i != picePos:
            legalMove.append(i)
            break
        else:
            legalMove.append(i)
    for i in np:
        if i in pl and i != picePos:
            break
        elif i in opl and i != picePos:
            legalMove.append(i)
            break
        else:
            legalMove.append(i)
    for i in pn:
        if i in pl and i != picePos:
            break
        elif i in opl and i != picePos:
            legalMove.append(i)
            break
        else:
            legalMove.append(i)
    for i in pp:
        if i in pl and i != picePos:
            break
        elif i in opl and i != picePos:
            legalMove.append(i)
            break
        else:
            legalMove.append(i)

    dumthing = []
    # removing duplicates
    [dumthing.append(x) for x in legalMove if x not in dumthing]
    return dumthing


def queenMove(move, piclist, grid, rank, sq):
    # using the rook and bishop movement to get all the possible squares
    rookm = rookMove(move, piclist, grid, rank, sq)
    bishm = bishopMove(move, piclist, grid, rank, sq)
    legalMove = []
    # making one long list not a list in a list
    for i in rookm:
        legalMove.append(i)
    for i in bishm:
        legalMove.append(i)
    return legalMove


def kingMove(move, poslist, grid, rank, sq, castel={}):
    # same think as queen but limited to 1 so it can only go 1 square away
    rookm = rookMove(move, poslist, grid, rank, sq, 1)
    bishm = bishopMove(move, poslist, grid, rank, sq, 1)
    picePos = grid[sq][rank]
    if move == "w":
        pl = poslist[0]
        opl = poslist[1]
    elif move == "b":
        pl = poslist[1]
        opl = poslist[0]
    try:
        for caslSid in castel:
            if move == "w" and caslSid.isupper():
                if caslSid == "K":
                    kingside = calcuatePos(grid, rank, sq, xp=True, amt=2)
                if caslSid == "Q":
                    queenside = calcuatePos(grid, rank, sq, xn=True, amt=2)
            elif move == "b" and caslSid.islower():
                if caslSid == "k":
                    kingside = calcuatePos(grid, rank, sq, xp=True, amt=2)
                if caslSid == "q":
                    queenside = calcuatePos(grid, rank, sq, xn=True, amt=2)
    except TypeError:
        kingside = []
        queenside = []
    legalMove = []
    for i in rookm:
        legalMove.append(i)
    for i in bishm:
        legalMove.append(i)
    try:
        for i in kingside:
            if i in pl and i != picePos:
                break
            elif i in opl and i != picePos:
                break
            else:
                legalMove.append(i)
    except UnboundLocalError:
        pass
    try:
        for i in queenside:
            if i in pl and i != picePos:
                break
            elif i in opl and i != picePos:
                break
            else:
                legalMove.append(i)
    except UnboundLocalError:
        pass
    dumthing = []
    # removing empyt lists and dupilicates
    [dumthing.append(x) for x in legalMove if x not in dumthing and x != []]
    return dumthing


def knightMove(move, poslist, grid, rank, sq):
    picepos = grid[sq][rank]
    li = [calcuatePosSpical(grid, rank, sq, upr=True),
          calcuatePosSpical(grid, rank, sq, rup=True),
          calcuatePosSpical(grid, rank, sq, rdown=True),
          calcuatePosSpical(grid, rank, sq, downr=True),
          calcuatePosSpical(grid, rank, sq, upl=True),
          calcuatePosSpical(grid, rank, sq, lup=True),
          calcuatePosSpical(grid, rank, sq, ldown=True),
          calcuatePosSpical(grid, rank, sq, downl=True)]
    if move == "w":
        pl = poslist[0]
    elif move == "b":
        pl = poslist[1]
    dumthing = []
    thing = []
    # conditional to prevent friendly fire
    for i in li:
        if i in pl and i != picepos:
            pass
        else:
            dumthing.append(i)
    for i in dumthing:
        if i != []:
            thing.append(i)
    thing.append(picepos)
    return thing


def pawnMove(move, poslist, grid, rank, sq, encrassont):
    picepos = grid[sq][rank]
    up = []
    down = []
    leftup = []
    rightup = []
    leftdown = []
    rightdown = []
    legalmoves = []
    discard = []
    dubol = False

    if move == "w":
        pl = poslist[0]
        opl = poslist[1]
    elif move == "b":
        pl = poslist[1]
        opl = poslist[0]
    # i know i could do this with nested ifs but that makes it more complicated and i don't want that
    if picepos[1] == 750 and move == "w":
        dubol = True
    elif picepos[1] == 125 and move == "b":
        dubol = True
    else:
        dubol = False
    # calcuating the positions the pawn can go, up is for the whight pawns and down is for black pawns
    if dubol:
        up = calcuatePos(grid, rank, sq, yn=True, amt=2)
        down = calcuatePos(grid, rank, sq, yp=True, amt=2)
    else:
        up = calcuatePos(grid, rank, sq, yn=True, amt=1)
        down = calcuatePos(grid, rank, sq, yp=True, amt=1)
    # all the taking squares for black and white
    leftup = calcuatePos(grid, rank, sq, yn=True, xn=True, amt=1)
    rightup = calcuatePos(grid, rank, sq, yn=True, xp=True, amt=1)
    leftdown = calcuatePos(grid, rank, sq, yp=True, xn=True, amt=1)
    rightdown = calcuatePos(grid, rank, sq, yp=True, xp=True, amt=1)
    # who move
    if move == "w":
        # check for peice in the way
        for whyyyy, i in enumerate(up):
            if whyyyy == 0:
                legalmoves.append(i)
            elif i in pl or i in opl:
                break
            else:
                legalmoves.append(i)
        # checks if peice is able to be taken
        for i in leftup:
            if i in opl or i == encrassont:
                legalmoves.append(i)
            else:
                discard.append(i)
        for i in rightup:
            if i in opl or i == encrassont:
                legalmoves.append(i)
            else:
                discard.append(i)
    elif move == "b":
        # check for peice in the way
        for whyyyy, i in enumerate(down):
            if whyyyy == 0:
                legalmoves.append(i)
            elif i in pl or i in opl:
                break
            else:
                legalmoves.append(i)
        # checks if peice is able to be taken
        for i in leftdown:
            if i in opl or i == encrassont:
                legalmoves.append(i)
            else:
                discard.append(i)
        for i in rightdown:
            if i in opl or i == encrassont:
                legalmoves.append(i)
            else:
                discard.append(i)
    dumthing = []
    # removing empyt lists and dupilicates
    [dumthing.append(x) for x in legalmoves if x not in dumthing and x != []]
    return dumthing, discard
