from read_and_parse import read_and_parse
from assemble_image import assemble_image
from remove_borders import remove_borders
from find_monsters_and_roughness import find_monsters_and_roughness

expected = 2152

tiles, tids_by_border = read_and_parse()
img, positions        = assemble_image(tiles, tids_by_border)
imglines              = remove_borders(img)
answer                = find_monsters_and_roughness(imglines)

print(expected == answer)
