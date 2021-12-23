def power(base_num , pow_num) :
    result = 1
    for index in range (pow_num):
        result = result *base_num
    return result
print(power(5,8))


no_list = [
    [ 9, 0 , 1 ],
    [ 8, 7 , 6 ],
    [ 5 , 4 , 3 ],
    [ 0 ]
]
for row in no_list:

  for column in row :
    print(column)

for row in no_list:

  for column in row :
    print(column*3)


for row in no_list:

  for column in row :
    print(column*(column+1))


name = input("enter your name :")
total = (int(input("enter  your degree in english :"))
+int(input("enter  your degree in math :"))
+int(input("enter  your degree in arabic:"))
+int(input("enter  your degree in physic :"))
+int(input("enter  your degree in chemistry :")))

rate = total / 5
print(rate)