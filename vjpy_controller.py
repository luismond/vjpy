"""vjpy controller."""

import os
from vjpy import VjPyDevice
vjpd = VjPyDevice()

# %% Wav concatenating
print("\nConcatenating wavs.")

notes = [
    38, 38, 40, 38,
    38, 38, 40, 38
    ]
vjpd.write_concatenated_wavs(notes)

# %% Pattern playing
print("\nPlaying a pattern.")
vjpd.play_pattern("khckhkckkhckhkkckhckhkhkckhkchkc")

# %% Bar playing
print("\nPlaying a bar.")
vjpd.play_bar(vjpd.bar_example)

# Bar looping
print("\nLooping a bar.")
vjpd.loop_bar(vjpd.bars_example[0], num_loops=2)

# Bars looping
print("\nLooping a sequence of bars.")
vjpd.loop_bars(vjpd.bars_example, num_loops=1)

# Random pattern generation
print("\nPlaying random pattern.")
rp = vjpd.generate_random_pattern(patt_len=4)
vjpd.play_pattern(rp)

# %% Test midi receiving
for msg in vjpd.yield_midi_msg():
    vjpd.play_drum_wav_from_midi_msg(msg)

# %% Test midi sending
vjpd.send_note(40)

# %% Test video sequencing

# video-sound banks directory
sound_banks_path = os.path.join('vjpy_media', 'sound_banks')
sound_bank_path = os.path.join(sound_banks_path, 'robodrum_bank_3')

# video-sound bank file names
video_filenames = sorted([video_fn for video_fn in os.listdir(sound_bank_path)])


# beats directory
beats_path = os.path.join('vjpy_media', 'beats')
beat_name = 'videobeat-009'
if not beat_name in os.listdir(beats_path):
    os.mkdir(os.path.join(beats_path, beat_name))


beat_directory = os.path.join(beats_path, beat_name)


#%% make video clip objects from video files

video_clips = {}
for video_filename in video_filenames:
    video_path = os.path.join(sound_bank_path, video_filename)
    video_clip = vjpd.get_video_clip(video_path)
    video_clips[video_filename[:-4]] = video_clip


# %% video clips corresponding to 1 drum sound each

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

c_subclips = vjpd.concatenate_subclips(patt2*1)
video_result_path = os.path.join(beat_directory, f'{beat_name}.mp4')
vjpd.write_concatenated_subclips(c_subclips, video_result_path)




