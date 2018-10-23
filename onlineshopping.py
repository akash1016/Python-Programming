from easygui import *
import sys
while 1:
    msgbox("Online Shopping")

    msg ="Which website do you want to choose?"
    title = "Online shopping"
    choices = ["Amazon", "Flipkart", "Snapdeal", "Myntra","Jabong"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
   
    if choice=="Amazon":
      msg="In which section you want to do shopping?"
      title="welcome to Amazon"
      choices=["Electronics", "Clothes", "Kitchen Appliances", "Mobile & Laptop"]
      choice=choicebox(msg, title, choice)

    elif choice=="Flipkart": 
      msg ="In which section you want do shopping ?"
      title = "welcome to Flipkart"
      choices = ["Electronics", "Clothes", "Mobile & Laptop", "Shoes"]
      choice = choicebox(msg, title, choices)

    elif choice=="Myntra": 
      msg ="In which section you want do shopping ?"
      title = "welcome to Myntra"
      choices = [ "Clothes", "Shoes"]
      choice = choicebox(msg, title, choices)

    elif choice=="Jabong": 
      msg ="In which section you want do shopping ?"
      title = "welcome to Jabong"
      choices = [ "Clothes"]
      choice = choicebox(msg, title, choices)

    elif choice=="Snapdeal": 
      msg ="In which section you want do shopping ?"
      title = "welcome to Snapdeal"
      choices = ["Electronics", "Clothes", "Mobile & Laptop", "Shoes"]
      choice = choicebox(msg, title, choices)
 
      msg="Do you want to continue?"
      title="please confirm"
      if ccbox(msg,title):
          pass
      else:
        sys.exit(0)
