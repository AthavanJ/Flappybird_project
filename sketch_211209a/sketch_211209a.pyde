mode = 1 #Start screen, 2 == play screen, 3 == end screen
x = 0
y = 0
birdx = 400
birdy = 400 



def setup():
    global mode
    size(675,900)
    
def draw():
    global mode, bird, birdx, birdy
    if mode == 1:
        start_screen()
    elif mode == 2:
        background('#DDE1C7')
        bird = loadImage("character_bird.jpg")
        background(0)
        image(bird,birdx,birdy,80,80)
        birdy += 1

        
            
def mousePressed():
    global mode
    if (mouseX >= 100 and mouseX <= 640) and (mouseY >= 640 and mouseY <= 852):
        mode = 2
    
    
def play_screen():
    global mode, bird, birdy
    if key == CODED:
        if keyCode == UP:
            birdy -= 100

def keyPressed():
    play_screen()

    
def start_screen():
    start_background = loadImage("Flappy_Bird_Start_Screen.png")
    background(start_background)
