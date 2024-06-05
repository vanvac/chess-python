import pygame
from pygame import image, display, MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT

import logic


def setPeice(dict, pice, pos, imgl, rects, typeL):
    dumRect = dict[pice].get_rect()
    dumRect.topleft = pos[0], pos[1]
    rects.append(dumRect)
    imgl.append(dict[pice])
    typeL.append(pice)

    return imgl, rects, typeL


def spstr(stri):
    return [i for i in stri]


def disRank(dic, rank, rankc, imgl1, rects1, typeL):
    imgl = []
    rects = []
    indx = 0
    passamt = 0
    while indx <= 7:
        if passamt != 0:
            passamt -= 1
        else:
            try:
                passamt = int(rank[0]) - 1
                rank.pop(0)
            except:
                pic = rank[0]
                rank.pop(0)
                imgl, rects, typeL = setPeice(dic, pic, rankc[indx], imgl1, rects1, typeL)
        indx += 1
    return imgl, rects, typeL


def setBoard(dic, cord, imgl1, rects1, typeL1, position="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
    imgl = []
    rects = []
    sl = position.split("/")
    casel = sl[-1].split(" ")
    sl.pop(-1)
    for i in casel:
        sl.append(i)

    rankCirdlis = []
    for i in cord:
        rankCirdlis.append(i)

    rank8c, rank7c, rank6c, rank5c, rank4c, rank3c, rank2c, rank1c = rankCirdlis
    rank8, rank7, rank6, rank5, rank4, rank3, rank2, rank1, whomove, castel, encrassont, halfm, mov = sl
    rank8 = spstr(rank8)
    rank7 = spstr(rank7)
    rank6 = spstr(rank6)
    rank5 = spstr(rank5)
    rank4 = spstr(rank4)
    rank3 = spstr(rank3)
    rank2 = spstr(rank2)
    rank1 = spstr(rank1)

    imgl, rects, typeL = disRank(dic, rank8, rank8c, imgl1, rects1, typeL1)
    imgl, rects, typeL = disRank(dic, rank7, rank7c, imgl1, rects1, typeL1)
    imgl, rects, typeL = disRank(dic, rank6, rank6c, imgl1, rects1, typeL1)
    imgl, rects, typeL = disRank(dic, rank5, rank5c, imgl1, rects1, typeL1)
    imgl, rects, typeL = disRank(dic, rank4, rank4c, imgl1, rects1, typeL1)
    imgl, rects, typeL = disRank(dic, rank3, rank3c, imgl1, rects1, typeL1)
    imgl, rects, typeL = disRank(dic, rank2, rank2c, imgl1, rects1, typeL1)
    imgl, rects, typeL = disRank(dic, rank1, rank1c, imgl1, rects1, typeL1)

    return imgl, rects, typeL, whomove, castel, encrassont, int(halfm), int(mov)


def legalMoveF(move, picType, grid, legalmy, legalmx, castlelis, ensq, typeL):
    blck = []
    whit = []
    discard = []
    for help, idk in enumerate(rects):
        if typeL[help].isupper():
            whit.append(idk.topleft)
        elif typeL[help].islower():
            blck.append(idk.topleft)
    listOfPiecesC = [whit, blck]
    if move == "w":
        if picType == "B":
            legalMoves = logic.bishopMove(move, listOfPiecesC, grid, legalmy, legalmx)
        elif picType == "R":
            legalMoves = logic.rookMove(move, listOfPiecesC, grid, legalmy, legalmx)
        elif picType == "Q":
            legalMoves = logic.queenMove(move, listOfPiecesC, grid, legalmy, legalmx)
        elif picType == "K":
            legalMoves = logic.kingMove(move, listOfPiecesC, grid, legalmy, legalmx, castlelis)
        elif picType == "N":
            legalMoves = logic.knightMove(move, listOfPiecesC, grid, legalmy, legalmx)
        elif picType == "P":
            legalMoves, discard = logic.pawnMove(move, listOfPiecesC, grid, legalmy, legalmx, ensq)
        else:
            legalMoves = [grid[legalm[0]][legalm[1]]]
    elif move == "b":
        if picType == "b":
            legalMoves = logic.bishopMove(move, listOfPiecesC, grid, legalmy, legalmx)
        elif picType == "r":
            legalMoves = logic.rookMove(move, listOfPiecesC, grid, legalmy, legalmx)
        elif picType == "q":
            legalMoves = logic.queenMove(move, listOfPiecesC, grid, legalmy, legalmx)
        elif picType == "k":
            legalMoves = logic.kingMove(move, listOfPiecesC, grid, legalmy, legalmx, castlelis)
        elif picType == "n":
            legalMoves = logic.knightMove(move, listOfPiecesC, grid, legalmy, legalmx)
        elif picType == "p":
            legalMoves, discard = logic.pawnMove(move, listOfPiecesC, grid, legalmy, legalmx, ensq)
        else:
            legalMoves = [grid[legalm[0]][legalm[1]]]
    else:
        legalMoves = [grid[legalm[0]][legalm[1]]]

    return legalMoves, discard


def promote(piceDicr, rectS, listT, imgList, currentPicT, move):
    picPos = rects[currentPicT].topleft
    whatPeice = None
    picChosen = False
    bg = pygame.image.load('promback.png')
    rectS.pop(currentPicT)
    listT.pop(currentPicT)
    imgList.pop(currentPicT)
    if move == "w":
        Q = piceDicr["Q"]
        R = piceDicr["R"]
        N = piceDicr["N"]
        B = piceDicr["B"]
        Qr = Q.get_rect()
        Rr = R.get_rect()
        Nr = N.get_rect()
        Br = B.get_rect()
        Qr.topleft = picPos
        Rr.topleft = (picPos[0], picPos[1] + 125 * 1)
        Nr.topleft = (picPos[0], picPos[1] + 125 * 2)
        Br.topleft = (picPos[0], picPos[1] + 125 * 3)
    if move == "b":
        Q = piceDicr["q"]
        R = piceDicr["r"]
        N = piceDicr["n"]
        B = piceDicr["b"]
        Qr = Q.get_rect()
        Rr = R.get_rect()
        Nr = N.get_rect()
        Br = B.get_rect()
        Qr.topleft = picPos
        Rr.topleft = (picPos[0], picPos[1] - 125 * 1)
        Nr.topleft = (picPos[0], picPos[1] - 125 * 2)
        Br.topleft = (picPos[0], picPos[1] - 125 * 3)
    promImagL = [Q, R, N, B]
    promrects = [Qr, Rr, Nr, Br]
    while not picChosen:
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                for which, pic in enumerate(promrects):
                    if pic.collidepoint(event.pos):
                        whatPeice = which
            if event.type == MOUSEBUTTONUP and not picChosen:
                if move == "w":
                    if whatPeice == 0:
                        whatPeice = "Q"
                        picChosen = True
                    if whatPeice == 1:
                        whatPeice = "R"
                        picChosen = True
                    if whatPeice == 2:
                        whatPeice = "N"
                        picChosen = True
                    if whatPeice == 3:
                        whatPeice = "B"
                        picChosen = True
                if move == "b":
                    if whatPeice == 0:
                        whatPeice = "q"
                        picChosen = True
                    if whatPeice == 1:
                        whatPeice = "r"
                        picChosen = True
                    if whatPeice == 2:
                        whatPeice = "n"
                        picChosen = True
                    if whatPeice == 3:
                        whatPeice = "b"
                        picChosen = True
        if move == "w":
            screen.blit(bg, picPos)
            for ofset, img in enumerate(promImagL):
                screen.blit(img, (picPos[0], picPos[1] + (125 * ofset)))
        if move == "b":
            screen.blit(bg, (picPos[0], picPos[1] - 375))
            for ofset, img in enumerate(promImagL):
                screen.blit(img, (picPos[0], picPos[1] + (-125 * ofset)))
        pygame.display.update()

    if whatPeice == "Q":
        imgList, rectS, listT = setPeice(piceDicr, whatPeice, picPos, imgList, rectS, listT)

    if whatPeice == "R":
        imgList, rectS, listT = setPeice(piceDicr, whatPeice, picPos, imgList, rectS, listT)

    if whatPeice == "N":
        imgList, rectS, listT = setPeice(piceDicr, whatPeice, picPos, imgList, rectS, listT)

    if whatPeice == "B":
        imgList, rectS, listT = setPeice(piceDicr, whatPeice, picPos, imgList, rectS, listT)

    if whatPeice == "q":
        imgList, rectS, listT = setPeice(piceDicr, whatPeice.lower(), picPos, imgList, rectS, listT)

    if whatPeice == "r":
        imgList, rectS, listT = setPeice(piceDicr, whatPeice.lower(), picPos, imgList, rectS, listT)

    if whatPeice == "n":
        imgList, rectS, listT = setPeice(piceDicr, whatPeice.lower(), picPos, imgList, rectS, listT)

    if whatPeice == "b":
        imgList, rectS, listT = setPeice(piceDicr, whatPeice.lower(), picPos, imgList, rectS, listT)

    return rectS, listT, imgList


def encode(grid, rectS, typl, move, ensq, casl, half, mov):
    result = ""
    li = []
    poslist = []
    for pic in rectS:
        poslist.append(pic.topleft)
    # encode the current postion into FEN notation
    for rank in grid:
        rankst = ""
        count = 0
        pictrigger = False
        cc = None
        for square in rank:
            if square in poslist:
                if count == 0:
                    inc = poslist.index(square)
                    pict = typl[inc]
                    rankst = rankst + pict
                else:
                    inc = poslist.index(square)
                    pict = typl[inc]
                    rankst = rankst + str(count)
                    rankst = rankst + pict
                    count = 0
                pictrigger = True
            else:
                count += 1
        if len(rankst) == 0:
            rankst = str(count)
        if count != 0 and pictrigger:
            rankst = rankst + str(count)
        li.append(rankst)
    picepart = "/".join(li)
    # encoding the enpassant sq's
    emp = "-"
    for y, ran in enumerate(grid):
        for x, sqq in enumerate(ran):
            if ensq != None and ensq == sqq:
                temp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
                emp = f"{temp[y]}{x + 1}"
    if len(casl) == 0:
        cc = "-"
    else:
        cc = "".join(casl)
    if move == "w":
        move = "b"
    elif move == "b":
        move = "w"
    result = f"{picepart} {move} {cc} {emp} {half} {mov}"
    print(result)
    return result


path = './big images/'

screen = display.set_mode((1000, 1000))

icon = image.load('chess.png')

promBack = image.load('promback.png')

darkcirce = image.load(path + "dark-circle.png")

wp = image.load(path + 'wp.png')

bp = image.load(path + 'bp.png')

wn = image.load(path + 'wn.png')

bn = image.load(path + 'bn.png')

wb = image.load(path + 'wb.png')

bb = image.load(path + 'bb.png')

wr = image.load(path + 'wr.png')

br = image.load(path + 'br.png')

wq = image.load(path + 'wq.png')

bq = image.load(path + 'bq.png')

wk = image.load(path + 'wk.png')

bk = image.load(path + 'bk.png')

picl = [wp, bp, wn, bn, wb, bb, wr, br, wq, bq, wk, bk]
piecelst = {"P": picl[0], "p": picl[1], "N": picl[2], "n": picl[3], "B": picl[4], "b": picl[5],
            "R": picl[6], "r": picl[7], "Q": picl[8], "q": picl[9], "K": picl[10], "k": picl[11]}
imgl = []
rects = []
typeL = []

board = image.load(path + 'board.png')
listc = [0, 125, 250, 375, 500, 625, 750, 875]
grid = []
for y in listc:
    rndl = []
    for x in listc:
        rndl.append((x, y))
    grid.append(rndl)
postions = ["rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"]
screen.blit(board, (0, 0))
imgl, rects, typeL, move, castle, encrassont, halfm, movnum = setBoard(piecelst, grid, imgl, rects, typeL)
display.set_caption('chess')
display.set_icon(icon)
castlelis = []
display.flip()


def enpassantDecode(encrassont):
    ensq = [i for i in encrassont]
    temp = ["a", "b", "c", "d", "e", "f", "g", "h"]
    if encrassont == "-":
        ensq = None
    else:
        lol = temp.index(encrassont[0])
        ensq = grid[int(encrassont[1]) - 1][lol]
    return ensq


def castDecode(castle1):
    if castle1 == "-":
        castle1 = None
    else:
        for i in castle1:
            castlelis.append(i)
            rookID = {}
            rookIndexW = [yep for yep, r in enumerate(typeL) if r == "R"]
            rookIndexB = [yep for yep, r in enumerate(typeL) if r == "r"]
            rookIndexW.reverse()
            rookIndexB.reverse()
    for i, side in enumerate(castlelis):
        if side.isupper():
            try:
                if side == "K":
                    rookID[side] = rookIndexW[0]
            except IndexError:
                pass
            try:
                if side == "Q":
                    rookID[side] = rookIndexW[1]
            except IndexError:
                pass
        if side.islower():
            try:
                if side == "k":
                    rookID[side] = rookIndexB[0]
            except IndexError:
                pass
            try:
                if side == "q":
                    rookID[side] = rookIndexB[1]
            except IndexError:
                pass
    return castlelis, rookID


running = True
movingbox = None
ensq = enpassantDecode(encrassont)
castlelis, rookID = castDecode(castle)
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                for indx, pice in enumerate(rects):
                    if pice.collidepoint(event.pos):
                        pbp = pice.topleft
                        movingbox = indx
                        picType = typeL[movingbox]
                        smallestX, smallestY = 1000, 1000
                        for indx, rnk in enumerate(grid):
                            for indy, pos in enumerate(rnk):
                                if abs(pos[0] - pbp[0]) <= smallestX and abs(pos[1] - pbp[1]) <= smallestY:
                                    legalm = [indx, indy]
                                    smallestX = abs(pos[0] - pbp[0])
                                    smallestY = abs(pos[1] - pbp[1])
                if movingbox is not None:
                    legalMoves, discard = legalMoveF(move, picType, grid, legalm[1], legalm[0], castlelis, ensq, typeL)

        if event.type == MOUSEBUTTONUP:
            if event.button == 1 and movingbox is not None:
                origin = grid[legalm[0]][legalm[1]]
                boxPos = rects[movingbox].topleft
                smallestX2, smallestY2 = 1000, 1000
                ind = 0
                for indxy, pos in enumerate(legalMoves):
                    if abs(pos[0] - boxPos[0]) <= smallestX2 and abs(pos[1] - boxPos[1]) <= smallestY2:
                        ind = indxy
                        smallestX2 = abs(pos[0] - boxPos[0])
                        smallestY2 = abs(pos[1] - boxPos[1])

                rects[movingbox].topleft = notOrigin = legalMoves[ind]
                # capturing pecies
                # and removing certian rook/ enpasant things

                for index, peice in enumerate(rects):
                    peicepos = peice.topleft
                    if peicepos == legalMoves[ind] and index != movingbox:
                        rects.pop(index)
                        typeL.pop(index)
                        imgl.pop(index)
                        tak = True
                        break
                    # remove pawn after en passant white
                    if peicepos[1] == notOrigin[1] + 125 and peicepos[0] == notOrigin[0] and typeL[index] == "p" and \
                            typeL[movingbox] == "P" and move == "w":
                        rects.pop(index)
                        typeL.pop(index)
                        imgl.pop(index)
                        tak = True
                        break
                    # remove pawn after en passant black
                    if peicepos[1] == notOrigin[1] - 125 and peicepos[0] == notOrigin[0] and typeL[index] == "P" and \
                            typeL[movingbox] == "p" and move == "b":
                        rects.pop(index)
                        typeL.pop(index)
                        imgl.pop(index)
                        tak = True
                        break
                # Promotion
                if notOrigin[1] == 0 and picType == "P":
                    # the 'if' is to prevent the peices index to be interpreted as a diffrent due to captures
                    if tak:
                        rects, typeL, imgl = promote(piecelst, rects, typeL, imgl, movingbox - 1, move)
                    else:
                        rects, typeL, imgl = promote(piecelst, rects, typeL, imgl, movingbox, move)
                if notOrigin[1] == 875 and picType == "p":
                    rects, typeL, imgl = promote(piecelst, rects, typeL, imgl, movingbox, move)
                veryDescriptiveVariableName = []
                # switching moves
                if move == "w" and legalMoves[ind] != origin:
                    postions.append(encode(grid, rects, typeL, move, ensq, castlelis, halfm, movnum))
                    cRemoveIndex = []
                    # en passant target set
                    if notOrigin[1] + 125 != origin[1]:
                        ensq = (origin[0], notOrigin[1] + 125)
                    else:
                        ensq = None
                    # moving the casle rook to the opposite side ofthe king
                    if picType == "K":
                        caslSid = None
                        if origin[0] - 250 == notOrigin[0]:
                            caslSid = "Q"
                        if origin[0] + 250 == notOrigin[0]:
                            caslSid = "K"
                        if caslSid == "Q":
                            rookcasle = rookID[caslSid]
                            rookpos = (notOrigin[0] + 125, notOrigin[1])
                            rects[rookcasle].topleft = rookpos
                        if caslSid == "K":
                            rookcasle = rookID[caslSid]
                            rookpos = (notOrigin[0] - 125, notOrigin[1])
                            rects[rookcasle].topleft = rookpos
                    move = "b"
                    # castle remove check king
                    if picType == "K":
                        try:
                            veryDescriptiveVariableName.append(castlelis.index("K"))
                        except ValueError:
                            pass
                    try:
                        veryDescriptiveVariableName.append(castlelis.index("Q"))
                    except ValueError:
                        pass
                elif move == "b" and legalMoves[ind] != origin:
                    postions.append(encode(grid, rects, typeL, move, ensq, castlelis, halfm, movnum))
                    cRemoveIndex = []
                    # en passant target set
                    if notOrigin[1] - 125 != origin[1]:
                        ensq = (origin[0], notOrigin[1] - 125)
                    else:
                        ensq = None
                    if picType == "k":
                        caslSid = None
                        if origin[0] - 250 == notOrigin[0]:
                            caslSid = "q"
                        if origin[0] + 250 == notOrigin[0]:
                            caslSid = "k"
                        if caslSid == "q":
                            rookcasle = rookID[caslSid]
                            rookpos = (notOrigin[0] + 125, notOrigin[1])
                            rects[rookcasle].topleft = rookpos
                        if caslSid == "k":
                            rookcasle = rookID[caslSid]
                            rookpos = (notOrigin[0] - 125, notOrigin[1])
                            rects[rookcasle].topleft = rookpos
                    move = "w"
                    if picType == "k":
                        try:
                            veryDescriptiveVariableName.append(castlelis.index("k"))
                        except ValueError:
                            pass
                        try:
                            veryDescriptiveVariableName.append(castlelis.index("q"))
                        except ValueError:
                            pass
                # rook move casle removal
                rookID.clear()
                caslw = []
                rookIndexB = []
                rookIndexW = []
                rookIndexW = [yep for yep, r in enumerate(typeL) if r == "R"]
                rookIndexB = [yep for yep, r in enumerate(typeL) if r == "r"]
                rookIndexW.reverse()
                rookIndexB.reverse()
                for item in rookIndexW:
                    if rects[item].topleft == (875, 875):
                        caslw.append("K")
                    if rects[item].topleft == (0, 875):
                        caslw.append("Q")
                for item in rookIndexB:
                    if rects[item].topleft == (875, 0):
                        caslw.append("k")
                    if rects[item].topleft == (0, 0):
                        caslw.append("q")

                for caslnt in castlelis:
                    if caslnt not in caslw:
                        veryDescriptiveVariableName.append(castlelis.index(caslnt))
                notVeryDescriptiveVariableName = []
                for i in veryDescriptiveVariableName:
                    if i not in notVeryDescriptiveVariableName:
                        notVeryDescriptiveVariableName.append(i)
                for ofset, ind in enumerate(notVeryDescriptiveVariableName):
                    castlelis.pop(ind - ofset)
                for i, side in enumerate(castlelis):
                    if side.isupper():
                        try:
                            if side == "K":
                                rookID[side] = rookIndexW[0]
                        except IndexError:
                            pass
                        try:
                            if side == "Q":
                                rookID[side] = rookIndexW[1]
                        except IndexError:
                            pass
                    if side.islower():
                        try:
                            if side == "k":
                                rookID[side] = rookIndexB[0]
                        except IndexError:
                            pass
                        try:
                            if side == "q":
                                rookID[side] = rookIndexB[1]
                        except IndexError:
                            pass

                legalMoves = []
                movingbox = None
                movnum += 1
                print(rookID)
                if movnum % 2 == 1:
                    halfm += 1

        if event.type == MOUSEMOTION and movingbox is not None:
            rects[movingbox].move_ip(event.rel)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                screen.blit(board, (0, 0))
                trig = False
                try:
                    position = postions[-2]
                    postions.pop(-1)
                    trig = True
                except IndexError:
                    try:
                        position = postions[-1]
                        postions.pop(-1)
                        trig = True
                    except IndexError:
                        print("CANNOT UNDO LOL!!!")
                        trig = False
                if trig:
                    imgl = []
                    rects = []
                    typeL = []
                    move = None
                    castle = None
                    encrassont = None
                    halfm = None
                    movnum = None
                    castlelis = []
                    rookID = []
                    imgl, rects, typeL, move, castle, encrassont, halfm, movnum = setBoard(piecelst, grid, imgl, rects,
                                                                                           typeL, position)
                    movingbox = None
                    ensq = enpassantDecode(encrassont)
                    castlelis, rookID = castDecode(castle)

    screen.blit(board, (0, 0))

    for ing, rect in enumerate(rects):
        screen.blit(imgl[ing], rect)
    if movingbox != None:
        for i in legalMoves:
            screen.blit(darkcirce, (i[0] + 37.5, i[1] + 37.5))
    pygame.display.update()

pygame.quit()
