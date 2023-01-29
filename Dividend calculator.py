#dividend calculators 


def dividend_payment():
    investment=float(input("How much are you planning to invest? "))
    syield2=float(input("What is the stocks dividend yield?"))
    stocksyield=syield2/100
    
    payout=int(input("Are dividends paid out monthly? (1:Yes\n 2:No) "))
    if payout == 1:
            monthly=(investment * stocksyield)/12
            print("The amount you will be paid out monthly is: $",monthly)
    else:
            quarterly=(investment * stocksyield)/4
            print("The amount you earn every quarterly is: $", quarterly)


dividend_payment()





def dividend_calculator():
    desired_income=(float(input("How much dividend income do you want annually? ")))
    syield=(float(input("What is the stocks dividend yield? ")))
    stocks_yield=syield /100
    total_invest=(desired_income / stocks_yield)
    shares=float(input("What is the share price? "))
    total_shares=int(total_invest/shares)
    reply= print("You will need $",total_invest,"today to make your desired income monthly.")
    reply_2= print("You will need",total_shares,"shares to reach that goal. Good luck!")
    return(reply, reply_2)

dividend_calculator() 


