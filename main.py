def get_client_details():
    client_name = input("Enter the client's name: ")
    project_name = input("Enter the project name: ")
    
    return client_name, project_name
def add_services():
    services=[]
    while True:
        services_name=input("Enter the service name :")
        price=float(input("Enter price : "))
        services.append((services_name,price))
        more=input("Do you want to add more services? (yes/no):")
        if more.lower()!="yes":
            break
    return services
def calculate_total(services):
    total=0
    for service in services:
        total+=service[1]
    return total   
def generate_invoice(client_name, project_name, services, total):
    print("="*30)
    print("    invoice")
    print("="*30)
    print(f"client  : {client_name}")
    print(f"project : {project_name}")
    print("="*30)
    print("Service\t\tPrice")
    for service in services:
        print(f"{service[0]}\t\t{service[1]}")
    print("="*30)
    print(f"Total Amount: ₹{total}")
    print("="*30)
def main():
   choice = input("Do you want to create an invoice? (yes/no):")
   if choice.lower()=="yes":
         client, project = get_client_details()
         services = add_services()
         total = calculate_total(services)
         generate_invoice(client, project, services, total)
   else:
       print("Exiting the program.")
        
if __name__== "__main__":
    main()   