#!/usr/bin/env python

import string
import StringIO
import unittest

import colorizer

class WarningCatcher:
    def __init__(self):
        self.warnings = []
    def warn(self,msg):
        self.warnings.append(msg)
        
class Test(unittest.TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def testReadBadStuff(self):
        wc = WarningCatcher()
        f = StringIO.StringIO("""The files in this directory contain pallette files for fractint. Most
of them came from Fractint itself or the Frxtra packages for fractint
addons, and some are mine. The allmaps.zip file is a zipfile of all mapfiles
that I've ever found. The ngmap.zip is just a collection of my own
and most of them are included in the allmaps file.""")

        c = colorizer.T(wc)
        c.parse_map_file(f, 0)

        self.assertEqual(
            wc.warnings,['Error reading colormap: No colors found'])

    def testReadMapFile(self):
        c = colorizer.T()
        c.parse_map_file(open("../maps/4zebbowx.map"))

        self.assertEqual(len(c.gradient.segments), 255)        

    def testSolids(self):
        c = colorizer.T()
        self.assertEqual([(0,0,0,255)], c.solids)
        
def suite():
    return unittest.makeSuite(Test,'test')

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
