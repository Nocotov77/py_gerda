def complex_systems(arr):
    if type(arr) is not list:
        return [arr]
    if not arr:
        return []
    return complex_systems(arr[0]) + complex_systems(arr[1:])