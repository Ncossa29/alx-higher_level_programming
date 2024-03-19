#!/usr/bin/python3
def multiple_returns(sentence):
    my_tle = ()
    if len(sentence) == 0:
        my_tle = 0, "None"
    else:
        my_tle = len(sentence), sentence[0]
    return my_tle
