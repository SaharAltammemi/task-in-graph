import emoji
print(emoji.emojize('Python is :thumbs_up:'))
Python is ok
print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
Python is ok
print(emoji.demojize('Python is 👍'))