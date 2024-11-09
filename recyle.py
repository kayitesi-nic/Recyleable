import pgzrun
import random

WIDTH= 800
HEIGHT= 600
CENTRE_X= WIDTH/2
CENTRE_Y= HEIGHT/2
CENTRE= (CENTRE_X , CENTRE_Y)
FINAL_LEVEL= 10
START_SPEED= 10

ITEMS= ["bag", "battery", "bottle", "chips"]

game_over= False
game_complete= False
current_level= 1

items=[]
Animations=[]

def draw():
    screen.clear()
    screen.blit("bg", (0,0))
    screen.draw.text(head, fontsize= 30, CENTRE=(200,300), color=(255,255,255))
    screen.draw.text(subhead, fontsize= 15, CENTRE=(100,150), color=(255,255,255))
def display_message(head,subhead):
    if game_over:
        screen.draw.text("Game over", fontsize=60, CENTRE=(200,300), color=(0,0,0))
        screen.draw.text("Try again", fontsize=30, CENTRE=(200,300), color=(0,0,0))
    elif game_complete:
        screen.draw.text("You Win", fontsize=60, CENTRE=(200,300), color=(0,0,0))
        screen.draw.text("Good Job", fontsize=30, CENTRE=(200,300), color=(0,0,0))
    else:
        for item in items:
            item.draw() 

def update():
    global items
    if len(items) == 0:
        items= make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create= get_options(number_of_extra_items)
    new_items= create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)

    return new_items


def get_options(number_of_extra_items):
    items_to_create=["paper"]
    for i in range(0, number_of_extra_items):
        random_option= random.choice(ITEMS) 
        items_to_create.append(random_option)
    return items_to_create

def create_items(items_to_create):
    new_items=[]
    for option in items_to_create:
        item= Actor(option + "img")
        new_items.append(item)
    return new_items

def handle_game_over():
    global game_over
    game_over= True

def handle_game_complete():
    global current_level, items, Animations, game_complete
    stop_Animation(Animations)
    if current_level == final_level:
        game_complete= True
    else:
        current_level +1
        items=[]
        Animations=[]

def layout_items(items_to_layout):
    number_of_gaps= len(items_to_layout) +1
    gap_size= WIDTH / number_of_gaps
    random.shuffle(items_to_layout)
    for i, item in items_to_layout:
        new_x= (index +1) *gap_size 
        item.x= new_x

def animate_items(items_to_animate):
    global Animations 
    for i in items_to_animate():
        speed= START_SPEED - current_level
        i.anchor= ("center", "bottom")
        Animation= animate (i,duration= speed, on_finished= handle_game_over)
        Animations.append(Animation)

def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper" in item.image:
                handle_game_complete
            else:
                handle_game_over

def stop_Animation(Animations_to_stop):
    for i in Animations_to_stop:
        if Animation.running:
            Animation.stop()











pgzrun.go()