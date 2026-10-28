

import os 

# Lista que vai guardar temporariamente os utilizadores lidos do DBmaster.txt
# Cada utilizador seguira o formato user_id|nome|password

list = []

def program_users(list): # Lê o ficheiro principal de utilizadores, caso exista
    if os.path.exists("DBmaster.txt"): #Se ficheiro existe no sistema percorre o programa
        with open("DBmaster.txt", "r") as ficheiro:
            for line in ficheiro: 
                spaces = line.strip().split("|") # .strip() remove espaços no inicio e no fim do texto introduzido, .split() divide a string por ("|")
                if len(spaces) == 3:
                    list.append([spaces[0], spaces[1], spaces[2]]) #Função irá percorrer os espaços e verificar se existem dados nos mesmo. Irá servir apenas no caso da lista estiver vazia.


def start_program(list):
    program_users(list)
    print("\nWelcome to the students aplication!\n")# O programa vai começar por perguntar o ID dos utilizadores existentes no DBmaster
    
    if len(list) == 0: #Se o tamanho da lista for 0. Irá propôr ao user para criar um novo contacto
        print("\nNo users in database. Please create an account to continue.\n")
        while True:
            user_id = input("Insert the ID of the student: ").strip()
            if user_id.isdigit(): #Validações 
                break
            print("Error! Must be a number")
        while True:  
            name = input("Insert the name of the student: ").strip()
            if name.isalpha():
                break
            print("Error! Must only contain letters.")
        while True:       
            password = input("Insert password: ").strip()
            if len(password) == 4 and password.isdigit():
                break
            print("Error! Password has to be 4 digits. Do not use letters only numbers.")

        student = [user_id, name, password]
        list.append(student) #Adiciona as informações do user na lista
        with open("DBmaster.txt", "a") as ficheiro:
            ficheiro.write(f"{user_id}|{name}|{password}\n") #Informações irão ser escritas no ficheiro e guardadas
        print(f"\nAccount created with sucess. Welcome {name}!")
        return user_id, name, password
    
    while True: #No caso de já existirem users no ficheiro. Irá pedir para inserir o ID do aluno.
        user_id = input("Please insert user ID to continue the program: ").strip()
        found = False # Controla se o ID introduzido foi encontrado na lista de utilizadores
        
        for user in list:
            if user [0] == user_id: #Se o ID corresponder a um numero que exista no ficheiro continua o programa
                found = True
                for trying in range(2): #User irá ter 2 tentativas para o inserir a password
                    password = input("Insert password: ").strip()
                    if password == user[2]:
                        print(f"\nWelcome, {user[1]}!")
                        return user_id, user[1], user[2]
                    else:
                        if trying == 0:
                            print("\nWrong password. Try again.")
                        else: # Se ambas as tentativas forem erradas. Irá dar a opção de mudar de ID.
                            op = input("\nWould you like to try different ID? (y/n): ").strip().lower() # Neste caso remove os espaços no iniico e no fim. Converte tudo para minusculas (irá ter de ser escrito "y" e nao "Y")
                            if op == "y":
                                break # Se for sim o programa voltará atrás ao qual irá pedir para ser inserido o ID correspondente.
                            else:
                                return None, None, None # Se for não o programa acaba. #Função start_program devolve sempre tres valores - user_id e name e password. Irá dar erro ao tentar dar unpack dos tres valores.
        if not found:
            op = input(f"User '{user_id}' not found. Would you like to create a new one? (y/n): ") #Se tentar inserir um ID nao existente na tabela. Irá dar a opção de criar um novo user.
            if op == "y":
                print("\nAdd new student")
                while True:
                    name = input("Insert the name of the student: ").strip() 
                    if name.isalpha():
                        break
                    print("Error! Must only contain letters.")
                while True:
                    user_id = input("Insert the ID of the student: ").strip()
                    if user_id.isdigit():
                        break
                    print("Error! Must be a number")
                while True:         
                    password = input("Insert password: ").strip()
                    if len(password) == 4 and password.isdigit():
                        break
                    print("Error! Password has to be 4 digits.")
                    
                student = [user_id, name, password]
                list.append(student)
                print(f"\nStudent {name, user_id} was added to the list.")
                with open("DBmaster.txt", "a") as ficheiro: # Novo user irá ser guardado no ficheiro
                    ficheiro.write(f"{user_id}|{name}|{password}\n")
                print(f"Account created with sucess! Welcome {name}!")
                return user_id, name, password
            else:
                op2 = input("\nTry a different ID? (y/n): ").strip().lower()
                if op2 != "y":
                    return None, None, None # Se não quer tentar outro ID termina o programa


def general_status(ucs, user_id):
    if len(ucs) == 0:
            print("\n# No subjects found! Please add a new subject (2) to be able to see General Status")
            return True
    
    print("############################################")
    print(f"#")
    print(f"# User: {user_id}")
    print(f"#")
    print(f"# Option: GENERAL STATUS")
    print(f"#")
    print("############################################")
    print(f"#")
    print(f"# {'Code':<10} {'Name':<12} {'Attendance':<12} {'Behaviour':<12} {'Assay':<8}") # FOi usado desta maneira sob a forma de f strings para garantir que a tabela impressa na consola ficasse alinhada.
    print(f"#")                                                                             #  O : indica onde vai começar, < significa o alinhamento a esquerda e os definem o espaço fixo em caracteres daquela coluna. 
    print(f"#")                                                                                    #Impede o desalinhamento do layout
    
   
    total = 0
    for uc in ucs: #Percorre tas as UCS na lista
        media_uc = (int(uc[2]) * 0.05) + (int(uc[3]) * 0.10) + (int(uc[4]) * 0.85) # As notas são convertidas de string para inteiro para ser possivel realizar o seu calculo.
        total += media_uc
        print(f"# {uc[0]:<10} {uc[1]:<12} {uc[2]:<12} {uc[3]:<12} {uc[4]:<8} Final: {media_uc:.1f}") #.1 faz a formatação do resultado para 1 casa decimal
        
    media_geral= total / len(ucs) # Divide total por numero de UCS existentes
    print(f"#")
    print(f"# Average: {media_geral:.1f}")

print("############################################")


def add_subject(ucs, user_id, changes):
    # UCS sao criadas numa lista de memoria.
    # So e atualizado quando for o user fizer save
    print(f"""
############################################
#
# User: {user_id}
#
# Option: ADD SUBJECT
#
############################################
#
# Format: UC<code> <name> <attendance> <behaviour> <assay>
# 
#
############################################ 
""")
    add = input("\n - - - ATENTION - - -\nCode must be in format UC00000 (UC + 5 numbers)\nGrades must be between 0 and 20\nFollow the format!\n\nInsert: ").strip().split()
    
    if len(add) != 5: #Verifica se foram inseridos exatamente 5 campos
        print("ERROR! Invalid format. Must have 5 fields.")
        return

    code = add[0] 
    name_uc = add[1]
    
    if len(code) != 7 or not code.startswith("UC") or not code[2:].isdigit():
        print("ERROR! Code must be in format UC00000 (UC + 5 numbers).")
        return
    
    if not add[2].isdigit() or not add[3].isdigit() or not add[4].isdigit():
        # Verifica se as notas sao numeros antes de converterem a int
        print("Error! Grades must be numbers!")
        return
        
    attendance = int(add[2])
    behaviour = int(add[3])
    assay = int(add[4])
    
    if not (0 <= attendance <= 20) or not (0 <= behaviour <= 20) or not (0 <= assay <= 20): #Vai fazer a verificação se as notas se encontram dentro do intervalo valido
        print("Error! Grades must be between 0 and 20.")
        return
    
    # Impede a criação de UC's com o mesmo codigo
    for uc in ucs:
        if uc[0] == code:
            print("ERROR! This UC already exists")
            return
            
    # As notas são convertidas novamente para string para manter o mesmo formato usado quando os dados são escritos no ficheiro.
        
    uc = [code, name_uc, str(attendance), str(behaviour), str(assay)] 
    ucs.append(uc) 
    changes.append(f"\nSubject {code} {name_uc} added with sucess!") # Alteração registada para depois ser o user ver as alterações no summary



def edit_subject(ucs, user_id, changes):
    if not verify_list(ucs):
        return
    
    list_ucs(ucs) #Verificação para ajudar de forma visual o que o utilizador pretende editar

    while True:
        indice = input("\nInsert the number of the UC to edit: ").strip()

        if indice.isdigit() and 1 <= int(indice) <= len(ucs):  # Valida se o número está dentro do intervalo da lista
            indice = int(indice) - 1 # Subtrai 1 porque a lista começa no índice 0
            break
        print(f"ERROR! Must be a number between 1 and {len(ucs)}.")
        
    code = ucs[indice][0] #Guarda o codigo para mostrar no final

    print("############################################")
    print(f"#")
    print(f"# UC selected:")
    print(f"#")
    print(f"# {'Code':<10} {'Name':<12} {'Attendance':<12} {'Behaviour':<12} {'Assay':<8}")
    print(f"#")
    print(f"# {ucs[indice][0]:<10} {ucs[indice][1]:<12} {ucs[indice][2]:<12} {ucs[indice][3]:<12} {ucs[indice][4]:<8}")
    print(f"#")
    print("############################################")

    print("\n--Edit Subject--") 
    print(f"""
############################################
#
# User: {user_id}
#
# Option: EDIT SUBJECT
#
# 1 - Edit Code
# 2 - Edit Name
# 3 - Edit Attendance Grade
# 4 - Edit Behaviour Grade
# 5 - Edit Assay Grade
#
############################################

""")
    op = input("Insert options: ").strip()
    
    ## Mais validações para ter a certeza que o user introduz os dados corretos no programa ##
    
    if op == "1":
        new = input("\nInsert new code: ").strip()
        if len(new) != 7 or not new.startswith("UC") or not new[2:].isdigit():
                print("ERROR! Code must be in format UC00000 (UC + 5 numbers).")
                return
            
        for i, uc in enumerate(ucs):
            if i != indice and uc[0] == new:
                print("ERROR! UC code already exists.")
                return
        old_code = ucs[indice][0]
        ucs[indice][0] = new #Vai fazer a substituição do valor introduzido ao longo do codigo
        changes.append(f"edit {old_code} Code -> {new}")
    elif op == "2":
        new = input("Insert new name: ").strip()
        if not new.isalpha():
            print("ERROR! Must only contain letters.")
            return
        old_name = ucs[indice][1]
        ucs[indice][1] = new
        changes.append(f"edit {code} name -> {old_name} -> {new}")
    elif op == "3":
        new = input("Insert new Attendance Grade: ").strip()
        if not new.isdigit() or not (0 <= int(new) <= 20):
            print("ERROR! Grade must be between 0 and 20.")
            return
        ucs[indice][2] = new
        changes.append(f"Edited Attendance -> {new}")
    elif op == "4":
        new = input("Insert new Behaviour Grade: ").strip()
        if not new.isdigit() or not (0 <= int(new) <= 20):
                    print("ERROR! Grade must be between 0 and 20.")
                    return
        ucs[indice][3] = new
        changes.append(f"Edited Behaviour -> {new}")
    elif op == "5":
        new = input("Insert new Assay Grade: ").strip()
        if not new.isdigit() or not (0 <= int(new) <= 20):
                    print("ERROR! Grade must be between 0 and 20.")
                    return
        ucs[indice][4] = new
        changes.append(f"Edited Grade -> {new}")
    else:
        print("Invalid option!")
        return
    
    print(f"\n{code} edited with sucess!")
    
def list_subject(ucs, user_id):
    if not verify_list(ucs):
        return
    list_ucs(ucs)
    
    while True:
        indice = input("\nInsert the number of the Subjet you wish to see: ").strip()

        if indice.isdigit() and 1 <= int(indice) <= len(ucs): 
            indice = int(indice) - 1 # A lista começa no indice 0, o utilizador escolhe a partir de 1
            break
        print(f"ERROR! Must be a number between 1 and {len(ucs)}.")
    
    uc_found = ucs[indice] # Guarda a UC encontrada para facilitar o acesso aos campos
    
    print("############################################")
    print(f"#")
    print(f"# User: {user_id}")
    print(f"#")
    print(f"# Option: LIST SUBJECT")
    print(f"#")
    print("############################################")
    print(f"# {'Code':<10} {'Name':<12} {'Attendance':<12} {'Behaviour':<12} {'Assay':<8}")
    print(f"#")
    print(f"# {uc_found[0]:<10} {uc_found[1]:<12} {uc_found[2]:<12} {uc_found[3]:<12} {uc_found[4]:<8}")
    print(f"#")
    print(f"#")
    print("############################################")

def save_ucs(ucs, user_id, changes):
    
    # Cada utilizador possui o seu proprio ficheiro de UCS
    # Será identificado pelo seu user_id
    
    filename = f"{user_id}_status.txt" 
    
    with open(filename, "w") as ficheiro: # W vai fazer a substituição por completo do ficheiro para nao haver duplicações
        for uc in ucs:
            ficheiro.write(f"{uc[0]}|{uc[1]}|{uc[2]}|{uc[3]}|{uc[4]}\n") # Guarda cada UC por linha, usando "|" como separador
     
    changes.clear() # Depois de guardar deixa de existir alterações pendentes
            
    print(f"\nData has been saved with sucess!")
    
def del_user(ucs, user_id, password_user, list):
    print("############################################")
    print(f"#")
    print(f"# User: {user_id}")
    print(f"#")
    print(f"# Option: DELETE")
    print(f"#")
    print(f"# --- Are you certain that you wish to permanently delete all user info? --- (y/n)")
    print(f"#")
    print("############################################")
    
    op = input("\nOption: ").strip().lower()
    
    if op != "y":
        print("\nDelete cancelled. Returning to menu.")
        return False
    
    print("############################################")
    print(f"#")
    print(f"# User: {user_id}")
    print(f"#")
    print(f"# Option: DELETE")
    print(f"#")
    print(f"# INSERT THE PASSWORD: ")
    print(f"#")
    print("############################################")

    password = input("\nPassword: ").strip()
    
    if password != password_user:
        print("Wrong password! Delete canceled.")
        return False
    
    ucs.clear()
    filename = f"{user_id}_status.txt"
    if os.path.exists(filename):
        os.remove(filename)
    
    if os.path.exists("DBmaster.txt"):
        with open("DBmaster.txt", "r") as ficheiro:
            lines = ficheiro.readlines()                #Vai fazer a leitura das linhas de codigo no ficheiro. E todas que começam pelo user_d ao qual vai ser deleted nao sao write no programa (rewrite)
        with open("DBmaster.txt", "w") as ficheiro:
            for line in lines:
                if not line.startswith(f"{user_id}|"):
                    ficheiro.write(line)
           
    print(f"\nAll data from the user '{user_id}' has been deleted.")
    return True
    
    
def exit_program(ucs, user_id, changes):
    
    # Nao havendo alterações pendentes o programa termina
    if len(changes) == 0:
        return True
    
    print("############################################")
    print(f"#")
    print(f"# User: {user_id}")
    print(f"#")
    print(f"# Option: EXIT")
    print(f"#")
    print(f"# --- You still have the following changes pending, do you wish to save them? --- (y/n)")
    print(f"#")
    print("############################################")
    print(f"#")
    print(f"#\tSUMMARY:")
    print(f"#")
    for change in changes: # Mostra todas as alterações pendentes
        print(f"#\t{change}")
    print("############################################")

    op = input("Option: ").strip().lower()
    if op == "y":
        save_ucs(ucs, user_id, changes)
    
    return True

def load_ucs(ucs, user_id):
    # Carrega as UCs guardadas no ficheiro para o programa
    # Função apenas e chamada no inicio do programa para evitar a duplicação de UCs no ficheiro
    filename= f"{user_id}_status.txt"
    if os.path.exists(filename):
        with open(filename, "r") as ficheiro:
            for line in ficheiro:
                spaces = line.strip().split("|")
                if len(spaces) == 5:
                    ucs.append([spaces[0], spaces[1], spaces[2], spaces[3], spaces[4]])
                    


def verify_list(ucs): # Esta função irá servir para verificar a existência de uma lista de UC's
    if len(ucs) == 0:
        print("\nList is empty.") # No caso de nao haver da return ao menu
        return False
    return True # Se existir continua o codigo
    

def list_ucs(ucs):
    if not verify_list(ucs):
        return
    print(f"\n -- List of UCs available ({len(ucs)}) in total --") # Vai mostrar a quantidade de Uc's no total (para ajudar o utilizador a escolher a UC que pretende alterar)
    for i in range(len(ucs)):
        print(f"{i + 1}. {ucs[i][0]} - {ucs[i][1]}")
        
# -------------------- MENU -----------------------#

user_id, name, password_user = start_program(list) #Inicia o programa e obtem o user_id e nome apos o login

list = [] 

ucs = [] 

def menu(user_id):
    print(f"""
############################################
#
# User: {user_id}
#
# Options:
# 1 - General Status
# 2 - Add Subject
# 3 - Edit Subject
# 4 - List Subject
# 5 - Save 
# 6 - Delete
# 7 - Exit
#
############################################
    """)


if user_id:
    load_ucs(ucs, user_id)
    changes = [] #Inicia a lista de alterações
    
    while True:
        menu(user_id)
        op = input("Options:").strip()

        if op.upper() == "1":
            general_status(ucs, user_id)

        elif op.upper() == "2":
            add_subject(ucs, user_id, changes)

        elif op.upper() == "3":
            edit_subject(ucs, user_id, changes)

        elif op.upper() == "4":
            list_subject(ucs, user_id)

        elif op.upper() == "5":
            save_ucs(ucs, user_id, changes)

        elif op.upper() == "6":
            deleted = del_user(ucs, user_id, password_user, list)
            if deleted:
                print("\nProgram closing . . .")
                break
            
    
        elif op.upper() == "7":
            exit_program(ucs, user_id, changes)
            break
            
            
        else:
            print("\nInvalid! Select the correct option.")
