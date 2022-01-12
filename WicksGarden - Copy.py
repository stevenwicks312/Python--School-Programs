from pprint import pprint
import pickle

gardenPlants = {'Sunflower': 'S', 'Tulip': 'T', 'Rose': 'R', 'Weeds': 'W', '-':'-'}

def grid_maker(h, w):

    newgrid = [["-" for i in range(w)] for i in range(h)]
    with open('list.pkl', 'wb') as f:
        pickle.dump(newgrid, f)
    return newgrid

def grid_planter(plant,plantx,planty):
    with open('list.pkl', 'rb') as f:
        newgrid = pickle.load(f)
        newgrid[plantx][planty] = gardenPlants[plant]
    with open('list.pkl', 'wb') as f:
        pickle.dump(newgrid, f)
    return newgrid

def grid_rain(plant,plantx,planty):
    with open('list.pkl', 'rb') as f:
        newgrid = pickle.load(f)
    if newgrid[plantx][planty] == gardenPlants[plant]:
        plantx +=1
    elif newgrid[plantx][planty] == gardenPlants[plant]:
        planty +=1

    newgrid[plantx][plantx] == gardenPlants[plant]
    with open('list.pkl', 'wb') as f:
        pickle.dump(newgrid, f)
    return newgrid

def grid_mover(plant,plantx,planty,movex,movey):
    with open('list.pkl', 'rb') as f:
        newgrid = pickle.load(f)
        newgrid[plantx][planty] = newgrid[movex][movey]
        newgrid[movex][movey] = gardenPlants[plant]
    with open('list.pkl', 'wb') as f:
        pickle.dump(newgrid, f)
    return newgrid

def print_grid(newgrid):
    for row in grid:
        for e in row:
            print(e),
            print

def print_newgrid():
    with open('list.pkl', 'rb') as f:
        newgrid = pickle.load(f)
        return newgrid

def main():
    menu = {}
    menu['0'] = "Create Garden"
    menu['1'] = "Plant"
    menu['2'] = "Reprint List"
    menu['3'] = "Remove Plant"
    menu['4'] = "Move Plant"
    menu['5'] = "Print Plant Locations"
    menu['6'] = "Save current garden"
    menu['7'] = "Load garden"
    menu['8'] = "Create raindrops"
    menu['9'] = "Create drought"
    menu['10'] = "View Empty Grids"
    while True:
        options = menu.keys()
        print(menu)
        for entry in options:
            print
            entry, menu[entry]

        selection = input("Please Select")
        if selection == '0':
            w = int(input('Enter Width: '))
            h = int(input('Enter Height: '))
            pprint(grid_maker(w, h))
        if selection == '1':
            print(gardenPlants)
            plant = input("Choose to plant")
            plantx = int(input("Choose where to plant: (ex. 02 or 1)"))
            planty = int(input("Choose where to plant: (ex. 02 or 1)"))
            pprint(grid_planter(plant,plantx,planty))
        elif selection == '2':
            pprint(print_newgrid())

        elif selection == '3':
            pprint(print_newgrid())
            plant = '-'
            plantx = int(input("X coordinate for plant to be removed"))
            planty = int(input("Y coordinate for plant to be removed"))
            pprint(grid_planter(plant,plantx,planty))

        elif selection == '4':
            pprint(print_newgrid())
            plant = '-'
            movex = int(input("Select x-coordinate of plant to move"))
            movey = int(input("Select y-coordinate of plant to move\n"))
            plantx = int(input("Select new x-coordinate"))
            planty = int(input("Select new y-coordinate"))
            pprint(grid_mover(plant,plantx,planty,movex,movey))

        elif selection == '5':
            with open('list.pkl', 'rb') as f:
                newgrid = pickle.load(f)
                print([(x,y,i) for x, row in enumerate(newgrid)
                       for y, i in enumerate(row) if i != '-'])


        elif selection == '6':
            gardenName = input("Enter garden name")
            with open('list.pkl', 'rb') as f:
                newgrid = pickle.load(f)
            with open('list.pkl', 'wb') as gardenName:
                pickle.dump(newgrid, gardenName)

        elif selection == '7':
            gardenName = input("Enter garden name")
            with open('list.pkl', 'rb') as gardenName:
                newgrid = pickle.load(gardenName)
                print("Garden Loaded")
                pprint(newgrid)

        elif selection == '8':
            print(gardenPlants)
            plant = input("choose plant")
            plantx = int(input("Select where to place rain (X-axis): "))
            planty = int(input("Select where to place rain (Y-axis): "))
            pprint(grid_rain(plant, plantx, planty))

        elif selection =='9':
            break

        elif selection =='10':
            break
        else:
            print
            "Unknown Option Selected!"


if __name__ == '__main__':
    main()



