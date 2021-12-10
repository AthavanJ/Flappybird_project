mode = 1 #Start screen, 2 == play screen, 3 == end screen



def setup():
    global mode
    size(675,900)
    
def draw():
    global mode
    if mode == 1:
        start_screen()
    elif mode == 2:
        background('#DDE1C7')
        
        
            
def mousePressed():
    global mode
    
    if (mouseX >= 100 and mouseX <= 640) and (mouseY >= 640 and mouseY <= 852):
        mode = 2
    
    
#def play_screen():
    
def start_screen():
    start_background = loadImage("Flappy_Bird_Start_Screen.png")
    background(start_background)
