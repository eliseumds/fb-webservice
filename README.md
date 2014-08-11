fb-webservice
=============

## Requirements

* PyPy 2.3.1
* pip 1.5.4

## Installation


```
virtualenv -p pypy env
source env/bin/activate
pip install -r requirements.txt
```

## Running

```
python run.py --env=dev.conf # env arg being optional
```

## Testing ##

```
sh run_tests.sh
```

With coverage report:

```
sh run_tests_coverage.sh
```

## Logs ##

```
python read_logs.py
```
