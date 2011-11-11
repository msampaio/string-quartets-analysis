#!/usr/bin/env python
# -*- coding: utf-8 -*-

import music21
import os

MAINDIR = '/home/marcos/Dropbox/ongoing/string-quartets-analysis'
beethoven_dir = MAINDIR + '/beethoven-quartets/'

quartets = sorted(os.listdir(beethoven_dir))

def testa_parts(filename, directory=beethoven_dir):
    """Testa arquivos"""

    if len(music21.converter.parse(directory + filename).parts) != 4:
        return filename


def flatten(seq):
    """Flatten Sequences.

    >>> flatten([[0, 1], [2, 3]])
    [0, 1, 2, 3]
    """

    return [item for sublist in seq for item in sublist]



q = music21.converter.parse(beethoven_dir + quartets[0])

v1 = q.parts[0]

n = v1.flat.notes
nr = v1.flat.notesAndRests

notas_simples = v1.flat.notes.getElementsNotOfClass(music21.chord.Chord)
acordes = v1.flat.notes.getElementsByClass(music21.chord.Chord)

todas_notas = flatten([notas_simples, flatten(acordes)])
