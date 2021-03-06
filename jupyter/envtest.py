
import spotipy
import spotipy.util as util
import json
import matplotlib.pyplot as plt
import numpy as np

def spotify_get(track, gettype):
    scope = 'user-library-read'
    token = util.prompt_for_user_token('5gc3kt2m0fhoq1bnadvaxzzo9',scope,client_id='7d1eac2d7f7c441c8ddfe339296e2e00',client_secret='1032f5fd209c49d9a69dde6e39dafaad',redirect_uri='https://www.google.com/')
    spotify = spotipy.Spotify(auth=token)
    analysis = spotify.audio_analysis(track)
    r = analysis[gettype]
    return r 

def spotify_get_list(track, gettype):
   # get spotify analysis for specified track
    scope = 'user-library-read'
    token = util.prompt_for_user_token('5gc3kt2m0fhoq1bnadvaxzzo9',scope,client_id='7d1eac2d7f7c441c8ddfe339296e2e00',client_secret='1032f5fd209c49d9a69dde6e39dafaad',redirect_uri='https://www.google.com/')
    spotify = spotipy.Spotify(auth=token)
    analysis = spotify.audio_analysis(track)
    a = analysis[gettype]
    r = {}
    if len(a)>0:
        r['start'] = [ k['start'] for k in a ]
        r['duration'] = [ k['duration'] for k in a ]
        if 'key' in a[0]:
            r['key'] = [ k['key'] for k in a ]
        if 'pitches' in a[0]:
            r['pitches'] =  [ k['pitches'] for k in a ]
        
    return r

def bar_envelope(bars, env_type):
    env = []
    for b in bars:
        env.append((b['start'], 1.0))
        env.append((b['start']+b['duration']*.125, 1.0))
        env.append((b['start']+b['duration']*.25, 0.0))
        env.append((b['start']+b['duration']*.875, 1.0))
    env.append((bars[-1]['start']+bars[-1]['duration'], 0.0))
    return env

print bar_envelope(spotify_get('3kW6TmJZY1jLf1PXlLdANt', 'bars'),'')

# Play PadSynth with Expseg envelope over top of track

from pyo import *
import pretty_midi as pm
import numpy as np

print pm.note_name_to_number('C5')
print pm.note_number_to_name(48)
s = Server().boot()
s.start()
bsize = 65536
floop = s.getSamplingRate() / bsize
fbase = midiToHz(60)
t = PadSynthTable(basefreq=fbase, spread=5, bw=10, bwscl=1.0, size=bsize)
# pt = ParaTable().play(dur=4)
fstroke=1.0
#pa = Expseg([(0,0),(fstroke/2,1.0), (fstroke,0)], loop=True)

bb = [(0.49047, 0), (1.42408, 1.0), (2.35769, 0), (3.285285, 1.0), (4.21288, 0), (5.14088, 1.0), (6.06888, 0), (6.99667, 1.0), (7.92445, 0), (8.8514, 1.0), (9.77835, 0), (10.705695, 1.0), (11.63304, 0), (12.560374999999999, 1.0), (13.48772, 0), (14.414235, 1.0), (15.34074, 0), (16.268105, 1.0), (17.19547, 0), (18.12265, 1.0), (19.04983, 0), (19.97681, 1.0), (20.90378, 0), (21.830975000000002, 1.0), (22.75817, 0), (23.685175, 1.0), (24.61219, 0), (25.53651, 1.0), (26.46083, 0), (27.387835000000003, 1.0), (28.31484, 0), (29.241600000000002, 1.0), (30.16836, 0), (31.094855, 1.0), (32.02135, 0), (32.947355, 1.0), (33.87336, 0), (34.80014, 1.0), (35.72692, 0), (36.654939999999996, 1.0), (37.58296, 0), (38.508925, 1.0), (39.4349, 0), (40.359445, 1.0), (41.28399, 0), (42.2109, 1.0), (43.13781, 0), (44.062365, 1.0), (44.98692, 0), (45.913835, 1.0), (46.84075, 0), (47.7679, 1.0), (48.69505, 0), (49.620365, 1.0), (50.54568, 0), (51.474104999999994, 1.0), (52.40253, 0), (53.330705, 1.0), (54.25888, 0), (55.184929999999994, 1.0), (56.11098, 0), (57.032865, 1.0), (57.95475, 0), (58.882, 1.0), (59.80925, 0), (60.7371, 1.0), (61.66495, 0), (62.591764999999995, 1.0), (63.51858, 0), (64.44626, 1.0), (65.37394, 0), (66.29854, 1.0), (67.22314, 0), (68.151045, 1.0), (69.07894, 0), (70.00414500000001, 1.0), (70.92936, 0), (71.85601, 1.0), (72.78266, 0), (73.707835, 1.0), (74.63301, 0), (75.559365, 1.0), (76.48572, 0), (77.412215, 1.0), (78.33871, 0), (79.26601000000001, 1.0), (80.19331, 0), (81.12061, 1.0), (82.04791, 0), (82.97522000000001, 1.0), (83.90252, 0), (84.82756499999999, 1.0), (85.75261, 0), (86.679525, 1.0), (87.60645, 0), (88.53089, 1.0), (89.45532, 0), (90.381415, 1.0), (91.30751, 0), (92.23585999999999, 1.0), (93.16421, 0), (94.090025, 1.0), (95.01583, 0), (95.942855, 1.0), (96.86988, 0), (97.796475, 1.0), (98.72308, 0), (99.64946499999999, 1.0), (100.57585, 0), (101.502225, 1.0), (102.4286, 0), (103.355565, 1.0), (104.28253, 0), (105.21112, 1.0), (106.13971, 0), (107.06532999999999, 1.0), (107.99095, 0), (108.91425, 1.0), (109.83755, 0), (110.29992999999999, 1.0), (110.76231, 0), (111.691645, 1.0), (112.62097, 0), (113.547425, 1.0), (114.47388, 0), (115.40011999999999, 1.0), (116.32637, 0), (117.25238999999999, 1.0), (118.17841, 0), (119.109585, 1.0), (120.04076, 0), (120.965055, 1.0), (121.88935, 0), (122.81340499999999, 1.0), (123.73746, 0), (124.663155, 1.0), (125.58885, 0), (126.51662499999999, 1.0), (127.4444, 0), (128.37181, 1.0), (129.29922, 0), (129.76098, 1.0), (130.22274, 0), (131.14794999999998, 1.0), (132.07317, 0), (132.99967, 1.0), (133.92616, 0), (134.85416500000002, 1.0), (135.78218, 0), (136.708805, 1.0), (137.63543, 0), (138.56191500000003, 1.0), (139.4884, 0), (140.41346000000001, 1.0), (141.33851, 0), (142.264825, 1.0), (143.19114, 0), (144.119325, 1.0), (145.04751, 0), (145.9734, 1.0), (146.8993, 0), (147.826815, 1.0), (148.75432, 0), (149.67909500000002, 1.0), (150.60388, 0), (151.52988, 1.0), (152.45588, 0), (153.3827, 1.0), (154.30952, 0), (155.23632999999998, 1.0), (156.16314, 0), (157.087885, 1.0), (158.01263, 0), (158.93907000000002, 1.0), (159.86551, 0), (160.79221, 1.0), (161.71891, 0), (162.64585499999998, 1.0), (163.57279, 0), (164.49953, 1.0), (165.42627, 0), (166.352385, 1.0), (167.2785, 0), (168.205025, 1.0), (169.13156, 0), (170.05805, 1.0), (170.98454, 0), (171.91078000000002, 1.0), (172.83701, 0), (173.76475, 1.0), (174.6925, 0), (175.61881, 1.0), (176.54512, 0), (177.471035, 1.0), (178.39695, 0), (179.326965, 1.0), (180.25697, 0), (181.18263, 1.0), (182.10829, 0), (183.030855, 1.0), (183.95342, 0), (184.88036, 1.0), (185.8073, 0), (186.73487, 1.0), (187.66244, 0), (188.587955, 1.0), (189.51347, 0), (190.44003, 1.0), (191.36659, 0), (192.29354, 1.0), (193.22049, 0), (194.145555, 1.0), (195.07062, 0), (195.995465, 1.0), (196.92031, 0), (197.84741, 1.0), (198.77451, 0), (199.70305, 1.0), (200.63159, 0), (201.557615, 1.0), (202.48364, 0), (203.40962000000002, 1.0), (204.3356, 0), (205.26133, 1.0), (206.18706, 0), (207.113385, 1.0), (208.03971, 0), (208.96516000000003, 1.0), (209.89061, 0), (210.81852500000002, 1.0), (211.74644, 0), (212.673735, 1.0), (213.60103, 0), (214.52749500000002, 1.0), (215.45397, 0), (216.379395, 1.0), (217.30482, 0), (218.231265, 1.0), (219.15771, 0), (220.08455, 1.0), (221.01139, 0), (221.941345, 1.0), (222.8713, 0), (223.799625, 1.0), (224.72794, 0), (225.6542, 1.0), (226.58047, 0), (227.50324, 1.0), (228.42601, 0), (229.35293, 1.0), (230.27984, 0), (231.208435, 1.0), (232.13704, 0), (233.06402500000002, 1.0), (233.991, 0), (234.914925, 1.0), (235.83885, 0), (236.76717000000002, 1.0), (237.69548, 0), (238.62465, 1.0), (239.55383, 0), (240.48013, 1.0), (241.40643, 0), (242.33299, 1.0), (243.25956, 0), (244.18533499999998, 1.0), (245.11111, 0), (246.03856, 1.0), (246.96602, 0), (247.89206, 1.0), (248.81809, 0), (249.74563, 1.0), (250.67318, 0), (251.598255, 1.0), (252.52333, 0), (253.45047499999998, 1.0), (254.37762, 0), (255.30494000000002, 1.0), (256.23226, 0), (257.159135, 1.0), (258.086, 0), (259.01367, 1.0), (259.94134, 0), (260.86689, 1.0), (261.79244, 0), (262.71942, 1.0), (263.6464, 0), (264.57421000000005, 1.0), (265.50203, 0), (266.428185, 1.0), (267.35434, 0), (268.28238999999996, 1.0), (269.21044, 0), (270.13897000000003, 1.0), (271.06751, 0), (271.994055, 1.0), (272.9206, 0), (273.84787, 1.0), (274.77514, 0), (275.70149000000004, 1.0), (276.62784, 0), (277.55468, 1.0), (278.48152, 0), (279.41006999999996, 1.0), (280.33861, 0), (281.26614, 1.0), (282.19367, 0), (282.658675, 1.0), (283.12368, 0), (284.04994, 1.0), (284.9762, 0), (285.903275, 1.0), (286.83035, 0), (287.75763, 1.0), (288.68491, 0), (289.612595, 1.0), (290.54028, 0), (291.467365, 1.0), (292.39445, 0), (293.32094, 1.0), (294.24743, 0), (295.175165, 1.0), (296.1029, 0), (297.03146, 1.0), (297.96002, 0), (298.889415, 1.0), (299.81881, 0), (300.74489, 1.0), (301.67097, 0), (302.581275, 1.0), (303.49157, 0), (304.39990500000005, 1.0), (305.30824, 0)]
pa = Expseg(bar_envelope(spotify_get('3kW6TmJZY1jLf1PXlLdANt', 'bars'),''), loop=False)
#pa = Expseg(bb, loop=False)
notes1 = ['C4', 'E4', 'G4']
midi1 = [pm.note_name_to_number(n) for n in notes1]
f1=list(np.array(midiToHz(midi1))/fbase)

notes2 = ['C4']
midi2 = [pm.note_name_to_number(n) for n in notes2]
f2=list(np.array(midiToHz(midi2))/fbase)

a = Osc(table=t, freq=f2, mul=pa, phase=[0, 0.5]).out()
pa.play(0)

# play track

snds = ['wav/spotify 50piV6SES6BqXrBldVW57I.wav']
snds = ['wav/spotify 2bqfMrkx6iaCzJ6vXtAHsX.wav']
snds = ['wav/spotify 3kW6TmJZY1jLf1PXlLdANt.wav'] # computer world
tabs = SndTable(snds)
d = tabs.getDur()
seq = Seq(time=0, seq=[0],onlyonce=True).play()
amp = TrigEnv(seq, tabs, dur=d, mul=.25).out()
