# args allows you to pass multiple variables to a function after previously passed hard-coded arguments
# *argv -> sequence of arguments seperated by variables
# think of "*" as a pointer to a list, as you can see we iterate through the "elements" of *argv as we would a list

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

# **kwargs allows you to pass keyworded variable length of arguments to a function 
# think of ** as a double pointer; pythonic interpretation: a dictionary argument containing addtional arguments
# note: function must be called with the ** in front of the kwargs variable e.g. below it's the var 'bati'

# example 1 - similar to practical use case the the .format builtin function used on strings

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))
# greet_me(name="Yaaqoob")

# example 2

def list_things(**kwargs):
    for key, value in kwargs.items():
        print(key+": "+value)

bati = {"name": "chris", "value": "high", "date of birth": "23 April 1969"}
list_things(**bati)



# practical use case in Dominos api:

url = "https://order.dominos.com/power/store/{store_id}/menu?lang={lang}&structured=true"
kwargs = {'lang': 'en', 'store_id': '10464'}
updated_url = url.format(**kwargs)
