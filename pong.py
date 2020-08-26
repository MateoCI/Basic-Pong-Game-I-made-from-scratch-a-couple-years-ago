import pygame
import time

soundPlayed = False
size = 1
speedamp = 0.5
speedlimit = 5
pygame.init()
ball_momentum_x = 0.1
ball_momentum_y = 3
gradualIncreaseRate = 0.09
win = pygame.display.set_mode((1000, 900))
ball_x = 250
ball_y = 250
pygame.display.set_caption("Pong")
def reverseInt(intToReverse):

    return 0 - int(intToReverse) 
def paddleJump():
    global ball_y
    global y
    global ball_momentum_x
    global ball_momentum_y
    RAWonpoint = y - 75 
    onpoint = onpoint / 12
    ball_momentum_x = onpoint
    ball_momentum_y = reverseInt(ball_momentum_y)

x = 500
y = 840

bounces = 1
ball_x = 500
ball_y = 400

width = 150
height = 10
vel = 2.857 * speedamp
run = True
RAWonpoint = 0
onpoint = 0
while run:

    #print("\ny:")
    #print(str(ball_momentum_x))
    #print("\nx:")
    #print(str(ball_momentum_x))
    pygame.time.delay(1)
    if ball_momentum_x > speedlimit:
        ball_momentum_x = speedlimit
    if ball_momentum_y > speedlimit:
        ball_momentum_y = speedlimit

    if ball_momentum_x == 0:
        ball_momentum_x = 1
        #print("your unstuck bro")
    if ball_x > 985: #right wall
        ball_momentum_x = reverseInt(ball_momentum_x)
        ball_x = ball_x - 1
        bounces = bounces + 100
        #print("left wall triggerd, bounces: " + str(bounces))

    if ball_x < 15: #left wall
        ball_momentum_x = reverseInt(ball_momentum_x)
        bounces = bounces + 1
        #print("right wall triggerd, bounces: " + str(bounces))
        ball_x = ball_x + 1

    if ball_y > 885: #bottom
        ball_momentum_y = reverseInt(ball_momentum_y)
        bounces = bounces + 1

    if ball_y < 15: #top
        ball_momentum_y = reverseInt(ball_momentum_y)
        bounces = bounces + 1
    
    
    if 825 <= ball_y <= 826:
        #print("ball under" + str(ball_y))
        if x <= ball_x <= x + 150:
            centerpoint = x + 75 
            onpoint = centerpoint - ball_x
            ball_momentum_x = ball_momentum_x + onpoint / -30
            ball_momentum_y = reverseInt(ball_momentum_y)
            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 5:
        x = x - vel
        
    if keys[pygame.K_RIGHT] and x < 845:
        x = x + vel
    
    ball_x = ball_x + (ball_momentum_x * speedamp)
    ball_y = ball_y + (ball_momentum_y  * speedamp)
    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 255, 255,), (x, y, width * size, height * size))
    pygame.draw.circle(win, (255, 255, 255,), (int(ball_x), int(ball_y)), 15, 0)
    pygame.display.update()

pygame.quit()
