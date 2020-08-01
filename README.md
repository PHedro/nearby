### Usage:
Install Python 3.8.5 or greater, you can do it via pyenv https://github.com/pyenv/pyenv#installation with and virtualenv
```commandline
pyenv install 3.8.5
pyenv virtualenv 3.8.5 nearby
```
Activate the virtualenv
```commandline
pyenv activate nearby
```
Clone the project
```commandline
git clone git@github.com:PHedro/nearby.git
```
Go to the project folder (the one where you can find the README file)
```commandline
cd /path/to/project/ 
```
At this folder you will find both `export.txt` and `sample_usage.py`. The `export.txt` one 
contains an output example using the `nearby/tests/data/customers.txt` file as 
input file, Origin at `GeoLocation(latitude=53.339428, longitude=-6.257664)` and
`100 KM` range from the Origin (default value). 
The `sample_usage.py` has an example on how to configure and use the `nearby` package.
It's configured with the configurations described above.
You can easily change the parameters to test other distances, input and output files and Origin point.
To execute `sample_usage.py`, after activating your virtualenv and changing directory to the same directorya as the script:
```commandline
python sample_usage.py
```
Or from anywhere, but with virtualenv activated:
```commandline
python /path/to/project/sample_usage.py
```

You don't need to install any extra library, the project uses only the batteries included in Python 3.8.5.