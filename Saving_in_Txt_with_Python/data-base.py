import os.path
from os import path
while True:
    def check_if_txt_exists():
        if path.exists('contacts.txt') == True:
            return True
        else:
            return False
    if check_if_txt_exists() == False:
        file = open('contacts.txt', 'w')
    print('{:^20}'.format('1 - ADD\n2 - CHANGE\n3 - DELETE\n4 - SEARCH\n5 - EXIT'))
    option = input('What you wanna do? ').strip()
    contacts = {}
    dic_aux = {}
    file = open('contacts.txt', 'r')
    lines = file.readlines()
    def is_empty():
        check_if_txt_exists()
        if not lines:   
            return True
        else:
            return False
    def get_datas_from_txt():
        check_if_txt_exists()
        file = open('contacts.txt', 'r')
        lines = file.readlines()
        for line in lines:
            line_split = line.split('-')
            name = line_split[0]
            name_string = ''.join(line_split[0]) # Name to string so we can use the upper and strip methods
            name = name_string.upper().strip()
            phoneNumber = line_split[1]
            dic_aux[name] = phoneNumber
        file.close()
    def setDatas_in_Empty_File():
        check_if_txt_exists()
        name = input('Name: ').upper().strip()
        phoneNumber = input('Phone number: ')
        dic_aux[name] = phoneNumber
        add_to_dict()
        send_to_database()
        get_datas_from_txt()
        your_contacts()        
    def setDatas_in_not_Empty_File():
        check_if_txt_exists()
        get_datas_from_txt()
        name = input('Name: ').upper().strip()
        phoneNumber = input('Phone number: ')
        dic_aux[name] = phoneNumber
        add_to_dict()
        send_to_database()
        get_datas_from_txt()
        your_contacts()
        file.close()
    def change():
        check_if_txt_exists()
        get_datas_from_txt()
        add_to_dict()
        your_contacts()
        contact_to_change = input('Contact name you wanna change: ').upper().strip()
        for key in dic_aux.keys():
            if key == contact_to_change:
                new_name = input('New name: ').upper().strip()
                new_phone_number = input('New phone number: ')
                dic_aux[new_name] = dic_aux.pop(key)
                dic_aux[new_name] = new_phone_number   
            else:
                continue
        your_contacts()           
    def delete():
        check_if_txt_exists()
        get_datas_from_txt()
        add_to_dict()
        your_contacts()
        contact_to_delete = input('Contact name you wanna delete: ').upper().strip()
        delete = [key for key in dic_aux if key == contact_to_delete]
        for key in delete: del dic_aux[key]           
        your_contacts()
    def search():
        check_if_txt_exists()
        get_datas_from_txt()
        add_to_dict()
        contact_to_search = input('Who u looking for? ').strip().upper()
        for key, value in dic_aux.items():
            if contact_to_search == key:
                print(f'Here it is. Nome: {key.capitalize()} ---- Telefone: {value}')
    def add_to_dict():
        check_if_txt_exists()
        for key, value in dic_aux.items():
            contacts[key] = value
    def your_contacts():
        check_if_txt_exists()
        print('YOUR CONTACTS LIST')
        for contact in sorted(dic_aux.items()):
            name_str = ''.join(contact[0])
            print(f'Nome: {name_str.capitalize()} ---- Telefone: {contact[1]}')
    def send_to_database():
        add_to_dict()
        file = open('contacts.txt', 'w')
        for contact in sorted(dic_aux.items()):
            string = f'{contact[0]}-{contact[1]}'
            file.write(f'{string.strip()}\n')
        file.close()    
    # Here starts the conditions
    if option == '1' and is_empty() == True:
        setDatas_in_Empty_File()
        send_to_database()
    elif option == '1' and is_empty() == False:
        setDatas_in_not_Empty_File()
        send_to_database()
    elif option == '2' and is_empty() == False:
        change() 
        send_to_database()
    elif option == '2' and is_empty() == True:
        print('No contacts found!')
    elif option == '3' and is_empty() == False:
        delete()
        send_to_database()        
    elif option == '3' and is_empty() == True:
        print('No contacts found!')
    elif option == '4' and is_empty() == False:
        search()
    elif option == '4' and is_empty() == True:
        print('No contacts found!')
    elif option == '5':
        break
    else:
        print('unavailable option')