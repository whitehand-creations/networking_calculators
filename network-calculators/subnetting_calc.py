# Subnetting Calculator

print("="*35); print("\tSUBNETTING CALCULATOR")
print("="*35)

# Lists CIDR Notations
def cidr_info():
   print()

   cidr_nots = """
        CIDR   \tUsable Hosts
        /32    \t0
        /31    \t0 (point-to-point)
        /30    \t2
        /29   \t6
        /28    \t14
        /27    \t30
        /26    \t62
        /25    \t126
        /24    \t254
        /23    \t510
        /22    \t1022
        /21    \t2046
        /20    \t4094
        /19    \t8190
        /18    \t16382
        /17    \t32766
        /16    \t65534
               """
   
   print("="*35); print(cidr_nots); print("="*35)
   
    

# Subnet Calculator
def subnet_calc():

    host_bits = int(input("Enter amount of host bits: "))
    eq = 2 ** host_bits - 2 # Subnetting Formula

    print(f"You have {eq} usuable hosts")


def main():
    # Indefinite Loop
    while True:
        chartop = input("Would you like to see the CIDR Chart? Yes or No: ").upper() # Chart options
        
        if chartop == "YES":
            cidr_info()
            proceed_opt = input("Proceed to subnet calculator? Yes or No: ").upper()
            if proceed_opt == "YES":
                subnet_calc()
            else:
                break
        else:
            subnet_calc()
        
        try_again = input("Try again? Yes or No: ").upper()

        if try_again != "YES":
            print("Goodbye!"); break



# Main function
if __name__ == "__main__":
    main()

