def format_string(name, age):
  
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    if number>10:
        return "Greater"
    if number<10:
        return "Lesser"
    elif number==10: 
        return "Equal"
   

def loop_sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum


def list_operations(numbers):
    sorted_numbers=sorted(numbers)
    max=sorted_numbers[0]
    min=sorted_numbers[-1]
    sum_num=sum(numbers)
    return (sum_num,min,max)

def dict_operations(students_dict):
    student_list=[]
    for student in students_dict:
        if students_dict[student] > 80:
            student_list.append(student)
    return student_list
    

def set_operations(list1, list2):
    set1=set(list1)
    set2=set(list2)
    return set1 & set2
    

def arithmetic_ops(a, b):

    
    return  {"sum":int(f"{a+b}"),"difference":int(f"{a-b}"),"product":int(f"{a*b}"),"quotient":int(f"{a/b}")}

def logical_ops(x, y):
    return{
        'and': x and y, 
        'or': x or y,    
        'not_x': not x   
    }

def bitwise_ops(a, b):
    return {
        'and': a & b,   
        'or': a | b,
        'xor':a^b,  
        'not_a': ~a     
    }
   