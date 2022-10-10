from src.stats import Stats


class DataCapture:
    def __init__(self):
        self._inputs_added = []  # Inputs
        self._min_value = None  # Minimum value added
        self._max_value = None  # Maximum value added

    def add(self, input: int):
        """
        Create a dictionary with all the inputs and how many times the input is added
        """
        self._set_min(input)
        self._set_max(input)
        self._inputs_added.append(input)
        # Original idea was to use a dictionary since the beginning
        # if self._inputs.get(input) == None:
        #     self._inputs[input] = 0
        # self._inputs[input] += 1

    def _set_min(self, input: int):
        """
        Set minimum value of inputs - None validation if first input is added
        """
        if self._min_value is None:
            self._min_value = input

        if input < self._min_value:
            self._min_value = input

    def _set_max(self, input: int):
        """
        Set maximum value of inputs - None validation if first input is added
        """
        if self._max_value is None:
            self._max_value = input

        if input > self._max_value:
            self._max_value = input

    def build_stats(self) -> Stats:
        """
        Build a new dictionary of statistics, the dictionary needs to be sorted from min to maximum added,
        That way we will be able to look over the statistics (less, greater, between) in the dictionary giving a O(1) solution.
        """
        inputs = sorted(self._inputs_added)
        inputs_index = {}

        # O(n)
        for index, input in enumerate(inputs):

            temp_list = []

            if input not in inputs_index:
                inputs_index[input] = []

            temp_list = inputs_index[input]
            temp_list.append(index)

            inputs_index[input] = temp_list

        return Stats(inputs_index, self._max_value)

