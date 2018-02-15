# Play 

import numpy as np

from pyo import *
import sys

import analysis as an
import ui
import time

s = None

def start():
	global s
	s=Server()

	# look for "VirtualMIDISynth"
	o = pm_get_output_devices()
	midi_out = [p[1] for p in zip(o[0],o[1]) if p[0][0]=='V'][0]
	s.setMidiOutputDevice(midi_out)

	# accept input from all MIDI inputs
	s.setMidiInputDevice(99)

	s.boot()
	s.start()

dd_snds = None
dd_tabs = None
dd_seq = None
dd_amp = None
beat_space = None
a = None
rm = None
patch_rhythm = None
patch_harmony = None
ii = 0
n=60
patch=115
vol=64
note=60
newnote=60
patch_rhythm = 115
patch_harmony = 90
patch_rhythm_new = 115
patch_harmony_new = 90

notelist = set([])
d_seq = None
start_time = None
d_func = None
time_last=None

pitches = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def setup(trackid):
	global dd_snds, dd_tabs, dd_seq, dd_amp, beat_space, a, rm, patch_rhythm, patch_harmony, d_seq, d_func
	# play beat click
	dd_snds = ['../wav/alum3.wav']
	dd_tabs = SndTable(dd_snds)
	dd_seq = Seq(time=1, seq=[0], onlyonce=True)
	dd_amp = TrigEnv(dd_seq, dd_tabs, dur=.25, mul=.25).out()
	a=an.analyze(trackid)
	a = an.pick_events(a, [['action', ['start', 'stop']], ['type',['beats','sections','segments']]])
	beat_space = list(np.diff(np.array([e['time'] for e in a])))+[0.0] 
	# Seq seems to ignore the last value in its seq list - needed to add this dummy 0 at end to get all beats

	# channel 1 is rhythm
	# channel 2 is harmony

	s.programout(patch_rhythm,1)

	an.show(an.GM_patches[patch_rhythm])

	s.programout(patch_harmony,2)
	an.show(an.GM_patches[patch_harmony])
	an.show(str(len(beat_space))+' beats')
	d_seq = Seq(time=1, seq=beat_space, onlyonce=True)
	d_func = TrigFunc(d_seq, seq_callback, 'sequence')
	rm = RawMidi(seq_callback)
	
def play():
	global a, start_time, d_seq, ii
	start_time = time.time()
	an.show('delay '+str(a[0]['time']))
	ii=0
	d_seq.play(delay=a[0]['time'])
	
def seq_callback(id, data1=None, data2=None):  
	global ii, patch, vol, s, note, newnote, a, start_time, patch_harmony, patch_rhythm, notelist, dd_seq, time_last, patch_harmony_new, patch_rhythm_new, pitches
	# dd_seq.play()
	if not patch_harmony_new == patch_harmony or not patch_rhythm_new == patch_rhythm:
		patch_rhythm = patch_rhythm_new
		patch_harmony = patch_harmony_new
		s.programout(patch_harmony,2)
		s.programout(patch_rhythm,1)
	if id=='sequence':
		an.show(str(ii)+' time '+str(a[ii]['time']))
		time_last = int(np.floor(a[ii]['time']*1000))
		# an.show(str(time.time()-start_time))
		for e in a[ii]['event']:
		# an.show(e['type']+' '+e['action'])
			if e['type']=='segments':
				pitches = e['etc']['pitches']
			if e['type']=='beats':
				if e['action']=='start': 
					dd_seq.play()
					s.noteout(note,64,1) 
					s.ctlout(123,0,2) # all notes off
					for n in notelist:
						s.noteout(n, vol, 2)
				else:
					s.noteout(note,0,1)
			if e['type']=='sections':
				notes=e['etc']['note']
				if e['action']=='stop': 
					an.show('stop '+str(notes))
					for n in notes:
						nv=an.midi_note(n)
						# s.noteout(nv,0,2)
						notelist.remove(nv)
				if e['action']=='start':
					an.show('start '+str(notes))
					for n in notes:
						nv=an.midi_note(n)
						#an.show(nv)
						#s.noteout(nv,vol,2)
						notelist.add(nv)
		if not ui.sliders==None:
			vol = int(ui.sliders[0])
			newnote = int(ui.sliders[1])
			ui.sliders[15]=ui.sliders[0]
			if not ui.mainFrame==None:
				ui.mainFrame.steps.setValues(ui.sliders)
		ii += 1
	else : # MIDI event
		if data1==8: # HotHands angle
			s.ctlout(7,data2,2) # set volume of pad
		elif id==144: # Note on
			if data1==53:  # harmony patch up
				patch_harmony += 1;
				s.programout(patch_harmony,2)
				an.show('Harmony -> '+an.GM_patches[patch_harmony])
			if data1==55:  # harmony patch down
				patch_harmony -= 1;
				s.programout(patch_harmony,2)
				an.show('Harmony -> '+an.GM_patches[patch_harmony])
			if data1==57:  # rhythm patch up
				patch_rhythm += 1;
				s.programout(patch_rhythm,1)
				an.show('Rhythm -> '+an.GM_patches[patch_rhythm])
			if data1==59:  # rhythm patch down
				patch_rhythm -= 1;
				s.programout(patch_rhythm,1)
				an.show('Rhythm -> '+an.GM_patches[patch_rhythm])
		elif id==128: # Note off
			pass;
		else:
			an.show(str(id)+' '+str(data1)+' '+str(data2))            



