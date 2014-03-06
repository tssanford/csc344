import random
from midiutil.MidiFile import MIDIFile

tempo = random.randrange(120, 220)
MIDIout = MIDIFile(2)
track = 0
time = 0
MIDIout.addTrackName(track, time, "Track1")
MIDIout.addTempo(track, time, tempo)

major = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24]
minor = [0, 2, 3, 5, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22, 24]
jminor = [0, 2, 3, 5, 7, 9, 10, 12, 14, 15, 17, 19, 21, 22, 24]
majorBass = [-12, -10, -8, -7, -5, -3, -1, 0, 2, 4, 5, 7, 9, 11, 12]
minorBass = [-12, -10, -9, -7, -5, -4, -2, 0, 2, 3, 5, 7, 8, 10, 12]
jminorBass = [-12, -10, -9, -7, -5, -3, -2, 0, 2, 3, 5, 7, 9, 10, 12]
majorMid = [0, 2, 4, 5, 7, 9, 11, 12]
minorMid = [0, 2, 3, 5, 7, 8, 10, 12]
jminorMid = [0, 2, 3, 5, 7, 9, 10, 12]
notes = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
badInterval = [-30, -25, -18, -13, -6, -1, 1, 6, 13, 18, 25, 30]

baseNote = notes[random.randrange(0, 23)]
length = 240
track1 = []
track2 = []
track3 = []
t1time = 0
t2time = 0
t3time = 0
curBeat = 1
curMeasure = 1
swap = 0
doubleChance = random.random()
sameChance = random.random()
skipChance = random.random()
modChance = random.random()
modFlag = 0
holdChance = random.random()

if random.random() <= 0.3:
   swap = 1
elif random.random() <= 0.3:
   swap = 2

for x in range(0, length + 20):
   track1.append(0)
   track2.append(0)   
   track3.append(0)

while t1time <= length or t2time <= length or t3time <= length:
   if t1time <= length:
      playNote = random.random()
      if curBeat in(1, 3) and playNote <= 0.8 or curBeat in(2, 4) and playNote <= 0.5:
         track = 0
         channel = 0
         while True:
            if random.random() <= 0.15:
               index = random.choice([0, 7, 14])
            elif random.random() <= 0.1:
               index = random.choice([4, 11])
            else:
               index = random.randrange(0, 15)
            if swap == 0:
               pitch = baseNote + major[index]
            elif swap == 1:
               pitch = baseNote - 3 + jminor[index]
            else:
               pitch = baseNote - 3 + minor[index]
            if (pitch - track2[t1time]) not in(badInterval) and (pitch - track3[t1time]) not in(badInterval):
               break
         time = t1time
         duration = random.randrange(1, 6 - curBeat)
         volume = 100
         j = 0
         while j < duration:
            track1[t1time + j] = pitch
            j += 1
         t1time += duration
         curBeat += duration
         if random.random() < doubleChance:
            if random.random() < skipChance:
               MIDIout.addNote(track, channel, pitch, time, duration - 0.5, volume)
            if random.random() < sameChance:
               while True:
                  if random.random() <= 0.15:
                     index = random.choice([0, 7, 14])
                  elif random.random() <= 0.1:
                     index = random.choice([4, 11])
                  else:
                     index = random.randrange(0, 15)
                  if swap == 0:
                     pitch = baseNote + major[index]
                  elif swap == 1:
                     pitch = baseNote - 3 + jminor[index]
                  else:
                     pitch = baseNote - 3 + minor[index]
                  if (pitch - track2[t1time]) not in(badInterval) and (pitch - track3[t1time]) not in(badInterval):
                     break
            MIDIout.addNote(track, channel, pitch, time + (duration - 0.5), 0.5, volume)
         else:
            MIDIout.addNote(track, channel, pitch, time, duration, volume)
      if curBeat > 4:
         curBeat -= 4
         curMeasure += 1
      if curMeasure > 16:
         curMeasure -= 16
   
   if t2time <= length:
      playNote = random.random()
      if curBeat in(1, 3) and playNote <= 0.8 or curBeat in(2, 4) and playNote <= 0.5:
         channel = 1
         while True:
            if random.random() <= 0.15:
               index = random.choice([0, 7, 14])
            elif random.random() <= 0.1:
               index = random.choice([4, 11])
            else:
               index = random.randrange(0, 15)
            if swap == 0:
               pitch = baseNote + majorBass[index]
            elif swap == 1:
               pitch = baseNote - 3 + jminorBass[index]
            else:
               pitch = baseNote - 3 + minorBass[index]
            if (pitch - track1[t2time]) not in(badInterval) and (pitch - track3[t2time]) not in(badInterval):
               break
         time = t2time
         duration = random.randrange(2, 7 - curBeat)
         volume = 100
         j = 0
         while j < duration:
            track2[t2time + j] = pitch
            j += 1
         t2time += duration
         curBeat += duration
         MIDIout.addNote(track, channel, pitch, time, duration, volume)
      if curBeat > 4:
         curBeat -= 4
         curMeasure += 1
      if curMeasure > 16:
         curMeasure -= 16
         
   if t3time <= length:
      playNote = random.random()
      channel = 2
      while True:
         if random.random() <= 0.15:
            index = random.choice([0, 7])
         elif random.random() <= 0.1:
            index = 4
         else:
            index = random.randrange(0, 8)
         if swap == 0:
            pitch = baseNote + majorMid[index]
         elif swap == 1:
            pitch = baseNote - 3 + jminorMid[index]
         else:
            pitch = baseNote - 3 + minorMid[index]
         if (pitch - track1[t3time]) not in(badInterval) and (pitch - track2[t3time]) not in(badInterval):
            break
      time = t3time
      duration = random.randrange(1, 6 - curBeat)
      volume = 100
      j = 0
      t3time += duration
      curBeat += duration
      if random.random() < holdChance:
         MIDIout.addNote(track, channel, pitch, time, duration * 2, volume)
         t3time += duration
         while j < (duration * 2):
            track2[t3time + j] = pitch
            j += 1
      else:
         MIDIout.addNote(track, channel, pitch, time, duration, volume)
         while j < duration:
            track2[t3time + j] = pitch
            j += 1
      if curBeat > 4:
         curBeat -= 4
         curMeasure += 1
      if curMeasure > 16:
         curMeasure -= 16

outfile = open("MIDIout.mid", "wb")
MIDIout.writeFile(outfile)
outfile.close()