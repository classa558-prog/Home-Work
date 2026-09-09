tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (6, 7, 8, 9, 10, 11)
tuple_result = ()
for i in tuple1:
    index_i = tuple1.index(i)
    tuple_result+=(i*tuple2[index_i],)
print(f"The result tuple is: {tuple_result}!")