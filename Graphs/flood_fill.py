
def flood_fill(pixel_row, pixel_column, new_color, image):
    # null checks
    # valid paramter checks
    old_color = image[pixel_row][pixel_column]
    # sneaky edge case
    if old_color == new_color:
        return image
    image[pixel_row][pixel_column] = new_color
    # up
    if pixel_row > 0 and image[pixel_row - 1][pixel_column] == old_color:
        flood_fill(pixel_row -1, pixel_column, new_color, image)
    # down
    if pixel_row < len(image) - 1 and image[pixel_row + 1][pixel_column] == old_color:
        flood_fill(pixel_row + 1, pixel_column, new_color, image)
    # left
    if pixel_column > 0 and image[pixel_row][pixel_column - 1] == old_color:
        flood_fill(pixel_row, pixel_column - 1, new_color, image)
    # right
    if pixel_column < len(image[pixel_row]) - 1 and image[pixel_row][pixel_column + 1] == old_color:
        flood_fill(pixel_row, pixel_column + 1, new_color, image)
    return image

pixel_row= 0
pixel_column= 4
new_color= 7
image= [
[7, 7, 7, 7, 7, 7]
]

print(flood_fill(pixel_row, pixel_column, new_color, image))