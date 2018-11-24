from better_cry import Transformable


class Brush(Transformable):
    """Wraps cryengine editor commands to make it easier to modify Brushes in a level"""

    def __init__(self, name):
        super(Transformable).__init__(name)
