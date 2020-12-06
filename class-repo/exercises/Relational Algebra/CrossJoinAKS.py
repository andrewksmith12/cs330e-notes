def cross_join_yield(table1, table2):
    for row1 in table1:
        for row2 in table2:
            yield dict(row1,**row2)
def cross_join_generator(table1,table2):
    return (dict(row1,**row2) for row1 in table1 for row2 in table2) 