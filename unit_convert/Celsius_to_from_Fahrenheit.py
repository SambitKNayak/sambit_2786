# sambit_2786/unit_convert/Celsius_to_from_Fahrenheit.py

def convert_c(fahrenheit):
    c = float(fahrenheit) 
    c = (c-32)*5/9 
    return(c) 
def convert_f(celsius): 
    f = float(celsius) 
    f = (f * 9/5) + 32. 
    return(f) 
