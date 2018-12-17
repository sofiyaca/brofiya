import os, sys
from PIL import Image

size = 8073, 609

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + ".jpeg"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG", quality=100, optimize=True)
        except IOError:
            print "cannot create thumbnail for '%s'" % infile