def age_assignment(*names, **data):
    result = []

    for letter, age in data.items():
        person_name = ""

        for name in names:
            if name.startswith(letter):
                person_name = name
                break

        result.append(f"{person_name} is {age} years old.")

    return '\n'.join(sorted(result))