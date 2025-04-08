#FroggerProject


from pygame import *

init()

# Screen Stuff
width = 600
height = 700
screen = display.set_mode((width, height))
display.set_caption('Frogger')
endGame = False

# bg music
mixer.music.load("C:/Users/Homework/Desktop/MirasStuff/pythonCodes/FroggerStuff/music.mp3")
mixer.music.play(-1)


#frog setup
frogPic = image.load("C:/Users/Homework/Desktop/MirasStuff/pythonCodes/FroggerStuff/frog.png").convert_alpha() 
frogPic = transform.scale(frogPic, (50,50))
frogRect = Rect(270,600,50,50)  # <- rect for image size

# car stuff
carPic1 = image.load("C:/Users/Homework/Desktop/MirasStuff/pythonCodes/FroggerStuff/car.png").convert_alpha() 
carPic1 = transform.scale(carPic1, (150,75))

carPic2 = image.load("C:/Users/Homework/Desktop/MirasStuff/pythonCodes/FroggerStuff/car2.png").convert_alpha() 
carPic2 = transform.scale(carPic2, (200,100))
carRect = Rect(200,200,200,100) # <- rect for image size

carPic3 = image.load("C:/Users/Homework/Desktop/MirasStuff/pythonCodes/FroggerStuff/car3.png").convert_alpha() 
carPic3 = transform.scale(carPic3, (150,75))

cars = [
    {"rect": Rect(100, 200, 150, 75), "image": carPic1},
    {"rect": Rect(300, 350, 150, 75), "image": carPic2},
    {"rect": Rect(50, 500, 150, 75), "image": carPic3}
]


# Player movement variables
px = 0
py = 0

# Game Loop
while not endGame:
    # Event handling
    for e in event.get():
        if e.type == QUIT:
            endGame = True
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                px = -3
            elif e.key == K_RIGHT:
                px = 3
            elif e.key == K_UP:
                py = -3
            elif e.key == K_DOWN:
                py = 3
        elif e.type == KEYUP:
            if e.key == K_LEFT or e.key == K_RIGHT:
                px = 0 # Stop horizontal movement when left or right key is released
            elif e.key == K_UP or e.key == K_DOWN:
                py = 0 # Stop vertical movement when up or down key is released

    # update player position
    frogRect.move_ip(px, py)
    frogRect.x = max(0, min(width - frogRect.width, frogRect.x)) # <- keeps player in bounds
    frogRect.y = max(0, min(height - frogRect.height, frogRect.y))

    # clear screen once
    screen.fill((0,0,0))
    draw.rect(screen, (255,255,255), (0,0,width,20))

    # draw cars
    for car in cars:
        screen.blit(car["image"], car["rect"])

    # draw frog player
    screen.blit(frogPic, frogRect)


    # Check collisions with all cars
    for car in cars:
        if frogRect.colliderect(car["rect"]):
            endGame = True
            print("Collision detected! Game over")
            break  # Exit loop early if crashed


    # update display
    display.update()
    time.delay(30)
