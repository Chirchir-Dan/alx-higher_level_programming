#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:  # Check if sentence is empty
        return (0, None)
    else:
        return (len(sentence), sentence[0])
