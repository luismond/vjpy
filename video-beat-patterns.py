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
