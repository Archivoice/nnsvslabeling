# nnsvslabeling
Python scripts made by UtaUtaUtau to make NNSVS labeling easier. Forked for NNSVS Chinese.

# How to Use
### General
You will need Python for all of these to work. Written in Python 3.7.

### lab2audacity.py
This script can convert between Audacity labels (in .txt filetype) and HTS mono labels (in .lab filetype). Drag and drop the file over the script file and it will do the conversion. It cannot batch convert labels.

This script automatically connects the ends of each label to the start of the next label. If the label ends with `-`, it will exclude it in the HTS label.

This script does not do anything about timing with HTS mono labels.

### check_labels.py

Exactly as the name states, will check if you have any phonemes outside of the phoneme list.

### lab2ust
The whole lab2ust folder will be put in the UTAU plugins folder.

Just follow the steps that the plugin gives you.

It will always separate the phonemes `pau`, `br`, and `Edge`.

This will only directly translate timing according to the BPM of the UST. It puts all notes at middle C (C4) unless a `.frq` file is fed for automatic note placement. It is recommended to generate `.mrq` files using moresampler via the FrqEditor tool for batch generation and batch convertion.

* Quantization reference table:
| Quantize | Note Length |
| --- | --- |
| 128th note | 15 |
| 64th triplet | 20 |
| 64th note | 30 |
| 32nd triplet | 40 |
| 32nd note | 60 |
| 16th triplet | 80 |
| 16th note | 120 |
| 8th triplet | 160 |
| 8th note | 240 |
| Quarter triplet | 320 |
| Quarter note | 480 |
