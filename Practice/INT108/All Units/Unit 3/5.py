"""
Q5. Type Conversion Function (Easy–Medium) 
Write function to_int_list(str_list) that receives list of strings and returns list of integers. 
"""

def to_int_lst(lst_str):
  # lst_int = [int(i) for i in lst_str]
  lst_int = []
  for i in lst_str:
    lst_str.apppend(int(i))

  print(lst_int)

lst_str = ['1', '2', '3']
to_int_lst(lst_str)