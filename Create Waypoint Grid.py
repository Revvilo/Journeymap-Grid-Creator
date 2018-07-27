import json, glob, os
from collections import OrderedDict

files = []
for file in glob.glob("*.json"):
    files.append(file)

print()

for i, file in enumerate(files):
    print('[{}] {}'.format(i, file))

print('\nChoose a file #\n')
chosen_file_number = int(input('File # >> '))
offset_x = int(input('X Offset >> '))
offset_z = int(input('Z Offset >> '))
grid_w = int(input('Grid Height >> '))
grid_h = int(input('Grid Width >> '))

chosen_file = files[chosen_file_number]

with open(chosen_file, 'r') as f:
    data = json.load(f, object_pairs_hook=OrderedDict)

# data['x'] = data['x'] - offset_x
# data['z'] = data['z'] - offset_z

original_x = data['x']
original_z = data['z']

data['name'] = 'Grid Point'

for i in range(grid_h):

    for i in range(grid_w):
        if not (data['x'] == original_x and data['z'] == original_z):
            outfile_name = 'grid_{}_{}_{}.json'.format(data['x'], data['y'], data['z'])
            with open(outfile_name, 'w') as outfile:
                print('Writing File: {} -- Waypoint @ pos: {} {} {}'.format(outfile_name, data['x'], data['y'], data['z']))
                json.dump(data, outfile, indent=2)
        else:
            print('Skipping first iteration as to not overlap with the Grid\'s starting point.')

        data['id'] = 'grid_{},{},{}'.format(data['x'], data['y'], data['z'])
        data['x'] = data['x'] + offset_x

    data['z'] = data['z'] + offset_z # Increment Z Pos
    data['x'] = original_x # Reset to starting pos to begin on the next line up
