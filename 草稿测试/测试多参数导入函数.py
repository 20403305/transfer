
show_list = ['name',  'gender','phone']

show_dict = {'name':'Dacky',  'gender':'boy','phone':'110'}

def personal_info_list(name,gender,phone):
    print(name)
    print(gender)
    print(phone)

personal_info_list(*show_list)
personal_info_list(**show_dict)

# 函数传参位置的*表示，需要明确指明变量名才能传入
def personal_info_dict(*,name,gender,phone):
    print(name)
    print(gender)
    print(phone)

# personal_info_dict(*show_dict)
personal_info_dict(**show_dict)
