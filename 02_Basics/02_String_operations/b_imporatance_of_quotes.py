
#!/usr/bin/python3
"""
Purpose: Importance and usage of multiple quotes
"""
language = 'Python Programming'
print(language, type(language))

question = 'How are you ?'
print(question, type(question))


# where_abouts = 'what's up?' # SyntaxError: invalid syntax
where_abouts = 'what\'s up?' 
check="whats' up?"
print(check)
print(where_abouts)

# NOTE 1: Placing \ before any operator with result
# in treating operator as a ordinary character


other_string = 'What\'s going in yours\' in-laws\' house'
print(other_string, type(other_string))


other_string = "What\'s going in yours\' in-laws\' house"
print(other_string, type(other_string))


other_string = "What's going in yours' in-laws' house"
print(other_string, type(other_string))


some_other_str = '''What's up in yours' daugther's "wedding"'''
print(some_other_str)

# db_command = "select * from mytable where name like "udha*""
# SyntaxError: invalid syntax

db_command = '''select * from mytable where name like "udha*"'''
print(db_command)


# db_command = '''select * from mytable where name like 'udha*''''
# SyntaxError: unterminated string literal (detected at line 41)

db_command = '''select * from mytable where name like 'udha*' '''
print(db_command)

db_command = '''select * from mytable where name like 'udha*'; '''
print(db_command)


db_command='''select *  from helloworld where name like 'udha*' '''
print(db_command)


some_other_str = """ python -c 'awdwad' asdss "sfdsdfd", '''dedfdfwef sd -m jd;jd''' """
print(some_other_str)


print("\n\n")
# '\''
# "'"
# '"'
# ''' '""' '''
# """ ''' '""' '''' """
# "  ''' "


# Multi-line Strings

# print(
#     "Today is an awesome day
#     to learn python"
# )
# SyntaxError: unterminated string literal (detected at line 66)


print(
    'Today is an awesome day \
    to learn python'
)

print(
    "Today is an awesome day \
    to learn python"
)



print(
    '''Today is an awesome day \
    to learn python'''
)

print(
    '''Today is an awesome day 
    to learn python'''
)

print(
    """Today is an awesome day 
    to learn python"""
)


print(
    '''
    a - apple
    b - ball
    c - cat
    d - dog'''
)

# NOTE 2: triple quote strings are multi-line strings


sql_cmd = '''
    Select  *
    from table1 t1
    LEFT JOIN table2 t2 on t1.id = t2.id
    ORDER BY t1.id;
'''
print(sql_cmd)
print()

# multiline concatenation
print(
   ( 
       "Today is an awesome day"
        "to learn python"
   )
)
print()



# Gotcha
# my_string = 'select * from my_table where column='python' and column2 = "django"'
# my_string = "select * from my_table where column='python' and column2 = "django""
my_string = ''' select * from my_table where column='python' and column2 = "django"'''
print(my_string)

# my_string = """  select * from my_table where column='python' and column2 = "django""""
# my_string = ''' select * from my_table where column='python' and column2 = 'django''''
my_string = """ select * from my_table where column='python' and column2 = 'django' """
print(my_string)

my_string = """ select * from my_table where column='python' and column2 = 'django';"""
print(my_string)
