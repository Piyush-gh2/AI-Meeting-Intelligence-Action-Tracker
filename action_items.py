import re

def extract_action_items(text):

    actions = []

    lines = text.split("\n")

    for line in lines:

        if "-" in line:
            actions.append(line.strip())

    return actions