# GUI-Based Client-Server Application with RPC

## Overview

This project is a graphical user interface (GUI) based Client-Server Application built to facilitate message broadcasting over a Local Area Network (LAN). The application utilizes Remote Procedure Call (RPC) protocol to manage communication between the client and server components.

## Features

- **Client Interface:**
  - User-friendly graphical interface for easy interaction.
  - Connect to the server on the LAN.
  - Recieve the broadcast messages from the server.

- **Server Functionality:**
  - Listens for incoming client connections.
  - Broadcasts messages to all connected clients.

- **RPC Protocol:**
  - Implements Remote Procedure Call for efficient communication.
  - Ensures secure and reliable message transmission.

## Prerequisites

- Python 3.x installed on both client and server machines.
- Tkinter library for GUI components (typically included in Python standard library).
- Additional libraries for RPC, if not included by default.

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repository
    ```

3. Run the server script on the server machine:

    ```bash
    python server.py
    ```

4. Run the client script on each client machine:

    ```bash
    python client.py
    ```

5. Use the GUI to connect to the server and start broadcasting messages.


## Contributing

If you would like to contribute to this project, please follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [GPL (General Public Licence)](LICENSE).


Feel free to reach out with any questions or issues!

