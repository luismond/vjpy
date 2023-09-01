#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""videobeat sounds and patterns"""

# robodrum_bank_3, videobeat-009
a = vjpd.get_video_subclip(video_clips['china'], start=0.05, subclip_duration=.7)
b = vjpd.get_video_subclip(video_clips['crash1'], start=0.05, subclip_duration=.7)
c = vjpd.get_video_subclip(video_clips['crash2'], start=0.05, subclip_duration=.7)
d = vjpd.get_video_subclip(video_clips['ride1'], start=0.045)
e = vjpd.get_video_subclip(video_clips['bell1'], start=0.05)
f = vjpd.get_video_subclip(video_clips['hat1']) # pedal
g = vjpd.get_video_subclip(video_clips['hat2'], start=0.05) 
h = vjpd.get_video_subclip(video_clips['hat3'], start=0.13) 
o = vjpd.get_video_subclip(video_clips['hat4'], start=0.1) # open
j = vjpd.get_video_subclip(video_clips['kick1'], start=0)
k = vjpd.get_video_subclip(video_clips['kick2'], start=0.075)
s = vjpd.get_video_subclip(video_clips['snare1'], start=0.05)
z = vjpd.get_video_subclip(video_clips['snare2'], start=0.075)
o = vjpd.get_video_subclip(video_clips['tom1'], start=0.05)
p = vjpd.get_video_subclip(video_clips['tom2'], start=0.05)
q = vjpd.get_video_subclip(video_clips['tom3'], start=0.05)
r = vjpd.get_video_subclip(video_clips['tom4'], start=0.05)
_ = vjpd.get_video_subclip(video_clips['silence'])


patt2 = [
      # 1  2  3  4  5  6  7  8  # intro
        k, _, k, _, k, _, k, k,
        k, _, k, _, k, _, k, k,
      
       # 1  2  3  4  5  6  7  8  # bum bap
         k, _, s, _, k, _, s, k,
         k, _, s, _, k, _, s, k,
         k, _, s, _, k, _, s, k,
         k, _, s, _, k, _, s, s,

      # # 1  2  3  4  5  6  7  8  # bum bap ts 1
      #   k, h, z, h, k, h, z, h,
      #   k, h, z, h, k, h, z, o,
      #   k, h, z, h, k, h, z, h,
      #   k, h, z, h, k, h, z, o,

      # # 1  2  3  4  5  6  7  8  # bum bap ts 2
      #   k, h, z, h, k, h, z, h,
      #   k, h, z, h, k, h, z, o,
      #   k, h, z, h, k, h, z, h,
      #   k, h, z, h, k, h, z, s,
        
      # # 1  2  3  4  5  6  7  8  # bum bap ts 1b
      #   k, d, z, d, k, d, z, d,
      #   k, d, z, d, k, d, z, e,
      #   k, d, z, d, k, d, z, d,
      #   k, d, z, d, k, d, z, o,

      # # 1  2  3  4  5  6  7  8  # bum bap ts 2b
      #   k, d, z, d, k, d, z, d,
      #   k, d, z, d, k, d, z, e,
      #   k, d, z, d, k, d, z, d,
      #   k, d, z, d, k, d, z, o, a
         ]



video_clip_fn = 'robodrum_bank_4_video_and_sound_cleaned'

## RIGHT HAND
### CYMBALS
a0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=0.087)     # hat_a_R
a1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=0.9)       # hat_b_R
a2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=2.23)      # hat_c_R
__ = vjpd.get_video_subclip(video_clips[video_clip_fn], start=3.50)      # hat_c_R silence

b0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=8.8565)    # crash1_R
b1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=18.51)     # crash2_R
c0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=14.77)     # china_R
d0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=11.05)     # ride_R
d1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=13.25)     # bell_R
d2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=12.76)     # bell_R

### DRUMS
f0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=4.6254)    # snare_R
g0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=6.989)     # tom1_R
h0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=20.46)     # tom2_R
h1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=20.1460)   # tom2_R silence

## LEFT HAND
### CYMBALS
i0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=34.50)     # ride_a_L
i1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=62.52)     # ride_b_L
i2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=65.65)     # bell_b_L
j0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=31.605)    # crash1_a_L
j1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=58.980)    # crash1_b_L
k0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=39.816)    # crash2_a_L
k1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=76.05)     # crash2_b_L
l0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=42.72)     # china_a_L
l1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=68.03)     # china_b_L
l2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=73.16)     # china_c_L

### DRUMS
m0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=27.10)     # snare_a_L
m1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=45.825)     # snare_b_L
m2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=48.10)     # snare_c_L
n0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=29.40)     # tom1_a_L
n1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=51.37)     # tom1_b_L
n2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=51.80)     # tom1_c_L
o0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=37.37)     # tom2_a_L
o1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=78.34)     # tom2_b_L


## RIGHT FOOT
p0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=22.70)     # kick_a
p1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=24.62)     # kick_b
p2 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=25.62)     # kick silence


## LEFT FOOT
q0 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=84.13)     # hat-pedal_a
q1 = vjpd.get_video_subclip(video_clips[video_clip_fn], start=96.305)     # hat-pedal_b


fn = 'robodrum_bank_3_clean'

dur = 0.14

b = vjpd.get_video_subclip(video_clips[fn], start=00.10, duration=dur) # bell
r = vjpd.get_video_subclip(video_clips[fn], start=03.71, duration=dur) # ride

x = vjpd.get_video_subclip(video_clips[fn], start=07.12, duration=dur) # china
c = vjpd.get_video_subclip(video_clips[fn], start=09.71, duration=dur) # crash1
d = vjpd.get_video_subclip(video_clips[fn], start=13.19, duration=dur) # crash2

h = vjpd.get_video_subclip(video_clips[fn], start=17.87, duration=dur) # hat1
i = vjpd.get_video_subclip(video_clips[fn], start=19.39, duration=dur) # hat2
j = vjpd.get_video_subclip(video_clips[fn], start=21.29, duration=dur) # hat3
y = vjpd.get_video_subclip(video_clips[fn], start=23.07, duration=dur) # hat4
o = vjpd.get_video_subclip(video_clips[fn], start=23.66, duration=dur) # hat5

k = vjpd.get_video_subclip(video_clips[fn], start=24.95, duration=dur) # kick1
l = vjpd.get_video_subclip(video_clips[fn], start=26.05, duration=dur) # kick2

s = vjpd.get_video_subclip(video_clips[fn], start=27.51, duration=dur) # snare1
z = vjpd.get_video_subclip(video_clips[fn], start=29.50, duration=dur) # snare2

t = vjpd.get_video_subclip(video_clips[fn], start=31.46, duration=dur) # tom1a
v = vjpd.get_video_subclip(video_clips[fn], start=34.23, duration=dur) # tom1b
w = vjpd.get_video_subclip(video_clips[fn], start=37.16, duration=dur) # tom2a
u = vjpd.get_video_subclip(video_clips[fn], start=39.03, duration=dur) # tom2b

_ = vjpd.get_video_subclip(video_clips[fn], start=01.50, duration=dur) # silence



# test pattern
# patt1 = [
#      # |1 . . . |2 . . . |3 . . . |4 . . . 
#         k,_,_,_, k,_,_,_, k,_,k,_, k,_,k,_,
        
#         k,_,b,_, k,_,b,_, k,_,r,_, k,_,r,_,
#         k,_,x,_, k,_,x,_, k,_,c,_, k,_,d,_,
        
#         k,_,h,_, k,_,i,_, k,_,j,_, k,_,y,_,
#         k,_,o,_, k,_,o,_, k,_,l,_, k,_,l,_,
        
#         k,_,s,_, k,_,z,_, k,_,t,_, k,_,v,_,
#         k,_,w,_, k,_,w,_, k,_,u,_, k,_,u,_,
#         ]

# pattern template
patt = [
      #|1 . . . |2 . . . |3 . . . |4 . . . 
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        
      #|5 . . . |6 . . . |7 . . . |8 . . . 
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        k,_,_,_, k,_,_,_, k,_,_,_, k,_,_,_,
        ]

patt1 = [
    #|1 . . . |2 . . . |3 . . . |4 . . .
      k,h,i,j, s,h,i,j, k,h,i,y, z,h,i,o
      ]

patt2 = [
    #|1 . . . |2 . . . |3 . . . |4 . . .
      k,h,i,j, s,h,i,j, k,h,i,y, s,z,s,z
      ]

patt3 = [
    #|1 . . . |2 . . . |3 . . . |4 . . .
      k,h,i,j, s,h,i,j, k,h,i,y, s,s,s,s
      ]

patt4 = [
    #|1 . . . |2 . . . |3 . . . |4 . . .
      k,x,c,d, s,x,c,r, k,x,c,d, z,x,c,b
      ]

patt5 = [
    #|1 . . . |2 . . . |3 . . . |4 . . .
      k,x,c,d, s,x,c,r, k,x,c,d, z,s,z,s
      ]

patt6 = [
    #|1 . . . |2 . . . |3 . . . |4 . . .
      k,x,c,d, s,x,c,r, k,x,c,d, z,s,z,s
      ]

patts = (patt1*3)+patt2+(patt1*3)+patt3+ (patt4*3)+patt5+(patt4*3)+patt6

