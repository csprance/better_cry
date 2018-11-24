# Better Cry
> Work with CRYENGINE objects in the editor in an object oriented way.

## Install
Drag and drop the `better_cry` folder into `Editor\Scripts`

## Usage
```python
from better_cry import Level
level = Level()
for item in level.selected:
    print(item.position)
    print(item.rotation)
    print(item.scale)
    print(item.bounding_box)
```
