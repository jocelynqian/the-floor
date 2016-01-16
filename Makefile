install-requirements:
		pip install -r requirements.txt

lint:
		flake8 games web tests

test:	lint
		PYTHONPATH=. py.test tests

