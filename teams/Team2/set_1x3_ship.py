import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
texture=51
light=89
fire=51
body=-1
down= 152
middle=42
up=98
inside=5
bomb= 46
glass= 20
def attack(n):
        if n == 1:
                for aattack in range(4):
                        for battack in range(3):
                                mc.setBlock(x-5-aattack,y+6,z-1+battack,fire)
        if n == 2:
                for cattack in range(8):
                        for dattack in range(5):
                                mc.setBlock(x-19-cattack,y+6,z-2+dattack,fire)
                                mc.setBlock(x-18-cattack,y+11,z-2+dattack,fire)
        if n == 3:
                for eattack in range(8):
                        for fattack in range(5):
                                mc.setBlock(x-19-14-eattack,y+6,z-2+fattack,fire)
def set_head(x,y,z):
        mc.setBlock(x-3,y-1,z,down)
        for a in range(3):
                mc.setBlock(x-4,y-1,z-1+a,down)
                mc.setBlock(x-5,y-1,z-1+a,down)
        for b in range(5):
                mc.setBlock(x-6,y-1,z-2+b,down)
                mc.setBlock(x-7,y-1,z-2+b,down)
        for c in range(7):
                for d in range(7):
                        mc.setBlock(x-8-c,y-1,z-3+d,down)
        for d in range(2):
                mc.setBlock(x-3,y+d,z,down)
                mc.setBlock(x-4,y+d,z-1,down)
                mc.setBlock(x-4,y+d,z+1,down)
                mc.setBlock(x-5,y+d,z-1,down)
                mc.setBlock(x-5,y+d,z+1,down)
                mc.setBlock(x-6,y+d,z-2,down)
                mc.setBlock(x-6,y+d,z+2,down)
                mc.setBlock(x-7,y+d,z-2,down)
                mc.setBlock(x-7,y+d,z+2,down)
                for e in range(7):
                        mc.setBlock(x-8-e,y+d,z-3,down)
                        mc.setBlock(x-8-e,y+d,z+3,down)
        for iin in range(7):
                mc.setBlock(x-8-iin,y,z-2,down)
                mc.setBlock(x-8-iin,y,z+2,down)
        mc.setBlock(x-2,y+2,z,middle)
        mc.setBlock(x-3,y+2,z-1,middle)
        mc.setBlock(x-3,y+2,z+1,middle)
        mc.setBlock(x-4,y+2,z-1,middle)
        mc.setBlock(x-4,y+2,z+1,middle)
        mc.setBlock(x-5,y+2,z-2,middle)
        mc.setBlock(x-5,y+2,z+2,middle)
        mc.setBlock(x-6,y+2,z-2,middle)
        mc.setBlock(x-6,y+2,z+2,middle)
        for f in range(8):
                mc.setBlock(x-7-f,y+2,z-3,middle)
                mc.setBlock(x-7-f,y+2,z+3,middle)
        mc.setBlock(x-1,y+3,z,up)
        mc.setBlock(x-2,y+3,z,up)
        mc.setBlock(x-3,y+3,z-1,up)
        mc.setBlock(x-3,y+3,z+1,up)
        mc.setBlock(x-4,y+3,z-1,up)
        mc.setBlock(x-4,y+3,z+1,up)
        mc.setBlock(x-5,y+3,z-2,up)
        mc.setBlock(x-5,y+3,z+2,up)
        mc.setBlock(x-6,y+3,z-2,up)
        mc.setBlock(x-6,y+3,z+2,up)
        for g in range(8):
                mc.setBlock(x-7-g,y+3,z-3,up)
                mc.setBlock(x-7-g,y+3,z+3,up)
        mc.setBlock(x-1,y+4,z,up)
        mc.setBlock(x-2,y+4,z-1,up)
        mc.setBlock(x-2,y+4,z+1,up)
        mc.setBlock(x-3,y+4,z-1,up)
        mc.setBlock(x-3,y+4,z+1,up)
        mc.setBlock(x-4,y+4,z-2,up)
        mc.setBlock(x-4,y+4,z+2,up)
        mc.setBlock(x-5,y+4,z-2,up)
        mc.setBlock(x-5,y+4,z+2,up)
        for h in range(9):
                mc.setBlock(x-6-h,y+4,z-3,up)
                mc.setBlock(x-6-h,y+4,z+3,up)
        for i in range(3):
                mc.setBlock(x-i,y+5,z-1,up)
                mc.setBlock(x-i,y+5,z,up)
                mc.setBlock(x-i,y+5,z+1,up)
        mc.setBlock(x-2,y+5,z,light)
        for j in range(5):
                mc.setBlock(x-2-j,y+5,z-2,up)
                mc.setBlock(x-2-j,y+5,z+2,up)
        for k in range(5):
                mc.setBlock(x-6-k,y+5,z-3,up)
                mc.setBlock(x-6-k,y+5,z+3,up)
        for n in range(1):
                for l in range(5):
                        for m in range(3):
                                mc.setBlock(x-3-l,y+5-n,z-1+m,inside)
                        for o in range(5):
                                mc.setBlock(x-6-l,y+5-n,z-2+o,inside)
        mc.setBlock(x-10,y+5,z-2,light)
        mc.setBlock(x-10,y+5,z+2,light)
        for p in range(4):
                for q in range(5):
                        mc.setBlock(x-11-p,y+4,z-2+q,inside)
        for qqe in range(5):
                        mc.setBlock(x-14,y+4,z-2+qqe,up)
        for r in range(2):
                for s in range(4):
                        for t in range(3):
                                mc.setBlock(x-5-s,y+4-r,z-1+t,inside)
        mc.setBlock(x-6,y+4,z,bomb)
        mc.setBlock(x-7,y+4,z,bomb)
        mc.setBlock(x-8,y+4,z,bomb)
        for inin in range(15):
                mc.setBlock(x-inin,y,z+3,0)
                mc.setBlock(x-inin,y,z-3,0)
                mc.setBlock(x-inin,y-1,z+3,0)
                mc.setBlock(x-inin,y-1,z-3,0)

def set_body(x,y,z):
        global body
        body=body+1
        for u in range(14):
                for w in range(5):
                        mc.setBlock(x-15-body*14-u,y-1,z-2+w,down)
                        mc.setBlock(x-15-body*14-u,y+4,z-2+w,inside)
                mc.setBlock(x-15-body*14-u,y,z-2,down)
                mc.setBlock(x-15-body*14-u,y,z+2,down)
                mc.setBlock(x-15-body*14-u,y+1,z-3,down)
                mc.setBlock(x-15-body*14-u,y+1,z+3,down)
                mc.setBlock(x-15-body*14-u,y+2,z-3,middle)
                mc.setBlock(x-15-body*14-u,y+2,z+3,middle)
                for v in range(2):
                        mc.setBlock(x-15-body*14-u,y+3+v,z-3,up)
                        mc.setBlock(x-15-body*14-u,y+3+v,z+3,up)
        for aa in range(5):
                mc.setBlock(x-28-body*14,y+4,z-2+aa,up)
        for bb in range(4):
                mc.setBlock(x-21-body*14-bb,y+4,z,inside)
        for ad in range(3):
                for ab in range(8):
                        for ac in range(5):
                                mc.setBlock(x-19-body*14-ab,y+5-ad,z-2+ac,inside)
        for ae in range(3):
                mc.setBlock(x-21-body*14-ae,y+4,z,bomb)
        mc.setBlock(x-21-body*14,y+4,z-1,bomb)
        mc.setBlock(x-21-body*14-2,y+4,z+1,bomb)
        mc.setBlock(x-21-body*14-1,y+3,z,bomb)
        u=0
        w=0
        v=0
        aa=0
        bb=0
        aa=0
        bb=0
        ad=0
        ab=0
        ac=0
        ae=0
def set_control_tower(x,y,z):
        for cc in range(8):
                for dd in range(5):
                        mc.setBlock(x-19-cc,y+6,z-2+dd,inside)
                        mc.setBlock(x-19-cc,y+8,z-2+dd,inside)
                        mc.setBlock(x-19-cc,y+7,z-2+dd,glass)
                        mc.setBlock(x-18-cc,y+11,z-2+dd,inside)
        mc.setBlock(x-20,y+6,z,light)
        for ee in range(7):
                for ff in range(5):
                        mc.setBlock(x-18-ee,y+9,z-2+ff,up)
                        mc.setBlock(x-18-ee,y+10,z-2+ff,glass)
        mc.setBlock(x-19,y+9,z,light)
        mc.setBlock(x-20,y+10,z,inside)
        mc.setBlock(x-21,y+10,z,bomb)
        mc.setBlock(x-22,y+10,z,bomb)
        mc.setBlock(x-23,y+10,z,inside)
        for gg in range(6):
                for hh in range(3):
                       mc.setBlock(x-19-gg,y+12,z-1+hh,inside)
        for ii in range(3):
                mc.setBlock(x-20,y+13+ii,z,light)
                mc.setBlock(x-22,y+13+ii,z,light)
                mc.setBlock(x-24,y+13+ii,z,light)
def set_bottom(x,y,z,num):
        for jj in range(3):
                mc.setBlock(x-15-14*num,y-1,z-1+jj,down)
                mc.setBlock(x-15-14*num,y,z-1+jj,down)
        for kk in range(5):
                mc.setBlock(x-15-14*num,y+1,z-2+kk,down)
                mc.setBlock(x-15-14*num,y+2,z-2+kk,middle)
                mc.setBlock(x-15-14*num,y+3,z-2+kk,up)
                mc.setBlock(x-15-14*num,y+4,z-2+kk,up)
               
set_head(x,y,z)
set_body(x,y,z)
set_control_tower(x,y,z)
set_body(x,y,z)
set_bottom(x,y,z,2)
               
        

        
        




                
                
