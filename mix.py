from pysndfx import AudioEffectsChain
import sys

if len(sys.argv) != 3:
    print("Usage: mix.py <input_file> <output_file>")

fx = (
    AudioEffectsChain()
    .tempo(0.8)#0.8
    .speed(7/8)#7/8
    .reverb(
        reverberance=70,
        hf_damping=70,
        pre_delay=20,
        wet_gain=3,
        wet_only=True,
        room_scale=100,
        stereo_depth=100
    )
#    .lowshelf(gain=20)
#    .phaser()
)

infile = sys.argv[1]
outfile = sys.argv[2]

fx(infile, outfile)
