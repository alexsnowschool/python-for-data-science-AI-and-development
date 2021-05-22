# data type 
# int, float, str, bool 
my_int = 123
my_float = 2.3
my_str = 'I Love Python'
my_bool = True # or False
print(my_int)

# Type casting ဆိုတာ data type တစ်ခုကနေ နောက်တစ်ခုကိုပြောင်းတာ
int_to_float = float(2)
float_to_int = int(2.6)
int_to_str = str(2.3)
bool_to_int = int(False)

print(int_to_float, float_to_int, int_to_str, bool_to_int)
print(type(int_to_str)) # type ဆိုတဲ့ function ကိုသုံပြီး data အမျိူးအစားကိုစစ်နိုင်သည်

###################################################################################

# Exprission and variables 
# Expression : Mathematical Operations
# + _ * /
a = 10
b = 5
add = a + b
sub = a - b
mul = a * b
power = a ** b
div = a / b # return float
div1 = a // b # return int

print('add = {}, sub = {}, mul = {}, power = {}, div = {}, div1 = {}'.format(add, sub, mul, power, div, div1))
# print('ရေးချင်တဲ့စာသား {}'.format(variable_name))

# Python မှာ Paranthesis မပါရင် * နဲ့ / အရင်အလုပ်လုပ်တယ်
operation = 20 + 5 * 4
operation1 = 4 / 2 + 4
operation2 = 3 * (5 + 6)

print(f'operation = {operation}, operation1 = {operation1}, operation2 = {operation2}')
# print(f'ရေးချင်တဲ့စာသား {variable_name}')

# ‌Python မှာ variable names တွေထပ်လို့ရတယ်
my_int = 10
my_int = 20
print(my_int) 

total_min = 43 + 42 + 57 # 142
total_hour = total_min / 60
print(f'Total hour is {total_hour}')
# print(10/3)

######################################################

# length of a string
a = 'hello'
print(len(a))

# check string (returns boolean)
name = "Htun Khaing Lynn"
print('Khaing' in name)
print('Ko' in name)
print('Ko' not in name)

# string slicing
x = 'Hello World'
   # 012345678910 <-- index
  #-11-10-9-8-7-6-5-4-3-2-1

# Slicing မှာ ဂဏန်း ၂ လုံးပါရင် ပထမ ဂဏန်းက include ဖြစ်ပြီးတော့ ဒုတိယ ဂဏန်းက exclude ဖြစ်သည်
# ဂဏန်း ၃ လုံးပါရင် နောက်ဆုံးဂဏန်းသည် step ကျော်ရန်ဖြစ်သည်
print(x[1])
print(x[:]) # same as original string
print(x[:5]) # slice from start
print(x[2:]) # slice to end
print(x[2:5]) # slice from 2 to 5
print(x[2:10:2]) # start stop step
print(x[::-1]) # reverse the string
print(x[-11:-2]) # negative slicing

# useful string methods
x = 'I love Python'
y = ' JavaScrip is not Java '

print(x.lower()) # change to lower
print(x.upper()) # change to upper
print(x.find('I')) # return its index
print(y.strip()) # remove blanks from start and end of string
print(y.replace('J', 'C')) # replace J with C
print(x.split(" ")) # return a list

# Concatenate string
a = 'Hello'
b = 'World'
c = a + b

print(c)
