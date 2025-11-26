tasks = input("enter your taskak").split(", ")
done = []
ongoing = []
for work in tasks:
    print(work)
    q = input("finish??")
    if q == "yes":
        print("goooood")
        done.append(work)
    else:
        print("do it please")
        ongoing.append(work)
qq = input("see progress????")
if qq == "yes":
  print(f"done tasks are: {done}")
  print(f"not yet tasks are: {ongoing}")
  
