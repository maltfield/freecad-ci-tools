# freecad-ci-tools

This repo contains tools to help you better work with FreeCAD files in your git repo.

Because FreeCAD files cannot be easily "viewed" or "diffed" in the Web Browser, they're significantly more difficult to work with collaboratively in a code forge. For example, it's not trivial to review a GitHub PR that contains updates to a FreeCAD file to see what changed before merging it.

This repo attempts to provide tools that you can integrate into your Continuous Integration workflow to make FreeCAD files easier for your team to work with.

## freecad-to-png.py

The `freecad-to-png.py` file is a simple python script that exports a PNG image from a given FreeCAD .FCStd file.

This can be useful to add to CIs that:

1. Automatically upload a screenshot to the comments thread of a PR for any FreeCAD files with changes
1. Automatically update screenshots of FreeCAD files in your documentation after merging to the main branch

# License

Copyright (C) 2023 Michael Altfield and the Eco-Libre Team

The contents of this repo are under the GPL version 3 or later.
In addition, any content other than code can also be used, at your
choice, under CC-BY-SA version 4.0.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
