[![CircleCI](https://circleci.com/gh/godatadriven/asekuro.svg?style=svg)](https://circleci.com/gh/godatadriven/asekuro)

# Asekuro

A commandline util for jupyter notebooks, possibly to be used in trainings and/or githooks.

> Asekuro means insurance in esperanto. 

![](notebook-img.png)

The main goal is to have a commandline app that can be used in githooks. The main 
feature we wanted in this app is that we had a nice way to: 

1. Clear notebook cells 
2. Be able to confirm that the notebook can run without errors.
3. Be able to deal with solutions via `%load` magic.  
4. Be able to automatically add a copyright notice and a logo at the top. 

# Quick-Start 

Installation currently needs to occur via git. 

```
> pip install asekuro
```

Note that we only support python 3. 

# Usage 

Once installed, the commandline app can be used. 

#### Testing a Notebook 

We merely test if the notebook can be run from top to bottom without any 
errors. This may be dependant on the virtualenv that you're currently running.

```
> asekuro test tests/testnb.ipynb
2018-07-30 15:40:04,060 [commandline.py:test_notebook:113] DEBUG - about to test tests/testnb.ipynb
...
2018-07-30 15:40:04,074 [commandline.py:clean_notebook:82] DEBUG - /tmp/testnb-test.ipynb is now stripped
============== test session starts =======================================================================
platform darwin -- Python 3.6.5, pytest-3.6.4, py-1.5.4, pluggy-0.7.1 -- 
/Users/coder/path/asekuro/venv/bin/python
cachedir: ../../../../../tmp/.pytest_cache
rootdir: /tmp, inifile:
plugins: nbval-0.9.1
collected 6 items                                                                                                                                                                                                                                                   

tmp/testnb-test::ipynb::Cell 0 PASSED                                        [ 16%]
tmp/testnb-test::ipynb::Cell 1 PASSED                                        [ 33%]
tmp/testnb-test::ipynb::Cell 2 PASSED                                        [ 50%]
tmp/testnb-test::ipynb::Cell 3 PASSED                                        [ 66%]
tmp/testnb-test::ipynb::Cell 4 PASSED                                        [ 83%]
tmp/testnb-test::ipynb::Cell 5 PASSED                                        [100%]
============== 6 passed in 1.11 seconds  ==================================================================
2018-07-30 15:40:05,983 [commandline.py:test_notebook:118] DEBUG - removing temporary testing notebook /tmp/testnb-test.ipynb
2018-07-30 15:40:05,984 [commandline.py:test_notebook:120] DEBUG - testing done for tests/testnb.ipynb
```

#### Clean Notebook 

Sometimes you may want to remove the output of the cells. This can be done automatically now too. 

```
> asekuro clean tests/testnb.ipynb 
2018-07-30 15:44:23,508 [commandline.py:clean_notebook:76] DEBUG - about to strip tests/testnb.ipynb of output
2018-07-30 15:44:23,516 [commandline.py:clean_notebook:82] DEBUG - tests/testnb.ipynb is now stripped
```

#### Testing 

You can run some unit tests via `pytest`. Note that we test using local notebooks 
as well as a docker container. We want the container that is there to break the build. 
