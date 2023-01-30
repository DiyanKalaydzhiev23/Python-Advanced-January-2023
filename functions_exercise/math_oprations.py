def math_operations(*numbers, **kwargs):
    for i in range(len(numbers)):
        key = list(kwargs.keys())[i % 4]

        if key == "a":
            kwargs[key] += numbers[i]
        elif key == "s":
            kwargs[key] -= numbers[i]
        elif key == "d":
            if numbers[i] != 0:
                kwargs[key] /= numbers[i]
        elif key == "m":
            kwargs[key] *= numbers[i]

    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return '\n'.join(f"{k}: {v:.1f}" for k, v in kwargs)
