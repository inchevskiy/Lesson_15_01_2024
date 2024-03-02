class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        if self.min_value <= start <= self.max_value:
            self.current = start
        else:
            raise ValueError(f"Invalid starting value {start}, should be between {self.min_value} and {self.max_value}")

    def set_max(self, max_max):
        if max_max >= self.min_value:
            self.max_value = max_max
            self.current = min(self.current, max_max)
        else:
            raise ValueError(f"Invalid maximum value {max_max}, should be greater than or equal to {self.min_value}")

    def set_min(self, min_min):
        if min_min <= self.max_value:
            self.min_value = min_min
            self.current = max(self.current, min_min)
        else:
            raise ValueError(f"Invalid minimum value {min_min}, should be less than or equal to {self.max_value}")

    def step_up(self):
        self.current = min(self.current + 1, self.max_value)

    def step_down(self):
        self.current = max(self.current - 1, self.min_value)

    def get_current(self):
        return self.current


# Example usage:
counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'

try:
    counter.step_up()
except ValueError as e:
    print(e)

assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'

try:
    counter.step_down()
except ValueError as e:
    print(e)