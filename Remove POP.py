#Remove element from an Array
colors = ["vioet", "indigo","blue","Green","Yellow", "orange","Red"]
print(colors)

del colors[4]
colors.remove("blue")
print(colors)

colors.pop(3)
print(colors)

#output#
#['vioet', 'indigo', 'blue', 'Green', 'Yellow', 'orange', 'Red']
#['vioet', 'indigo', 'Green', 'orange', 'Red']
#['vioet', 'indigo', 'Green', 'Red']
