import general
import physics


def restore_selection(func):

    def function_wrapper(*args, **kwargs):
        selected = general.get_names_of_selected_objects()
        func(*args, **kwargs)
        general.clear_selection()
        general.select_objects(selected)

    return function_wrapper


class Transformable(object):
    """Wraps cryengine editor commands to make it easier to modify Brushes in a level"""

    def __init__(self, name):
        self.name = name

    @property
    def position(self):
        return list(general.get_position(self.name))

    @position.setter
    def position(self, value):
        [x, y, z] = value
        general.set_position(self.name, x, y, z)

    @property
    def scale(self):
        return list(general.get_scale(self.name))

    @scale.setter
    def scale(self, value):
        [x, y, z] = value
        general.set_scale(self.name, x, y, z)

    @property
    def rotation(self):
        return list(general.get_rotation(self.name))

    @rotation.setter
    def rotation(self, value):
        [x, y, z] = value
        general.set_rotation(self.name, x, y, z)

    @property
    def bounding_box(self):
        general.clear_selection()
        general.select_object(self.name)
        return list(general.get_selection_aabb())

    def delete(self):
        general.delete_object(self.name)

    def select(self):
        general.clear_selection()
        general.select_object(self.name)

    @property
    def geometry_file(self):
        return general.get_entity_geometry_file(self.name)

    @geometry_file.setter
    def geometry_file(self, filepath):
        general.set_entity_geometry_file(self.name, filepath)

    @property
    def material(self):
        return general.get_assigned_material(self.name)

    @material.setter
    def material(self, filepath):
        general.set_custom_material(self.name, filepath)

    def hide(self):
        general.hide_object(self.name)

    def unhide(self):
        general.unhide_object(self.name)

    def get_physics_state(self):
        physics.get_state(self.name)

    @restore_selection
    def simulate(self):
        general.clear_selection()
        general.select_object(self.name)
        physics.simulate_selection()

    @property
    def height(self):
        """Z Height"""
        [minx, miny, minz, maxx, maxy, maxz] = self.bounding_box
        return maxz - minz

    @property
    def width(self):
        """Y Width"""
        [minx, miny, minz, maxx, maxy, maxz] = self.bounding_box
        return maxy - miny

    @property
    def depth(self):
        """X Depth"""
        [minx, miny, minz, maxx, maxy, maxz] = self.bounding_box
        return maxx - minx
