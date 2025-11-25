def filterfunc(func, sub):
    filtered = filter(func,sub)
    return filtered
func = eval(input())
sub = eval(input())
for i in filterfunc(func, sub):
    print(i)