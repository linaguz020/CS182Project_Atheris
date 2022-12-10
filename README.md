# CS182Project_Atheris

## Steps to run our code

0. Make sure CLang and Python are installed on your software and that you are running on a Linux OS or Linux distribution. 

1. Install Atheris
```pip install atheris```

2. Install Beautiful Soup
```pip install beautifulsoup4```

3. Install requests
```pip install requests```

4. Clone our repository into your environment.

5. Run the following command to simulate our program.
```python3 fuzzer.py```

If you want to use the corpus, run the code at least once to allow requests to pull the html into the corpus.txt file. From there, run with seeded corpus with
```python3 fuzzer.py -seed_inputs=corpus.txt
