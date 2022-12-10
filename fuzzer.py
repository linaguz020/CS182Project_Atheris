import atheris
import sys
import requests

with atheris.instrument_imports():
    from bs4 import BeautifulSoup as bs

with open("corpus.txt", 'w') as f:
    f.write(requests.get("https://google.com").text)


def CustomMutator(data, max_size, seed):
    try:
        res = bs(data, features="html.parser")
    # except UnicodeEncodeError:
    #     with open("corpus.txt", 'rb') as f:
    #         data = f.read()
    except TypeError:
        with open("corpus.txt", 'rb') as f:
            data = f.read()
    else:
        data = atheris.Mutate(data, len(data))
    return data


@atheris.instrument_func
def Test(inp):
    # fdp = atheris.FuzzedDataProvider(inp)
    # inp = fdp.ConsumeString(len(inp))
    # inp = fdp.ConsumeUnicodeNoSurrogates(len(inp))
    
    a = bs(inp, features="html.parser")
    return a.prettify()


# atheris.Setup(sys.argv, Test, custom_mutator=CustomMutator)
atheris.Setup(sys.argv, Test)
atheris.Fuzz()
