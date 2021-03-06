"""
    This is Pycao, a modeler and raytracer interpreter for 3D drawings
    Copyright (C) 2015  Laurent Evain

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
"""



#pycaoDir="/home/laurent/subversion/articlesEtRechercheEnCours/pycao/pycaogit"
#pycaoDir="/users/evain/subversion/articlesEtRechercheEnCours/pycao/pycaogit/core/"
import os
thisFileAbsName=os.path.abspath(__file__)
pycaoDir=os.path.dirname(thisFileAbsName)+"/../core"

import sys
sys.path.append(pycaoDir)


"""
                MODULES IMPORT
"""


from uservariables import *
from generic import *
from mathutils import *
from aliases import *
from genericwithmaths import *
from elaborate import *
from compound import *
import povrayshoot 
from cameras import *
from lights import *
from material import *




###############################
# By default, lights you will append in the file  are appended to existing cameras. So probably 
# you want to leave the first line defining the camera at the beginning of the file


camera=Camera()

#######################################

"""
                SCENE DESCRIPTION
"""

#bbloc1
p=plane(Z,origin)
c=Cube(1,1,1)
d=c.clone().translate(2*X)
e=d.clone().translate(2*X) 
f=d.clone().translate(4*X)

pig1=Pigment.from_photo("oak.png",dimx=2.,dimy=10.,center=None,symmetric=False)
p.textured(pig1)
pig2=Pigment.from_photo("woodFloor1.png",dimx=2.,dimy=3.,center=None,symmetric=False)
#pig3=Pigment.from_photo("parquet1.png",dimx=2.,dimy=3.,center=None,symmetric=False)
for ob in [c,d,e,f]:
    ob.textured(pig2)
unleash_texture([c,d]) # Now, c,d  have a texture different from e,f
d.rotate(X,3.14/2) # The pigment move both in d and c, sharing the same structure, but not in e,f on the right
#ebloc1




#################################################
#  Now, what you see
#################################################


directory=os.path.dirname(os.path.realpath(__file__))
base=os.path.basename(__file__)
camera.file=directory+"/generatedImages/"+os.path.splitext(base)[0]+".pov"
camera.povraypath=pycaoDir+"/../images/" # where you put your images,photos for the textures
print (camera.povraypath)
camera.zoom(0.55)
camera.imageHeight=800 # in pixels
camera.imageWidth=1200 
camera.quality=9 # a number between 0 and 11,  Consider using a lower quality setting if you're just testing your scene


camera.lookAt=origin+3*X+.75*Z # look at the center of cyl

#camera.actors=[] # If you want to fill this list and use it, you should set camera.filmAllActors to False. 
camera.filmAllActors=True # overrides the camera.actors list



camera.hooked_on(origin+1.6*X-4*Y+3.6*Z)  # the positive y are in front of us if the camera is located in negative Y and we look at  a point close to the origin
light=Light().hooked_on(origin+8*X+10*Z) # a light located close to the camera

camera.shoot # takes the photo, ie. creates the povray file, and stores it in camera.file
camera.pov_to_png # show the photo, ie calls povray. 
#camera.pov_to_png_without_viewer # if you want only the photo but not the graphical interface
