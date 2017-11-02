import pygame, random
from random import randint
pygame.init()
pygame.font.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

initCredit = 0
initBet = 0
initWin = 0

gameStats = [initCredit, initBet, initWin]

display_width = 1280
display_height = 720

screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

EMPTY = 0
BJARKI = 2
BIRGIR = 3
DAVID = 4
HAVAR = 5
VIDAR = 6
TH = 7
HAUKUR = 8
SHIT = 9

thePics = {
    EMPTY: pygame.image.load('Images/11.jpg'),
    BJARKI: pygame.image.load('Images/Bjarki.png'),
    BIRGIR: pygame.image.load('Images/Birgir.png'),
    DAVID: pygame.image.load('Images/David.png'),
    HAVAR: pygame.image.load('Images/Havar.png'),
    VIDAR: pygame.image.load('Images/Viddi.png'),
    TH: pygame.image.load('Images/TH.png'),
    HAUKUR: pygame.image.load('Images/Haukur.png'),
    SHIT: pygame.image.load('Images/Bonus.png')
}

EMPTY = 0
KingD = 1
KingH = 2
KingC = 7
KingS = 8
QueenD = 3
QueenH = 4
QueenC = 9
QueenS = 10
JackD = 5
JackH = 6
JackC = 11
JackS = 12

theCards = {
    EMPTY: pygame.image.load('Images/Cards/back.png'),
    KingD: pygame.image.load('Images/Cards/KingD.png'),
    KingH: pygame.image.load('Images/Cards/KingH.png'),
    KingC: pygame.image.load('Images/Cards/KingC.png'),
    KingS: pygame.image.load('Images/Cards/KingS.png'),
    QueenD: pygame.image.load('Images/Cards/QueenD.png'),
    QueenH: pygame.image.load('Images/Cards/QueenH.png'),
    QueenC: pygame.image.load('Images/Cards/QueenC.png'),
    QueenS: pygame.image.load('Images/Cards/QueenS.png'),
    JackD: pygame.image.load('Images/Cards/JackD.png'),
    JackH: pygame.image.load('Images/Cards/JackH.png'),
    JackC: pygame.image.load('Images/Cards/JackC.png'),
    JackS: pygame.image.load('Images/Cards/JackS.png')
}

ARNAR = 0
ATLI = 1
DANIEL = 2
MARTIN = 3
ULFUR = 4
THOR = 5
BACK = 6

theBonusGuys = {
    ARNAR: pygame.image.load('Images/Arnar.png'),
    ATLI: pygame.image.load('Images/Atli.png'),
    DANIEL: pygame.image.load('Images/Daniel.png'),
    MARTIN: pygame.image.load('Images/Martin.png'),
    ULFUR: pygame.image.load('Images/Ulfur.png'),
    THOR: pygame.image.load('Images/Thor.png'),
    SHIT: pygame.image.load('Images/Bonus.png'),
    BACK: pygame.image.load('Images/Back.png')
}

chances = {}

chances['2'] = 7
chances['3'] = 7
chances['4'] = 7
chances['5'] = 7
chances['6'] = 7
chances['7'] = 2
chances['8'] = 1
chances['9'] = 4


font = pygame.font.Font('Fonts/freesansbold.ttf', 30)
creditFont = pygame.font.Font('Fonts/digital-7italic.ttf', 50)
inGameCreditFont = pygame.font.Font('Fonts/digital-7italic.ttf', 30)
pygame.display.set_caption('Slot Machine: Deluxe Version')

def introMenu():
    # list of menu text
    text = ['Play', 'Rules', 'Quit', '+']
    run = True
    bg = pygame.image.load("Images/SlotsMenu.png")

    pygame.mixer.music.load("Music/SlotMenu.mp3")
    pygame.mixer.music.play(-1)
    while run:
        mouseClicked = False
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouseClicked = True

        x = display_width / 3.6
        y = display_height / 1.33
        # isClick = stores location of menu items "rect"
        isClick = []

        moneyDisp = creditFont.render('%d kr.' % gameStats[0], True, red)
        moneyRect = moneyDisp.get_rect()
        moneyRect.topleft = (920, 445)
        screen.blit(moneyDisp, moneyRect)

        # writes menu text, diff col if mouseover
        for t in text:
            tex = font.render(t, True, black)
            texR = tex.get_rect()
            texR.center = (x, y)
            if texR.collidepoint(pygame.mouse.get_pos()):
                tex = font.render(t, True, white)
            screen.blit(tex, texR)
            if t == text[2]:
                x += 315
                y += 4
            else:
                x += 193
                y += 3
            isClick.append(texR)
        # clickable menu items
        if mouseClicked and isClick[0].collidepoint(event.pos):
            theGame()
        if mouseClicked and isClick[1].collidepoint(event.pos):
            theRules(1)
        if mouseClicked and isClick[2].collidepoint(event.pos):
            pygame.quit()
            quit()
        if mouseClicked and isClick[3].collidepoint(event.pos):
            if gameStats[0] < 5000:
                gameStats[0] += 1000

        pygame.display.update()
        clock.tick(60)


def theRules(number):
    screen.fill(black)
    mousex = 0
    mousey = 0
    ruleString = "Images/Rule" + str(number) + '.png'
    rule = pygame.image.load(ruleString)
    run = True
    while run:
        mouseClicked = False
        screen.blit(rule, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                mouseClicked = True

        clickable = []

        homeDisp = font.render('Home', True, black)
        homeRect = homeDisp.get_rect()
        homeRect.topleft = (335, 597)
        screen.blit(homeDisp, homeRect)

        nextDisp = font.render('Next', True, black)
        nextRect = nextDisp.get_rect()
        nextRect.topleft = (525, 597)
        screen.blit(nextDisp, nextRect)

        clickable.append(homeRect)
        clickable.append(nextRect)

        if mouseClicked and clickable[0].collidepoint(event.pos):
            introMenu()
        if mouseClicked and clickable[1].collidepoint(event.pos):
            if number < 3:
                theRules(number+1)
            else:
                theRules(1)
        pygame.display.update()
        clock.tick(15)


def theGame():
    pygame.mixer.music.stop()
    screen.fill(black)
    mousex = 0
    mousey = 0
    run = True
    newBoard = True
    background = pygame.image.load("Images/background.png")
    doubleUpBack = pygame.image.load("Images/DoubleUp.png")
    board = {}
    doubleUp = False
    doublePressed = False
    getDoubleUp = False
    spin = False
    while run:
        mouseClicked = False
        keyPressed = False
        pressed = pygame.key.get_pressed()
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
            if event.type == pygame.KEYDOWN:
                keyPressed = True
                pressed = pygame.key.get_pressed()

        click = []
        if newBoard:
            fillBoard(board)
            if spin:
                checkWin(board)
                gameStats[0] += gameStats[2]
                spin = False
            newBoard = False

        boardX = 112
        boardY = 75
        pos = 11
        for item in board:
            if pos == 16:
                pos = 21
                boardX = 112
                boardY += 170
            elif pos == 26:
                boardX = 112
                boardY += 170
                pos = 31
            screen.blit(thePics[int(board[str(pos)])], (boardX, boardY))
            boardX += 210
            pos += 1

        doubleClicked = []
        if getDoubleUp:
            theRandom = randint(1,12)
            theCard = theCards[theRandom]
            start_time = pygame.time.get_ticks()
            getDoubleUp = False

        if doubleUp:
            screen.blit(doubleUpBack, (350, 100))
            if doublePressed == False:
                screen.blit(theCards[0], (530, 220))
            else:
                if pygame.time.get_ticks() - start_time < 3000:
                    screen.blit(theCard, (500,200))
                else:
                    doublePressed = False
                    doubleUp = False

            redDisp = font.render('Red' , True, red)
            redRect = redDisp.get_rect()
            redRect.topleft = (750, 500)
            screen.blit(redDisp, redRect)

            blackDisp = font.render('Black' , True, black)
            blackRect = blackDisp.get_rect()
            blackRect.topleft = (400, 500)
            screen.blit(blackDisp, blackRect)

            doubleClicked.append(redRect)
            doubleClicked.append(blackRect)

        clicked = []
        if gameStats[2] > 0:
            doubleDisp = creditFont.render('Double Up!' , True, green)
            doubleRect = doubleDisp.get_rect()
            doubleRect.topleft = (530, 670)
            screen.blit(doubleDisp, doubleRect)
            clicked.append(doubleRect)
            #pygame.mixer.music.load("Music/Win.mp3")
            #pygame.mixer.music.play(-1)
            #þarf að skoða betur

        balanceDisp = inGameCreditFont.render('%d kr.' % gameStats[0], True, red)
        balanceRect = balanceDisp.get_rect()
        balanceRect.topleft = (250, 601)
        screen.blit(balanceDisp, balanceRect)

        winDisp = inGameCreditFont.render('%d kr.' % gameStats[2], True, red)
        winRect = winDisp.get_rect()
        winRect.topleft = (605, 601)
        screen.blit(winDisp, winRect)

        betDisp = inGameCreditFont.render('%d kr.' % gameStats[1], True, red)
        betRect = betDisp.get_rect()
        betRect.topleft = (940, 601)
        screen.blit(betDisp, betRect)

        plusDisp = inGameCreditFont.render('+', True, red)
        plusRect = plusDisp.get_rect()
        plusRect.topleft = (1058, 612)
        screen.blit(plusDisp, plusRect)

        minusDisp = inGameCreditFont.render('-', True, red)
        minusRect = minusDisp.get_rect()
        minusRect.topleft = (867, 612)
        screen.blit(minusDisp, minusRect)

        spinDisp = creditFont.render('Spin!', True, green)
        spinRect = spinDisp.get_rect()
        spinRect.topleft = (1160, 670)
        screen.blit(spinDisp, spinRect)

        homeDisp = creditFont.render('Home', True, green)
        homeRect = homeDisp.get_rect()
        homeRect.topleft = (25, 670)
        screen.blit(homeDisp, homeRect)

        click.append(plusRect)
        click.append(minusRect)
        click.append(homeRect)
        click.append(spinRect)

        if mouseClicked and click[2].collidepoint(event.pos):
            introMenu()
        if mouseClicked and click[1].collidepoint(event.pos):
            if gameStats[1] >= 10:
                gameStats[1] -= 10
                print(click)
        if mouseClicked and click[0].collidepoint(event.pos):
            if gameStats[1] <= 90:
                gameStats[1] += 10
                pygame.mixer.music.load("Music/Cashin.mp3")
                pygame.mixer.music.play(0)
        if mouseClicked and click[3].collidepoint(event.pos):
            if gameStats[1] > 0 and gameStats[0] >= gameStats[1]:
                gameStats[0] -= gameStats[1]
                gameStats[2] = 0
                newBoard = True
                spin = True
                pygame.mixer.music.load("Music/spinJump.mp3")
                pygame.mixer.music.play(0)
        if doubleUp:
            if mouseClicked and doubleClicked[0].collidepoint(event.pos):
                doublePressed = True
                if theRandom <= 6:
                    gameStats[0] += gameStats[2]
                    gameStats[2] = gameStats[2]*2
                else:
                    gameStats[0] -= gameStats[2]
                    gameStats[2] = 0
            elif mouseClicked and doubleClicked[1].collidepoint(event.pos):
                doublePressed = True
                if theRandom >= 7:
                    gameStats[0] += gameStats[2]
                    gameStats[2] = gameStats[2]*2
                else:
                    gameStats[0] -= gameStats[2]
                    gameStats[2] = 0
        if len(clicked) > 0:
            if mouseClicked and clicked[0].collidepoint(event.pos) and gameStats[2] > 0:
                doubleUp = True
                getDoubleUp = True

        pygame.display.update()
        clock.tick(10)


def bonusGame():
    bonusRun = True
    background = pygame.image.load("Images/background.png")
    bonusBoard = {}
    done = {11: False, 12: False, 13: False, 14: False, 15: False, 21: False, 22: False, 23: False, 24: False, 25: False, 31: False, 32: False, 33: False, 34: False, 35: False}
    newBonusBoard = True
    pygame.mixer.music.load("Music/partyHorn.mp3")
    pygame.mixer.music.play(0)
    clickables = {}
    bonusOn = True
    spin = []
    while bonusRun:
        mouseClicked = False
        keyPressed = False
        pressed = pygame.key.get_pressed()
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEMOTION:
                mousex, mousey = event.pos
                pos = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
            if event.type == pygame.KEYDOWN:
                keyPressed = True
                pressed = pygame.key.get_pressed()
        if newBonusBoard:
            fillBonusBoard(bonusBoard)
            newBonusBoard = False

        boardX = 112
        boardY = 75
        pos = 11
        for item in bonusBoard:
            if pos == 16:
                pos = 21
                boardX = 112
                boardY += 170
            elif pos == 26:
                boardX = 112
                boardY += 170
                pos = 31
            if done[pos] == True:
                screen.blit(theBonusGuys[int(bonusBoard[str(pos)])], (boardX, boardY))
            else:
                theImg = theBonusGuys[6]
                theRect = theImg.get_rect()
                theRect.topleft = (boardX, boardY)
                screen.blit(theBonusGuys[6], theRect)
                clickables[pos] = theRect
            boardX += 210
            pos += 1


        balanceDisp = inGameCreditFont.render('%d kr.' % gameStats[0], True, red)
        balanceRect = balanceDisp.get_rect()
        balanceRect.topleft = (250, 601)
        screen.blit(balanceDisp, balanceRect)

        winDisp = inGameCreditFont.render('%d kr.' % gameStats[2], True, red)
        winRect = winDisp.get_rect()
        winRect.topleft = (605, 601)
        screen.blit(winDisp, winRect)

        betDisp = inGameCreditFont.render('%d kr.' % gameStats[1], True, red)
        betRect = betDisp.get_rect()
        betRect.topleft = (940, 601)
        screen.blit(betDisp, betRect)

        plusDisp = inGameCreditFont.render('+', True, red)
        plusRect = plusDisp.get_rect()
        plusRect.topleft = (1058, 612)
        screen.blit(plusDisp, plusRect)

        minusDisp = inGameCreditFont.render('-', True, red)
        minusRect = minusDisp.get_rect()
        minusRect.topleft = (867, 612)
        screen.blit(minusDisp, minusRect)

        if bonusOn == False:
            spinDisp = creditFont.render('Exit!', True, green)
            spinRect = spinDisp.get_rect()
            spinRect.topleft = (1160, 670)
            screen.blit(spinDisp, spinRect)

            homeDisp = creditFont.render('Home', True, green)
            homeRect = homeDisp.get_rect()
            homeRect.topleft = (25, 670)
            screen.blit(homeDisp, homeRect)

            spin.append(homeRect)
            spin.append(spinRect)

            if mouseClicked and spin[0].collidepoint(event.pos):
                introMenu()
            elif mouseClicked and spin[1].collidepoint(event.pos):
                theGame()


        if mouseClicked and bonusOn:
            print(clickables)
            for pos, rect in clickables.items():
                if done[pos] == False and clickables[pos].collidepoint(event.pos):
                    done[pos] = True
                    print(bonusBoard)
                    if bonusBoard[str(pos)] == ARNAR:
                        gameStats[2] += gameStats[1]*3
                        pygame.mixer.music.load("Music/AmericaFuckYeahCut.mp3")
                        pygame.mixer.music.play(0)
                    elif bonusBoard[str(pos)] == ATLI:
                        gameStats[2] += gameStats[1]*3
                        pygame.mixer.music.load("Music/Whistle.mp3")
                        pygame.mixer.music.play(0)
                    elif bonusBoard[str(pos)] == DANIEL:
                        gameStats[2] += gameStats[1]*3
                    elif bonusBoard[str(pos)] == MARTIN:
                        gameStats[2] += gameStats[1]*2
                        pygame.mixer.music.load("Music/OpenCan.mp3")
                        pygame.mixer.music.play(0)
                    elif bonusBoard[str(pos)] == ULFUR:
                        gameStats[2] += gameStats[1]*3
                    elif bonusBoard[str(pos)] == THOR:
                        gameStats[2] += gameStats[1]*100
                        pygame.mixer.music.load("Music/Fireworks.mp3")
                        pygame.mixer.music.play(0)
                    elif bonusBoard[str(pos)] == SHIT:
                        gameStats[0] += gameStats[2]
                        pygame.mixer.music.load("Music/Toilet.mp3")
                        pygame.mixer.music.play(0)
                        bonusOn = False


        pygame.display.update()
        clock.tick(10)

def fillBonusBoard(board):
    arrayOfAll = [ARNAR, ARNAR, ATLI, ATLI, DANIEL, DANIEL, MARTIN, MARTIN, MARTIN, MARTIN, ULFUR, ULFUR, THOR, SHIT, SHIT]
    left = 14
    for i in range(1, 16):
        if i <= 5:
            rand = randint(0, left)
            board['1' + str(i)] = arrayOfAll[rand]
            del arrayOfAll[rand]
            left -= 1
        elif i > 5 and i <= 10:
            rand = randint(0, left)
            board['2' + str(i-5)] = arrayOfAll[rand]
            del arrayOfAll[rand]
            left -= 1
        else:
            rand = randint(0, left)
            board['3' + str(i-10)] = arrayOfAll[rand]
            del arrayOfAll[rand]
            left -= 1


def fillBoard(board):
    for i in range(1, 16):
        if i <= 5:
            board['1' + str(i)] = getRandomBlock()
        elif i > 5 and i <= 10:
            board['2' + str(i-5)] = getRandomBlock()
        else:
            board['3' + str(i-10)] = getRandomBlock()




def getRandomBlock():
    return random.choice([x for x in chances for y in range(chances[x])])

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
        bonusGame() ##Needs bonus game implementation

    # #Hauk's double
    for key, value in board.items():
        if value == '8':
            gameStats[2] = gameStats[2]*2


introMenu()
pygame.quit()
quit()