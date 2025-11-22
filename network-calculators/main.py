# Main Python File


# Running Function
def run():
    print("-" * 35); print("\tMAIN MENU"); print("-" * 35)

    menu_options = "[A] Full Mesh Calculator\n[B] OSPF Calculator\n[C] Subnetting Calculator"
    
    print(menu_options)
    user_choice = input("Your choice: ").upper()
    
    # Conditions to selection of options 
    if user_choice == "A":
        import full_mesh
        full_mesh.fullmesh_calc()
    elif user_choice == "B":
        import ospf
        ospf.ospf_calc()
    elif user_choice == "C":
        import subnetting_calc
        subnetting_calc.main()
    else:
        exit()


run()



    

