import bpy
import numpy as np
from mathutils import Vector

# Get the selected objects
selected_objects = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

print("hello")

if not selected_objects:
    print("No mesh objects selected")
else:
    # Initialize min and max coordinates
    min_coords = np.array([np.inf, np.inf, np.inf])
    max_coords = np.array([-np.inf, -np.inf, -np.inf])

    # Calculate the bounding box for each selected object
    for obj in selected_objects:
        # Update the min and max coordinates
        for vertex in obj.bound_box:
            world_vertex = obj.matrix_world @ Vector(vertex)
            min_coords = np.minimum(min_coords, world_vertex)
            max_coords = np.maximum(max_coords, world_vertex)

    # Calculate the dimensions
    dimensions = (max_coords - min_coords)*1000
    print(f"Total dimensions: {dimensions[0]:.2f} x {dimensions[1]:.2f} x {dimensions[2]:.2f}")
