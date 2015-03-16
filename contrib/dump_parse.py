#!/usr/bin/env python
# ex:ts=4:sw=4:sts=4:et
# -*- tab-width: 4; c-basic-offset: 4; indent-tabs-mode: nil -*-

#
# This is used for dumping the results of parsing a recipe.
#
import os
import sys
import warnings

# For importing bb modules
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), '../lib'))
import bb
import bb.parse
import bb.siggen


def main(argv=None):
    """
    Get the parsed variables for the target recipe.
    """
    if len(argv) != 2:
        print >>sys.stderr, "Usage: dump_parse <topdir> <recipe>"
        return 2

    topdir = os.path.realpath(argv[0])
    recipefile = argv[1]

    d = bb.data.init()
    d.setVar("TOPDIR", topdir)
    bb.parse.init_parser(d)
    bb.parse.handle(recipefile, d, False)

    for k in d:
        print k, "=", d.getVar(k, True)

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

