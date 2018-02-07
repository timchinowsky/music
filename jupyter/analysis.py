# Spotify analysis functions

USER_ID = 'gracechinowsky'
CLIENT_ID ='de884d7ced254bc999e0fda964b82934'
CLIENT_SECRET='849c0fb9303a4cc19af7eadc960afff4'



import spotipy
import spotipy.util as util
import json
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import sys
import pretty_midi as pm
import requests
import pyperclip

def spotify_ctrl():
	scope = 'user-read-playback-state,user-library-read,user-modify-playback-state'
	token = util.prompt_for_user_token(USER_ID,scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri='https://www.google.com/')
	spotify = spotipy.Spotify(auth=token)
	return spotify

"""
spotify.current_playback()
spotify.pause_playback()
spotify.seek_track(0)
spotify.start_playback()
spotify.seek_track(0);spotify.start_playback()
spotify.pause_playback();spotify.start_playback()
spotify.pause_playback();spotify.seek_track(0);spotify.start_playback()
spotify.pause_playback();spotify.seek_track(0);
spotify.start_playback()
history
"""

mpl.rcParams['figure.figsize'] = (16,4)

def show(v):
    sys.stderr.write(repr(v)+'\n')
	
def midi_note(name):
		return pm.note_name_to_number(name)
		
def indent(s,ind):
	return ind+('\n'+ind).join(s.splitlines())+'\n'
	
def summ(obj, ind='\t'):
	type_set=set([])
	t = type(obj)
	if t==list:
		desc = '\n' # 'List of '+str(len(obj))+'\n'
		copies = 1
		s = summ(obj[0])
		last = s['desc']
		type_set = type_set.union(s['types'])
		for item in obj[1:]:
			s = summ(item)
			# print s['types']
			type_set = type_set.union(s['types'])
			if s['desc']==last:
				copies +=1
			else:
				if True: # copies>1:
					desc += indent(str(copies)+'x '+last, ind)
				else:
					desc += indent(last, ind)
				last = s['desc']
				copies=1
		if True: # copies>1:
			desc += indent(str(copies)+'x '+last, ind)
		else:
			desc += indent(last, ind)
	else:
		if t==dict or t==requests.structures.CaseInsensitiveDict:
			k = obj.keys()
			desc = '\n' # 'Dict of '+str(len(k))+' keys\n'
			for key in sorted(k):
				s=summ(obj[key])
				desc=desc+indent(key+': '+s['desc'], ind)
				type_set = type_set.union(s['types'])
		else:
			desc = t.__name__+'\n'
	type_set.add(t)
	return {'types':type_set, 'desc':desc}
	
	
def summarize(obj, ind='\t'):
	s = summ(obj, ind)
	pyperclip.copy(s['desc'])
	return s

	
def spotify_get(track, gettype):
	scope = 'user-library-read'
	# token = util.prompt_for_user_token('5gc3kt2m0fhoq1bnadvaxzzo9',scope,client_id='7d1eac2d7f7c441c8ddfe339296e2e00',client_secret='1032f5fd209c49d9a69dde6e39dafaad',redirect_uri='https://www.google.com/')
	token = util.prompt_for_user_token(USER_ID,scope,client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri='https://www.google.com/')
	spotify = spotipy.Spotify(auth=token)
	analysis = spotify.audio_analysis(track)
	r = analysis[gettype]
	return r 



def spotify_track(track):
	scope = 'user-library-read'
	token = util.prompt_for_user_token('5gc3kt2m0fhoq1bnadvaxzzo9',scope,client_id='7d1eac2d7f7c441c8ddfe339296e2e00',client_secret='1032f5fd209c49d9a69dde6e39dafaad',redirect_uri='https://www.google.com/')
	spotify = spotipy.Spotify(auth=token)
	t = spotify.track(track)
	return t 


def analysis_get(analysis, gettype):
	 # get spotify analysis for specified track
	a = analysis[gettype]
	r = {}
	if len(a)>0:
		r['start'] = [ k['start'] for k in a ]
		r['duration'] = [ k['duration'] for k in a ]
		if 'key' in a[0]:
			r['key'] = [ k['key'] for k in a ]
		if 'mode' in a[0]:
			r['mode'] = [ k['mode'] for k in a ]
		if 'pitches' in a[0]:
			r['pitches'] =  [ k['pitches'] for k in a ]    
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
		env.append((b['start'], 0))
		env.append((b['start']+b['duration']/2, 1.0))
	env.append((bars[-1]['start']+bars[-1]['duration'], 0))
	return env

key_roots = range(60,71) # C4-B4

key_root_offsets = {'C':0, 'C#':1, 'Db':1, 'D':2, 'D#':3, 'Eb':3, 'E':4, 'F':5, 'F#':6, 'Gb':6,
					'G':7, 'G#':8, 'Ab':8, 'A':9, 'A#':10, 'Bb':10, 'B':11}

def key_root(key_name):
	if len(key_name)>1:
		if key_name[0:2] in key_root_offsets:
			return key_root_offsets(key_name[0:2])
		else:
			return key_root_offsets(key_name[0])

def mode_chord_offsets(key_name):
	if key_name(-1)=='m':
		return [0, 3, 7]
	else:
		return [0, 4, 7]
	
	
keys = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
key_roots = ['C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4','A4','A#4','B4']
modes =['minor', 'major']
mode_note_add = {'minor':[0, 3, 7], 'major':[0, 4, 7]}
voice_ranges = [['E2', 'E4'], ['C3', 'C5'], ['F3', 'F5'], ['C4', 'C6']]

def key_name(s):
	k = keys[s['key']]
	if s['mode']==0:
		k=k+'m'
	return k
	
def chord_notes(chord_name, note_range):
	if type(chord_name)==list:
		return [chord_notes(c, note_range) for c in chord_notes]
	else:
		if type(note_range[0])==list:
			return(chord_notes(chord_name, nr) for nr in note_range)
		note_range_numbers = midi_numbers(note_range)
		
def midi_numbers(note_names):
	if type(note_names)==str:
		return pm.note_name_to_number(note_names)
	else:
		if type(note_names)==list:
			return [midi_numbers(n) for n in note_names ]
		else:
			if type(note_names)==dict:
				r = {}
				for k in note_names:
					r[k]=midi_numbers(note_names[k])
				return r

		

chord_roots = range(60,71) # C4-B4

chord_root_offsets = {'C':0, 'C#':1, 'Db':1, 'D':2, 'D#':3, 'Eb':3, 'E':4, 'F':5, 'F#':6, 'Gb':6,
										'G':7, 'G#':8, 'Ab':8, 'A':9, 'A#':10, 'Bb':10, 'B':11}

chords = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
chord_roots = ['C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4','A4','A#4','B4']
modes =['minor', 'major']
mode_note_add = {'minor':[0, 3, 7], 'major':[0, 4, 7]}
voice_ranges = [['E2', 'E4'], ['C3', 'C5'], ['F3', 'F5'], ['C4', 'C6']]
voice_balance=[[0.5, 0.5], [0.1, 0.9], [0.9, 0.1], [0.5, 0.5]]


def midi_numbers(note_names):
		if type(note_names)==str:
				return pm.note_name_to_number(note_names)
		else:
				if type(note_names)==list:
						return [midi_numbers(n) for n in note_names ]
				else:
						if type(note_names)==dict:
								r = {}
								for k in note_names:
										r[k]=midi_numbers(note_names[k])
								return r
						
def chord_root(chord_name, octaves=[4]):
		if len(chord_name)>1:
				if chord_name[0:2] in chord_root_offsets:
						offset = chord_root_offsets[chord_name[0:2]]
				else:
						offset = chord_root_offsets[chord_name[0]]
		else:
				offset = chord_root_offsets[chord_name[0]]
		return (np.array(octaves)+1.0)*12 + offset
		
def chord_mode_offsets(chord_name):
		if chord_name[-1]=='m':
				return [0, 3, 7]
		else:
				return [0, 4, 7]
		
def chord_notes(chord_name, octaves=[4]):
		roots = chord_root(chord_name, octaves)
		notes = chord_mode_offsets(chord_name)
		n = []
		for r in roots:
				n += [pm.note_number_to_name(r+note) for note in notes]
		return n

def chord_tones(chord_name, octaves=[4]):
		roots = chord_root(chord_name, octaves)
		notes = chord_mode_offsets(chord_name)
		n = []
		for r in roots:
				n += notes
		return n



def spotify_analysis(track):
	scope = 'user-library-read'
	token = util.prompt_for_user_token('5gc3kt2m0fhoq1bnadvaxzzo9',scope,client_id='7d1eac2d7f7c441c8ddfe339296e2e00',client_secret='1032f5fd209c49d9a69dde6e39dafaad',redirect_uri='https://www.google.com/')
	spotify = spotipy.Spotify(auth=token)
	analysis = spotify.audio_analysis(track)
	for s in analysis['sections']:
		s['key_name']=key_name(s)
		s['note']=chord_notes(s['key_name'])
		s['tone']=chord_tones(s['key_name'])

	return analysis 

def section_analysis(track):
	a = spotify_analysis(track)
	t = spotify_track(track)
	sec = analysis_get(a, 'sections')
	# sys.stderr.write(repr(sec))
	# sys.stderr.write(repr(t))
	sec_ends = list(np.array(sec['start']) + np.array(sec['duration']))

	plt.plot([sec['start'],sec_ends], [sec['key'], list(np.array(sec['key'])+0)])
	for s,k,m in zip(sec['start'],sec['key'],sec['mode']):
		plt.text(s,k,keys[k]+' '+modes[m])
	plt.title('Reported section times and keys for '+t['name']+' (Spotify '+track+')')
	plt.xlabel('Time, s')
	plt.ylabel('Key')

import time
event = []

def analysis_events(a, event):
	for k in a:
		if not k=='tatums' and type(a[k])==list:
			for ii in range(0, len(a[k])):
				#print 'item', item
				#time.sleep(0.1)
				item = a[k][ii]
				event_id=k+str(ii)
				if type(item)==dict and 'start' in item:
					e = {'type':k, 'id':event_id, 'action':'start'}
					e['time']=item['start']
					e['etc']=item
					event.append(e)
					if 'duration' in item:
						e = {'type':k, 'id':event_id, 'action':'stop'}
						e['time']=item['start']+item['duration']
						del item['duration']
						e['etc']=item
						event.append(e)
					del item['start']

def condense_events(events):
	ec=[]
	i0=0
	while i0 < len(events):
		t0 = events[i0]['time']
#		print 't0', t0
		e0 = dict(events[i0])
		del e0['time']
		e = {'time':t0, 'event':[e0]}
		i0 += 1
#		print 't0', t0, 't1', events[i0]['time'], t0-events[i0]['time']<0.00001
		while i0 < len(events) and events[i0]['time']-t0<0.0001:
#			print 'Loop t0', t0, 't1', events[i0]['time']
			e0 = dict(events[i0])
			del e0['time']
			e['event'].append(e0)
			i0 += 1
		ec.append(e)
	return ec

def analyze(id):
	a=spotify_analysis(id)
	event = []
	analysis_events(a,event)
	ecc=condense_events(sorted(event, key=lambda e: e['time']))
	return ecc
	
def timediffplot(ev):
	t=np.array([e['time'] for e in ev])
	dt = np.diff(t)
	print np.min(dt), np.max(dt)
	plt.plot(t[0:-1], dt, 'g.')
	plt.show()

# pick_events(a, [['action', ['start', 'stop']], ['type',['sections']]])

def pick_events(a, cri):
	picked = []
	for elist in a:
		el = []
		for e in elist['event']:
			match=True
			for c in cri:
				if not e[c[0]] in c[1]:
					match=False
					break
			if match:
				el.append(e)
		if len(el)>0:
			picked.append({'time': elist['time'], 'event':sorted(el, key=lambda x: x['action'], reverse=True)}) # hack puts 'stop' before 'start' for correct order of MIDI events
	return picked
	
	
GM_patches = ['Acoustic Grand Piano',
'Bright Acoustic Piano',
'Electric Grand Piano',
'Honky-tonk Piano',
'Electric Piano 1',
'Electric Piano 2',
'Harpsichord',
'Clavi',
'Celesta',
'Glockenspiel',
'Music Box',
'Vibraphone',
'Marimba',
'Xylophone',
'Tubular Bells',
'Dulcimer',
'Drawbar Organ',
'Percussive Organ',
'Rock Organ',
'Church Organ',
'Reed Organ',
'Accordion',
'Harmonica',
'Tango Accordion',
'Acoustic Guitar (nylon)',
'Acoustic Guitar (steel)',
'Electric Guitar (jazz)',
'Electric Guitar (clean)',
'Electric Guitar (muted)',
'Overdriven Guitar',
'Distortion Guitar',
'Guitar harmonics',
'Acoustic Bass',
'Electric Bass (finger)',
'Electric Bass (pick)',
'Fretless Bass',
'Slap Bass 1',
'Slap Bass 2',
'Synth Bass 1',
'Synth Bass 2',
'Violin',
'Viola',
'Cello',
'Contrabass',
'Tremolo Strings',
'Pizzicato Strings',
'Orchestral Harp',
'Timpani',
'String Ensemble 1',
'String Ensemble 2',
'SynthStrings 1',
'SynthStrings 2',
'Choir Aahs',
'Voice Oohs',
'Synth Voice',
'Orchestra Hit',
'Trumpet',
'Trombone',
'Tuba',
'Muted Trumpet',
'French Horn',
'Brass Section',
'SynthBrass 1',
'SynthBrass 2',
'Soprano Sax',
'Alto Sax',
'Tenor Sax',
'Baritone Sax',
'Oboe',
'English Horn',
'Bassoon',
'Clarinet',
'Piccolo',
'Flute',
'Recorder',
'Pan Flute',
'Blown Bottle',
'Shakuhachi',
'Whistle',
'Ocarina',
'Lead 1 (square)',
'Lead 2 (sawtooth)',
'Lead 3 (calliope)',
'Lead 4 (chiff)',
'Lead 5 (charang)',
'Lead 6 (voice)',
'Lead 7 (fifths)',
'Lead 8 (bass + lead)',
'Pad 1 (new age)',
'Pad 2 (warm)',
'Pad 3 (polysynth)',
'Pad 4 (choir)',
'Pad 5 (bowed)',
'Pad 6 (metallic)',
'Pad 7 (halo)',
'Pad 8 (sweep)',
'FX 1 (rain)',
'FX 2 (soundtrack)',
'FX 3 (crystal)',
'FX 4 (atmosphere)',
'FX 5 (brightness)',
'FX 6 (goblins)',
'FX 7 (echoes)',
'FX 8 (sci-fi)',
'Sitar',
'Banjo',
'Shamisen',
'Koto',
'Kalimba',
'Bag pipe',
'Fiddle',
'Shanai',
'Tinkle Bell',
'Agogo',
'Steel Drums',
'Woodblock',
'Taiko Drum',
'Melodic Tom',
'Synth Drum',
'Reverse Cymbal',
'Guitar Fret Noise',
'Breath Noise',
'Seashore',
'Bird Tweet',
'Telephone Ring',
'Helicopter',
'Applause',
'Gunshot']









































































































































































































































































































































































































































































































































































































































































































































































































































































































"""
plt.figure()
section_analysis('3kW6TmJZY1jLf1PXlLdANt')
plt.figure()
section_analysis('2bqfMrkx6iaCzJ6vXtAHsX')
#plt.figure()
#section_analysis('50piV6SES6BqXrBldVW57I')
plt.figure()
section_analysis('5W3cjX2J3tjhG8zb6u0qHn')
plt.figure()
section_analysis('30NTB3ooCZlzJPv13pihQh')
"""