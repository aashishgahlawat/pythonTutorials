def lesson_002_helper(*, _list: list, _dict: dict):
    _surprise_txt = "I might surprise you"
    _list.append(_surprise_txt)
    _dict.update({"surprise": _surprise_txt})


def lesson_010_generator():
    # Generators are memory efficient
    # Not necessarily faster
    for i in range(10_000):
        yield i

def lesson_010_generator_return():
    _list: list[int, ...] = []
    for i in lesson_010_generator():
        if i == 1_000:
            # Yielding back list of 1_000 instead of 10_000
            break
        _list.append(i)
    return _list

def lesson_010_for_loop():
    _list: list[int, ...] = []
    for i in range(10_000):
        _list.append(i)
    return _list

def lesson_026_real_data():
    return {"data": "Real Data"}

def lesson_026_data():
    return lesson_026_real_data()

def lesson_026_monkey_patched_data():
    return {"data": "Dummy Data"}
