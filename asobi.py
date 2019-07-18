print('靴下何食べる？')
aaa = input('食べる(yes)/食べない(no)')



if 'no' or '食べない' in aaa:
    aka = input('何故？')
    reason = aka


elif 'yes'or '食べない' in aaa:
    iki = input('何故？')
    reason = iki

else:
    print('yes か no　でヨロ')
    quit()




print('衛生的に靴下食べるのはどうかと思います。')




open_kutusita = open('kutusita.txt', 'a', encoding = "utf_8")

open_kutusita.write('{}/'.format(reason))
open_kutusita.close()


