#Import the resources and set up the window.
import pyglet
from pyglet import shapes

game_window=pyglet.window.Window(1000, 800)
main_batch=pyglet.graphics.Batch()

from pyglet.window import mouse
from pyglet.window import key
from pyglet import image


#Initial Labels
words=pyglet.text.Label(text="Yes", font_name="American typewriter", x=250, y=80, anchor_x="center", font_size=40, batch=main_batch, color=(100, 200, 10, 255))
words2=pyglet.text.Label(text="No", font_name="American typewriter", x=750, y=80, anchor_x="center", font_size=40, batch=main_batch, color=(255, 200, 10, 250))

#Shapes and buttons
square=pyglet.shapes.Rectangle(x=0, y=0, width=500, height=200, color=(0, 255, 0))
square2=pyglet.shapes.Rectangle(x=500, y=0, width=500, height=200, color=(255, 0, 0))
square3=pyglet.shapes.Rectangle(x=0, y=200, width=1000, height=100, color=(0, 0, 255))
square4=pyglet.shapes.Rectangle(x=0, y=700, width=1000, height=100, color=(210, 105, 30))
level1=pyglet.shapes.Rectangle(x=0, y=0, width=1000, height=800, color=(0, 150, 255))
click=pyglet.shapes.Rectangle(x=350, y=400, width=300, height=100, color=(255, 0, 0))
instructions=pyglet.shapes.Rectangle(x=800, y=470, width=250, height=50, color=(0, 150, 255))
next_button=pyglet.shapes.Rectangle(x=900, y=300, width=100, height=70, color=(0, 150, 255))

#Words
question=pyglet.text.Label(text="Is this a suspect?", font_name="American typewriter",
                           x=500, y=235, anchor_x="center", font_size=40, batch=main_batch, color=(255, 255, 255, 255))
task=pyglet.text.Label(text="Find suspects with brown eyes or blond hair.",
                       font_name="American typewriter", x=500, y=730, anchor_x="center", font_size=30, batch=main_batch, color=(0, 0, 0, 255))
l3words=pyglet.text.Label(text="",
                       font_name="American typewriter", x=500, y=750, anchor_x="center", font_size=25, batch=main_batch, color=(0, 255, 0, 255))
Score=pyglet.text.Label(text="Score: 0",
                       font_name="American typewriter", x=900, y=780, anchor_x="center", font_size=10, batch=main_batch, color=(0, 0, 0, 255))
level1words=pyglet.text.Label(text="The Detective: A Game in Logic",
                       font_name="American typewriter", x=500, y=750, anchor_x="center", font_size=50, batch=main_batch, color=(0, 0, 0, 255))
clickwords=pyglet.text.Label(text="Click here to continue",
                       font_name="American typewriter", x=500, y=425, anchor_x="center", font_size=20, batch=main_batch, color=(255, 255, 255, 255))
levelwords=pyglet.text.Label(text="Level One", font_name="American typewriter",
                           x=850, y=600, anchor_x="center", font_size=30, batch=main_batch, color=(255, 255, 255, 255))
next_words=pyglet.text.Label(text="", font_name="American typewriter",
                           x=950, y=325, anchor_x="center", font_size=20, batch=main_batch, color=(255, 255, 255, 255))
iwords=pyglet.text.Label(text="INSTRUCTIONS", font_name="American typewriter",
                           x=900, y=485, anchor_x="center", font_size=20, batch=main_batch, color=(255, 255, 255, 255))
#Import images and set them up.
check=pyglet.image.load('checkmark.png')
check1=pyglet.sprite.Sprite(img=check, x=-500, y=-500)
x=pyglet.image.load('xmark.png')
x1=pyglet.sprite.Sprite(img=x, x=-500, y=-500)
s1=pyglet.image.load('suspect1.png')
s2=pyglet.image.load('suspect2.png')
s3=pyglet.image.load('suspect3.png')
s4=pyglet.image.load('suspect4.png')
s5=pyglet.image.load('suspect5.png')
s6=pyglet.image.load('suspect6.png')
s7=pyglet.image.load('suspect7.png')
s8=pyglet.image.load('suspect8.png')
s9=pyglet.image.load('suspect9.png')
s10=pyglet.image.load('suspect10.png')
s11=pyglet.image.load('suspect1 copy.png')
s12=pyglet.image.load('suspect3 copy.png')
s13=pyglet.image.load('suspect4 copy.png')
s14=pyglet.image.load('suspect5 copy.png')
s15=pyglet.image.load('suspect7 copy.png')
s16=pyglet.image.load('suspect8 copy.png')
s17=pyglet.image.load('suspect10 copy.png')
s18=pyglet.image.load('suspect3 copy 2.png')
s19=pyglet.image.load('suspect4 copy 2.png')
s20=pyglet.image.load('suspect5 copy 2.png')
s21=pyglet.image.load('suspect8 copy 2.png')
s22=pyglet.image.load('suspect10 copy 2.png')
s23=pyglet.image.load('suspect3 copy 3.png')
s24=pyglet.image.load('suspect5 copy 3.png')
s25=pyglet.image.load('suspect8 copy 3.png')
img1=pyglet.sprite.Sprite(img=s1, x=100, y=300)
img2=pyglet.sprite.Sprite(img=s2, x=-500, y=-500)
img3=pyglet.sprite.Sprite(img=s3, x=-500, y=-500)
img4=pyglet.sprite.Sprite(img=s4, x=-500, y=-500)
img5=pyglet.sprite.Sprite(img=s5, x=-500, y=-500)
img6=pyglet.sprite.Sprite(img=s6, x=-500, y=-500)
img7=pyglet.sprite.Sprite(img=s7, x=-500, y=-500)
img8=pyglet.sprite.Sprite(img=s8, x=-500, y=-500)
img9=pyglet.sprite.Sprite(img=s9, x=-500, y=-500)
img10=pyglet.sprite.Sprite(img=s10, x=-500, y=-500)
img11=pyglet.sprite.Sprite(img=s11, x=-500, y=-500)
img12=pyglet.sprite.Sprite(img=s12, x=-500, y=-500)
img13=pyglet.sprite.Sprite(img=s13, x=-500, y=-500)
img14=pyglet.sprite.Sprite(img=s14, x=-500, y=-500)
img15=pyglet.sprite.Sprite(img=s15, x=-500, y=-500)
img16=pyglet.sprite.Sprite(img=s16, x=-500, y=-500)
img17=pyglet.sprite.Sprite(img=s17, x=-500, y=-500)
img18=pyglet.sprite.Sprite(img=s18, x=-500, y=-500)
img19=pyglet.sprite.Sprite(img=s19, x=-500, y=-500)
img20=pyglet.sprite.Sprite(img=s20, x=-500, y=-500)
img21=pyglet.sprite.Sprite(img=s21, x=-500, y=-500)
img22=pyglet.sprite.Sprite(img=s22, x=-500, y=-500)
img23=pyglet.sprite.Sprite(img=s23, x=-500, y=-500)
img24=pyglet.sprite.Sprite(img=s24, x=-500, y=-500)
img25=pyglet.sprite.Sprite(img=s25, x=-500, y=-500)
level1screen=pyglet.image.load('Level1.png')
l1=pyglet.sprite.Sprite(img=level1screen, x=-2000, y=-2000)
level2screen=pyglet.image.load('Level2.png')
l2=pyglet.sprite.Sprite(img=level2screen, x=-2000, y=-2000)
level3screen=pyglet.image.load('Level3.png')
l3=pyglet.sprite.Sprite(img=level3screen, x=-2000, y=-2000)
level4screen=pyglet.image.load('Level4.png')
l4=pyglet.sprite.Sprite(img=level4screen, x=-2000, y=-2000)
ti1=pyglet.image.load('Title1.png')
t1=pyglet.sprite.Sprite(img=ti1, x=100, y=475)
ti2=pyglet.image.load('Title2.png')
t2=pyglet.sprite.Sprite(img=ti2, x=100, y=0)
c1=pyglet.image.load('congrats.png')
congrats=pyglet.sprite.Sprite(img=c1, x=-500, y=-500)



#Mouse events
@game_window.event
def on_mouse_press(x, y, button, modifiers):
    #Level 1
    if img1.x==100:
        status="True"
        score=0
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l1.x=50
            l1.y=10
    if img2.x==100:
        status="False"
        score=100
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l1.x=50
            l1.y=10
    if img3.x==100:
        status="True"
        score=200
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l1.x=50
            l1.y=10
    if img4.x==100:
        status="True"
        score=300
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l1.x=50
            l1.y=10
    if img5.x==100:
        status="True"
        score=400
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l1.x=50
            l1.y=10
    if img6.x==100:
        status="False"
        score=500
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l1.x=50
            l1.y=10
    if img7.x==100:
        status="True"
        score=600
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l1.x=50
            l1.y=10
    if img8.x==100:
        status="True"
        score=700
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l1.x=50
            l1.y=10
    if img9.x==100:
        status="False"
        score=800
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l1.x=50
            l1.y=10
    if img10.x==100:
        status="True"
        score=900
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l1.x=50
            l1.y=10
    #Level 2
    if img11.x==100:
        status="False"
        score=1000
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l2.x=50
            l2.y=10
    if img12.x==100:
        status="True"
        score=1100
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l2.x=50
            l2.y=10
    if img13.x==100:
        status="True"
        score=1200
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l2.x=50
            l2.y=10
    if img14.x==100:
        status="True"
        score=1300
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l2.x=50
            l2.y=10
    if img15.x==100:
        status="False"
        score=1400
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l2.x=50
            l2.y=10
    if img16.x==100:
        status="True"
        score=1500
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l2.x=50
            l2.y=10
    if img17.x==100:
        status="True"
        score=1600
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l2.x=50
            l2.y=10
    #Level 3
    if img18.x==100:
        status="True"
        score=1700
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l3.x=50
            l3.y=10
    if img19.x==100:
        status="False"
        score=1800
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l3.x=50
            l3.y=10
    if img20.x==100:
        status="True"
        score=1900
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l3.x=50
            l3.y=10
    if img21.x==100:
        status="True"
        score=2000
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l3.x=50
            l3.y=10
    if img22.x==100:
        status="False"
        score=2100
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l3.x=50
            l3.y=10
    #Level 4
    if img23.x==100:
        status="False"
        score=2200
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l4.x=50
            l4.y=10
    if img24.x==100:
        status="False"
        score=2300
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l4.x=50
            l4.y=10
    if img25.x==100:
        status="True"
        score=2400
        if button==mouse.LEFT and x>=800 and x<=1000 and y>=470 and y<=520:
            l4.x=50
            l4.y=10

    if check1.x==200 and check1.y==100:
        score+=100
        Score.text="Score: "+str(score)
    if button==mouse.LEFT and level1.width==1000 and x>=350 and x<=650 and y>=400 and y<=500:
        level1.width=0
        level1.height=0
        level1words.text=''
        clickwords.text=''
        click.width=0
        click.height=0
        t1.x=-500
        t1.y=-500
        t2.x=-500
        t2.y=-500
        next_words.text="NEXT"
    if status=="True":
        if button == mouse.LEFT and x>=0 and x<=500 and y>=0 and y<=200 and level1.width==0:
            check1.x=200
            check1.y=100
        if button==mouse.LEFT and x>=500 and x<=1000 and y>=0 and y<=200:
            x1.x=200
            x1.y=100
    if status=="False":
        if button == mouse.LEFT and x>=0 and x<=500 and y>=0 and y<=200:
            x1.x=200
            x1.y=100
        if button==mouse.LEFT and x>=500 and x<=1000 and y>=0 and y<=200:
            check1.x=200
            check1.y=100
    if button==mouse.LEFT and x>=900 and x<=1000 and y>=90 and y<=370:
        check1.x=-500
        check1.y=-500
        x1.x=-500
        x1.y=-500
        l1.x=-2000
        l1.y=-2000
        l2.x=-2000
        l2.y=-2000
        l3.x=-2000
        l3.y=-2000
        l4.x=-2000
        l4.y=-2000

    #Level 1
    if score==0:
        status="True"
        img1.x=100
        img1.y=300
    if score==100:
        status="False"
        img1.x=-500
        img1.y=-500
        img2.x=100
        img2.y=300
    if score==200:
        status="True"
        img2.x=-500
        img2.y=-500
        img3.x=100
        img3.y=300
    if score==300:
        status="True"
        img3.x=-500
        img3.y=-500
        img4.x=100
        img4.y=300
    if score==400:
        status="True"
        img4.x=-500
        img4.y=-500
        img5.x=100
        img5.y=300
    if score==500:
        status="False"
        img5.x=-500
        img5.y=-500
        img6.x=100
        img6.y=300
    if score==600:
        status="True"
        img6.x=-500
        img6.y=-500
        img7.x=100
        img7.y=300
    if score==700:
        status="True"
        img7.x=-500
        img7.y=-500
        img8.x=100
        img8.y=300
    if score==800:
        status="False"
        img8.x=-500
        img8.y=-500
        img9.x=100
        img9.y=300
    if score==900:
        status="True"
        img9.x=-500
        img9.y=-500
        img10.x=100
        img10.y=300
    #Level 2
    if score>=1000 and score<1700:
        task.text="Find suspects with blond hair and blue eyes."
        levelwords.text="Level Two"
    if score==1000:
        status="False"
        img10.x=-500
        img10.y=-500
        img11.x=100
        img11.y=300
    if score==1100:
        status="True"
        img11.x=-500
        img11.y=-500
        img12.x=100
        img12.y=300
    if score==1200:
        status="True"
        img12.x=-500
        img12.y=-500
        img13.x=100
        img13.y=300
    if score==1300:
        status="True"
        img13.x=-500
        img13.y=-500
        img14.x=100
        img14.y=300
    if score==1400:
        status="False"
        img14.x=-500
        img14.y=-500
        img15.x=100
        img15.y=300
    if score==1500:
        status="True"
        img15.x=-500
        img15.y=-500
        img16.x=100
        img16.y=300
    if score==1600:
        status="True"
        img16.x=-500
        img16.y=-500
        img17.x=100
        img17.y=300
    #Level 3
    if score>=1700 and score<2200:
        task.font_size=25
        task.y=720
        l3words.text="Interrogate the suspects; whoever was at the bank is a suspect:"
        levelwords.text="Level Three"
    if score==1700:
        status="True"
        img17.x=-500
        img17.y=-500
        img18.x=100
        img18.y=300
        task.text='"I went to the mall and then the bank."'
    if score==1800:
        status="False"
        img18.x=-500
        img18.y=-500
        img19.x=100
        img19.y=300
        task.text='"I went to the store, then to the dentist."'
    if score==1900:
        status="True"
        img19.x=-500
        img19.y=-500
        img20.x=100
        img20.y=300
        task.text='"I went to the arcade and then to the bank."'
    if score==2000:
        status="True"
        img20.x=-500
        img20.y=-500
        img21.x=100
        img21.y=300
        task.text='"I went to the daycare and then to the bank."'
    if score==2100:
        status="False"
        img21.x=-500
        img21.y=-500
        img22.x=100
        img22.y=300
        task.text="I went to the park and then to the restaurant."
    #Level 4
    if score>2100:
        levelwords.text="Level Four"
        l3words.text="Whoever's statement negates to that they robbed the bank is the criminal."
        l3words.font_size=15
        question.text="Is this the criminal?"
    if score==2200:
        status="False"
        img22.x=-500
        img22.y=-500
        img23.x=100
        img23.y=300
        task.text='"I was at the daycare, or I robbed the bank."'
    if score==2300:
        status="False"
        img23.x=-500
        img23.y=-500
        img24.x=100
        img24.y=300
        task.text='"I was not at the arcade, and I went home."'
    if score==2400:
        status="True"
        img24.x=-500
        img24.y=-500
        img25.x=100
        img25.y=300
        task.text='"I was never at the bank, or I did not rob it."'
    if score==2500:
        congrats.x=100
        congrats.y=300
        



@game_window.event
def on_draw():
    game_window.clear()
    img1.draw()
    img2.draw()
    img3.draw()
    img4.draw()
    img5.draw()
    img6.draw()
    img7.draw()
    img8.draw()
    img9.draw()
    img10.draw()
    img11.draw()
    img12.draw()
    img13.draw()
    img14.draw()
    img15.draw()
    img16.draw()
    img17.draw()
    img18.draw()
    img19.draw()
    img20.draw()
    img21.draw()
    img22.draw()
    img23.draw()
    img24.draw()
    img25.draw()
    words.draw()
    words2.draw()
    task.draw()
    l3words.draw()
    square.draw()
    square2.draw()
    square3.draw()
    square4.draw()
    levelwords.draw()
    instructions.draw()
    main_batch.draw()
    level1.draw()
    level1words.draw()
    click.draw()
    l1.draw()
    l2.draw()
    l3.draw()
    l4.draw()
    next_button.draw()
    next_words.draw()
    clickwords.draw()
    t1.draw()
    t2.draw()
    check1.draw()
    x1.draw()
    congrats.draw()

#Start it up!
if __name__ == "__main__":
    pyglet.app.run() 
