"""
Every Message (including a message pack) begins with a 1 byte header (2 hex characters): 
the Message Type, and the Protocol Version (which is always 2).

After the header, there are 24 bytes (48 hex characters), representing the data contained
in the message.

Read the ASTM Remote ID standard for details about how the individual bytes represent
data within each message.

Message Type Summary:
0x0: Basic ID Message
0x1: Location/Vector Message
0x2: Authentication Message
0x3: Self-ID Message
0x4: System Message
0x5: Operator ID
0xF: Messag Packs
"""

hex_str = "47 5E 09 09 1E B8 06 61 93 D0 70 0A 53 16 FA FF 0D 01 F2 19 03 02 10 31 35 39 36 46 33 35 30 34 35 37 37 39 31 31 35 31 35 32 33 00 00 00 52 00 4E 55 4C 4C 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 42 04 00 00 00 00 00 00 00 00 01 00 19 00 00 00 00 10 00 00 00 00 00 00 00"

hex_str = hex_str.replace(" ", "")

MSG_TYPE_MAP = {
    0: "Basic ID",
    1: "Location/Vector",
    2: "Authentication",
    3: "Self-ID",
    4: "System",
    5: "Operator",
}

""" 
Note: the data in the secondary advertising frame before the ODID Msg ID "0D"
does not matter to us; it contains various bluetooth header data that does not
provide information about the broadcasting drone.
"""

app_code_idx = hex_str.find("0D")
msg_counter_idx = app_code_idx + 2
first_header_idx = app_code_idx + 4

# MESSAGE PACK
if hex_str[first_header_idx] == "F":
    num_msgs = int(hex_str[first_header_idx + 4 : first_header_idx + 6])

    # idx of the 1st byte of the first message in the message pack
    msg_1_start_idx = first_header_idx + 6

    # Create a list of all the messages in the message pack (each element in the list is 25 bytes or 50 hex chars)
    msg_strs = [hex_str[msg_1_start_idx + i*50 : msg_1_start_idx + i*50 + 50] for i in range(num_msgs)]
    msgs = []
    for msg_str in msg_strs:
        msg = {}  # Initialize dict to hold data about message
        msg["type"] = int(msg_str[0])
        msg["type_description"] = MSG_TYPE_MAP[msg["type"]]
        msg["raw hex"] = msg_str

        if msg["type"] == 0:  # BASIC ID MESSAGE
            pass

        if msg["type"] == 1:  # LOCATION/VECTOR MESSAGE
            pass

        if msg["type"] == 2:  # AUTHENTICATION MESSAGE
            pass

        if msg["type"] == 3:  # SELF-ID MESSAGE
            pass

        if msg["type"] == 4:  # SYSTEM MESSAGE
            pass

        if msg["type"] == 5:  # OPERATOR ID
            pass

        print(msg)

# INDIVIDUAL MESSAGES
else:
    print("Support for non-message-packs is not yet supported. Please try to parse a message pack.")
    print("Bluetooth 5 Long Range and Wi-Fi Beacon frame methods both require the use of message packs.")

