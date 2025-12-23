def insert_btree(_root, value):
       _root.append(value)
       _root.sort()

       if len(_root) == 3:
           middle_index = len(_root) // 2

           middle = _root[middle_index]
           left = _root[:middle_index]
           right = _root[middle_index+1:]

           return [middle, left, right]

       return _root

root = []
insert_btree(root,10)
insert_btree(root,4)
insert_btree(root,2)

print(root)