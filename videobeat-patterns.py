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

# %% african kid a

soundbank_name = 'drums_06'
soundbank_dir_path = os.path.join(vjpd.soundbanks_path, soundbank_name)
soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')
soundbank_videoclip = vjpd.get_videoclip(soundbank_video_path)

dur = .5
#%%
# chunks
a = vjpd.get_videosubclip(soundbank_videoclip, start=02.1120, duration=dur)
b = vjpd.get_videosubclip(soundbank_videoclip, start=02.6340, duration=dur)
c = vjpd.get_videosubclip(soundbank_videoclip, start=03.1240, duration=dur)
d = vjpd.get_videosubclip(soundbank_videoclip, start=03.6450, duration=dur)

e = vjpd.get_videosubclip(soundbank_videoclip, start=04.1694, duration=dur)
f = vjpd.get_videosubclip(soundbank_videoclip, start=04.6664, duration=dur)
g = vjpd.get_videosubclip(soundbank_videoclip, start=05.1600, duration=dur)
h = vjpd.get_videosubclip(soundbank_videoclip, start=05.6600, duration=dur)

i = vjpd.get_videosubclip(soundbank_videoclip, start=06.1514, duration=dur)
j = vjpd.get_videosubclip(soundbank_videoclip, start=06.6787, duration=dur)
k = vjpd.get_videosubclip(soundbank_videoclip, start=07.1909, duration=dur)
l = vjpd.get_videosubclip(soundbank_videoclip, start=07.6833, duration=dur)

m = vjpd.get_videosubclip(soundbank_videoclip, start=08.1850, duration=dur)
n = vjpd.get_videosubclip(soundbank_videoclip, start=08.7360, duration=dur)


# PATTERNS 
         # 12345678
patt_01 = [a,b,c,d]
patt_02 = [e,f,g,h]
patt_03 = [a,b,c,d]
patt_04 = [e,f,f,h]

patt_05 = [a,b,c,d]
patt_06 = [e,f,g,h]
patt_07 = [i,j,k,l]
patt_08 = [n,n,n,n]


# BARS
       # |1 . . . |2 . . . |3 . . . |4 . . . 
bar_01 = [patt_01, patt_02, patt_03, patt_04 ]
bar_02 = [patt_05, patt_06, patt_07, patt_08 ]

bars = [bar_01, bar_02]#, bar_01, bar_02]#, bar_02, bar_01, bar_02]

# make final clip
subclips = []
for bar_ in bars:
    for patt in bar_:
        for subclip in patt:
            subclips.append(subclip)
final_clip = vjpd.concatenate_subclips(subclips)
# save final clip
vjpd.write_concatenated_subclips(final_clip, 'drums_06_beat_1.mp4')

#%% african kid b

dur = .3

# chunks
a = vjpd.get_videosubclip(soundbank_videoclip, start=02.1120, duration=dur)
b = vjpd.get_videosubclip(soundbank_videoclip, start=02.6340, duration=dur)
c = vjpd.get_videosubclip(soundbank_videoclip, start=03.1240, duration=dur)
d = vjpd.get_videosubclip(soundbank_videoclip, start=03.6450, duration=dur)

e = vjpd.get_videosubclip(soundbank_videoclip, start=04.1694, duration=dur)
f = vjpd.get_videosubclip(soundbank_videoclip, start=04.6664, duration=dur)
g = vjpd.get_videosubclip(soundbank_videoclip, start=05.1600, duration=dur)
h = vjpd.get_videosubclip(soundbank_videoclip, start=05.6600, duration=dur)

i = vjpd.get_videosubclip(soundbank_videoclip, start=06.1514, duration=dur)
j = vjpd.get_videosubclip(soundbank_videoclip, start=06.6787, duration=dur)
k = vjpd.get_videosubclip(soundbank_videoclip, start=07.1909, duration=dur)
l = vjpd.get_videosubclip(soundbank_videoclip, start=07.6833, duration=dur)

m = vjpd.get_videosubclip(soundbank_videoclip, start=08.1850, duration=dur)
n = vjpd.get_videosubclip(soundbank_videoclip, start=08.7360, duration=dur)


# PATTERNS 
         # 12345678
patt_01 = [a,b,c,d]
patt_02 = [a,a,c,d]
patt_03 = [a,b,c,d]
patt_04 = [a,a,c,e]

patt_05 = [a,b,c,d]
patt_06 = [a,a,c,d]
patt_07 = [a,b,c,d]
patt_08 = [a,a,g,h]

patt_09 = [g,h,g,h]


# BARS
       # |1 . . . |2 . . . |3 . . . |4 . . . 
bar_01 = [patt_01, patt_02, patt_03, patt_04 ]
bar_02 = [patt_05, patt_06, patt_07, patt_08 ]
#bar_03 = [patt_05, patt_06, patt_09, patt_09 ]


bars = [
        bar_01, bar_01, bar_01, bar_02,
        bar_01, bar_01, bar_01, bar_02,]
        # bar_01, bar_02, bar_01, bar_03,
        # ]

# make final clip
subclips = []
for bar_ in bars:
    for patt in bar_:
        for subclip in patt:
            subclips.append(subclip)
final_clip = vjpd.concatenate_subclips(subclips)
# save final clip
vjpd.write_concatenated_subclips(final_clip, 'drums_06_beat_3.mp4')

# %% cello bank
soundbank_name = 'cello_bank_1'
soundbank_dir_path = os.path.join(vjpd.soundbanks_path, soundbank_name)
soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')
soundbank_videoclip = vjpd.get_videoclip(soundbank_video_path)
dur = .6
a = vjpd.get_videosubclip(soundbank_videoclip, start=01.025, duration=dur)
b = vjpd.get_videosubclip(soundbank_videoclip, start=03.209, duration=dur)
c = vjpd.get_videosubclip(soundbank_videoclip, start=04.271, duration=dur)
d = vjpd.get_videosubclip(soundbank_videoclip, start=08.531, duration=dur)
# PATTERNS
         # 12345678
patt_00 = [a,b,c,d ]
patt_01 = [b,b,b,b ]
patt_02 = [b,b,d,d ]
# BARS
       # |1 . . . |2 . . . |3 . . . |4 . . . 
bar_01 = [patt_01, patt_02, patt_01, patt_02 ]
bars = [bar_01, bar_01, bar_01, bar_01]
# make final clip
subclips = []
for bar_ in bars:
    for patt in bar_:
        for subclip in patt:
            subclips.append(subclip)
final_clip = vjpd.concatenate_subclips(subclips)
# save final clip
vjpd.write_concatenated_subclips(final_clip, 'test_cello.mp4')

#%% robodrum_bank_3
soundbank_name = 'robodrum_bank_3'
soundbank_dir_path = os.path.join(vjpd.soundbanks_path, soundbank_name)
soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')
soundbank_videoclip = vjpd.get_videoclip(soundbank_video_path)
dur = 0.15

b = vjpd.get_videosubclip(soundbank_videoclip, start=00.100, duration=dur) # bell
r = vjpd.get_videosubclip(soundbank_videoclip, start=03.710, duration=dur) # ride
x = vjpd.get_videosubclip(soundbank_videoclip, start=07.137, duration=dur) # china
c = vjpd.get_videosubclip(soundbank_videoclip, start=09.770, duration=dur) # crash1
d = vjpd.get_videosubclip(soundbank_videoclip, start=13.220, duration=dur) # crash2
i = vjpd.get_videosubclip(soundbank_videoclip, start=17.800, duration=dur) # hat1 pedal
j = vjpd.get_videosubclip(soundbank_videoclip, start=19.390, duration=dur) # hat2
h = vjpd.get_videosubclip(soundbank_videoclip, start=21.290, duration=dur) # hat3
y = vjpd.get_videosubclip(soundbank_videoclip, start=23.700, duration=dur) # hat5
o = vjpd.get_videosubclip(soundbank_videoclip, start=23.113, duration=dur) # hat4 open
k = vjpd.get_videosubclip(soundbank_videoclip, start=24.950, duration=dur) # kick1
l = vjpd.get_videosubclip(soundbank_videoclip, start=26.050, duration=dur) # kick2
s = vjpd.get_videosubclip(soundbank_videoclip, start=27.513, duration=dur) # snare1
z = vjpd.get_videosubclip(soundbank_videoclip, start=29.512, duration=dur) # snare2
t = vjpd.get_videosubclip(soundbank_videoclip, start=31.505, duration=dur) # tom1a
v = vjpd.get_videosubclip(soundbank_videoclip, start=34.248, duration=dur) # tom1b
w = vjpd.get_videosubclip(soundbank_videoclip, start=37.160, duration=dur) # tom2a
u = vjpd.get_videosubclip(soundbank_videoclip, start=39.010, duration=dur) # tom2b
_ = vjpd.get_videosubclip(soundbank_videoclip, start=01.500, duration=dur) # silence
# patterns and bars
         # 1.2.3.4.
patt_01 = [k,_,h,_ ] # bar 01
patt_02 = [s,_,h,_ ]
patt_03 = [k,_,h,h ]
patt_04 = [z,_,h,_ ]
          # 1.2.3.4.
patt_05 = [k,_,h,_ ] # bar 02
patt_06 = [s,_,h,_ ]
patt_07 = [k,k,h,h ]
patt_08 = [z,_,o,_ ]
          # 1.2.3.4.
patt_09 = [k,_,h,_ ] # bar 03
patt_10 = [s,_,h,s ]
patt_11 = [k,_,h,h ]
patt_12 = [z,_,h,_ ]
          # 1.2.3.4.
patt_13 = [k,_,h,_ ] # bar 04
patt_14 = [s,_,h,h ]
patt_15 = [w,_,u,_ ]
patt_16 = [s,z,s,z ]
          # 1.2.3.4.
patt_17 = [k,_,h,k ] # bar 05
patt_18 = [s,_,h,b ]
patt_19 = [k,_,h,_ ]
patt_20 = [z,_,h,x ]
          # 1.2.3.4.
patt_21 = [k,_,h,k ] # bar 06
patt_22 = [s,_,h,b ]
patt_23 = [k,_,h,_ ]
patt_24 = [z,_,h,c ]
          # 1.2.3.4.
patt_25 = [k,_,h,k ] # bar 07
patt_26 = [s,_,h,b ]
patt_27 = [k,_,h,_ ]
patt_28 = [z,_,h,d ]
          # 1.2.3.4.
patt_29 = [k,_,h,k ] # bar 08
patt_30 = [s,_,h,b ]
patt_31 = [k,_,h,_ ]
patt_32 = [z,s,w,u ]
# BARS
        # |1 . . . |2 . . . |3 . . . |4 . . . 
bar_01 = [patt_01, patt_02, patt_03, patt_04 ]
bar_02 = [patt_05, patt_06, patt_07, patt_08 ]
bar_03 = [patt_09, patt_10, patt_11, patt_12 ]
bar_04 = [patt_13, patt_14, patt_15, patt_16 ]
        # |1 . . . |2 . . . |3 . . . |4 . . . 
bar_05 = [patt_17, patt_18, patt_19, patt_20 ]
bar_06 = [patt_21, patt_22, patt_23, patt_24 ]
bar_07 = [patt_25, patt_26, patt_27, patt_28 ]
bar_08 = [patt_29, patt_30, patt_31, patt_32 ]
bars = [
        bar_01, bar_02, bar_03, bar_04,
        bar_01, bar_02, bar_03, bar_04,
        bar_05, bar_06, bar_07, bar_08,
        bar_05, bar_06, bar_07, bar_08,
        ]
# make final clip
subclips = []
for bar_ in bars:
    for patt in bar_:
        for subclip in patt:
            subclips.append(subclip)
final_clip = vjpd.concatenate_subclips(subclips)
vjpd.write_concatenated_subclips(final_clip, 'bank3_test.mp4')

soundbank_name = 'drums_05'
soundbank_dir_path = os.path.join(vjpd.soundbanks_path, soundbank_name)
soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')
soundbank_video = vjpd.get_videoclip(soundbank_video_path)

# VJPY!
dur = .12
h = vjpd.get_videosubclip(soundbank_video, start=00.5461, duration=dur) # hat
k = vjpd.get_videosubclip(soundbank_video, start=07.6810, duration=dur) # kick
s = vjpd.get_videosubclip(soundbank_video, start=04.3190, duration=dur) # snare
x = vjpd.get_videosubclip(soundbank_video, start=06.9290, duration=dur) # kick+crash
_ = vjpd.get_videosubclip(soundbank_video, start=00.1280, duration=dur) # silence


soundbank_name = 'drums_06'
soundbank_dir_path = os.path.join(vjpd.soundbanks_path, soundbank_name)
soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')
soundbank_video = vjpd.get_videoclip(soundbank_video_path)

# VJPY!
dur = .12
h = vjpd.get_videosubclip(soundbank_video, start=00.5461, duration=dur) # hat
k = vjpd.get_videosubclip(soundbank_video, start=07.6810, duration=dur) # kick
s = vjpd.get_videosubclip(soundbank_video, start=04.3190, duration=dur) # snare
x = vjpd.get_videosubclip(soundbank_video, start=06.9290, duration=dur) # kick+crash
_ = vjpd.get_videosubclip(soundbank_video, start=00.1280, duration=dur) # silence

# PATTERNS 
#         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
patt_01 = [k,   _,   _,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
patt_02 = [k,   _,   _,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
patt_03 = [k,   _,   k,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
patt_04 = [k,   _,   _,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   x,   _   ]

patt_05 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
patt_06 = [k,   _,   h,   h,   h,   h,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
patt_07 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
patt_08 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   s,   _,   h,   h   ]

patt_09 = [k,   _,   _,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
patt_10 = [k,   _,   _,   h,   k,   h,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
patt_11 = [k,   _,   k,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
patt_12 = [k,   _,   _,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   x,   _   ]

patt_13 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
patt_14 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
patt_15 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
patt_16 = [k,   _,   k,   _,   k,   _,   k,   _,   s,   s,   s,   s,   h,   h,   h,   h   ]

patt_17 = [k,   k,   h,   _,   s,   _,   k,   _,   k,   k,   h,   _,   s,   _,   k,   _,  ]
patt_18 = [k,   k,   h,   _,   s,   _,   k,   _,   k,   k,   h,   _,   s,   s,   x,   x,  ]


# BARS
#        |1 . . . |2 . . . |3 . . . |4 . . . 
bar_01 = [patt_01, patt_02, patt_03, patt_04 ]
bar_02 = [patt_05, patt_06, patt_07, patt_08 ]
bar_03 = [patt_09, patt_10, patt_11, patt_12 ]
bar_04 = [patt_13, patt_14, patt_15, patt_16 ]

bar_05 = [patt_17, patt_17, patt_17, patt_18 ]

bars = [bar_01,
        # bar_01, bar_02, bar_03, bar_05,
        # bar_01, bar_02, bar_03, bar_05,
        ]

# make final clip
subclips = []
for bar_ in bars:
    for patt in bar_:
        for subclip in patt:
            subclips.append(subclip)
final_clip = vjpd.concatenate_subclips(subclips)
# save final clip
vjpd.write_concatenated_subclips(final_clip, 'drums_05_beat_1.mp4')
