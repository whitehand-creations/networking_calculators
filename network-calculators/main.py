# Main Python File


# Running Function
def run():
    print("-" * 35); print("\tMAIN MENU"); print("-" * 35)

    menu_options = "[A] Full Mesh Calculator\n[B] OSPF Calculator"
    
    print(menu_options)
    user_choice = input("Your choice: ").upper()
    
    if user_choice == "A":
        import full_mesh
        full_mesh.fullmesh_calc()
    elif user_choice == "B":
        import ospf
        ospf.ospf_calc()
    else:
        exit()


run()



    

