mode = 2 #Start screen, 2 == play screen, 3 == end screen
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
        textSize(50) 
        bird = loadImage("leflappybird.png")
        image(bird,birdx,birdy,80,80)
        play_screen()
        
            
def mousePressed():
    global mode
    if (mouseX >= 170 and mouseX <= 670) and (mouseY >= 650 and mouseY <= 800):
        mode = 2
        
    
def play_screen():
    global mode, bird, birdy
    if ((keyPressed) and  (key == 'SPACE')):
        birdy -= 5
    elif :
        birdy += 5

def keyReleased():
    
    
      
def start_screen():
    textSize(20)
    fill('#FFA500')
    rect(200, 425, 420, 150)
    fill(255)
    text("Instructions: tap the space bar to jump. \nPass through the pipes to score points. \nIf you hit the ground or hit the pipes, \nthe game is over.", 200, 450)
    fill('#FFA500')
    rect(170, 650, 500, 150)
    fill(0,0,0)
    textSize(100)
    text("- Play - ",230,750)
    

    
