def all_variants(text):
    len_ = len(text)
    for i in range(1, len_ + 1):
        for j in range(len_ - i + 1):
            yield text[i:j + i]


a = all_variants("abc")
for i in a:
    print(i)
