#FroggerProject


from pygame import *

init()

# Screen Stuff
width = 600
height = 400
screen = display.set_mode((width, height))
display.set_caption('Frogger')
endGame = False

mixer.music.load("C:/Users/Homework/Desktop/MirasStuff/pythonCodes/FroggerStuff/music.mp3")
mixer.music.play()

frogPic = image.load("C:/Users/Homework/Desktop/MirasStuff/pythonCodes/FroggerStuff/frog.png")
frogPic = transform.scale(frogPic, (40,40))

frogRect = Rect(100,0,40,40)

cars = []
cars.append(Rect(200,200,40,40))



# Game Loop
while endGame == False:
    # Event handling
    for e in event.get():
        if e.type == QUIT:
            endGame = True
        if e.type == KEYDOWN:
          if e.key == K_s:
            frogRect.move_ip(0,5)

    screen.fill((0,0,0))
    draw.rect(screen, (255,255,255), (0,0,width,20))
    screen.blit(frogPic, (100,100))
   

# check collisions
    for c in cars:
      if c.colliderect(frogRect):
        endGame=True
    # draw cars
    screen.fill((0,0,0))
    for c in cars:
      draw.rect(screen, (255,255,255),c)
    screen.blit(frogPic,frogRect)   

    display.update()
    time.delay(30)

    display.update()