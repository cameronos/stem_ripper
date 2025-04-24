import subprocess
import os
import time
from termcolor import colored

print(colored('CAMERONOS STEM SPLITTER', 'red'))
print(colored('Insert name of file including extension: ', 'green'))
file = input("")

start_time = time.time()  # Start the timer

try:
    # Force CUDA usage
    env = os.environ.copy()
    env['DEMUCS_USE_GPU'] = '1'

    subprocess.run(
        ['python', '-m', 'demucs', '-n', 'mdx_extra', file],
        check=True,
        env=env
    )
except subprocess.CalledProcessError as e:
    print(colored('An error occurred during audio source separation:', 'red'))
    print(colored(str(e), 'red'))
    exit(1)

end_time = time.time()  # End the timer
elapsed_time = end_time - start_time

print(colored('Finished', 'green'))
print(colored(f'Time taken: {elapsed_time:.2f} seconds', 'cyan'))