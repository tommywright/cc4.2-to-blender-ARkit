# cc4.2-to-blender-ARkit
Updates the Shape Keys exported from CC4.2 so that they adhere to the ARkit naming convention. 

Why was this made?
At the moment, adding the ARkit morph targets inside Character Creator 4.2 forces you to disable wrinkles. I wanted wrinkles along with the proper morph target names inside Blender.

Running this script takes a CC4.2 character with wrinkles that has been imported into Blender and changes the names of the Blend Shapes (morph targets) to the standard ARkit naming convention. It will rename shapes, combines the cheek puff and inner brow to get the single shape from those and put a keyframe on every shape (needed to copy animation like Rokoko face).  
![image](https://user-images.githubusercontent.com/7697182/235367036-5193c79e-3fa9-4e97-8053-ee1424ce6867.png)

Make sure you export from CC4.2 with Mouth Open as Morph!!

Combine Facial hair to the body mesh before running script CTRL+j in Blender.


Install:

With your character body mesh selected, select the Scripting tab at the top of Blender's screen. Drag and drop the .py file into the text feild and hit the "Run" arrow.


Afterrunning the script, you will need to manually change the Driver names that use browInnerUp to get the forehead wrinkle as Icouldn't figure out how to do that in Python code.
![image](https://user-images.githubusercontent.com/7697182/235366984-03f0f7b4-901a-41f1-a012-46d7322474f5.png)
