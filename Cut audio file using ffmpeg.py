import os
import subprocess
from datetime import datetime

input_file = r'C:\Users\Administrator\Downloads\Breathe Carolina - Nights.wav'

start = '01:00.000'  # HOURS:MM:SS.MILLISECONDS or MM:SS.MILLISECONDS
end = '02:00.000'

name, ext = os.path.splitext(input_file)
output_file = name + '_new' + ext

delta = datetime.strptime(end, '%M:%S.%f') - datetime.strptime(start, '%M:%S.%f')
delta_sec = delta.seconds + delta.microseconds / 1000000

subprocess.call(['ffmpeg', '-i', input_file, '-ss', start, '-t', str(delta_sec), '-acodec', 'copy', output_file])

# Following didn't work if there is/are space/s in path
# subprocess.call(f'ffmpeg -i {input_file} -ss {start} -t {delta_sec} -acodec copy {output_file}')

# command line
# !ffmpeg -i $input_file -ss $start -t $delta_sec -acodec copy $output_file
