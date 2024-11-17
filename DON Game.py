def namingthetextfile(): # Naming the text file
     # Geting the current date and time
    current_date_time = datetime.datetime.now()
    
    date=current_date_time.strftime("%Y_%m_%d")
    time=current_date_time.strftime("%H_%M_%S")

    randomnum=str(random.randrange(0,9999)).zfill(4)

    filename = f"{date}_{time}_{randomnum}.txt"
    return filename
       
def gamestatus(name,attempt,life,status): # Game status
    print(f"\n\n***Game status***\nPlayer name : {name}\nTotal attempts : {attempt}\nFinal score : {life}\n{name} {status}")    
    
def play_game(name): # Gameplay
    attempt=1
    enemylist=[]
    fight=0
    status="was defeated!!!"
    
    filename=namingthetextfile()
    with open(filename, 'w') as file: # opening the text file
        file.write("")
        
        if (attempt==1):
            life=random.randrange(1,51)
            while (attempt<20):

                file.write(f"Player name : {name}\n")
                print(f"Attempt : {attempt} \n{name}'s life score is : {life}")
                file.write(f"Attempt : {attempt} \n{name}'s life score is : {life}\n")
            
                enemycount=0
                if (attempt<=5):
                   #Enemies
                    while (enemycount<5):
                        enemycount+=1
                        enemy=random.randrange(15,101)
                        print(enemy,end=" ")
                        file.write(f"{enemy} ")
                        enemylist.append(enemy)
                    print("")
                    fight=int(input("Select a number to fight : "))
                    file.write(f"\nSelect a number to fight : {fight}\n")
                    
                    if (fight in enemylist):
                        if (fight<=life):
                            print(f"{name} killed {fight}\n")
                            file.write(f"{name} killed {fight}\n\n")
                            life=life+fight
                            attempt+=1
                            continue
                        else:
                            print(f"{fight} killed {name}")
                            file.write(f"{name} killed {fight}\n")
                            break
                    
                    else:
                        print("No such enemy")
                        file.write("No such enemy\n")
                        break
                    
                elif (attempt<=10):
                    #Enemies
                    while (enemycount<5):
                        enemycount+=1
                        enemy=random.randrange(250,2001)
                        print(enemy,end=" ")
                        file.write(f"{enemy} ")
                        enemylist.append(enemy)
                    print("")
                    fight=int(input("Select a number to fight : "))
                    file.write(f"\nSelect a number to fight : {fight}\n")
                    
                    if (fight in enemylist):
                        if (fight<=life):
                            print(f"{name} killed {fight}\n")
                            file.write(f"{name} killed {fight}\n\n")
                            life=life+fight
                            attempt+=1
                            continue
                        else:
                            print(f"{fight} killed {name}")
                            file.write(f"{name} killed {fight}\n")
                            break
                    
                    else:
                        print("No such enemy")
                        file.write("No such enemy\n")
                        break

                elif (attempt<=15):
                    #Enemies
                    while (enemycount<5):
                        enemycount+=1
                        enemy=random.randrange(3000,10001)
                        print(enemy,end=" ")
                        file.write(f"{enemy} ")
                        enemylist.append(enemy)
                    print("")
                    fight=int(input("Select a number to fight : "))
                    file.write(f"\nSelect a number to fight : {fight}\n")
                
                    if (fight in enemylist):
                        if (fight<=life):
                            print(f"{name} killed {fight}\n")
                            file.write(f"{name} killed {fight}\n\n")
                            life=life+fight
                            attempt+=1
                            continue
                        else:
                            print(f"{fight} killed {name}")
                            file.write(f"{name} killed {fight}\n")
                            break
                    
                    else:
                        print("No such enemy")
                        file.write("No such enemy\n")
                        break

                elif (attempt<=20):
                    #Enemies
                    while (enemycount<5):
                        enemycount+=1
                        enemy=random.randrange(20000,100001)
                        print(enemy,end=" ")
                        file.write(f"{enemy} ")
                        enemylist.append(enemy)
                    print("")
                    fight=int(input("Select a number to fight : "))
                    file.write(f"\nSelect a number to fight : {fight}\n")
                    
                    if (fight in enemylist):
                        if (fight<=life):
                            print(f"{name} killed {fight}\n")
                            file.write(f"{name} killed {fight}\n\n")
                            life=life+fight
                            status="saved letter-kind"
                            attempt+=1
                            continue
                        else:
                            print(f"{fight} killed {name}")
                            file.write(f"{name} killed {fight}\n")
                            break
                    
                    else:
                        print("No such enemy")
                        file.write("No such enemy\n")
                        break

            gamestatus(name,attempt,life,status)
            file.write(f"\n\n***Game status***\nPlayer name : {name}\nTotal attempts : {attempt}\nFinal score : {life}\n{name} {status}")
            file.close() # Closing the text file

# MAIN PROGRAM    
import sys
import datetime
import random
don=input("Player name : ")
play_game(don) 
