# """videobeat clips and patterns"""


# # %% soundbank_name = 'drums_06' 'african kid drummer, rhythm a'
# soundbank_dir_path = os.path.join(vjpd.soundbanks_path, soundbank_name)
# soundbank_video_path = os.path.join(soundbank_dir_path, f'{soundbank_name}.mp4')
# soundbank_videoclip = vjpd.get_videoclip(soundbank_video_path)

# dur = .5
# # chunks
# a = vjpd.get_videosubclip(soundbank_videoclip, start=02.1120, duration=dur)
# b = vjpd.get_videosubclip(soundbank_videoclip, start=02.6340, duration=dur)
# c = vjpd.get_videosubclip(soundbank_videoclip, start=03.1240, duration=dur)
# d = vjpd.get_videosubclip(soundbank_videoclip, start=03.6450, duration=dur)

# e = vjpd.get_videosubclip(soundbank_videoclip, start=04.1694, duration=dur)
# f = vjpd.get_videosubclip(soundbank_videoclip, start=04.6664, duration=dur)
# g = vjpd.get_videosubclip(soundbank_videoclip, start=05.1600, duration=dur)
# h = vjpd.get_videosubclip(soundbank_videoclip, start=05.6600, duration=dur)

# i = vjpd.get_videosubclip(soundbank_videoclip, start=06.1514, duration=dur)
# j = vjpd.get_videosubclip(soundbank_videoclip, start=06.6787, duration=dur)
# k = vjpd.get_videosubclip(soundbank_videoclip, start=07.1909, duration=dur)
# l = vjpd.get_videosubclip(soundbank_videoclip, start=07.6833, duration=dur)

# m = vjpd.get_videosubclip(soundbank_videoclip, start=08.1850, duration=dur)
# n = vjpd.get_videosubclip(soundbank_videoclip, start=08.7360, duration=dur)

# # PATTERNS 
#           # 12345678
# patt_01 = [a,b,c,d]
# patt_02 = [e,f,g,h]
# patt_03 = [a,b,c,d]
# patt_04 = [e,f,f,h]

# patt_05 = [a,b,c,d]
# patt_06 = [e,f,g,h]
# patt_07 = [i,j,k,l]
# patt_08 = [n,n,n,n]

# # BARS
#         # |1 . . . |2 . . . |3 . . . |4 . . . 
# bar_01 = [patt_01, patt_02, patt_03, patt_04 ]
# bar_02 = [patt_05, patt_06, patt_07, patt_08 ]
# bars = [bar_01, bar_02]

# # %% soundbank_name = 'drums_06' 'african kid drummer, rhythm b'
# dur = .3

# a = vjpd.get_videosubclip(soundbank_videoclip, start=02.1120, duration=dur)
# b = vjpd.get_videosubclip(soundbank_videoclip, start=02.6340, duration=dur)
# c = vjpd.get_videosubclip(soundbank_videoclip, start=03.1240, duration=dur)
# d = vjpd.get_videosubclip(soundbank_videoclip, start=03.6450, duration=dur)

# e = vjpd.get_videosubclip(soundbank_videoclip, start=04.1694, duration=dur)
# f = vjpd.get_videosubclip(soundbank_videoclip, start=04.6664, duration=dur)
# g = vjpd.get_videosubclip(soundbank_videoclip, start=05.1600, duration=dur)
# h = vjpd.get_videosubclip(soundbank_videoclip, start=05.6600, duration=dur)

# i = vjpd.get_videosubclip(soundbank_videoclip, start=06.1514, duration=dur)
# j = vjpd.get_videosubclip(soundbank_videoclip, start=06.6787, duration=dur)
# k = vjpd.get_videosubclip(soundbank_videoclip, start=07.1909, duration=dur)
# l = vjpd.get_videosubclip(soundbank_videoclip, start=07.6833, duration=dur)

# m = vjpd.get_videosubclip(soundbank_videoclip, start=08.1850, duration=dur)
# n = vjpd.get_videosubclip(soundbank_videoclip, start=08.7360, duration=dur)


# # PATTERNS 
#           # 12345678
# patt_01 = [a,b,c,d]
# patt_02 = [a,a,c,d]
# patt_03 = [a,b,c,d]
# patt_04 = [a,a,c,e]

# patt_05 = [a,b,c,d]
# patt_06 = [a,a,c,d]
# patt_07 = [a,b,c,d]
# patt_08 = [a,a,g,h]

# patt_09 = [g,h,g,h]


# # BARS
#         # |1 . . . |2 . . . |3 . . . |4 . . . 
# bar_01 = [patt_01, patt_02, patt_03, patt_04 ]
# bar_02 = [patt_05, patt_06, patt_07, patt_08 ]

# bars = [bar_01, bar_01, bar_01, bar_02,
#         bar_01, bar_01, bar_01, bar_02,]

# # %% soundbank_name = 'cello_01' # 'subway asian cellist'

# dur = .6
# a = vjpd.get_videosubclip(soundbank_videoclip, start=01.025, duration=dur)
# b = vjpd.get_videosubclip(soundbank_videoclip, start=03.209, duration=dur)
# c = vjpd.get_videosubclip(soundbank_videoclip, start=04.271, duration=dur)
# d = vjpd.get_videosubclip(soundbank_videoclip, start=08.531, duration=dur)

# # PATTERNS
#           # 12345678
# patt_00 = [a,b,c,d ]
# patt_01 = [b,b,b,b ]
# patt_02 = [b,b,d,d ]

# # BARS
#         # |1 . . . |2 . . . |3 . . . |4 . . . 
# bar_01 = [patt_01, patt_02, patt_01, patt_02 ]
# bars = [bar_01, bar_01, bar_01, bar_01]


# # %% soundbank_name = 'drums_03' # me, denim jacket, single hits
# dur = 0.15

# b = vjpd.get_videosubclip(soundbank_videoclip, start=00.100, duration=dur) # bell
# r = vjpd.get_videosubclip(soundbank_videoclip, start=03.710, duration=dur) # ride
# x = vjpd.get_videosubclip(soundbank_videoclip, start=07.137, duration=dur) # china
# c = vjpd.get_videosubclip(soundbank_videoclip, start=09.770, duration=dur) # crash1
# d = vjpd.get_videosubclip(soundbank_videoclip, start=13.220, duration=dur) # crash2
# i = vjpd.get_videosubclip(soundbank_videoclip, start=17.800, duration=dur) # hat1 pedal
# j = vjpd.get_videosubclip(soundbank_videoclip, start=19.390, duration=dur) # hat2
# h = vjpd.get_videosubclip(soundbank_videoclip, start=21.290, duration=dur) # hat3
# y = vjpd.get_videosubclip(soundbank_videoclip, start=23.700, duration=dur) # hat5
# o = vjpd.get_videosubclip(soundbank_videoclip, start=23.113, duration=dur) # hat4 open
# k = vjpd.get_videosubclip(soundbank_videoclip, start=24.950, duration=dur) # kick1
# l = vjpd.get_videosubclip(soundbank_videoclip, start=26.050, duration=dur) # kick2
# s = vjpd.get_videosubclip(soundbank_videoclip, start=27.513, duration=dur) # snare1
# z = vjpd.get_videosubclip(soundbank_videoclip, start=29.512, duration=dur) # snare2
# t = vjpd.get_videosubclip(soundbank_videoclip, start=31.505, duration=dur) # tom1a
# v = vjpd.get_videosubclip(soundbank_videoclip, start=34.248, duration=dur) # tom1b
# w = vjpd.get_videosubclip(soundbank_videoclip, start=37.160, duration=dur) # tom2a
# u = vjpd.get_videosubclip(soundbank_videoclip, start=39.010, duration=dur) # tom2b
# _ = vjpd.get_videosubclip(soundbank_videoclip, start=01.500, duration=dur) # silence
# # patterns and bars
#           # 1.2.3.4.
# patt_01 = [k,_,h,_ ] # bar 01
# patt_02 = [s,_,h,_ ]
# patt_03 = [k,_,h,h ]
# patt_04 = [z,_,h,_ ]
#           # 1.2.3.4.
# patt_05 = [k,_,h,_ ] # bar 02
# patt_06 = [s,_,h,_ ]
# patt_07 = [k,k,h,h ]
# patt_08 = [z,_,o,_ ]
#           # 1.2.3.4.
# patt_09 = [k,_,h,_ ] # bar 03
# patt_10 = [s,_,h,s ]
# patt_11 = [k,_,h,h ]
# patt_12 = [z,_,h,_ ]
#           # 1.2.3.4.
# patt_13 = [k,_,h,_ ] # bar 04
# patt_14 = [s,_,h,h ]
# patt_15 = [w,_,u,_ ]
# patt_16 = [s,z,s,z ]
#           # 1.2.3.4.
# patt_17 = [k,_,h,k ] # bar 05
# patt_18 = [s,_,h,b ]
# patt_19 = [k,_,h,_ ]
# patt_20 = [z,_,h,x ]
#           # 1.2.3.4.
# patt_21 = [k,_,h,k ] # bar 06
# patt_22 = [s,_,h,b ]
# patt_23 = [k,_,h,_ ]
# patt_24 = [z,_,h,c ]
#           # 1.2.3.4.
# patt_25 = [k,_,h,k ] # bar 07
# patt_26 = [s,_,h,b ]
# patt_27 = [k,_,h,_ ]
# patt_28 = [z,_,h,d ]
#           # 1.2.3.4.
# patt_29 = [k,_,h,k ] # bar 08
# patt_30 = [s,_,h,b ]
# patt_31 = [k,_,h,_ ]
# patt_32 = [z,s,w,u ]
# # BARS
#         # |1 . . . |2 . . . |3 . . . |4 . . . 
# bar_01 = [patt_01, patt_02, patt_03, patt_04 ]
# bar_02 = [patt_05, patt_06, patt_07, patt_08 ]
# bar_03 = [patt_09, patt_10, patt_11, patt_12 ]
# bar_04 = [patt_13, patt_14, patt_15, patt_16 ]
#         # |1 . . . |2 . . . |3 . . . |4 . . . 
# bar_05 = [patt_17, patt_18, patt_19, patt_20 ]
# bar_06 = [patt_21, patt_22, patt_23, patt_24 ]
# bar_07 = [patt_25, patt_26, patt_27, patt_28 ]
# bar_08 = [patt_29, patt_30, patt_31, patt_32 ]
# bars = [
#         bar_01, bar_02, bar_03, bar_04,
#         bar_01, bar_02, bar_03, bar_04,
#         bar_05, bar_06, bar_07, bar_08,
#         bar_05, bar_06, bar_07, bar_08,
#         ]

# # %% soundbank_name = 'drums_05' # 'african drummer''

# # VJPY!
# dur = .12
# h = vjpd.get_videosubclip(soundbank_video, start=00.5461, duration=dur) # hat
# k = vjpd.get_videosubclip(soundbank_video, start=07.6810, duration=dur) # kick
# s = vjpd.get_videosubclip(soundbank_video, start=04.3190, duration=dur) # snare
# x = vjpd.get_videosubclip(soundbank_video, start=06.9290, duration=dur) # kick+crash
# _ = vjpd.get_videosubclip(soundbank_video, start=00.1280, duration=dur) # silence


# # PATTERNS 
# #         |01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   
# patt_01 = [k,   _,   _,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
# patt_02 = [k,   _,   _,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
# patt_03 = [k,   _,   k,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
# patt_04 = [k,   _,   _,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   x,   _   ]

# patt_05 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
# patt_06 = [k,   _,   h,   h,   h,   h,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
# patt_07 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
# patt_08 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   s,   _,   h,   h   ]

# patt_09 = [k,   _,   _,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
# patt_10 = [k,   _,   _,   h,   k,   h,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
# patt_11 = [k,   _,   k,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   _,   _   ]
# patt_12 = [k,   _,   _,   _,   k,   _,   _,   _,   s,   _,   _,   _,   k,   _,   x,   _   ]

# patt_13 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
# patt_14 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
# patt_15 = [k,   _,   h,   _,   h,   _,   h,   _,   s,   _,   h,   _,   h,   _,   h,   _   ]
# patt_16 = [k,   _,   k,   _,   k,   _,   k,   _,   s,   s,   s,   s,   h,   h,   h,   h   ]

# patt_17 = [k,   k,   h,   _,   s,   _,   k,   _,   k,   k,   h,   _,   s,   _,   k,   _,  ]
# patt_18 = [k,   k,   h,   _,   s,   _,   k,   _,   k,   k,   h,   _,   s,   s,   x,   x,  ]

# # BARS
# #        |1 . . . |2 . . . |3 . . . |4 . . . 
# bar_01 = [patt_01, patt_02, patt_03, patt_04 ]
# bar_02 = [patt_05, patt_06, patt_07, patt_08 ]
# bar_03 = [patt_09, patt_10, patt_11, patt_12 ]
# bar_04 = [patt_13, patt_14, patt_15, patt_16 ]
# bar_05 = [patt_17, patt_17, patt_17, patt_18 ]

# bars = [bar_01]


# # %% soundbank_name = 'drums_07' # "fun emerging drums"

# # CLIPS
# dur = .15
# h = vjpd.get_videosubclip(soundbank_video, start=00.8070 ,duration=dur) # hat
# k = vjpd.get_videosubclip(soundbank_video, start=23.8760, duration=dur) # kick
# s = vjpd.get_videosubclip(soundbank_video, start=03.0156, duration=dur) # snare
# t = vjpd.get_videosubclip(soundbank_video, start=39.1680, duration=dur) # snare
# r = vjpd.get_videosubclip(soundbank_video, start=33.4865, duration=dur) # ride
# _ = vjpd.get_videosubclip(soundbank_video, start=02.6210, duration=dur) # silence

# # PATTERN
# #         |01   02   03   04   05   06   07   08    09   10   11   12   13   14   15   16   
# patt_00 = [k,   _,   k,   _,   k,   _,   k,   _,    s,   s,   h,   h,   r,   r,   t,   t   ]

# #         |01   02   03   04   05   06   07   08    09   10   11   12   13   14   15   16   
# patt_01 = [k,   _,   k,   _,   s,   h,   h,   s,    k,   _,   h,   _,   s,   _,   h,   _   ]
# patt_02 = [k,   h,   k,   _,   s,   _,   h,   s,    k,   _,   k,   _,   s,   k,   k,   s   ]
# patt_03 = [k,   _,   k,   _,   s,   h,   h,   s,    k,   _,   h,   _,   s,   _,   h,   _   ]
# patt_04 = [k,   h,   k,   _,   s,   _,   h,   s,    k,   _,   k,   _,   s,   r,   r,   r   ]

# #         |01   02   03   04   05   06   07   08    09   10   11   12   13   14   15   16   
# patt_08 = [k,   h,   h,   h,   s,   h,   h,   s,    k,   h,   h,   h,   s,   r,   r,   r   ]

# #         |01   02   03   04   05   06   07   08    09   10   11   12   13   14   15   16   
# patt_09 = [k,   k,   k,   _,   s,   h,   h,   h,    k,   _,   r,   r,   s,   s,   t,   t   ]


# # BARS
# bar_00 = [patt_00]
# bar_01 = [patt_01, patt_02, patt_03, patt_02 ]
# bar_02 = [patt_01, patt_02, patt_03, patt_04 ]
# bar_03 = [patt_01, patt_02, patt_03, patt_08 ]
# bar_04 = [patt_01, patt_02, patt_03, patt_09 ]
# bars = [bar_01]

# # %% soundbank_name = 'drums_08' # "overqualified drummer"

# # # CLIPS
# dur = .18
# h = vjpd.get_videosubclip(soundbank_video, start=02.5300 ,duration=dur) # hat
# t = vjpd.get_videosubclip(soundbank_video, start=06.6548, duration=dur) # kick 
# k = vjpd.get_videosubclip(soundbank_video, start=53.0572, duration=dur) # kick2
# s = vjpd.get_videosubclip(soundbank_video, start=07.2790, duration=dur) # snare
# z = vjpd.get_videosubclip(soundbank_video, start=21.9867, duration=dur) # snare2
# _ = vjpd.get_videosubclip(soundbank_video, start=00.0000, duration=dur) # silence

# # PATTERN
# #         |01   02   03   04   05   06   07   08    09   10   11   12   13   14   15   16   

# #         |01   02   03   04    05   06   07   08    09   10   11   12    13   14   15   16   
# patt_01 = [k,   _,   _,   z,    k,   _,   s,   _,    k,   _,   _,   z,    k,   _,   s,   _,  ]
# patt_02 = [k,   _,   _,   z,    k,   _,   s,   _,    k,   k,   _,   z,    k,   _,   s,   s,  ]
# patt_03 = [k,   _,   _,   z,    k,   _,   s,   _,    k,   _,   _,   z,    k,   _,   s,   _,  ]
# patt_04 = [k,   _,   _,   z,    k,   _,   s,   _,    k,   k,   _,   z,    k,   s,   s,   k,  ]

# # BARS
# bar_01 = [patt_01, patt_02, patt_03, patt_04 ]
# bars = [bar_01, bar_01, bar_01, bar_01]

# bankname = "drums_03"
# # drum_subclips = {
#     "r": vd.get_subclip(videoclip, start=03.710), # ride
#     "x": vd.get_subclip(videoclip, start=07.137), # china
#     "c": vd.get_subclip(videoclip, start=09.770), # crash
#     "h": vd.get_subclip(videoclip, start=21.290), # hat
#     "o": vd.get_subclip(videoclip, start=23.113), # hat open
#     "k": vd.get_subclip(videoclip, start=24.950), # kick
#     "s": vd.get_subclip(videoclip, start=27.513), # snare1
#     "z": vd.get_subclip(videoclip, start=29.512), # snare2
#     "t": vd.get_subclip(videoclip, start=31.505), # tom1a
#     "v": vd.get_subclip(videoclip, start=34.248), # tom1b
#     "w": vd.get_subclip(videoclip, start=37.160), # tom2a
#     "u": vd.get_subclip(videoclip, start=39.010), # tom2b
#     "_": vd.get_subclip(videoclip, start=06.005)  # silence
# }
