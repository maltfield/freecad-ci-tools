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

FreeCADGui.showMainWindow()
document= FreeCAD.openDocument(str(file_path))
FreeCADGui.activeView().saveImage( 'image1.png' )

sys.exit(0)

