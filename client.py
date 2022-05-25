import xmlrpc.client
import asyncio
import time



proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

async def deffsyncfunction():
    for k in range(0,15):
        await asyncio.sleep(.7)
        print("performing client operations--->")
    

async def quicksortclient(arr):
    rslt = proxy.bubbleSort(arr)
    await asyncio.sleep(0.7)
    print("Sorted array List is:------->")
    print(rslt)

    return rslt

async def defquicksortclient(arr):
    await asyncio.sleep(5)
    rslt = proxy.bubbleSort(arr)
    await asyncio.sleep(1.0)
    print("Sorted array List is:------->")
    print(rslt)

    return rslt




def synchronous():
    print("SYNCHRONOUS CALL")
    print("1st we will have input for ADDITION of two numbers and then input for SORT")
    print("<-End->")
    print("1.Addition of two numbers is :- add(a,b)")
    print("    ")
    frst_num = input("enter the first number:- ")
    frst_num = int(frst_num)
    scnd_num = input("enter the Second number:- ")
    scnd_num = int(scnd_num)
    print("<-End->")
    print("      ")
    print("2.Sorting an Array is :- sort(arr)")
    print("       ")
    arr = []
    m = input("enter the array length:- ")
    print("enter the array values:- ")
    m = int(m)
    for k in range(0, m):
        # print(k)
        val = input()
        arr.append(int(val))
    print(arr)
    print("      ")
    print("calling add function and giving 4 seconds delay in server side and calling sort function")
    add_rslt = proxy.additionoftwonumbers(frst_num, scnd_num)
    print("Sum of ",frst_num," and ",scnd_num," is: ",add_rslt)
    print("calling Sort Function")
    rslt = proxy.bubbleSort(arr)
    print("Sorted array is:")
    print(rslt)

async def asynchronous():
    print("ASYNCHRONOUS CALL")
    print("1st we will have input for ADDITION of two numbers and then input for SORT")
    print("<-End->")
    print("1.Addition of two numbers- add(a,b)")
    print("    ")
    frst_num = input("enter the first number:- ")
    frst_num = int(frst_num)
    scnd_num = input("enter the Second number:- ")
    scnd_num = int(scnd_num)
    print("<-End->")
    print("      ")
    print("2.Sorting an Array- sort(arr)")
    print("       ")
    arr = []
    m = input("enter the array length:- ")
    print("enter the array values:- ")
    m = int(m)
    for k in range(0, m):
        # print(i)
        val = input()
        arr.append(int(val))
    print(arr)
    print("      ")
    add_rslt = proxy.asyadd(frst_num, scnd_num)
    task_2 = asyncio.create_task(quicksortclient(arr))
    print("making sorting async and calling it  ")
    print("calling add function and giving a pause of 2 second and the async function does not wait for that and it prints sorting first")

    await asyncio.sleep(2)
    print("Sum of ", frst_num, " and ", scnd_num, " is: ", add_rslt)

    rslt = await task_2



async def deffsync():
    print("DEFERRED SYNCHRONOUS CALL")
    print("first we get input for addition of two numbers and then input for sort")
    print("<-End->")
    print("1.Addition of two numbers- add(a,b)")
    print("    ")
    frst_num = input("enter the first number:- ")
    frst_num = int(frst_num)
    scnd_num = input("enter the Second number:- ")
    scnd_num = int(scnd_num)
    print("<-End->")
    print("      ")
    print("2.Sorting an Array- sort(arr)")
    print("       ")
    arr = []
    m = input("enter the array length:- ")
    print("enter the array values:- ")
    m = int(m)
    for k in range(0, m):
        # print(i)
        val = input()
        arr.append(int(val))
    print(arr)
    print("   ")
    task_3 = asyncio.create_task(defquicksortclient(arr))
    task2 = asyncio.create_task(deffsyncfunction())
    print("making sorting async and calling it  ")
    print("calling add function and giving a pause of 1 second and the async function does not wait for that and it prints sorting first")
    add_rslt = proxy.asyadd(frst_num, scnd_num)
    await asyncio.sleep(1.5)
    print("Sum of ", frst_num, " and ", scnd_num, " is: ", add_rslt)
    returnval = await task_3
    returnval1 = await task2



if __name__ == "__main__":
    print("1.SYNCHRONOUS")
    print("2.ASYNCHRONOUS")
    print("3.DEFERRED SYNCHRONOUS")
    val = int(input("select a operation to perform either 1 or 2 or 3 :"))
    print(val)
    if(val==1):
        synchronous()
    elif(val==2):
       asyncio.run(asynchronous())
    elif(val==3):
        asyncio.run(deffsync())
    else:
        print("choose the given options ---")






