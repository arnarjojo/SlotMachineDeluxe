import pygame

pygame.init()
pygame.font.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

initCredit = 0

gameStats = [initCredit]

display_width = 1280
display_height = 720

screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

ARNAR = 1
BJARKI = 2
BIRGIR = 3
DAVID = 4
HAUKUR = 5
HAVAR = 6
VIDAR = 7
TH = 8
SHIT = 9

thePics = {
    ARNAR: pygame.image.load('Images/Arnar.png'),
    BJARKI: pygame.image.load('Images/Bjarki.png'),
    BIRGIR: pygame.image.load('Images/Birgir.png'),
    DAVID: pygame.image.load('Images/David.jpg'),
    HAUKUR: pygame.image.load('Images/Haukur.png'),
    HAVAR: pygame.image.load('Images/Havar.png'),
    VIDAR: pygame.image.load('Images/Viddi.png'),
    TH: pygame.image.load('Images/TH.png'),
    SHIT: pygame.image.load('Images/Bonus.jpg')
}

font = pygame.font.Font('Fonts/freesansbold.ttf', 30)
creditFont = pygame.font.Font('Fonts/digital-7italic.ttf', 50)
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
        clock.tick(15)

def theGame():
    pygame.mixer.music.stop()
    screen.fill(black)
    mousex = 0
    mousey = 0
    run = True
    background = pygame.image.load("Images/background.png")
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


introMenu()
pygame.quit()
quit()