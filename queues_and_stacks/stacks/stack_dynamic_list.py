dynamic_list = []

def push(value):
    global dynamic_list
    dynamic_list += [value]

def pop():
    global dynamic_list
    last = dynamic_list-1
    dynamic_list = dynamic_list[0:len(dynamic_list)-1]

push("a")
push("b")
print(dynamic_list)
pop()
print(dynamic_list)