#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:54:48 2023

@author: user
"""



# videobeat-003
patt1 = [
    r, r, rb, r,
    r, r, sh1, ch,
    sh2, sh2, hp, hp,
    hha, hha, hhb, hho,
    
    r, r, rb, r,
    r, r, sh1, ch,
    sh2, sh2, hp, hp,
    hha, hha, hhb, hho
    ]


patt2 = [
    kb, kb, sb, x,
    kb, x, sa, x,
    kb, kb, sb, x,
    kb, x, sa, x,
    
    kb, kb, sb, x,
    kb, x, sa, x,
    kb, kb, sb, sa,
    kb, sa, sb, sa
    ]

patt1 = [
    hha, hha, hha, hha,
    hha, hha, hha, hha,
    hha, hha, hha, hha,
    hha, hha, ch, ch,
    
    hha, hha, hha, hha,
    hha, hha, hha, hha,
    hha, hha, hha, hha,
    sh1, sh1, sh1, sh2,
    ]


kick_snare_patt = [
    kb, x, sb, x,
    kc, kc, x, sb, x,
    kb, x, sb, x,
    kc, kc, x, sb, x,
    
    kb, x, sb, x,
    kc, kc, x, sb, x,
    kb, x, sb, x,
    kc, kc, kc, kc, sb, t1a,
    
    kb, x, sb, x,
    kc, kc, x, sb, x,
    kb, x, sb, x,
    kc, kc, x, sb, x,
    
    kb, x, sb, x,
    kc, kc, x, sb, x,
    kb, kb, kb, kb,
    kc, kc, kc, kc, kc, kc, kc, kc,
    
    kb, x, sb, x,
    kc, kc, x, sb, x,
    kb, x, sb, x,
    kc, kc, x, sb, x,
    
    kb, x, sb, x,
    kc, kc, x, sb, x,
    kb, x, sb, x,
    kc, kc, kc, kc, sb, t1a,
    
    kb, x, sb, x,
    kc, kc, x, sb, x,
    kb, x, sb, x,
    kc, kc, x, sb, x,
    
    kb, x, sb, x,
    kc, kc, x, sb, x,
    kc, kc, kc, kc, kc, kc, kc, kc,
    kc, kc, kc, kc, kc, kc, kc, kc,
    ]


cymb_patt = [
    hha, hha, hha, hha,
    hha, hha, hha, hha,
    hha, hha, hha, hha,
    hha, hha, ch, ch,
    
    hha, hha, hha, hha,
    hha, hha, hha, hha,
    hha, hha, hha, hha,
    sh1, sh1, sh1, sh1,
    ]


# videobeat-007
patt = [j, j, g, s, m, s, h, s,
        j, s, g, s, n, s, h, s,
        j, s, d, s, m, s, d, s,
        j, s, d, s, n, m, n, m,
        
        j, j, g, h, m, s, h, s,
        j, s, g, s, n, s, h, s,
        j, s, d, s, m, d, d, d,
        j, s, d, s, n, m, o, q,
        
        j, j, g, i, m, h, h, s,
        j, s, g, s, n, s, h, s,
        j, s, d, s, m, d, d, d,
        j, s, o, p, n, m, n, m,
        
        j, j, g, i, m, h, h, s,
        j, s, g, s, n, s, h, s,
        j, s, d, s, m, d, d, d,
        j, j, a, b, n, m, o, q,
        
        ]

# robodrum_bank_3, videobeat-009
a = vjpd.get_video_subclip(video_clips['china'], start=0.05, subclip_duration=.7)
#b = vjpd.get_video_subclip(video_clips['crash1'], start=0.05, subclip_duration=.7)
c = vjpd.get_video_subclip(video_clips['crash2'], start=0.05, subclip_duration=.7)


d = vjpd.get_video_subclip(video_clips['ride1'], start=0.045)
e = vjpd.get_video_subclip(video_clips['bell1'], start=0.05)

# f = vjpd.get_video_subclip(video_clips['hat1']) # pedal
# g = vjpd.get_video_subclip(video_clips['hat2'], start=0.05) 
h = vjpd.get_video_subclip(video_clips['hat3'], start=0.13) 
o = vjpd.get_video_subclip(video_clips['hat4'], start=0.1) # open

# j = vjpd.get_video_subclip(video_clips['kick1'], start=0)
k = vjpd.get_video_subclip(video_clips['kick2'], start=0.075)

s = vjpd.get_video_subclip(video_clips['snare1'], start=0.05)
z = vjpd.get_video_subclip(video_clips['snare2'], start=0.075)

# o = vjpd.get_video_subclip(video_clips['tom1'], start=0.05)
# p = vjpd.get_video_subclip(video_clips['tom2'], start=0.05)
# q = vjpd.get_video_subclip(video_clips['tom3'], start=0.05)
# r = vjpd.get_video_subclip(video_clips['tom4'], start=0.05)

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