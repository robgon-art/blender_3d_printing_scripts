import bpy
import bmesh

def set_vertices_to_value_global(dimension='Z', value=100):
    # Iterate through all selected objects in the scene
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            # Set the object to edit mode
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode='EDIT')
            
            # Get the mesh data
            mesh = bmesh.from_edit_mesh(obj.data)
            
            # Get the world matrix of the object
            world_matrix = obj.matrix_world
            
            # Iterate through all selected vertices and set the specified dimension to the given value
            for vertex in mesh.verts:
                if vertex.select:
                    # Transform vertex coordinates to global space
                    global_coord = world_matrix @ vertex.co
                    
                    if dimension == 'X':
                        global_coord.x = value
                    elif dimension == 'Y':
                        global_coord.y = value
                    elif dimension == 'Z':
                        global_coord.z = value
                    
                    # Transform back to local space
                    local_coord = world_matrix.inverted() @ global_coord
                    
                    # Set the vertex coordinates
                    vertex.co = local_coord
            
            # Update the mesh to reflect changes
            bmesh.update_edit_mesh(obj.data)
            
            # Switch back to object mode to apply the changes
            # bpy.ops.object.mode_set(mode='OBJECT')

# Call the function with the desired dimension and value
set_vertices_to_value_global(dimension='Z', value=0.500)

# To call the function with a different dimension, you can use:
# set_vertices_to_value_global(dimension='X', value=50)
# set_vertices_to_value_global(dimension='Y', value=25)
