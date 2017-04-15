import sys

def draw_board(size = 3):
    top = " ---"
    side = "|"

    for i in range(size):
        # Print top part
        print(size * top)
        print()
        
        # Print mid part
        print(size * (side + "   ") + side)

        print()

    print(size * top)

if __name__ == "__main__":
    # Exception handling
    if len(sys.argv) != 2:
        print("Wrong # of arguments. Please start script with ./<name> <grid size(int)>")
        exit(1)

    try: 
        size = int(sys.argv[1])
    except:
        print("Exception caught. Please start script with ./<name> <grid size(int)>")
        exit(1)

    draw_board(size)