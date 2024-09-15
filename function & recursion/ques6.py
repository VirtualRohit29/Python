def remove(l, word):
    n = []
    for item in l:
        if item != word:  # Skip the word to be removed
            n.append(item.strip())  # Strip whitespace, not the word itself
    return n  # Return should be outside the loop

l = ["harry ", " rohit", " sachin ", "nadeem "]
print(remove(l, "rohit"))  # Remove "rohit" and strip whitespaces

