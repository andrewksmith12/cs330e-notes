def theta_join_yield(table1, table2, up):
    for row1 in table1:
        for row2 in table2:
            if up (row1, row2):
                yield dict(row1, **row2)

def theta_join_generator(table1, table2, up):
    return (dict(row1, **row2) for row1 in table1 for row2 in table2 if up(row1,row2))