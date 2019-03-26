import emoji
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
print(emoji.emojize('Python is :car:', use_aliases=True))
print(emoji.demojize('Python is 👍'))
print("\U0001f600")
