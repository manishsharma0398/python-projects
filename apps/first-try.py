import subprocess
import time


def create_ssh_tunnel():
    try:
        subprocess.call(['ssh', '-N', 'ec2-user@ec2-18-130-235-150.eu-west-2.compute.amazonaws.com',
                        '-L', '5000:vw2yrfu9p0.execute-api.eu-west-2.amazonaws.com:443'])
        print('Tunnel established successfully.')

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        # Print the stderr to get more details about the error
        print(f"Error output: {e.stderr}")
        # Handle the error and attempt to reconnect
        reconnect()

    except Exception as e:
        print(f"Unexpected error: {e}")
        reconnect()


def reconnect():
    '''Reconnect'''
    print('Reconnecting...')
    time.sleep(10)  # Wait for 10 seconds before attempting to reconnect
    create_ssh_tunnel()


if __name__ == "__main__":
    while True:
        create_ssh_tunnel()
        time.sleep(60)  # Check every 60 seconds if the tunnel is still active
