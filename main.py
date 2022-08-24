import pygame
import math
pygame.init()

print("Hi universe")

ASTRONOMICAL_UNIT = 146.6e6 * 1000  # Distance in meters
GRAVITATIONAL_CONSTANT = 6.67428e-11
SCALE = 200 / ASTRONOMICAL_UNIT  # Scale down to fit the solar system on the laptop Screen
TIME_STEP = 60*60*24

WIDTH, HEIGHT = 650, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System Simulation")

frame_rate = pygame.time.Clock()

class planet:  

    def __init__(self, x, y, radius, color, mass) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.x_velocity = 0
        self.y_velocity = 0
    
    def draw(self, win):
        x = self.x * SCALE + WIDTH/2
        y = self.y * SCALE + HEIGHT/2
        pygame.draw.circle(win, self.color, (x,y), self.radius)
    
    def attraction(self, planets):
        force_x, force_y = 0, 0
        for planet in planets:
            if self == planet:
                continue

            distance_x = planet.x - self.x
            distance_y = planet.y - self.y
            distance_squared = distance_x**2 + distance_y**2 

            force = GRAVITATIONAL_CONSTANT* self.mass * planet.mass / distance_squared
            angle = math.atan2(distance_y, distance_x)

            force_x += force*math.cos(angle)
            force_y += force*math.sin(angle)


        self.x_velocity += force_x/self.mass * TIME_STEP
        self.y_velocity += force_y/self.mass * TIME_STEP

        self.x += self.x_velocity * TIME_STEP
        self.y += self.y_velocity * TIME_STEP


sun = planet(0,0, 30, (255,255,255), 1.98892 * 10**30)

mercury = planet(-0.387 * ASTRONOMICAL_UNIT,1,8,(255,255,255), 3.3 * 10**23)
mercury.y_velocity = 47.4 * 1000

venus = planet(-0.723*ASTRONOMICAL_UNIT, 0, 14, (255,255,255), 6.39 * 10**23)
venus.y_velocity = 35.02 * 1000

earth = planet(-1*ASTRONOMICAL_UNIT, 0, 16, (255,255,255), 5.974 * 10**24)
earth.y_velocity = 29.783 * 1000 

mars = planet(-1.524*ASTRONOMICAL_UNIT, 0, 12, (255,255,255), 4.8685 * 10**24)
mars.y_velocity = 24.077 * 1000


planets = [sun, mercury,venus,earth,mars]

while True:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    sun.draw(screen)
    for planet in planets:
        planet.attraction(planets)
        planet.draw(screen)
        
    frame_rate.tick(60)
    pygame.display.update()  # 
      # Max Frame rate




    