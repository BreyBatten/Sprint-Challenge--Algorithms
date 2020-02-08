'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # if length of passed in word is 2 chars or longer, run next conditional, else return 0 at the end
    if len(word) >= 2:
        # from the start of the word, if it contains a substring of "th"
        if word[:2] == 'th':
            # add 1 and call the function again starting at next index through the end of the word
            return 1 + count_th(word[1:])
        # call function again starting at next index
        else: return count_th(word[1:])
    return 0
