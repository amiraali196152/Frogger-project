#FroggerProject


from pygame import *

init()

# Screen Stuff
width = 600
height = 700
screen = display.set_mode((width, height))
display.set_caption('Frogger')
endGame = False

mixer.music.load("C:/Users/Homework/Desktop/MirasStuff/pythonCodes/FroggerStuff/music.mp3")
mixer.music.play(-1)

#frog setup
frogPic = image.load("C:/Users/Homework/Desktop/MirasStuff/pythonCodes/FroggerStuff/frog.png").convert_alpha() 
frogPic = transform.scale(frogPic, (40,40))
frogRect = Rect(100,0,40,40)

# car stuff
cars = []
cars.append(Rect(200,200,40,40))

# Player movement variables
px = 0
py = 0

# Game Loop
while endGame == False:
    # Event handling
    for e in event.get():
        if e.type == QUIT:
            endGame = True
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                px = -3  # Move left
            elif e.key == K_RIGHT:
                px = 3  # Move right
            elif e.key == K_UP:
                py = -3  # Move up
            elif e.key == K_DOWN:
                py = 3  # Move down
        elif e.type == KEYUP:
            if e.key == K_LEFT or e.key == K_RIGHT:
                px = 0  # Stop horizontal movement when left or right key is released
            elif e.key == K_UP or e.key == K_DOWN:
                py = 0  # Stop vertical movement when up or down key is released

  # Update player position
    frogRect.move_ip(px, py)
    frogRect.x = max(0, min(width - frogRect.width, frogRect.x))  # Keep within bounds
    frogRect.y = max(0, min(height - frogRect.height, frogRect.y))

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
