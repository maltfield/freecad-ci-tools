#!/usr/bin/env python3
################################################################################
# File:    freecad-to-png.py
# Version: 0.1
# Purpose: Extracts a png screenshot of a given .FCStd freecad file
# Authors: Michael Altfield <michael@michaelaltfield.net>
# Created: 2024-02-06
# Updated: 2024-02-06
################################################################################

################################################################################
#                                   IMPORTS                                    #
################################################################################

import sys
sys.path.append( '/usr/lib/freecad-python3/lib' )
sys.path.append( '/usr/share/freecad/Mod' )

import FreeCAD
import FreeCADGui

################################################################################
#                                  SETTINGS                                    #
################################################################################

################################################################################
#                                  FUNCTIONS                                   #
################################################################################

################################################################################
#                                  MAIN BODY                                   #
################################################################################

# TODO: change this to be an argument
file_path = './assembly.FCStd'

##################
# CHECK SETTINGS #
##################

####################
# HANDLE ARGUMENTS #
####################

#####################
# DECLARE VARIABLES #
#####################

# showMainWindow() without blocking stderr & stdout
# https://forum.freecad.org/viewtopic.php?p=493152#p493152
origStdout = sys.stdout
origStderr = sys.stderr
FreeCADGui.showMainWindow()
sys.stdout = origStdout
sys.stderr = origStderr

document= FreeCAD.openDocument(str(file_path))

# TODO: change export path to be an argument
FreeCADGui.activeView().saveImage( 'docs/images/assembly1.png' )

sys.exit(0)

