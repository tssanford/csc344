import random
from midiutil.MidiFile import MIDIFile

tempo = random.randrange(160, 220)
MIDIout = MIDIFile(2)
track = 0
time = 0
MIDIout.addTrackName(track, time, "Track1")
MIDIout.addTempo(track, time, tempo)
track = 1
time = 0
MIDIout.addTrackName(track, time, "Drum")
MIDIout.addTempo(track, time, tempo)

bassNote = 68
cymbNote = 66
rideNote = 67
snarNote = 71

major = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24]
minor = [0, 2, 3, 5, 7, 8, 10, 12, 14, 15, 17, 19, 20, 22, 24]
jminor = [0, 2, 3, 5, 7, 9, 10, 12, 14, 15, 17, 19, 21, 22, 24]
majorBass = [-12, -10, -8, -7, -5, -3, -1, 0]
minorBass = [-12, -10, -9, -7, -5, -4, -2, 0]
jminorBass = [-12, -10, -9, -7, -5, -3, -2, 0]
majorMid = [0, 2, 4, 5, 7, 9, 11, 12]
minorMid = [0, 2, 3, 5, 7, 8, 10, 12]
jminorMid = [0, 2, 3, 5, 7, 9, 10, 12]
notes = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
badInterval = [-30, -25, -23, -22, -21, -20, -18, -13, -11, -10. -9, -8, -6, -1, 1, 6, 8, 9, 10, 11, 13, 18, 20, 21, 22, 23, 25, 30]

bassPattern = [ [bassNote, 0, bassNote, 0], [bassNote, bassNote, bassNote, bassNote], [bassNote, bassNote, bassNote, bassNote], [bassNote, 0, bassNote, 0], [bassNote, 0, bassNote, 0] ]
cymbPattern = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, cymbNote, 0, cymbNote], [0, cymbNote, 0, cymbNote], [0, cymbNote, 0, cymbNote] ]
ridePattern = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [rideNote, 0, rideNote, 0], [0, rideNote, 0, rideNote] ]
snarPattern = [ [0, snarNote, 0, snarNote], [0, snarNote, 0, snarNote], [0, snarNote, 0, snarNote], [0, snarNote, 0, snarNote], [snarNote, 0, snarNote, 0] ]

baseNote = notes[random.randrange(0, 11)]
drums = random.randrange(0, 5);
length = 256
track1 = []
track2 = []
track3 = []
drum1 = []
drum2 = []
drum3 = []
drum4 = []
t1time = 0
t1prev = 0
t2time = 0
t3time = 0
i = 0
curBeat = 1
curMeasure = 1
swap = 0
doubleChance = random.random()
sameChance = random.random()
skipChance = random.random()
modChance = random.random()
modFlag = 0
holdChance = random.random()
repeatChance = random.random()/4 + 0.35
repeatSpot = random.randrange(0, length/64)
count = 0
maxCount = 1000

if random.random() <= 0.3:
   swap = 2

for x in range(0, length + 50):
   track1.append(0)
   track2.append(0)   
   track3.append(0)
   drum1.append(0)
   drum2.append(0)
   drum3.append(0)
   drum4.append(0)
   
def checkMelodic(num, loc, pitch):
   thirds = [-16, -4, 4, 16]
   octs = [-24, -12, 12, 24]
   inter1 = 0
   inter2 = 0
   inter3 = 0
   
   if num == 1:
      inter1 = pitch - track1[loc - 1]
      inter2 = track2[loc] - track2[loc - 1]
      inter3 = track3[loc] - track3[loc - 1]
   elif num == 2:
      inter1 = pitch - track2[loc - 1]
      inter2 = track1[loc] - track1[loc - 1]
      inter3 = track3[loc] - track3[loc - 1]
   elif num == 3:
      inter1 = pitch - track3[loc - 1]
      inter2 = track2[loc] - track2[loc - 1]
      inter3 = track1[loc] - track1[loc - 1]
      
   ret = not ((inter1 in(thirds) and inter2 in(thirds)) or (inter2 in(thirds) and inter3 in(thirds)) or (inter3 in(thirds) and inter1 in(thirds)))
   return ret or (not ((inter1 in(octs) and inter2 in(octs)) or (inter2 in(octs) and inter3 in(octs)) or (inter3 in(octs) and inter1 in(octs))))
   
while i <= length:
   if random.random() <= repeatChance and (i - 16) >= (repeatSpot * 16) and (i % 16) == 0:
      for j in range(0, 16):
         track1[i + j] = track1[(repeatSpot * 16) + j]
         track2[i + j] = track2[(repeatSpot * 16) + j]
         track3[i + j] = track3[(repeatSpot * 16) + j]
         drum1[i + j] = drum1[(repeatSpot * 16) + j]
   else:
      if True:
         if i == length:
            track3[i] = baseNote - 12
      
         if track1[i] == 0:
            playNote = random.random()
            if ((i + 1) % 4) in(1, 3) and playNote <= 0.8 or ((i + 1) % 4) in(2, 4) and playNote <= 0.5:
               track = 0
               channel = 0
               count = 0
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
                  if t1prev != 0:
                     if pitch - t1prev > 8:
                        pitch -= 8
                     if pitch - t1prev < -8:
                        pitch += 8
                  count += 1
                  if (pitch - track2[i]) not in(badInterval) and (pitch - track3[i]) not in(badInterval) and (pitch - track1[i - 1]) not in(badInterval) and checkMelodic(1, i, pitch):
                     break
                  elif count == maxCount:
                     pitch = 0
                     break
               time = i
               duration = random.randrange(1, 6 - ((i + 1) % 4))
               volume = 100
               j = 0
               
               while j < duration:
                  track1[i + j] = pitch
                  j += 1
               t1prev = pitch               
                  
         if track2[i] == 0:
            playNote = random.random()
            if ((i + 1) % 4) in(1, 3) and playNote <= 0.8 or ((i + 1) % 4) in(2, 4) and playNote <= 0.5:
               channel = 1
               count = 0
               while True:
                  if random.random() <= 0.15:
                     index = random.choice([0, 7])
                  elif random.random() <= 0.1:
                     index = random.choice([4])
                  else:
                     index = random.randrange(0, 8)
                  if swap == 0:
                     pitch = baseNote + majorBass[index]
                  elif swap == 1:
                     pitch = baseNote - 3 + jminorBass[index]
                  else:
                     pitch = baseNote - 3 + minorBass[index]
                  count += 1
                  if (pitch - track1[i]) not in(badInterval) and (pitch - track3[i]) not in(badInterval) and (pitch - track2[i - 1]) not in(badInterval) and checkMelodic(2, i, pitch):
                     break
                  elif count == maxCount:
                     pitch = 0
                     break
               time = i
               duration = random.randrange(2, 7 - ((i + 1) % 4))
               volume = 100
               j = 0
               if random.random() < holdChance:
                  while j < (duration * 2):
                     track2[i + j] = pitch
                     j += 1
               else:
                  while j < duration:
                     track2[i + j] = pitch
                     j += 1    
               
         if track3[i] == 0:
            playNote = random.random()
            channel = 2
            count = 0
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
               count += 1
               if (pitch - track1[i]) not in(badInterval) and (pitch - track2[i]) not in(badInterval) and (pitch - track3[i - 1]) not in(badInterval) and checkMelodic(3, i, pitch):
                  break
               elif count == maxCount:
                     pitch = 0
                     break
            time = i
            duration = random.randrange(1, 6 - ((i + 1) % 4))
            volume = 100
            j = 0
            while j < duration:
               track3[i + j] = pitch
               j += 1
               
         if drum1[i] == 0 and ((i + 1) % 4) in(1, 3):
            drum1[i] = 36
          
         drum1[i] = bassPattern[drums][i % 4]
         drum2[i] = cymbPattern[drums][i % 4]
         drum3[i] = ridePattern[drums][i % 4]
         drum4[i] = snarPattern[drums][i % 4]
         
   i += 1

i = 0
previous = 0
pitch = 0
while i <= length:
   track = 0
   channel = 0
   time = i
   duration = 0
   volume = 100
   if track1[i] != previous:
      pitch = track1[i]
      previous = track1[i]
      j = i
      while track1[j] == pitch and j <= length:
         j += 1
         duration += 1
      if pitch != 0:
         if random.random() < doubleChance:
            if random.random() < skipChance:
               MIDIout.addNote(track, channel, pitch, time, duration - 0.5, volume)
            if random.random() < sameChance:
               count = 0
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
                  if t1prev != 0:
                     if pitch - t1prev > 8:
                        pitch -= 8
                     if pitch - t1prev < -8:
                        pitch += 8
                  count += 1
                  if (pitch - track2[i]) not in(badInterval) and (pitch - track3[i]) not in(badInterval) and (pitch - track1[i - 1]) not in(badInterval):
                     break
                  elif count == maxCount:
                     pitch = 0
                     break
            MIDIout.addNote(track, channel, pitch, time + (duration - 0.5), 0.5, volume)
         else:
            MIDIout.addNote(track, channel, pitch, time, duration, volume)
         t1prev = pitch
   i += 1

i = 0
previous = 0
while i <= length:
   track = 0
   channel = 1
   time = i
   duration = 0
   volume = 100
   if track2[i] != previous:
      pitch = track2[i]
      previous = track2[i]
      j = i
      while track2[j] == pitch and j <= length:
         j += 1
         duration += 1
      if pitch != 0:
         MIDIout.addNote(track, channel, pitch, time, duration, volume)
   i += 1
      
i = 0 
previous = 0
while i <= length:
   track = 0
   channel = 2
   time = i
   duration = 0
   volume = 100
   if track3[i] != previous:
      pitch = track3[i]
      previous = track3[i]
      j = i
      while track3[j] == pitch and j <= length:
         j += 1
         duration += 1
      if pitch != 0:
         MIDIout.addNote(track, channel, pitch, time, duration, volume)
   i += 1

i = 0 
previous = 0
while i <= length:
   track = 1
   channel = 0
   time = i
   duration = 1
   volume = 100
   pitch = drum1[i]
   if pitch != 0:
      MIDIout.addNote(track, channel, pitch, time, duration, volume)
   i += 1
   
i = 0 
previous = 0
while i <= length:
   track = 1
   channel = 1
   time = i
   duration = 1
   volume = 40
   pitch = drum2[i]
   if pitch != 0:
      MIDIout.addNote(track, channel, pitch, time, duration, volume)
   i += 1
   
i = 0 
previous = 0
while i <= length:
   track = 1
   channel = 2
   time = i
   duration = 1
   volume = 60
   pitch = drum3[i]
   if pitch != 0:
      MIDIout.addNote(track, channel, pitch, time, duration, volume)
   i += 1
   
i = 0 
previous = 0
while i <= length:
   track = 1
   channel = 3
   time = i
   duration = 1
   volume = 60
   pitch = drum4[i]
   if pitch != 0:
      MIDIout.addNote(track, channel, pitch, time, duration, volume)
   i += 1

outfile = open("MIDIout.mid", "wb")
MIDIout.writeFile(outfile)
outfile.close()