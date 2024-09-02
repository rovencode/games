
test1 = {"spple":1, "dressel":2, 4:6}
test2 = {"a": 3, 4:5}

"""
{
 "spple":1, "dressel":2, 4:5, "a": 3}
}

"""

def merge_dicts():
    new_test = {}
    new_test.update(test1)
    new_test.update(test2)
    print(new_test)
merge_dicts()
