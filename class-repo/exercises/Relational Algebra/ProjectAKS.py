def project_yield(table, *atr):
    for row in table:
        row_dict = {}
        for attribute in row:
            if attribute in atr:
                row_dict[attribute] = row[attribute]
        yield row_dict
def project_comprehension(table, *atr):
    for row in table:
        yield {attribute : row[attribute] for attribute in row if attribute in atr}
def project_generator(table, *atr):
    return ({attribute : row[attribute] for attribute in row if attribute in atr} for row in table)