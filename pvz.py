from tkinter import *
from time import *
from random import*
def c(event):                 #植物种植
    global ps
    global sunflowers
    global sunlights
    global plant
    global card
    global plants
    chick = False
#    print(event.x, event.y)
    for s in ses:
        if event.x < s.x2 and event.x > s.x1 and event.y < s.y2 and event.y > s.y1:
            s.move = True
            chick = True
    if chick == False:
        for g in gds:
            if event.x < g.x2 and event.x > g.x1:
                if event.y < g.y2 and event.y > g.y1 and g.full == False:
                    if plant == 'peashooter' and sunlights >= 100:
                        np = pea(g.x1+5, g.y1+5, g.x2, g.y2, (g.y1-80)/97+1, g)
                        ps.append(np)
                        plants.append(np)
                        g.full = True
                        sunlights -= 100
                    elif plant == 'sunflower' and sunlights >= 50:
                        s = flower(g.x1+5, g.y1+5, g.x2, g.y2, (g.y1-80)/97+1, g)
                        sunflowers.append(s)
                        plants.append(s)
                        g.full = True
                        sunlights -= 50
                    sunlight_update()
    if event.y >= 600 and event.y <= 671:
        if event.x >= 150 and event.x <= 221:
            plant = 'peashooter'
            cv.delete(card)
            card = cv.create_rectangle(150, 600, 221, 671)
        elif event.x >= 225 and event.x <= 296:
            plant = 'sunflower'
            cv.delete(card)
            card = cv.create_rectangle(225, 600, 296, 671)
tk = Tk()
cv = Canvas(tk, height=700, width=1800, background='#a0a0a0')
cv.bind('<Button-1>',c)
cv.focus_set()
cv.pack()
tk.title('植物大战僵尸')
bg = PhotoImage(file='bg.gif')
cv.create_image(0, 0, image=bg, anchor='nw')          #设置背景
back = PhotoImage(file='SunBack.gif')
cv.create_image(0, 600, image=back, anchor='nw')
sizex, sizey = 80, 97
gds = []
sunlights = 500
light = cv.create_text(75, 615, text=str(sunlights), font=('Segoe Print', 15))
cardp = PhotoImage(file='Peashooter_00.gif')
cardf = PhotoImage(file='SunFlower_00.gif')
cv.create_image(150, 600, image=cardp, anchor='nw')
cv.create_image(225, 600, image=cardf, anchor='nw')
card = None
#card = cv.create_rectangle(150, 600, 221, 671)
class ground:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.road = (self.y1-80)/97+1
        self.full = False
class pea:
    def __init__(self, x1, y1, x2, y2, r, ad):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.bg = [PhotoImage(file='Peashooter_00.gif'), PhotoImage(file='Peashooter_01.gif'), 
                   PhotoImage(file='Peashooter_02.gif'), PhotoImage(file='Peashooter_03.gif'),
                   PhotoImage(file='Peashooter_04.gif'), PhotoImage(file='Peashooter_05.gif'),
                   PhotoImage(file='Peashooter_06.gif'), PhotoImage(file='Peashooter_07.gif'),
                   PhotoImage(file='Peashooter_08.gif'), PhotoImage(file='Peashooter_09.gif'),
                   PhotoImage(file='Peashooter_10.gif'), PhotoImage(file='Peashooter_11.gif'),
                   PhotoImage(file='Peashooter_12.gif')
            ]
        self.now = self.bg[0]
        self.id = cv.create_image(self.x1, self.y1, image=self.now, anchor='nw')
        self.num = 0
        self.road = r
        self.ad = ad
        self.hp = 100
        self.attacked = False
        self.eating = []
        self.amslow = 3
        self.kind = 'peashooter'
class flower:
    def __init__(self, x1, y1, x2, y2, r, ad):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.bg = [PhotoImage(file='SunFlower_00.gif'), PhotoImage(file='SunFlower_01.gif'), 
                   PhotoImage(file='SunFlower_02.gif'), PhotoImage(file='SunFlower_03.gif'),
                   PhotoImage(file='SunFlower_04.gif'), PhotoImage(file='SunFlower_05.gif'),
                   PhotoImage(file='SunFlower_06.gif'), PhotoImage(file='SunFlower_07.gif'),
                   PhotoImage(file='SunFlower_08.gif'), PhotoImage(file='SunFlower_09.gif'),
                   PhotoImage(file='SunFlower_10.gif'), PhotoImage(file='SunFlower_11.gif'),
                   PhotoImage(file='SunFlower_12.gif')
            ]
        self.now = self.bg[0]
        self.id = cv.create_image(self.x1, self.y1, image=self.now, anchor='nw')
        self.num = 0
        self.road = r
        self.ad = ad
        self.hp = 100
        self.attacked = False
        self.eating = []
        self.amslow = 3
        self.kind = 'sunflower'
        self.make_sunlight_time = randint(1, 1000)
        self.make_times = 0
class z:
    def __init__(self, x1, y1, x2, y2, r, mbg, atbg, dbg):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.mbg = mbg
        self.atbg = atbg
        self.dbg = dbg
        self.bg = self.mbg
        self.now = self.bg[0]
        self.id = cv.create_image(self.x1, self.y1, image=self.now, anchor='nw')
        self.num = 0
        self.fast = 0.3
        self.road = r
        self.hp = 100
        self.die = False
        self.amslow = 3        
class bullet:
    def __init__(self, x1, y1, x2, y2, r, bg):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.bg = bg
        self.id = cv.create_image(self.x1, self.y1, image=self.bg, anchor='nw')
        self.road = r        
class sunlight:
    def __init__(self, x1, y1, bg, stop):
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = self.x1 + 78, self.y1 +78
        self.bg = bg
        self.id = cv.create_image(self.x1, self.y1, image=self.bg, anchor='nw')
        self.stop = stop
        self.move = False               
def draw(s, ft, pic):
    s.now = pic[s.num]
    s.newid = cv.create_image(s.x1, s.y1, image=s.now, anchor='nw')
    if ft == True:
        cv.move(s.id, -s.fast, 0)
        s.x1 -= s.fast
        if s.die == True and s.num == 9:
            cv.delete(s.id)
            cv.delete(s.newid)
            zs.remove(s)
    cv.delete(s.id)
    s.id = s.newid
    if s.num == len(s.bg)-1:
        s.num = 0
    if loop % s.amslow == 0:
        s.num += 1
def sunlight_update():
    global light
    cv.delete(light)
    newsun = cv.create_text(75, 615, text=str(sunlights), font=('Segoe Print', 15))
    light = newsun
for y in range(80, 485, sizey):
    for x in range(255, 960, sizex):
        g = ground(x, y, x+sizex, y+sizey)
        gds.append(g)
loop = 0
plant = 'peashooter'
zs = []
ps = []
bs = []
ses = []
sunflowers = []
plants = []
zypos = [30, 127, 224, 321, 418]
butpic = PhotoImage(file='Bullet_1.gif')
mbg = [     PhotoImage(file='Zombie_0.gif'), PhotoImage(file='Zombie_1.gif'),
            PhotoImage(file='Zombie_2.gif'), PhotoImage(file='Zombie_3.gif'),
            PhotoImage(file='Zombie_4.gif'), PhotoImage(file='Zombie_5.gif'),
            PhotoImage(file='Zombie_6.gif'), PhotoImage(file='Zombie_7.gif'),
            PhotoImage(file='Zombie_9.gif'), PhotoImage(file='Zombie_10.gif'),
            PhotoImage(file='Zombie_11.gif'), PhotoImage(file='Zombie_12.gif'),
            PhotoImage(file='Zombie_13.gif'), PhotoImage(file='Zombie_14.gif'),
            PhotoImage(file='Zombie_15.gif'), PhotoImage(file='Zombie_16.gif'),
            PhotoImage(file='Zombie_17.gif'), PhotoImage(file='Zombie_18.gif'),
            PhotoImage(file='Zombie_19.gif'), PhotoImage(file='Zombie_20.gif'),
            PhotoImage(file='Zombie_21.gif')
            ]
atbg = [    PhotoImage(file='ZombieAttack_0.gif'), PhotoImage(file='ZombieAttack_1.gif'),
            PhotoImage(file='ZombieAttack_2.gif'), PhotoImage(file='ZombieAttack_3.gif'),
            PhotoImage(file='ZombieAttack_4.gif'), PhotoImage(file='ZombieAttack_5.gif'),
            PhotoImage(file='ZombieAttack_6.gif'), PhotoImage(file='ZombieAttack_7.gif'),
            PhotoImage(file='ZombieAttack_8.gif'), PhotoImage(file='ZombieAttack_9.gif'),
            PhotoImage(file='ZombieAttack_10.gif'), PhotoImage(file='ZombieAttack_11.gif'),
            PhotoImage(file='ZombieAttack_12.gif'), PhotoImage(file='ZombieAttack_13.gif'),
            PhotoImage(file='ZombieAttack_14.gif'), PhotoImage(file='ZombieAttack_15.gif'),
            PhotoImage(file='ZombieAttack_16.gif'), PhotoImage(file='ZombieAttack_17.gif'),
            PhotoImage(file='ZombieAttack_18.gif'), PhotoImage(file='ZombieAttack_19.gif'), 
            PhotoImage(file='ZombieAttack_20.gif')
            ]
dbg = [     PhotoImage(file='ZombieDie_0.gif'), PhotoImage(file='ZombieDie_1.gif'),
            PhotoImage(file='ZombieDie_2.gif'), PhotoImage(file='ZombieDie_3.gif'),
            PhotoImage(file='ZombieDie_4.gif'), PhotoImage(file='ZombieDie_5.gif'),
            PhotoImage(file='ZombieDie_6.gif'), PhotoImage(file='ZombieDie_7.gif'),
            PhotoImage(file='ZombieDie_8.gif'), PhotoImage(file='ZombieDie_9.gif'),
            PhotoImage(file='ZombieDie_9.gif'), PhotoImage(file='ZombieDie_9.gif')]
over = PhotoImage(file='GameOver.gif')
sun = PhotoImage(file='Sun_11.gif')
while True:
    while loop < 1000:
        for l in ses:
            pos = cv.coords(l.id)
            l.x1, l.y1, l.x2, l.y2 = pos[0], pos[1], pos[0]+78, pos[1]+78
            if l.y2 <= l.stop:
                cv.move(l.id, 0, 3)
            if l.move == True:
                if l.x1 > 0:
                    cv.move(l.id, (0-l.x1)/18, 0)
                if l.y1 < 600:
                    cv.move(l.id, 0, (600-l.y1)/18)
            if l.x1 <= 20 and l.y1 >= 580:
                cv.delete(l.id)
                ses.remove(l)
                sunlights += 25
                sunlight_update()
        for zz in zs:
            if zz.x1 <= 106:
                cv.create_image(300, 0, image=over,anchor='nw')
            for g in plants:
                if g.road == zz.road:
                    if zz.x1 + 80 < g.x2 and zz.y1 + 60 <= g.y2 and zz.y1 + 60 >= g.y1:
                        zz.fast = 0               #检测是否碰到植物
                        zz.bg = zz.atbg
                        g.attacked = True
                        g.eating.append(zz)
            draw(zz, True, zz.bg)
        for pp in ps:                             #植物动画
            draw(pp, False, pp.bg)
        for ss in sunflowers:
            draw(ss, False, ss.bg)
            if loop == ss.make_sunlight_time:
                ss.make_times += 1
                if ss.make_times == 2:
                    sunlight1 = sunlight(ss.x1+30, ss.y1, sun, ss.y1 + 100)
                    ses.append(sunlight1)
                    ss.make_times = 0
        for bb in bs:
            cv.move(bb.id, 10, 0)                  #子弹移动
            bb.x1 += 10
            if bb.x1 >= 1300:                     #飞出屏幕后清除子弹
                cv.delete(bb.id)
                bs.remove(bb)
            for zz in zs:
                if zz.road == bb.road and bb.x1 - 30 >= zz.x1 and bb in bs:
                    cv.delete(bb.id)              #检测是否碰到僵尸
                    bs.remove(bb)
                    zz.hp -= 10
                if zz.hp <= 0:                  #僵尸死亡
                    zz.bg = zz.dbg
                    zz.die = True
                    zz.fast = 0
                    zz.num = 0
                    zz.amslow = 10
                    zz.hp = 10000
        tk.update()
        tk.update_idletasks()
        sleep(0.01)
        if loop % 1000 == 0:                       #生成僵尸
            zy = choice(zypos)
            z2 = z(1300, zy, 3, 4, (zy-30)/97+1, mbg, atbg, dbg)
            zs.append(z2)
        if loop % 200 == 0:
            for pp in plants:
                for zz in zs:
                    if zz.road == pp.road and pp.kind == 'peashooter':        #若这一路有僵尸，发射子弹
                        b = bullet(pp.x1, pp.y1, 0, 0, pp.road, butpic)
                        bs.append(b)
                        break
                if pp.attacked == True:           #检测植物是否被僵尸吃掉
                    pp.hp -= 100
                    if pp.hp <= 0:
                        for e in pp.eating:
                            e.bg = e.mbg
                            e.fast = 0.4      #吃完植物后，恢复走路
                        pp.ad.full = False
                        pp.eating = []
                        cv.delete(pp.id)
                        plants.remove(pp)
                        if pp.kind == 'peashooter':
                            ps.remove(pp)
                        elif pp.kind == 'sunflower':
                            sunflowers.remove(pp)
        if loop == 500:
            s = sunlight(randint(200, 1500), -100, sun, randint(100, 500))
            ses.append(s)
        loop += 1
        if loop == 1000:
            loop = 0