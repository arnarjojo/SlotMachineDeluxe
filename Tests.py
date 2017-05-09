
initCredit = 1000
initBet = 100
initWin = 0

gameStats = [initCredit, initBet, initWin]

def tests():
    board = {'11': '2', '12': '1', '13': '1', '14': '1', '15': '3','21': '2', '22': '2', '23': '2', '24': '2', '25': '2','31': '1', '32': '3', '33': '3', '34': '4', '35': '8'}
    checkWin(board)
    print('Straight 1 with Hauks, expecting 600:  ' + str(gameStats[2]))

    gameStats[2] = 0
    board = {'11': '2', '12': '2', '13': '2', '14': '2', '15': '2','21': '4', '22': '3', '23': '1', '24': '6', '25': '6','31': '6', '32': '5', '33': '6', '34': '2', '35': '2'}
    checkWin(board)
    print('Straight 2, expecting 300:  ' + str(gameStats[2]))

    gameStats[2] = 0
    board = {'11': '7', '12': '3', '13': '4', '14': '2', '15': '2','21': '6', '22': '3', '23': '2', '24': '5', '25': '6','31': '2', '32': '2', '33': '1', '34': '4', '35': '3'}
    checkWin(board)
    print('Straight 3, expecting 300:  ' + str(gameStats[2]))

    gameStats[2] = 0
    board = {'11': '2', '12': '2', '13': '4', '14': '5', '15': '4','21': '6', '22': '3', '23': '2', '24': '5', '25': '6','31': '1', '32': '1', '33': '2', '34': '2', '35': '2'}
    checkWin(board)
    print('Half-cut 1, expecting 300:  ' + str(gameStats[2]))

    gameStats[2] = 0
    board = {'11': '7', '12': '3', '13': '4', '14': '2', '15': '2','21': '6', '22': '3', '23': '2', '24': '5', '25': '6','31': '2', '32': '2', '33': '1', '34': '4', '35': '3'}
    checkWin(board)
    print('Half-cut 2, expecting 300:  ' + str(gameStats[2]))

    gameStats[2] = 0
    board = {'11': '2', '12': '3', '13': '7', '14': '1', '15': '2','21': '6', '22': '2', '23': '6', '24': '2', '25': '6','31': '2', '32': '1', '33': '7', '34': '8', '35': '2'}
    checkWin(board)
    print('Diagonal both with TH in the middle and hauk, expecting 1200:  ' + str(gameStats[2]))

    gameStats[2] = 0
    board = {'11': '2', '12': '9', '13': '7', '14': '9', '15': '2','21': '9', '22': '2', '23': '6', '24': '2', '25': '6','31': '2', '32': '1', '33': '7', '34': '8', '35': '2'}
    checkWin(board)
    print('Diagonal both with TH in the middle and hauk and expecting bonus, expecting 3600:  ' + str(gameStats[2]))

    gameStats[2] = 0
    board = {'11': '1', '12': '1', '13': '4', '14': '2', '15': '2','21': '6', '22': '3', '23': '2', '24': '5', '25': '6','31': '2', '32': '2', '33': '1', '34': '3', '35': '2'}
    checkWin(board)
    print('Pyramid 1, expecting 300:  ' + str(gameStats[2]))

    gameStats[2] = 0
    board = {'11': '2', '12': '2', '13': '4', '14': '1', '15': '2','21': '6', '22': '3', '23': '7', '24': '5', '25': '6','31': '8', '32': '1', '33': '3', '34': '2', '35': '2'}
    checkWin(board)
    print('Pyramid 2 with TH and Hauks, expecting 600:  ' + str(gameStats[2]))


def checkWin(board):
    ##Straight line
    temp = board['11']
    for i in range(12,16):
        if temp == '7':
            temp = board[str(i)]
            if i >= 13:
                gameStats[2] += gameStats[1]
        elif temp == board[str(i)] or board[str(i)] == '7':
            if i >= 13:
                gameStats[2] += gameStats[1]
        else:
            break

    temp = board['21']
    for i in range(22,26):
        if temp == '7':
            temp = board[str(i)]
            if i >= 23:
                gameStats[2] += gameStats[1]
        elif temp == board[str(i)] or board[str(i)] == '7':
            if i >= 23:
                gameStats[2] += gameStats[1]
        else:
            break

    temp = board['31']
    for i in range(32,36):
        if temp == '7':
            temp = board[str(i)]
            if i >= 33:
                gameStats[2] += gameStats[1]
        elif temp == board[str(i)] or board[str(i)] == '7':
            if i >= 33:
                gameStats[2] += gameStats[1]
        else:
            break

    ##Diagonal line
    tempArr = ['22', '33', '24', '15']
    temp = board['11']
    for i in tempArr:
        if temp == '7':
            temp = board[str(i)]
            if tempArr.index(i) >= 1:
                gameStats[2] += gameStats[1]
        elif temp == board[i] or board[i] == '7':
            if tempArr.index(i) >= 1:
                gameStats[2] += gameStats[1]
        else:
            break

    tempArr = ['22', '13', '24', '35']
    temp = board['31']
    for i in tempArr:
        if temp == '7':
            temp = board[str(i)]
            if tempArr.index(i) >= 1:
                gameStats[2] += gameStats[1]
        elif temp == board[i] or board[i] == '7':
            if tempArr.index(i) >= 1:
                gameStats[2] += gameStats[1]
        else:
            break

    #Half-cut
    tempArr = ['12', '23', '34', '35']
    temp = board['11']
    for i in tempArr:
        if temp == '7':
            temp = board[str(i)]
            if tempArr.index(i) >= 1:
                gameStats[2] += gameStats[1]
        elif temp == board[i] or board[i] == '7':
            if tempArr.index(i) >= 1:
                gameStats[2] += gameStats[1]
        else:
            break

    tempArr = ['32', '23', '14', '15']
    temp = board['31']
    for i in tempArr:
        if temp == '7':
            temp = board[str(i)]
            if tempArr.index(i) >= 1:
                gameStats[2] += gameStats[1]
        elif temp == board[i] or board[i] == '7':
            if tempArr.index(i) >= 1:
                gameStats[2] += gameStats[1]
        else:
            break

    #Pyramid
    tempArr = ['32', '33', '34', '25']
    temp = board['21']
    for i in tempArr:
        if temp == '7':
            temp = board[str(i)]
            if tempArr.index(i) >= 2:
                gameStats[2] += gameStats[1]
        elif temp == board[i] or board[i] == '7':
            if tempArr.index(i) >= 2:
                gameStats[2] += gameStats[1]
        else:
            break

    tempArr = ['12', '13', '14', '25']
    temp = board['21']
    for i in tempArr:
        if temp == '7':
            temp = board[str(i)]
            if tempArr.index(i) >= 1:
                gameStats[2] += gameStats[1]
        elif temp == board[i] or board[i] == '7':
            if tempArr.index(i) >= 1:
                gameStats[2] += gameStats[1]
        else:
            break

    #Bonus game
    count = 0
    for key, value in board.items():
        if value == '9':
            count += 1
    if count >= 3:
        gameStats[2] += 1000 ##Needs bonus game implementation

    # #Hauk's double
    for key, value in board.items():
        if value == '8':
            gameStats[2] = gameStats[2]*2


tests()