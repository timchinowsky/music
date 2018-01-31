# get spotify analysis for specified track


import spotipy
import spotipy.util as util
import json
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from pyo import *
import math
import sys
import itertools as it

mpl.rcParams['figure.figsize'] = (16,6)

#track = '2bqfMrkx6iaCzJ6vXtAHsX' # violin scale with click
track = '5v2Zz8H3DaVYN1CEQSYXRl' # bad horse chorus
track = '3kW6TmJZY1jLf1PXlLdANt' # computer world


scope = 'user-library-read'
token = util.prompt_for_user_token('5gc3kt2m0fhoq1bnadvaxzzo9',scope,client_id='7d1eac2d7f7c441c8ddfe339296e2e00',client_secret='1032f5fd209c49d9a69dde6e39dafaad',redirect_uri='https://www.google.com/')
spotify = spotipy.Spotify(auth=token)
analysis=spotify.audio_analysis(track)
json = json.dumps(analysis)
f = open("c:/data/analysis_"+track+".json","w")
f.write(json)
f.close()

n_bars = len(analysis['bars'])
n_segments = len(analysis['segments'])
n_beats = len(analysis['beats'])
n_tatums = len(analysis['tatums'])

#print n_bars,'bars, ', n_segments, 'segments,', n_beats, 'beats,', n_tatums, 'tatums'

bar_starts = [ k['start'] for k in analysis['bars'] ]
bar_ends = [ k['start']+k['duration'] for k in analysis['bars'] ]

segment_starts = [ k['start'] for k in analysis['segments'] ]
segment_ends = [ k['start']+k['duration'] for k in analysis['segments'] ]

beat_starts = [ k['start'] for k in analysis['beats'] ]
beat_ends = [ k['start']+k['duration'] for k in analysis['beats'] ]

tatum_starts = [ k['start'] for k in analysis['tatums'] ]
tatum_ends = [ k['start']+k['duration'] for k in analysis['tatums'] ]

bar_y=0
segment_y=1
beat_y=2
tatum_y=3
delta_y=0.5

if False:
    plt.plot([bar_starts, bar_ends], [[bar_y]*len(bar_starts), [bar_y+delta_y]*len(bar_starts)],'b-')
    plt.plot([segment_starts, segment_ends], [[segment_y]*len(segment_starts), [segment_y+delta_y]*len(segment_starts)], 'g-')
    plt.plot([beat_starts, beat_ends], [[beat_y]*len(beat_starts), [beat_y+delta_y]*len(beat_starts)], 'r-')
    plt.plot([tatum_starts, tatum_ends], [[tatum_y]*len(tatum_starts), [tatum_y+delta_y]*len(tatum_starts)], 'c-')
    plt.title('Bars, segments, beats, tatums');
    plt.text(0,bar_y+delta_y/2, 'Bars', horizontalalignment='right')
    plt.text(0,segment_y+delta_y/2, 'Segments', horizontalalignment='right')
    plt.text(0,beat_y+delta_y/2, 'Beats', horizontalalignment='right')
    plt.text(0,tatum_y+delta_y/2, 'Tatums', horizontalalignment='right')

# Play clicks and recorded track at same time

s = Server().boot()
s.start()
snds = ['wav/spotify '+track+'.wav']

tabs = SndTable(snds)
vt = tabs[1].getTable()
d = tabs.getDur()
print d, len(vt)
mv = np.max(vt)
tt = np.linspace(0,d[0],len(vt))


bar_starts = [b[0] for b in zip(bar_starts, bar_ends) if b[0]<=d[0]]
bar_ends =   [b[1] for b in zip(bar_starts, bar_ends) if b[0]<=d[0]]
beat_starts = [b[0] for b in zip(beat_starts, beat_ends) if b[0]<=d[0]]
beat_ends = [b[1] for b in zip(beat_starts, beat_ends) if b[0]<=d[0]]


maxpts = 10000
tt = list(it.islice(tt, 0, None, math.floor(len(tt)/maxpts)))
vt = list(it.islice(vt, 0, None, math.floor(len(vt)/maxpts)))

plt.plot(tt, vt, 'gray')
plt.plot([bar_starts, bar_ends], [[0]*len(bar_starts), [mv/4]*len(bar_starts)],'b-')
plt.plot([beat_starts, beat_ends], [[0]*len(beat_starts), [mv/4]*len(beat_starts)], 'r-');


beat_delay = beat_starts[0]
beat_space = list(np.diff(beat_starts))

bar_delay = bar_starts[0]
bar_space = list(np.diff(bar_starts))

# play music
seq = Seq(time=0, seq=[0],onlyonce=True).play()
amp = TrigEnv(seq, tabs, dur=d, mul=.25).out()

# play beat click
d_snds = ['wav/alum3.wav']
d_tabs = SndTable(d_snds)
d_seq = Seq(time=1, seq=beat_space, onlyonce=True).play(delay=beat_delay)
d_amp = TrigEnv(d_seq, d_tabs, dur=.25, mul=.25).out()

# play bar click
d2_snds = ['wav/alum1.wav']
d2_tabs = SndTable(d2_snds)
d2_seq = Seq(time=1, seq=bar_space, onlyonce=True).play(delay=bar_delay)
d2_amp = TrigEnv(d2_seq, d2_tabs, dur=.25, mul=.6).out()

