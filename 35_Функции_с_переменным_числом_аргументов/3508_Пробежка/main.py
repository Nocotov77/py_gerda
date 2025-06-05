def jogging(workout_time, *, speed, kkal, reduce):
    km = (workout_time * 60 * speed) // 1000
    burned = km * kkal
    return burned, burned >= reduce