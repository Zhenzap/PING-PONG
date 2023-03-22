from pygame import * 

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 50:
            self.rect.y += self.speed   
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 50:
            self.rect.y += self.speed        

win_width = 600
win_height = 500
display.set_caption("Ping-pong")
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load("table.png"), (win_width, win_height))

player1 = Player("platforma1.png", 5, 50, 20, 100, 5)
player2 = Player("platforma2.png", 575, 350, 20, 100, 5)
ball = GameSprite("ball.png", 250, 200, 20, 20, 50)

goal = 7
point_right = 0
point_left = 0

speed_x = 3
speed_y = 3

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False     
    if not finish:
        window.blit(back, (0, 0))
        player1.update1()
        player2.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height - 20 or ball.rect.y < 0:
            speed_y *= -1 
        if ball.rect.x < 0:
            point_right += 1
            ball.rect.x = 250
            ball.rect.y = 200
            speed_x *= -1
        elif ball.rect.x > win_width:
            point_left += 1
            ball.rect.x = 250
            ball.rect.y = 200
            speed_x *= -1    
        if ball.rect.colliderect(player1.rect):
            speed_x *= -1
            ball.rect.x = player1.rect.right
        elif ball.rect.colliderect(player2.rect):
            speed_x *= -1
            ball.rect.x = player2.rect.left - ball.rect.width
        player1.reset()
        player2.reset()
        ball.reset()
        font.init()
        font1 = font.Font(None, 40)
        text1 = font1.render(str(point_left), True, (0, 0, 0))
        text2 = font1.render(str(point_right), True, (0, 0, 0))
        window.blit(text1, (280, 10))
        window.blit(text2, (300, 10))
        if point_right >= goal or point_left >= goal:
            finish = True
    display.update()
    clock.tick(FPS)