data = "14inch l@ptop,699|16inch l@ptop,999|sm@rtphone,1099|t@blet,499|g@ming pc,1999"

device_list = data.split("|")
formatted_list = []

# Process each device entry
for device in device_list:
    device_info_list = device.split(",")
    name = device_info_list[0]  # Extract the device name
    price = int(device_info_list[1])  # Extract and convert the device price to an integer
    new_price = int(price + (price * 0.10))  # Calculate the new price with a 10% increase
    
    # Create a formatted device string and correct the device name
    formatted_device = f"Device Name: {name}, Device Price: ${price}"
    corrected_formatted_device = formatted_device.replace("@", "a")
    
    formatted_list.append(corrected_formatted_device)  # Add the formatted device to the list

print(formatted_list)  # Print the list of formatted device information
