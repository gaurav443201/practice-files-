def main():
    try:
        a =  int(input("hey,Enter the number:"))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
         print("i am inside finally")    

main()  