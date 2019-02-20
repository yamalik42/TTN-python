from abc import ABC, abstractmethod

class Box(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def add(self):
        pass

    @abstractmethod    
    def empty(self):
        pass

    @abstractmethod    
    def count(self):
        pass

class Item():
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
class ListBox(Box):
    def __init__(self, *items):
        self.items = list()
        do_put(items, self.items)
    
    def add(self, *items):
        do_put(items, self.items)

    def empty(self):
        tmp = self.items[:]
        self.items.clear()
        return tmp
    
    def count(self):
        return len(self.items)

class DictBox(Box):
    def __init__(self, *items):
        self.items = {}
        do_put(items, self.items)
    
    def add(self, *items):
        do_put(items, self.items)

    def empty(self):
        tmp = list(self.items.values())
        self.items.clear()
        return tmp
    
    def count(self):
        return len(self.items)

def do_put(iterable, container):
    class NonItemError(Exception):
        pass
    for item in iterable:
        try:
            if type(item) != Item:
                raise NonItemError
            if type(container) == list:
                container.append(item)
            else:
                key = item.name
                container[key] = item
        except NonItemError:
            msg = (f'{item} is not of Item class so it was not added to box.\n'
                    'If any other Items present, they were added to box.')
            print(msg)

def repack_boxes(*boxes):
    class NonBoxError(Exception):
        pass
    all_boxes = []
    all_items = list() 
    for box in boxes:
        try:
            if not isinstance(box, Box):
                raise NonBoxError
            all_boxes.append(box)
            if type(box) == ListBox:
                all_items.extend(box.items)
                box.empty()
            else:
                all_items.extend(box.items.values())
                box.empty()
        except NonBoxError:
            msg = (f'{box} is not a Box instance so it was not repacked.\n'
                    'If any other Boxes present, they were repacked.')
            print(msg)
    while len(all_items):
        i = len(all_items) % len(all_boxes)
        all_boxes[i].add(all_items.pop())
    return
            

########## TEST CASE ############
if __name__ == '__main__':
    box1 = ListBox()
    box2 = ListBox()
    box3 = DictBox()

    [box1.add(Item(f'item{i}', i)) for i in range(1,21)]
    [box2.add(Item(f'item{i}', i)) for i in range(21,30)]
    [box3.add(Item(f'item{i}', i)) for i in range(30,35)]
    print(f'box1 has {box1.count()} items before repacking.')
    print(f'box2 has {box2.count()} items before repacking.')
    print(f'box3 has {box3.count()} items before repacking.\n')

    repack_boxes(box1,box2,box3)
    print(f'box1 has {box1.count()} items after repacking.')
    print(f'box2 has {box2.count()} items after repacking.')
    print(f'box3 has {box3.count()} items after repacking.\n')
