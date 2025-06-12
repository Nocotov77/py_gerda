def big_data(*data, key=None):
    if key is None:
        key = x[0]
    result = []
    for tpl in data:
        id_val, date, email = tpl
        login_part = email.split('@')[0]
        login = login_part[0].upper() + login_part[1:].lower() if login_part else ''
        d, m, y = date.split('-')
        login += d[0] + m[-1] + y[-1]
        result.append(tpl + (login,))
    return sorted(result, key=key)