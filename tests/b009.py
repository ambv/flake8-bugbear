def inefficent_set():
    my_list = [1, 2, 2, 3, 4]
    return set([x for x in my_list if x % 2 == 0])

def inefficent_dict():
    my_list = [1, 2, 2, 3, 4]
    return dict([(e, 0) for e in my_list])

def do_this_instead():
    my_list = [1, 2, 2, 3, 4]
    # no need to build a list just to throw it away later!
    return set(x for x in my_list if x % 2 == 0)
