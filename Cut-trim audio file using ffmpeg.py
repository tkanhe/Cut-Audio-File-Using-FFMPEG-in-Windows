import os
import subprocess
from datetime import datetime

input_file = 'a.opus'

s1 = '02:49.000'  # HOURS:MM:SS.MILLISECONDS
s2 = '03:20.300'

name, ext = os.path.splitext(input_file)
output_file = name + '_new' + ext

tdelta = datetime.strptime(s2, '%M:%S.%f') - datetime.strptime(s1, '%M:%S.%f')
delta = tdelta.seconds + tdelta.microseconds / 1000000

subprocess.call(f'ffmpeg -i {input_file} -ss {s1} -t {delta} -acodec copy {output_file}')
# subprocess.call(['ffmpeg', '-i', input_file, '-ss', s1, '-t', str(delta), '-acodec', 'copy', output_file])
# !ffmpeg -i $input_file -ss $s1 -t $delta -acodec copy $output_file
