import numpy as np

def crop_image(image, cr, cc, half_r = 50, half_c=50, fill_edge=True, fill_value=np.nan):
    r_left = min(half_r, cr)
    r_right = min(half_r, image.shape[0] - 1 - cr)
    c_left = min(half_c, cc)
    c_right = min(half_c, image.shape[1] - 1 - cc)


    image_slice = image[cr - r_left: cr + r_right + 1, cc - c_left: cc + c_right + 1].copy()

    if fill_edge:
        cutout = np.full( (2 * half_r + 1, 2 * half_c + 1), fill_value)
        cutout[half_r - r_left: half_r + r_right + 1, half_c - c_left: half_c + c_right + 1] = image_slice
        return cutout
    else:
        return image_slice
