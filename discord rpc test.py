from pypresence import Presence
import time

def connect_rpc():
    client_id = 'PLACE YOUR APPLICATION ID HERE'  # Replace with your actual application's client ID
    RPC = Presence(client_id)
    RPC.connect()
    
    # Update your status here
    RPC.update(
        state="Testing rpc option from loader.py",           # Secondary status text
        details="Top level status",       # Primary status text
        large_image="large_image_key",    # Name of the image asset from the Discord Developer Portal
        large_text="Large image text",    # Text when hovering over the large image
        small_image="small_image_key",    # Name of the small image asset (optional)
        small_text="Small image text",    # Text when hovering over the small image (optional)
        start=time.time(),                # Start time (optional)
    )

    print("RPC connected. Now showing status on Discord.")

    return RPC

def disconnect_rpc(RPC):
    print("Closing RPC connection.")
    RPC.close()

def main():
    print("Coded by Cam")

    rpc_enabled = False
    rpc = None

    while True:
        command = input("Enter 'on' to enable RPC, 'off' to disable RPC, 'quit' to exit: ").strip().lower()

        if command == 'on' and not rpc_enabled:
            rpc = connect_rpc()
            rpc_enabled = True
        elif command == 'off' and rpc_enabled:
            disconnect_rpc(rpc)
            rpc_enabled = False
        elif command == 'quit':
            if rpc_enabled:
                disconnect_rpc(rpc)
            print("Exiting program.")
            break
        else:
            print("Invalid command or RPC is already in the requested state.")

if __name__ == "__main__":
    main()
