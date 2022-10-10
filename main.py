from src.data_capture import DataCapture


# Test inputs
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()

# querying stats
stats_less_function = 4
stats_between_function = (3, 6)
stats_greater_function = 4

less_result = stats.less(stats_less_function)
between_result = stats.between(stats_between_function[0], stats_between_function[1])
greater_result = stats.greater(stats_greater_function)

# printing results
print(f"Inputs added: {capture._inputs_added}")
print(f"Items Less than {stats_less_function}: { less_result }")
print(f"Items Between than {stats_between_function}: { between_result }")
print(f"Items Greater than {stats_greater_function}: { greater_result }")
