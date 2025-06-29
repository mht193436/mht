import rasterio
import numpy as np
import matplotlib.pyplot as plt


def read_sentinel_bands(file_path):
    with rasterio.open(file_path) as src:
        bands = src.read([1, 2, 3])  # Assuming B2, B3, B4 are the first three bands
    return bands


def compress_to_8bit(band_data, original_range=(0, 10000), target_range=(0, 255)):
    min_val, max_val = original_range
    new_min, new_max = target_range

    # Clip data to the original range
    clipped_data = np.clip(band_data, min_val, max_val)

    # Scale data to the new range
    compressed_data = ((clipped_data - min_val) / (max_val - min_val)) * (new_max - new_min) + new_min

    # Convert to uint8
    return compressed_data.astype(np.uint8)


def create_rgb_image(red_band, green_band, blue_band):
    rgb_image = np.stack((red_band, green_band, blue_band), axis=-1)
    return rgb_image


# Example usage
if __name__ == "__main__":
    # Path to your Sentinel-2 multi-band TIF file
    sentinel_file_path = r'D:\shixun\pythonProject\day2\2020_0427_fire_B2348_B12_10m_roi.tif'

    # Read each band
    bands = read_sentinel_bands(sentinel_file_path)
    red_band = bands[2]  # B4 is the third band
    green_band = bands[1]  # B3 is the second band
    blue_band = bands[0]  # B2 is the first band

    # Compress each band to 8-bit
    red_band_compressed = compress_to_8bit(red_band)
    green_band_compressed = compress_to_8bit(green_band)
    blue_band_compressed = compress_to_8bit(blue_band)

    # Create RGB image
    rgb_image = create_rgb_image(red_band_compressed, green_band_compressed, blue_band_compressed)

    # Display the RGB image
    plt.imshow(rgb_image)
    plt.title('Sentinel-2 RGB Image')
    plt.axis('off')  # Turn off axis labels
    plt.show()



