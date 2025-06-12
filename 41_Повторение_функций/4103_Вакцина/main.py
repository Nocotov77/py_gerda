def vaccine_effect(value):
    immunoglobulins[:] = [x for x in immunoglobulins if x[1] >= value]
