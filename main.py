from solid import Solid
from solids import Cone, Sphere
from solidset import SolidSet

def displayMenu():
    print('Welcome to solid set!\nEnter one of the following numbers for options:\n1. Display all the solid shapes in the solid set.\n2. Search for and display a certain solid by its ID.\n3. Display all the spheres in the solid set.\n4. Display all the cones in the solid set.\n5. Add a sphere to the solid set.\n6. Add a cone to the solid set.\n7. Get the total volume of the solid set.\n8. Quit the application.\n')
    
if __name__ == "__main__" :
    SS = SolidSet()
    user = 0
    
    while user != '8':
        displayMenu()
        user = input('Enter your choice: ')
        if user == '1':
            if len(SS.getSolids()) == 0:
                print()
            else:
                for index in SS.getSolids():
                    print(index)
                    print()
        if user == '2':
            found = False
            userID = input("Enter a solid ID: ")
            for index in SS.getSolids():
                if userID == index.getID():
                    print(f'Found ID: {userID}')
                    print(index)
                    found = True
            if found == False:
                print(f'Cannot Find ID: {userID}')
        if user =='3':
            if len(SS.getSpheres()) == 0:
                print()
            else:
                print(SS.getSpheres())
        if user =='4':
            if len(SS.getCones()) == 0:
                print()
            print(SS.getCones())
        if user =='5':
            userradius = input('Enter the radius: ')
            usercolor = input('Enter color: ')
            userSphere = Sphere(userradius, usercolor)
            SS.addSolid(userSphere)
        if user =='6':
            userradius = input('Enter the radius: ')
            userheight = input('Enter the height: ')
            usercolor = input('Enter color: ')
            userCone = Cone(userradius, userheight, usercolor)
            SS.addSolid(userCone)
        if user =='7':
            print(f'Total Volume of Solid Set is: {SS.getTotalVolume()}')
        if user =='8':
            print('Goodbye')
#cone1 = Cone(1,2)
#print('test')
#print(cone1.getID())
#sphere1 = Sphere(2)
#sphere2 = Sphere(3)
#print(sphere1.getID())
#print(cone1.getID())