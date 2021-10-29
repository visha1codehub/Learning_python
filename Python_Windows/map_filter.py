###map function###
# lis = ['23','765','34','98']
# lis = list(map(int,lis))

# for item in lis:
#     item += 1
#     print(item)

# num = [3,6,8,12,14,17,90,9,10]
# square = list(map(lambda a : a*a,num))
# print(square)

###fiter function###
list1 = [1,2,3,4,5,6,7,8,9,10]
grtr_than_5 = list(filter(lambda x:x>5,list1))
print(grtr_than_5)

list2 = [1,2,4,5,8,9,16,24,25,100]
def is_sqt(x):
    return int(x**0.5)**2 == x
prfct_sqr = list(filter(is_sqt,list2))
print(prfct_sqr)