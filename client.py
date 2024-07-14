import socket  # for networking
import pickle  # for sending/receiving objects

# import the game
from tic_tac_toe import TicTacToe

HOST = '127.0.0.1'  # the server's IP address
PORT = 12783        # the port we're connecting to 

# Connect to the host
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print(f"\nConnected to {s.getsockname()}!")

# Receive the board size from the server
size = pickle.loads(s.recv(4096))
print(f"Board size received from server: {size}")

# Set up the game with the same board size
player_o = TicTacToe("O", size=size)

# Allow the player to suggest playing again
rematch = True

while rematch:
    # A header for an intense tic-tac-toe match!
    print(f"\n\n T I C - T A C - T O E ")

    # Draw the grid
    player_o.draw_grid()

    # Host goes first, client receives first
    print(f"\nWaiting for other player...")
    x_symbol_list = s.recv(4096)
    x_symbol_list = pickle.loads(x_symbol_list)
    player_o.update_symbol_list(x_symbol_list)

    # The rest is in a loop; if either player has won, it exits
    while not (player_o.did_win("O") or player_o.did_win("S") or player_o.is_draw()):
        # Draw grid, ask for coordinate
        print(f"\n       Your turn!")
        player_o.draw_grid()
        player_coord = input(f"Enter coordinate: ")
        player_o.edit_square(player_coord)

        # Draw grid again
        player_o.draw_grid()

        # Pickle the symbol list and send it
        o_symbol_list = pickle.dumps(player_o.symbol_list)
        s.send(o_symbol_list)

        # If the player won with the last move or it's a draw, exit the loop
        if player_o.did_win("O") or player_o.is_draw():
            break

        # Wait for the server's move
        print(f"\nWaiting for host's move...")
        x_symbol_list = s.recv(4096)
        x_symbol_list = pickle.loads(x_symbol_list)
        player_o.update_symbol_list(x_symbol_list)

    # End game messages
    if player_o.did_win("O"):
        print(f"Congrats, you won!")
    elif player_o.is_draw():
        print(f"It's a draw!")
    else:
        print(f"Sorry, the host won.")

    # Ask for a rematch
    client_response = input(f"\nRematch? (Y/N): ")
    client_response = client_response.capitalize()

    # Pickle the response and send it to the server
    client_response = pickle.dumps(client_response)
    s.send(client_response)

    # Receive the host's response
    host_response = s.recv(4096)
    host_response = pickle.loads(host_response)

    if host_response == "N":
        print(f"\nThe host does not want a rematch.")
        rematch = False
    else:
        player_o.restart()
        size = pickle.loads(s.recv(4096))  # Receive new board size from the server
        print(f"New board size received from server: {size}")
        player_o.size = size
        player_o.symbol_list = [" " for _ in range(size * size)]

spacer = input(f"\nThank you for playing!\nPress enter to quit...\n")

s.close()
