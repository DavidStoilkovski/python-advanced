def age_assignment(*args, **kwargs):
    my_dict = {}

    for i in range(len(args)):
        for el in kwargs:
            name = args[i]
            if name.startswith(el):
                my_dict[name] = kwargs[el]

    return my_dict