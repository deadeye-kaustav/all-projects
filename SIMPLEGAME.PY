print("hello,welcome guys!!")

ans = input("are you ready to play (yes/no): ")
score = 0
total_q = 4

if ans.lower() == "yes":
    
    ans = input("1.what is another name for graphic card? ")
    if ans.lower() == "video card":
        score += 1
        print("correct")
    else:
        print("incorrect")
        
        

    ans = input("2.who is the most fit footballer? ")
    if ans.lower() == "cristiano ronaldo":
        score += 1
        print("correct")
    else:
        print("incorrect")
        
        

    ans = input("3. 2 + 8+9 - 1 ")
    if ans.lower() == "18":
        score += 1
        print("correct")
    else:
        print("incorrect")
        
        

    ans = input("4.who won the fifa 1st time? ")  
    if ans.lower() == "uruguay":
        score += 1
        print("correct")
    else:
        print("incorrect")


print("thankyou for playing, you got" , score, "questions correct.")
mark = (score/total_q) * 100
print("mark: ", mark)
print("goodbye play again!!")



    



        
