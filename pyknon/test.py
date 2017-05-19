from pyknon.genmidi import Midi
from pyknon.music import NoteSeq

notes1 = NoteSeq("G G G G G  G E D E G C  G E D E C D  C A. C C A. G. C  C A. C C A. G. C  G A G E D C.")
midi = Midi(5, tempo=70) 
midi.seq_notes(notes1, track=0)
midi.write("demo2.mid")