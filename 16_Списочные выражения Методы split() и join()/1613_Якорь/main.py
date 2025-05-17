url = input().strip()
print([part for part in url.split('#')[0].split('/') if part][-1])