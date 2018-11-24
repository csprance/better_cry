import general
from better_cry import Transformable


def mutate(item_names):
    mutated = []
    for item in item_names:
        object_type = general.get_object_type(item)
        if object_type == "Brush":
            mutated.append(Transformable(item))
        elif object_type == "Designer":
            mutated.append(Transformable(item))
        else:
            mutated.append(Transformable(item))
    return mutated


def restore_selection(func):
    def function_wrapper(*args, **kwargs):
        selected = general.get_names_of_selected_objects()
        func(*args, **kwargs)
        general.clear_selection()
        general.select_objects(selected)
    return function_wrapper
