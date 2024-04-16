#!/usr/bin/python3
"""
This module provides class LockedClass that prevents the user form
dynamically creating new instance attributes
"""


class LockedClass:
    """
    This class prevents dynamic creation of new instance attributes,
    except for 'first_name'.
    """

    __slots__ = ['first_name']
