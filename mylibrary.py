#Introduce the concept of doc string for documentation of the function 
def hello_func(greeting, name ='You' ):
    """ Greeting function 
        You need to pass two parameters
        The first parameter is the Greeting you want and 
        the first paramter is the name to whom we want to greet
    """
    return '{}, {} '.format ( greeting, name ) 