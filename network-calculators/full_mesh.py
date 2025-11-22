# Full Mesh Calculator
print("-" * 35); print("\tFULL MESH CALCULATOR")
print("-" * 35)


# Full Mesh Formula
def fullmesh_calc():
    n = int(input("Amount of hosts: "))
    undirected_connections = n * (n-1) // 2
    directed_connections = n * (n-1)

    print(f"Undirected connections:{undirected_connections}\nDirected Connections: {directed_connections}")
    

# Main Function
if __name__ == "__main__":
    while True:
        fullmesh_calc()
        
        use_again = input("\nUse Again?[Y/N]\t\n").upper()

        if use_again != "Y":
            back_to_menu = input("Back to Main Menu?[Y/N]\t").upper()
            if back_to_menu == "Y":
                import main 
                main.run()
