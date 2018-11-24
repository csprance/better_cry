import general
from better_cry import Transformable
from better_cry.utils import mutate


class Level(object):
    """Wraps cryengine editor commands to make it easier to modify items in a level"""

    def __init__(self):
        self.name = general.get_current_level_name()
        self.path = general.get_current_level_path()
        self.layers = general.get_all_layers()

    @property
    def selected(self):
        return mutate(general.get_names_of_selected_objects())

    @property
    def objects(self):
        return mutate(
            [general.get_all_objects_of_layer(layer) for layer in self.layers]
        )

    @staticmethod
    def save():
        general.save_level()

    @staticmethod
    def new_object(entity_type, model, name, x, y, z):
        return Transformable(general.new_object(entity_type, model, name, x, y, z))

    @staticmethod
    def clear_selection():
        general.clear_selection()

    @staticmethod
    def select(name, add=False):
        if not add:
            general.clear_selection()
        general.select_object(name)

    def get_object_by_name(self, name):
        return Transformable(name)
