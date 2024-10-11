#!/usr/bin/python3
"""
This module contains the canUnlockAll function that determines if
all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked starting from box 0.

    Args:
        boxes (list of lists): A list where each index represents a box
                               and the list at that index contains the keys
                               to other boxes.
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # Create a set to track the opened boxes (starting with the first box)
    opened_boxes = set([0])
    # Stack to track boxes that need to be opened
    keys_stack = [0]
    # Process each box using DFS
    while keys_stack:
        current_box = keys_stack.pop()

        # Go through each key in the current box
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                # If the box isn't opened yet and the key is valid
                opened_boxes.add(key)
                keys_stack.append(key)  # Add the new box to the unlocked stack

    # If all boxes have been opened, return True
    return len(opened_boxes) == len(boxes)
