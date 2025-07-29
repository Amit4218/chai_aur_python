#  You are building a smart thermo stat system
#   If the device status id "active":
#           -- And temperature > 35 ->. warn . "high temperature alert!"
#           -- Else : "Temperature Normal"
#  if device is off -> "Device is offline"

device_status = "active"
temperature = 40

if device_status == "active":
    if temperature > 35:
        print("high temperature alert!")

    else:
        print("Temperature Normal")

elif device_status != "active":
    print("Device is offline!")
