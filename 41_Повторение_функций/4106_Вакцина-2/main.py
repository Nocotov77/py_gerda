def vaccine_filter(func):
    immunoglobulins[:] = [x for x in immunoglobulins if func(x)]