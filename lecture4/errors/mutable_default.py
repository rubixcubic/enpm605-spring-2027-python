def log_reading(r, history=[]):
    history.append(r)
    return history


a = log_reading(2.5)
b = log_reading(0.9)
print(a, b, a is b)
print(log_reading.__defaults__)
