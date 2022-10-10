<h1>Python code challenge</h1>	

<h2>Requirements:</h2>

<p>Python solution created with Python 3.9.6<p>



<h2>Set Up</h2>

<p>Since I used "PyTest" for Unit Testing, virtual environment needs to be created.</p>

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

<h1>Entry point</h1>
<p>The file: <strong>src/main.py</strong> will be our entry point. Update this file in order to add more values </p>

```
# Test inputs
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()

# Querying stats
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
```

<strong>"Test inputs":</strong> <br>
<p>Add more "capture.add(number)" lines if you want to add new values or even remove existing ones. That's the way to populate our capture object.</p>

<strong>"Querying stats":</strong>
<p>Here are the parameters that will be passed to our 'less', 'between', and 'greater' methods. </p>

<h2>NOTE:</h2>
<p>For querying stats:  </p>
<p>
When try to call stats functions (less, between, greater), parameter value should exists in the capture object. It means, if you try to call stats functions with a non-existing value added, the app will raise an exception.

Example:
Values added: [3,9,3,4,6]
If you try to do: stats.less(5) <- non-existing value added, the app will raise an exception.



</p>


<h1>Running the application:</h1>

```
python3 main.py
```

<h1>Running unit test:</h1>

```
pytest
```


