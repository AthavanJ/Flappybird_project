#import audio library
add_library('minim')


#global variables
mode = 1 #Start screen, 2 == play screen, 3 == end screen
x = 0
y = 0
speed = 2
birdx = 100
birdy = 400 
start_game = False
switch = False
score = 0
highscore = 0
choiceA1 = 17
choiceA2 = 53
choiceB1 = 23
choiceB2 = 53
circleX1 = 155
circleX2 = 173
circleY1 = 445
circleY2 = 455
max_height = 0

def setup():
    global mode
    global Xcoor_play, Ycoor_play, canvasX, canvasY, play_screen_background, Playscreen_Height, Playscreen_Width, Play_Width_Size, Increment, image_PlayX, image_PlayY, coin_sound
    play_screen_move_variables()
    pipes_move_variables()
    size(675,900)
    minim = Minim(this)
    coin_sound = minim.loadSample("coin_sound.mp3")

    
def draw():
    global mode, bird, birdx, birdy, score, start_game, highscore, circleY1, circleY2, pipe1, pipe2, pipe3, circleX1, circleX2, circleY1, circleY2, choiceA1, choiceA2, choiceB1, choiceB2
    global Xcoor_play, Ycoor_play, canvasX, canvasY, play_screen_background, Playscreen_Height, Playscreen_Width, Play_Width_Size, Increment, image_PlayX, image_PlayY
    if mode == 1:
        start_screen()
        
    elif mode == 2:
        moving_play_screen()
        #body
        fill(255)
        stroke(255)
        ellipse(155, circleY1, 45, 52)
        #beak
        ellipse(173, circleY2, 16, 23)
        bird = loadImage("character_bird.png")
        image(bird,birdx,birdy,110,80)
        if start_game == True:
            birdy += 2
            circleY1 += 2
            circleY2 += 2
            pipes_draw()
            pipes_move()
            check_lengths()
            reset_pipes()
            check_collisions_top(pipe1, choiceA2, choiceB2, circleX1, circleY1)
            check_collisions_top(pipe2, choiceA2, choiceB2, circleX1, circleY1)
            check_collisions_top(pipe3, choiceA2, choiceB2, circleX1, circleY1)
            check_collisions_top(pipe1, choiceA1, choiceB1, circleX2, circleY2)
            check_collisions_top(pipe2, choiceA1, choiceB1, circleX2, circleY2)
            check_collisions_top(pipe3, choiceA1, choiceB1, circleX2, circleY2)
            
            check_collisions_bottom(pipe1, choiceA1, choiceB1, circleX2, circleY2)
            check_collisions_bottom(pipe2, choiceA1, choiceB1, circleX2, circleY2)
            check_collisions_bottom(pipe3, choiceA1, choiceB1, circleX2, circleY2)
            check_collisions_bottom(pipe1, choiceA2, choiceB2, circleX1, circleY1)
            check_collisions_bottom(pipe2, choiceA2, choiceB2, circleX1, circleY1)
            check_collisions_bottom(pipe3, choiceA2, choiceB2, circleX1, circleY1)
            
            points(pipe1)
            points(pipe2)
            points(pipe3)
        
        elif start_game == False:
            animation_playscreen()
            pipes_draw()
            fill(255)
            circleX1 = 153
            circleX2 = 173
            circleY1 = 445
            circleY2 = 455
            stroke(255)
            ellipse(155, circleY1, 45, 52)
            #beak
            ellipse(173, circleY2, 16, 23)
            birdx = 100
            birdy = 400
            bird = loadImage("character_bird.png")
            image(bird,birdx,birdy,110,80)
            pipe1 = [[300, 0, topleftx1, toplefty1, 280, 100],[ 300, 483, bottomleftx1, bottomlefty1, 280, 100]]
            pipe2 = [[550, 0, topleftx2, toplefty2, 375, 100], [550, 563, bottomleftx2, bottomlefty2, 200, 100]]
            pipe3 = [[800, 0, topleftx3, toplefty3, 120, 100], [800, 363, bottomleftx3, bottomlefty3, 400, 100]]
            
    elif mode == 3:
        end_screen()
        if score >= highscore:
                highscore = score
        #print score 
        score_text= createFont("Cursive", 100)
        fill(255, 105, 180)
        textFont(score_text)
        text((score), 190, 400)
        text((highscore), 490, 400) 
    
        start_game = False
             
def mousePressed():
    global mode, score
    if (mouseX >= 100 and mouseX <= 640) and (mouseY >= 640 and mouseY <= 852) and (mode == 1):
        mode = 2
        score = 0
    elif (mouseX >= 105 and mouseX <= 555) and (mouseY >= 415 and mouseY <= 577) and (mode == 3):
        mode = 2
        score = 0
    elif (mouseX >= 105 and mouseX <= 555) and (mouseY >= 635 and mouseY <= 795) and (mode == 3):
        mode = 1
        score = 0
    
    
        
        
        
def play_screen():
    global mode, bird, birdy, start_game, circleY1, circleY2, max_height
    if key == CODED:
        start_game = True
        
    if start_game == True:
        if keyCode == UP:
            max_height = 0
            while max_height <= 80:
                birdy -= 0.5
                circleY1 -= 0.5
                circleY2 -= 0.5
                max_height += 0.5
            


def keyPressed():
    play_screen()

    
    
def start_screen():
    start_background = loadImage("Flappy_Bird_Start_Screen.png")
    background(start_background)
    
def end_screen():
    end_background = loadImage("Flappy_Bird_End_Screen.png")
    background(end_background)

def play_screen_move_variables():
    global Xcoor_play, Ycoor_play, canvasX, canvasY, play_screen_background, Playscreen_Height, Playscreen_Width, Play_Width_Size, Increment, image_PlayX, image_PlayY
    Playscreen_Height = 900 
    Playscreen_Width = 1600  
    Play_Width_Size = 675 
    Increment = 2  
    image_PlayX = 0    
    image_PlayY = 0      
    Xcoor_play = 0 
    Ycoor_play = 0 
    canvasX = 675 
    canvasY = 900 
    play_screen_background = loadImage( "Flappy_Bird_Play_Screen.png" )
    
def moving_play_screen():
    global Xcoor_play, Ycoor_play, canvasX, canvasY, play_screen_background, Playscreen_Height, Playscreen_Width, Play_Width_Size, Increment, image_PlayX, image_PlayY
    image_PlayX += Increment 
    if ( image_PlayX + Play_Width_Size ) >= Playscreen_Width: 
        image_PlayX = 0 
    copy(play_screen_background, image_PlayX, image_PlayY, Play_Width_Size, Playscreen_Height, Xcoor_play, Ycoor_play, canvasX, canvasY)
    

def animation_playscreen():
    global switch
    stroke(255)
    fill(255, 0, 0)
    triangle(220, 400, 200, 420, 220, 420)
    rect(220, 395, 80, 30)
    fill(255)
    animation_font = createFont("animation", 20)
    textFont(animation_font)
    text(("Begin"), 235, 415)
    if switch == False:
        stroke(0)
        line(235, 385, 245, 375)
        line(275, 385, 285, 375)
        line(310, 405, 320, 415)
        line(235, 435, 245, 445)
        line(275, 435, 285, 445) 
        if frameCount % 25 == 0:
            switch = True
    elif switch == True:
        stroke(0)  
        line(235, 385, 225, 375)
        line(275, 385, 265, 375)
        line(310, 405, 320, 395)
        line(235, 435, 225, 445)
        line(275, 435, 265, 445)  
        if frameCount % 25 == 0:
            switch = False

    
def pipes_move_variables():
    global pipes, pipe1, pipe2, pipe3, topleftx1, toplefty1, bottomleftx1, bottomlefty1, topleftx2, toplefty2, bottomleftx2, bottomlefty2, topleftx3, toplefty3, bottomleftx3, bottomlefty3
    temp = 0
    pipes = [[300, 0, temp, temp, 280, 100],[ 300, 483, temp, temp, 280, 100], [550, 0, temp, temp, 375, 100],[550, 563, temp, temp, 200, 100], [800, 0, temp, temp, 120, 100],[800, 363, temp, temp, 400, 100]] #[topleftx,toplefty,bottomleftx, bottomlefty, length, width] 
 
    topleftx1 = pipes[0][0]
    toplefty1 = pipes[0][1] + pipes[0][4]
    topleftx2 = pipes[2][0]
    toplefty2 = pipes[2][1] + pipes[2][4]
    topleftx3 = pipes[4][0]
    toplefty3 = pipes[4][1] + pipes[4][4]

    bottomleftx1 = pipes[1][0]
    bottomlefty1 = pipes[1][1] + pipes[1][4]
    bottomleftx2 = pipes[3][0]
    bottomlefty2 = pipes[3][1] + pipes[3][4]
    bottomleftx3 = pipes[5][0]
    bottomlefty3 = pipes[5][1] + pipes[5][4]
    
    
    #[topleftx,toplefty,bottomleftx, bottomlefty, length, width] 
    #pipe1/2/3 = [[top], [bottom]]
    pipe1 = [[300, 0, topleftx1, toplefty1, 280, 100],[ 300, 483, bottomleftx1, bottomlefty1, 280, 100]]
    pipe2 = [[550, 0, topleftx2, toplefty2, 375, 100], [550, 563, bottomleftx2, bottomlefty2, 200, 100]]
    pipe3 = [[800, 0, topleftx3, toplefty3, 120, 100], [800, 363, bottomleftx3, bottomlefty3, 400, 100]]
     

    
def pipes_draw():
    global pipe1, speed
    stroke('#228C22')
    fill('#228C22')
    #1st set of pipes
    #Top
    rect(pipe1[0][0],pipe1[0][1], pipe1[0][5], pipe1[0][4])
    #bottom
    rect(pipe1[1][0],pipe1[1][1], pipe1[1][5], pipe1[1][4])
         
    #2nd set of pipes
    #Top
    rect(pipe2[0][0],pipe2[0][1], pipe2[0][5], pipe2[0][4])
    #Bottom
    rect(pipe2[1][0],pipe2[1][1], pipe2[1][5], pipe2[1][4])
    
    #3rd set of pipes
    #Top
    rect(pipe3[0][0],pipe3[0][1], pipe3[0][5], pipe3[0][4])
    #Bottom
    rect(pipe3[1][0],pipe3[1][1], pipe3[1][5], pipe3[1][4])
    
def pipes_move():
    pipe1[0][0] -= speed
    pipe1[1][0] -= speed
    pipe2[0][0] -= speed
    pipe2[1][0] -= speed
    pipe3[0][0] -= speed
    pipe3[1][0] -= speed
    
def reset_pipes():
    global pipe1, pipe2, pipe3
    #pipe1
    #check if top reached end
    if (pipe1[0][0] + pipe1[0][5]) <= 0:
            pipe1[0][0] = 675
            pipe1[0][4] += 10
    #check if bottom reached end
    if (pipe1[1][0] + pipe1[1][5]) <= 0:
            pipe1[1][0] = 675
    #pipe2
    #check if top reached end
    if (pipe2[0][0] + pipe2[0][5]) <= 0:
            pipe2[0][0] = 675
    #check if bottom reached end
    if (pipe2[1][0] + pipe2[1][5]) <= 0:
            pipe2[1][0] = 675  
            pipe2[1][4] += 10
            pipe2[1][1] = 763 - pipe2[1][4]
            
    #pipe3
    if (pipe3[0][0] + pipe3[0][5]) <= 0:
            pipe3[0][0] = 675
            pipe3[0][4] += 10
    #check if bottom reached end
    if (pipe3[1][0] + pipe3[1][5]) <= 0:
            pipe3[1][0] = 675

    
    
def check_lengths():
    global pipe1, pipe2, pipe3
    #check pipe 1
    if (pipe1[1][1] - pipe1[0][1]) <= 95:
        pipe1[0][4] = 350
    #check pipe 2
    if (pipe2[1][1] - pipe2[0][1]) <= 95:
        pipe2[1][4] = 200
        pipe2[1][1] = 700
    #check pipe 3
    if (pipe3[1][1] - pipe3[0][1]) <= 95:
        pipe3[1][4] = 500   
        
        
        
def check_collisions_bottom(pipe, choiceA, choiceB, circleX, circleY):
    global circleX2, circleX1, circleY2, circleY1, pipe1, pipe2, pipe3, start_game, mode
    #small circle
    for a in range(choiceA):
        for b in range(choiceB):
            #bottom pipes - top
            #(+,+)
            if (circleX + (a-1)//2) <= (pipe[1][0] + pipe[0][5]) and (circleX + (a-1)//2) >= pipe[1][0] and (circleY + (b-1)//2) >= pipe[1][1] and (circleY + (b - 1)//2) <= 763:
                start_game = False
                mode = 3
            #(+, -)
            elif (circleX + (a-1)//2) <= (pipe[1][0] + pipe[0][5]) and (circleX + (a-1)//2) >= pipe[1][0] and (circleY - (b-1)//2) >= pipe[1][1] and (circleY - (b - 1)//2) <= 763:
                start_game = False
                mode = 3
            #(-,-)
            elif (circleX - (a-1)//2) <= (pipe[1][0] + pipe[0][5]) and (circleX - (a-1)//2) >= pipe[1][0] and (circleY - (b-1)//2) >= pipe[1][1] and (circleY - (b - 1)//2) <= 763:
                start_game = False
                mode = 3
            #(-, +)
            elif (circleX - (a-1)//2) <= (pipe[1][0] + pipe[0][5]) and (circleX - (a-1)//2) >= pipe[1][0] and (circleY + (b-1)//2) >= pipe[1][1] and (circleY + (b - 1)//2) <= 763:
                start_game = False
                mode = 3
            #bottom pipes - left vertical and right vertical 
            #(+,+)
            if ((circleX + (a-1)//2) >= pipe[1][0] and (circleX + (a-1)//2) <= (pipe[1][0] + pipe[1][5]) and circleY >= pipe[1][1] and (circleY + (b-1)//2) <= (pipe[1][1] + pipe[1][5])):
                start_game = False
                mode = 3
            #(+,-)
            elif ((circleX + (a-1)//2) >= pipe[1][0] and (circleX + (a-1)//2) <= (pipe[1][0] + pipe[1][5]) and circleY >= pipe[1][1] and (circleY - (b-1)//2) <= (pipe[1][1] + pipe[1][5])):
                start_game = False
                mode = 3
            #(-,-)
            elif ((circleX - (a-1)//2) >= pipe[1][0] and (circleX - (a-1)//2) <= (pipe[1][0] + pipe[1][5]) and circleY >= pipe[1][1] and (circleY - (b-1)//2) <= (pipe[1][1] + pipe[1][5])):
                start_game = False
                mode = 3
            #(-,+)
            elif ((circleX - (a-1)//2) >= pipe[1][0] and (circleX - (a-1)//2) <= (pipe[1][0] + pipe[1][5]) and circleY >= pipe[1][1] and (circleY + (b-1)//2) <= (pipe[1][1] + pipe[1][5])):
                start_game = False
                mode = 3
            
    #ground        
            elif (circleY + (b-1)//2) >= 763:
                start_game = False
                mode = 3
    #sky
            elif (circleY + (b-1)//2) < 0:
                start_game = False
                mode = 3





def check_collisions_top(pipe, choiceA, choiceB, circleX, circleY):
    global circleX2, circleX1, circleY2, circleY1, pipe1, pipe2, pipe3, start_game, mode
    #small circle
    for a in range(choiceA):
        for b in range(choiceB):
            #top pipes - left vertical and right vertical 
            #(+, +)
            if ((circleX + (a-1)//2) >= pipe[0][0] and (circleX + (a-1)//2) <= (pipe[0][0] + pipe[0][5]) and (circleY + (b-1)//2) >= 0 and (circleY + (b-1)//2) <= pipe[0][4]):
                start_game = False
                mode = 3
            #(+,-)
            elif ((circleX + (a-1)//2) >= pipe[0][0] and (circleX + (a-1)//2) <= (pipe[0][0] + pipe[0][5]) and (circleY - (b-1)//2) >= 0 and (circleY - (b-1)//2) <= pipe[0][4]):
                start_game = False
                mode = 3
            #(-,-)
            elif ((circleX - (a-1)//2) >= pipe[0][0] and (circleX - (a-1)//2) <= (pipe[0][0] + pipe[0][5]) and (circleY - (b-1)//2) >= 0 and (circleY - (b-1)//2) <= pipe[0][4]):
                start_game = False
                mode = 3
            #(-,+)
            elif ((circleX - (a-1)//2) >= pipe[0][0] and (circleX - (a-1)//2) <= (pipe[0][0] + pipe[0][5]) and (circleY + (b-1)//2) >= 0 and (circleY + (b-1)//2) <= pipe[0][4]):
                start_game = False
                mode = 3
            #top pipes - bottom 
            #(+,-)
            if (circleX + (a-1)//2) <= (pipe[0][0] + pipe[0][5]) and (circleX + (a-1)//2) >= pipe[0][0] and (circleY - (b-1)//2) >= 0 and (circleY - (b - 1)//2) <= pipe[0][4]:
                start_game = False
                mode = 3
            #(+,+)
            elif (circleX + (a-1)//2) <= (pipe[0][0] + pipe[0][5]) and (circleX + (a-1)//2) >= pipe[0][0] and (circleY + (b-1)//2) >= 0 and (circleY + (b - 1)//2) <= pipe[0][4]:
                start_game = False
                mode = 3
            #(-,-)
            elif (circleX - (a-1)//2) <= (pipe[0][0] + pipe[0][5]) and (circleX - (a-1)//2) >= pipe[0][0] and (circleY - (b-1)//2) >= 0 and (circleY - (b - 1)//2) <= pipe[0][4]:
                start_game = False
                mode = 3
            #(-, +)
            elif (circleX - (a-1)//2) <= (pipe[0][0] + pipe[0][5]) and (circleX - (a-1)//2) >= pipe[0][0] and (circleY + (b-1)//2) >= 0 and (circleY + (b - 1)//2) <= pipe[0][4]:
                start_game = False
                mode = 3



def points(pipe):
    global score, circleX1, circleX2, circleY1, circleY2, coin_sound, pipe1, pipe2, pipe3, speed
    if (circleX1 - 44//2) == (pipe[0][0] + pipe[0][5]): 
            score += 1
            coin_sound.trigger()
    elif (circleX1 - 44//2) == (pipe[0][0] + pipe[0][5] + 1): #if speed = 2 add +1
            score += 1
            coin_sound.trigger()

    
    



                                                        
                                                                       
    
    
