#SHADOWS OF MIRKWOOD..

print("Welcome to Shadows of Mirkwood!")

playername = input("Give me your name : ") #str
print("And now your journey begins" , playername , ".Do not lose courage")
steps_left = 5 #int
courage = 5.0 #float
has_ring = False #boolean
choice = "" #empty string
attempt = 0#int

#challenge 1 : confusing paths
while(steps_left > 0 and attempt < 2):
 choice = input(" You reached a giant thorn in the forest. Go left or right?" )
 steps_left = steps_left - 1
 if choice == 'left':
    print("Phew, your path is safe " ,"steps left: " , steps_left)
 else :
    courage = courage - 1.0
    print("Bad luck! you took the wrong path. Your courage is decreased to " + str(courage) + " Steps left: " + str(steps_left))
 ultimate_question = ''
 
 if(steps_left <= 0 or courage <= 0):
    break
 
 #challenge 2 : jumbo Spider attack!!
 choice = input("A gigantic spider is blocking your path. Fight or Run?")
 if choice == 'fight':
    steps_left = steps_left - 1
    has_ring = True

    print("You defeated the spider. Now you will be facing Sauron.")
    print("Sauron - " , playername , "What is the ring called?\n" + "These are your options > 1 = One ring  2 = Narya  3 = Elven ring")
    ultimate_question = input(">")
    if(ultimate_question == "1"):
        print("Your answer is correct. The One Ring is now yours..\n" , "steps left : ", steps_left)
        break
    else:
       steps_left = steps_left - 2
       courage = courage - 1
       has_ring = False
       print("The answer is wrong. You still don't have the ring - lost courage, Courage left:" , courage , "steps_left: " , steps_left)
 else:
   has_ring = False
   courage = courage - 1
   print("You did not show courage. Courage left:" , courage)

 if(steps_left <= 0 or courage <= 0):
    break

 
 # Challenge 3 : Illusion 
 choice = input("Are you going to believe the given illusion? Yes or No : ")
 if choice == 'yes':
    courage = courage - 2
    print("You let it weaken you -- Your courage has been decreased to " , courage)
    print(" You have no courage left. You are lost in the shadows forever..")
 else: 
   print("You found the One ring. Now you can stop the darkness from spreading.")
 break 
 
    


 
      



   
   

print("""
                                                                                                    
                                                                                                                                                                                                                                                                                                                                                                                 
                                                                                                    
                                                                  .%@*#%%@@=                        
                                                               .%%..-   .@.                         
                                                            :@#. .*:.:++#.                          
                                                         :%#. .=:   .+@=.                           
                                                     ..%%.  :-.  .=@#.                              
                                                   .#%.  :+.  .-@#.                                 
                                                .+@:   =.   -@#.                                    
                                             .-@=.  ::   -@#.                                       
                                           .%*. .:-. .-@*.                                          
                                        .#*.  .:.  :@*.                                             
                                :@=*..+#.  .:   .%#.                                                
                                 .#:%.  .-.  .##.                                                   
                                 .##:*-.   -@:                                                      
                                .#%#@*@..#+.                                                        
                             .*@:=.#+%=@.                                                           
                          .#@+ -:@*. .@:=+                                                          
                        =**=-=@#.     .#=.                                                          
                        :@=#%.                                                                      
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
""")
