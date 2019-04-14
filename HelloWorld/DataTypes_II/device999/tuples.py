

if __name__ == '__main__':
    tuplex = tuple()
    tuplex = (False,1,42,3.2)
    print(len(tuplex))
    tuplex = reversed(tuplex)
    print(tuple(tuplex))
    empty_tuple= [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
    new_list = []
    for i in empty_tuple:
        if i:
            new_list.append(i)
    print (new_list)