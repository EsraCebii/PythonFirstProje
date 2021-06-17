def flatten(top_l):
    for elem in top_l:
        if isinstance(elem,list):
            yield from flatten(elem)
        else:
            yield elem

l=[[1,'a',['cat'],2],[[[3]], 'dog'],4,5]
flat_list=[a for a in flatten(l)]
print(flat_list)