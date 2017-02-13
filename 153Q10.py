def simple_interest(principal,time,rate):
  return(principal*time*rate/100)
  p=input("Enter the principal money")
  r=input("Enter the rate of interest")
  t=input("Enter the time in years")
  print("Simple Interest:%.2f\ntherefore,total amount is %.2f"%(simple_interest(p,r,t),(simple_interest(p,r,t)+p)))
  
