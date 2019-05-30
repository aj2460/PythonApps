import pandas

df1 =  pandas.DataFrame([[2,4,6],[10,20,30]],columns=["Price","Age","Value"])

print(df1)


#Dictionary method
# df2=pandas.DataFrame([{"Name":"Anand","Age":40}])
# print(df2)

# print(dir(df1))

print ("-"*40)
print(type(df1))
print ("-"*40)
print(type(df1.Price))

print ("-"*40)

print(df1.mean())
print(df1.Price.max())

print ("-"*40)

print(df1.mean().mean())

