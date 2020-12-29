from read_and_parse import read_and_parse
from assemble_image import assemble_image
from find_corners import find_corners

expected = 63187742854073

tiles, tids_by_border = read_and_parse()
img, positions        = assemble_image(tiles, tids_by_border)
answer                = find_corners(img, positions)

print(expected == answer)
