def oxford_comma(items):
    if len(items) == 1:
        return items[0]

    elif len(items)== 2:
        first = items[0]
        second = items[1]
        return f"{first} and {second}"
    else:
        all_but_last = items[0:-1]
        last = items[-1]
        new_but_last = ", ".join(all_but_last)
        return f"{new_but_last}, and {last}"
