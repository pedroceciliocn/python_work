#3-4. Guest List:
guest_list = ['akira toryiama', 'david bowie', 'diego maradona']
print(guest_list)
print(f"Hi Mrs. {guest_list[0].title()}, i would like to invite you to a dinner.")
print(f"Hello Sr. {guest_list[1].title()}, i would like to invite you to a fantastic dinner tonight.")
print(f"Ola Sr. {guest_list[2].title()}, gostaria de invitarlo para um jantar.")

#3-5. Changing Guest List:
##removing:
cant_make_it = guest_list.pop(0)
print(f"The guest that cant come to the dinner tonight is {cant_make_it.title()}.")
print(guest_list)
##replacing:
guest_list.append('Louro José')
print(guest_list)

##or replacing in a different way:
guest_list = ['akira toryiama', 'david bowie', 'diego maradona']
cant_make_it = 'akira toryiama'
guest_list.remove(cant_make_it)
print(f"The guest that cant come to the dinner tonight is {cant_make_it.title()}.")
guest_list.append('louro josé')

##printing invites:
print(f"Hi Mrs. {guest_list[0].title()}, i would like to invite you to a dinner.")
print(f"Hello Sr. {guest_list[1].title()}, i would like to invite you to a dinner tonight.")
print(f"Ola Sr. {guest_list[2].title()}, gostaria de convidá-lo para um jantar.")

#3-6. More Guests:
print(guest_list) #checking updated List
new_invited = ['pai do menino maluquinho', 'dona benta', 'roupa nova']
print("Hello all people that are invited to the wonderful dinner tonight,\ni got excelent news! we have 3 more places on table.")
print(f"The new invited important and welcome people are Sr. {new_invited[0].title()}, Ms. {new_invited[1].title()}, and Sir {new_invited[2].title()}.")

##inserting new guest to the beginning of the list:
new_separated = new_invited.pop()
guest_list.insert(0, new_separated)
print(guest_list)

new_separated = new_invited.pop()
print(new_invited) #checking list
print(new_separated) #checking list
guest_list.insert(2, new_separated)
print(guest_list)

new_separated = new_invited.pop()
guest_list.append(new_separated)
print(guest_list)

print(f"Oi Sr. {guest_list[0].title()}, gostaria de convidá-lo para um jantar hoje à noite.")
print(f"Hello Sir {guest_list[1].title()}, i would like to invite you to a dinner tonight.")
print(f"Ola Sra. {guest_list[5].title()}, gostaria de convidá-la para um jantar.")
print(f"Ola Sr. {guest_list[2].title()}, gostaría de invitarlo para uno jantar.")
print(f"Ola Sr. {guest_list[5].title()}, gostaria de convidá-lo para um jantar.")
print(f"Ola Sr. {guest_list[5].title()}, gostaria de chamá-lo para um rango à noite.")

#3-7. Shrinking Guest List:
print(guest_list) #checking the updated list
print("I have some bad news for you all srs. Saddly we cant receive you all tonight, only 2 guests will come to dinner.")

##popping out and telling people that they are uninvited:
im_sorry_list = guest_list.pop()
print(f"Foi mal {im_sorry_list.title()}, mas não poderemos recebê-lo no dia de hoje.")
print(f"A lista de convidados agora é:{guest_list}.")

im_sorry_list = guest_list.pop()
print(f"Mil desculpas {im_sorry_list.title()} não podemos receber o Sr. hoje.")
print(f"A lista de convidados agora é:{guest_list}.")

im_sorry_list = guest_list.pop()
print(f"Mil desculpas {im_sorry_list.title()} não podemos receber o Sr. hoje.")
print(f"A lista de convidados agora é:{guest_list}.")

im_sorry_list = guest_list.pop()
print(f"Mil desculpas {im_sorry_list.title()} não podemos recebê-la hoje.")
print(f"A lista de convidados agora é:{guest_list}.")

##sending a reinvite to people that still on list
print(f"Hello Sir {guest_list[1]}, we still have places for you tonight. We count with you on dinner later, cya!")
print(f"Olá Sr. {guest_list[0]}, estamos mandando essa mensagem para confirmar o seu lugar no jantar de hoje à noite. Esperamos você lá.")

##clearing the list
del guest_list[1]
del guest_list[0]
print(guest_list)