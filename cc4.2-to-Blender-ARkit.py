import bpy

name_mapping = {
    "Brow_Drop_L": "browDownLeft",
    "Brow_Drop_R": "browDownRight",
    "Brow_Raise_Outer_L": "browOuterUpLeft",
    "Brow_Raise_Outer_R": "browOuterUpRight",
    "Eye_L_Look_Up": "eyeLookUpLeft",
    "Eye_R_Look_Up": "eyeLookUpRight",
    "Eye_L_Look_Down": "eyeLookDownLeft",
    "Eye_R_Look_Down": "eyeLookDownRight",
    "Eye_L_Look_L": "eyeLookOutLeft",
    "Eye_L_Look_R": "eyeLookInLeft",
    "Eye_R_Look_L": "eyeLookInRight",
    "Eye_R_Look_R": "eyeLookOutRight",
    "Eye_Blink_L": "eyeBlinkLeft",
    "Eye_Blink_R": "eyeBlinkRight",
    "Eye_Squint_L": "eyeSquintLeft",
    "Eye_Squint_R": "eyeSquintRight",
    "Eye_Wide_L": "eyeWideLeft",
    "Eye_Wide_R": "eyeWideRight",
    "Cheek_Raise_L": "cheekSquintLeft",
    "Cheek_Raise_R": "cheekSquintRight",
    "Nose_Sneer_L": "noseSneerLeft",
    "Nose_Sneer_R": "noseSneerRight",
    "Jaw_Open": "--DeleteThis--",
    "Jaw_Forward": "jawForward",
    "Jaw_L": "jawLeft",
    "Jaw_R": "jawRight",
    "Mouth_Funnel": "mouthFunnel",
    "Mouth_Pucker": "mouthPucker",
    "Mouth_L": "mouthLeft",
    "Mouth_R": "mouthRight",
    #"Mouth_Roll_In_Upper": "mouthRollUpper",
    #"Mouth_Roll_In_Lower": "mouthRollLower",
    "Mouth_Shrug_Upper": "mouthShrugUpper",
    "Mouth_Shrug_Lower": "mouthShrugLower",
    "Mouth_Close": "mouthClose",
    "Mouth_Smile_L": "mouthSmileLeft",
    "Mouth_Smile_R": "mouthSmileRight",
    "Mouth_Frown_L": "mouthFrownLeft",
    "Mouth_Frown_R": "mouthFrownRight",
    "Mouth_Dimple_L": "mouthDimpleLeft",
    "Mouth_Dimple_R": "mouthDimpleRight",
    "Mouth_Up_Upper_L": "mouthUpperUpLeft",
    "Mouth_Up_Upper_R": "mouthUpperUpRight",
    "Mouth_Down_Lower_L": "mouthLowerDownLeft",
    "Mouth_Down_Lower_R": "mouthLowerDownRight",
    "Mouth_Press_L": "mouthPressLeft",
    "Mouth_Press_R": "mouthPressRight",
    "Mouth_Stretch_R": "mouthStretchRight",
    "Mouth_Stretch_L": "mouthStretchLeft",
    "Tongue_Out": "tongueOut",
    "Merged_Open_Mouth": "jawOpen"
}

for shapekey in bpy.data.shape_keys:
    for keyblock in shapekey.key_blocks:
        if keyblock.name in name_mapping:
            keyblock.name = name_mapping[keyblock.name]
        else:
            print("Skipping unknown key:", keyblock.name)
        
def create_shape_key(obj, name, shape_keys_to_combine):
    # Set the value of the shape keys to 1.0
    for shape_key in shape_keys_to_combine:
        shape_key.value = 1.0

    # Create a new shape key from the mix of the two shape keys
    obj.shape_key_add(name=name, from_mix=True)

    # Set the value of the shape keys back to 0
    for shape_key in shape_keys_to_combine:
        shape_key.value = 0

    # Remove the old shape keys
    for shape_key in shape_keys_to_combine:
        obj.shape_key_remove(shape_key)

    # Update the object
    obj.data.update()


# Get the active object
obj = bpy.context.object

# Cheek puff shape keys
cheek_puff_left = obj.data.shape_keys.key_blocks.get('Cheek_Puff_L')
cheek_puff_right = obj.data.shape_keys.key_blocks.get('Cheek_Puff_R')
create_shape_key(obj, 'cheekPuff', [cheek_puff_left, cheek_puff_right])

# Inner brow shape keys
inner_brow_left = obj.data.shape_keys.key_blocks.get('Brow_Raise_Inner_L')
inner_brow_right = obj.data.shape_keys.key_blocks.get('Brow_Raise_Inner_R')
create_shape_key(obj, 'browInnerUp', [inner_brow_left, inner_brow_right])

# Mouth Roll upper shape keys
mouth_roll_up_left = obj.data.shape_keys.key_blocks.get('Mouth_Roll_In_Upper_L')
mouth_roll_up_right = obj.data.shape_keys.key_blocks.get('Mouth_Roll_In_Upper_R')
create_shape_key(obj, 'mouthRollUpper', [mouth_roll_up_left, mouth_roll_up_right])

# Mouth Roll lower shape keys
mouth_roll_down_left = obj.data.shape_keys.key_blocks.get('Mouth_Roll_In_Lower_L')
mouth_roll_down_right = obj.data.shape_keys.key_blocks.get('Mouth_Roll_In_Lower_R')
create_shape_key(obj, 'mouthRollLower', [mouth_roll_down_left, mouth_roll_down_right])

# Mouth Funnel shape keys
mouth_funnel_up_left = obj.data.shape_keys.key_blocks.get('Mouth_Funnel_Up_L')
mouth_funnel_up_right = obj.data.shape_keys.key_blocks.get('Mouth_Funnel_Up_R')
mouth_funnel_down_left = obj.data.shape_keys.key_blocks.get('Mouth_Funnel_Down_L')
mouth_funnel_down_right = obj.data.shape_keys.key_blocks.get('Mouth_Funnel_Down_R')
create_shape_key(obj, 'mouthFunnel', [mouth_funnel_up_left, mouth_funnel_up_right, mouth_funnel_down_left, mouth_funnel_down_right])

# Mouth Pucker shape keys
mouth_pucker_up_left = obj.data.shape_keys.key_blocks.get('Mouth_Pucker_Up_L')
mouth_pucker_up_right = obj.data.shape_keys.key_blocks.get('Mouth_Pucker_Up_R')
mouth_pucker_down_left = obj.data.shape_keys.key_blocks.get('Mouth_Pucker_Down_L')
mouth_pucker_down_right = obj.data.shape_keys.key_blocks.get('Mouth_Pucker_Down_R')
create_shape_key(obj, 'mouthPucker', [mouth_pucker_up_left, mouth_pucker_up_right, mouth_pucker_down_left, mouth_pucker_down_right])

# Now set a keyframe on every shape key

frames = bpy.context.scene.frame_end + 1

# For the active object...
ob = bpy.context.active_object
me = ob.data

# Remove ['Basis'] from a shallow copy of *ob's* shape-keys list.
kblocks = dict(me.shape_keys.key_blocks)
del kblocks['Basis']

# Keyframe shapekeys' values to 1 for the frame corresponding
# to their position in remaining list, 0 for other frames
for f in range(frames):
    for i, kb in enumerate(kblocks):
        kblocks[kb].value = (f == i)
        kblocks[kb].keyframe_insert("value", frame=f)
