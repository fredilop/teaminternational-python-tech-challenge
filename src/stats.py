class Stats:

    def __init__(self, inputs_index: dict, max_value: int):
        self._inputs_index = inputs_index
        self._max_value = max_value

    def less(self, value: int) -> int:
        try:
            if value in self._inputs_index:
                return self._inputs_index[value][0]
            raise KeyError

        except KeyError:
            raise KeyError("Not valid arguments")

        except Exception:
            raise Exception("General exception")

    def between(self, min_value: int, max_value: int) -> int:
        try:
            min = self._inputs_index[min_value][0]
            max = self._inputs_index[max_value][-1]
            return (max - min) + 1
        except KeyError:
            raise KeyError("Not valid arguments")
        except Exception:
            raise Exception("General exception")

    def greater(self, value: int) -> int:
        try:
            min = self._inputs_index[value][-1]
            max = self._inputs_index[self._max_value][-1]
            return max-min
        except KeyError:
            raise KeyError("Not valid arguments")
        except Exception:
            raise Exception("General exception")
