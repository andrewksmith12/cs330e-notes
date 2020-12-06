def natural_join_yield(table1, table2):
    def filter(row1,row2):
        return not any(row1[column] != row2[column] for column in row1 if column in row2)
    for row1 in table1:
        for row2 in table2:
            if filter(row1, row2):
                yield dict(row1, **row2)
def natural_join_generator(table1, table2):
    return (dict(row1,**row2) for row1 in table1 for row2 in table2 if not any(row1[column] != row2[column] for column in row1 if column in row2))


def natural_join_other(table1, table2):
    def bp(row1,row2):
        for key in row1:
            if (key in row2) and (row1[key] != row2[key]):
                return False
        return True
    for row1 in table1:
        for row2 in table2:
            if bp(row1,row2):
                yield dict(row1, **row2)