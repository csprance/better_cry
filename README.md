# Better Cry
> Work with CRYENGINE objects in the editor in an object oriented way.

## Install
Drag and drop the `better_cry` folder into `Editor\Scripts`

## Usage
```python
from better_cry import Level
level = Level()
for item in level.selected:
    # set an items position
    item.position = [0,0,0]
    # read its rotation
    print(item.rotation)
    print(item.scale)
    # get the aabb of the item
    print(item.bounding_box)
    # get the width/height/depth x/z/y
    print(item.width)
    print(item.height)
    print(item.depth)
```
