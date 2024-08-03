class State:
    def __init__(self):
        self.values = {}

    def update(self, key, value):
        self.values[key] = value

state = State()
w = 'exampleKey'
data = ['value1', 'value2', 'value3']
i = 1

state.update(w, data[i])

print(state.values)  # {'exampleKey': 'value2'}
