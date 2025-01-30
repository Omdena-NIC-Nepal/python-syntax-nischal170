def format_string(name, age):
  
    
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    if number>10:
        return "Greater"
    if number<10:
        return "Lesser"
    if number>10:
        return "Equal"
   

def loop_sum(n):
    sum=0
    for i in range(n):
        sum=sum+i
    return sum


def list_operations(numbers):
    new_tuple=tuple(numbers)
    return new_tuple

def dict_operations(students_dict):
    
    
    
    student_list=list()
    for student in students_dict:
        if student.score > 80:
            student_list.append(student.name)
            return student_list
    

def set_operations(list1, list2):
    list3=list1 & list2
    return list3
    

def arithmetic_ops(a, b):
    
    return  dict(sum=f"{a+b}",difference=f"{a-b}",product=f"{a*b}",quotient=f"{a/b}")

def logical_ops(x, y):
    {
        'and': x and y, 
        'or': x or y,    
        'not_x': not x   
    }

def bitwise_ops(a, b):
    return {
        'and': a & b,   
        'or': a | b,   
        'not_a': ~a     
    }
   