def funct(*args, **kwargs): # *args is positional, **kwargs is named
    # print("Positional:", args)
    print("Named:", kwargs)


# positional = funct(100, 25, 75)
named = funct(ones=3000, benjamins=600)