def get_lines(file_type='sample'):
    '''
    Read in the lines of today's sample/input file line by line. 
    Assumes the file is in folder called 'inputs/'
    
    Parameters
    ----------
    file_type : str
        Either sample or input
    
    Returns
    -------
    list of inputs stripped of whitespace
    '''
    import datetime
    day = str(datetime.datetime.today().day).zfill(2)
    filename = f'inputs/{day}-{file_type}.txt'
    try:
        with open(filename,'r') as file:
            lines = [line.strip() for line in file.readlines()]
        return lines
    except:
        print(filename+' does not exist')
        
def create_empty_notebook(file):
    '''
    Helper function to batch create empty ipynb notebooks
    
    Parameters
    ----------
    file : <class '_io.TextIOWrapper'>
        This is a file object that you can write to.
        Write json to initialize a notebook.
    '''
    empty_lines = '{"cells": [],"metadata": {},"nbformat": 4,"nbformat_minor": 5}'
    try:
        file.write(empty_lines)
    except:
        print(f'{file} does not exist')
        
def batch_create_files(start=1):
    '''
    Create empty files at the beginning of the month for easy copy-pasting the day of.
    Assumes all files will go into folder labelled 'inputs/'
    
    Parameters
    ----------
    start : int
        Which day you want to start autopopulating (in case you forgot about this function on Day 1)

    '''
    for i in range(start,26):
        day = str(i).zfill(2)
        with open(f'inputs/{day}-sample.txt','w') as file:
            pass
        with open(f'inputs/{day}-input.txt','w') as file:
            pass
        with open(f'Day {day}-1.ipynb','w') as file:
            create_empty_notebook(file)
        with open(f'Day {day}-2.ipynb','w') as file:
            create_empty_notebook(file)