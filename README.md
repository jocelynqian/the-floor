Things you can play on the floor.

# Installing requirements
1. Get pip: https://pip.pypa.io/en/stable/installing/
2. Get virtualenv: `pip install virtualenv`
3. Create a virtualenv: `virtualenv <name of directory for your virtualenv>`
4. Go into your virtualenv: `source <your virtualenv dir>/bin/activate`
5. Install required python packages: `make install-requirements`

# Running
In the root directory, run `PYTHONPATH=. python web/app.py`
You should be able to hit `localhost:8888` on your browser.

# Running tests
`make test`
