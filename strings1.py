######################################
# message = 'five night at freddy\'s'

# print(message)

# >> output: /el-python$ py strings1.py
#                    five night at freddy's  
# >> \ ters slash ile ' kullanıldı

  ###
# message = "hi there"

# print(len(message))

# output >> /el-python$ py strings1.py >>> 8  len()>boşluklar dahil harf sayısı 

#############################

message = "hi there"

raw = r'this %d that is a %s ' %(21 , 'postal' )

multi = r"""what? \n you don't 
sell postal"""





print(message[1:100]) 
#print(len(message))
#print(message + str(" ") + str('would you like to sign my petition'))

# [] içinde yazılan sayı ile kaç numaralı dizede olduğunu gösterir   örn: [0:5] 0dan 5e kadar olanları yazar, 5 dahil
# len() dizenin uzunluğunu gösterir 
# str() fazladan string eklemek için kullanılır sadece + eklenmez


#print(message.count('e'))     # upper() , lower() ,  count('hi there') , find('t')   

#print(raw)
# >> kesme işaretinin başına r harfini eklersen alt satıra geçmez


#print(multi)



greeting = "hi there "

name = "ugurhan"

xmessage = f'{greeting}, {name.capitalize()}. would you like to sign my petition'

print(xmessage)