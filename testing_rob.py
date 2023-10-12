with open('output_price.txt', 'r') as f:
    outputs_check = f.readline().strip()
    out_price_check = f.readline()

with open('output_price.txt', 'w') as f:
    f.write(str(["a|a","a|a"]))
    f.write("\n")
    f.write(str([1,2,3]))

print(1,outputs_check)
print(2,out_price_check)
print(3,out_price_check == str([1,2,3]))
