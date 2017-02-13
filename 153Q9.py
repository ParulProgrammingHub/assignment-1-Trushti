sum=0
print("Enter marks out of 100")
for i in range(5):
  sum=float(sum+input("Enter marks of subject %s"%(i+1)))
mean=float(sum/5);
percent=float((um/500)*100)
print("Mean is %.2f\nPercent is %.2f"%(mean,percent))
if(percent<35):print("FAIL")
else:print("PASS")
