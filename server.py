import socket  # for networking
import pickle  # for sending/receiving objects

# import the game
from tic_tac_toe import TicTacToe

HOST = '127.0.0.1'  # this address is the "local host"
PORT = 12783        # port to listen on for clients  

# set up the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

# accept a connection from the client
client_socket, client_address = s.accept()
print(f"\nConnected to {client_address}!")

# Get board size from the user
size = int(input("Enter the size of the board (e.g., 3 for 3x3, 6 for 6x6): "))
player_x = TicTacToe("S", size=size)

# Send the board size to the client
client_socket.send(pickle.dumps(size))

# Allow the player to suggest playing again
rematch = True

while rematch:
    # A header for an intense tic-tac-toe match!
    print(f"\n\n T I C - T A C - T O E ")

    # The rest is in a loop; if either player has won, it exits
    while not (player_x.did_win("S") or player_x.did_win("O") or player_x.is_draw()):
        # Draw grid, ask for coordinate
        print(f"\n       Your turn!")
        player_x.draw_grid()
        player_coord = input(f"Enter coordinate: ")
        player_x.edit_square(player_coord)

        # Draw the grid again
        player_x.draw_grid()

        # Pickle the symbol list and send it
        x_symbol_list = pickle.dumps(player_x.symbol_list)
        client_socket.send(x_symbol_list)

        # If the player won with the last move or it's a draw, exit the loop
        if player_x.did_win("S") or player_x.is_draw():
            break

        # Wait to receive the symbol list and update it
        print(f"\nWaiting for other player...")
        o_symbol_list = client_socket.recv(4096)
        o_symbol_list = pickle.loads(o_symbol_list)
        player_x.update_symbol_list(o_symbol_list)

    # End game messages
    if player_x.did_win("S"):
        print(f"Congrats, you won!")
    elif player_x.is_draw():
        print(f"It's a draw!")
    else:
        print(f"Sorry, the client won.")

    # Ask for a rematch
    host_response = input(f"\nRematch? (Y/N): ")
    host_response = host_response.capitalize()

    # Pickle response and send it to the client
    host_response = pickle.dumps(host_response)
    client_socket.send(host_response)

    # If the host doesn't want a rematch, we're done here
    if host_response == b"N":
        rematch = False
    else:
        # Receive client's response
        print(f"Waiting for client response...")
        client_response = client_socket.recv(4096)
        client_response = pickle.loads(client_response)

        if client_response == "N":
            print(f"\nThe client does not want a rematch.")
            rematch = False
        else:
            player_x.restart()
            size = int(input("Enter the size of the board (e.g., 3 for 3x3, 6 for 6x6): "))
            player_x.size = size
            player_x.symbol_list = [" " for _ in range(size * size)]
            client_socket.send(pickle.dumps(size))  # Send new board size to the client

spacer = input(f"\nThank you for playing!\nPress enter to quit...\n")

client_socket.close()
