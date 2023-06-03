import asyncio
import logging
import hassquitto as hq

logging.getLogger("hassquitto").setLevel(logging.DEBUG)

# Create a new device with the name "Example Device"
device = hq.Device(name="Example Device")

# To see the device, open the following URL in browser:
#   http://homeassistant.local:8123/config/devices/dashboard

counter = 0


# Function to run when the device connects to the MQTT broker
@device.on_interval(seconds=2)
async def tick():
    global counter
    print(f"Tick {counter}")

    # Update device status
    await device.status(f"Tick {counter}")
    counter += 1


async def main():
    try:
        # Run the device with MQTT username and password "example"
        # Default MQTT broker: homeassistant.local:1883
        await device.run(
            username="example",
            password="example",
        )
    except asyncio.CancelledError:
        pass
    finally:
        await device.destroy()
        await device.stop()


if __name__ == "__main__":
    asyncio.run(main())
