class Person:
    def __init__(self,user_id,name):
        self.name=name
        self.user_id=user_id
        
    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.user_id
    
    def display_info(self):
        pass



class Student(Person):
    def __init__(self,user_id,name,department,year):
        super().__init__(user_id,name)
        self.department=department
        self.year=year

    def display_info(self):
        pass


class Resource:
    def __init__(self, resource_id, name, category, quantity):
        self.__resource_id = resource_id     
        self.name = name
        self.category = category
        self.total_quantity = quantity
        self.available_quantity = quantity
    
    def get_resource_id(self):
        return self.__resource_id
    
    def allocate(self):
        if self.available_quantity>0:
            self.available_quantity-=1
            return True
        else:
            return False
        
    def return_resource(self):
        if self.available_quantity < self.total_quantity:
            self.available_quantity += 1


class ResourceManager:
    def __init__(self):
        self.users = []
        self.resources = []
        self.allocations = {}

    def add_user(self, user):
        self.users.append(user)
        print("User added successfully.")

    def add_resource(self, resource):
        self.resources.append(resource)
        print("Resource added successfully.")

    def find_user(self, user_id):
        for user in self.users:
            if user.get_id() == user_id:
                return user
        return None

    def find_resource(self, resource_id):
        for resource in self.resources:
            if resource.get_resource_id() == resource_id:
                return resource
        return None

    def allocate_resource(self, user_id, resource_id):

        user = self.find_user(user_id)
        if not user:
            print("User not found.")
            return

        resource = self.find_resource(resource_id)
        if not resource:
            print("Resource not found.")
            return

        if user_id in self.allocations:
            print("User already has a resource.")
            return

        if resource.allocate():
            self.allocations[user_id] = resource_id
            print("Resource allocated successfully.")
        else:
            print("Resource not available.")

    def return_resource(self, user_id):

        if user_id not in self.allocations:
            print("No resource allocated to this user.")
            return

        resource_id = self.allocations[user_id]
        resource = self.find_resource(resource_id)

        if resource:
            resource.return_resource()

        del self.allocations[user_id]
        print("Resource returned successfully.")
        
    def show_allocations(self):
        if not self.allocations:
            print("No active allocations.")
            return

        for user_id, resource_id in self.allocations.items():
            print(f"User {user_id} → Resource {resource_id}")



def add_student(manager):
    uid = int(input("Student ID: "))
    name = input("Name: ")
    dept = input("Dept: ")
    year = int(input("Year: "))
    manager.add_user(Student(uid, name, dept, year))


def add_resource(manager):
    rid = int(input("Resource ID: "))
    name = input("Name: ")
    category = input("Category: ")
    qty = int(input("Quantity: "))
    manager.add_resource(Resource(rid, name, category, qty))


def allocate(manager):
    uid = int(input("User ID: "))
    rid = int(input("Resource ID: "))
    manager.allocate_resource(uid, rid)


def return_res(manager):
    uid = int(input("User ID: "))
    manager.return_resource(uid)


def main():
    manager = ResourceManager()

    while True:
        print("1.Student  2.Resource  3.Allocate  4.Return  5.Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_student(manager)

        elif choice == "2":
            add_resource(manager)

        elif choice == "3":
            allocate(manager)

        elif choice == "4":
            return_res(manager)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

main()

