# OSPF Calculator




print("-" * 35); print("\tOSPF CALCULATOR")
print("-" * 35)



def ospf_calc():

    rb = int(input("Please input reference bandwidth: "))
    ib = int(input("Please enter interface bandwidth: "))
    cost = rb // ib 

    # cost = reference bandwidth / interface bandwidth

    print(f"Cost: {cost}")


# Main Function
if __name__ == "__main__":
    while True:
        ospf_calc()

        use_again = input("Use again? [Y/N]\t").upper()
        if use_again != "Y":
            print("Goodbye!"); break

    