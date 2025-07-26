import Quartz
import numpy as np

class WindowCapture:
    def __init__(self):
        pass

    def get_screenshot(self):
        display_id = Quartz.CGMainDisplayID()
        image_ref = Quartz.CGDisplayCreateImage(display_id)

        width = Quartz.CGImageGetWidth(image_ref)
        height = Quartz.CGImageGetHeight(image_ref)
        bytes_per_row = Quartz.CGImageGetBytesPerRow(image_ref)

        data_provider = Quartz.CGImageGetDataProvider(image_ref)
        data = Quartz.CGDataProviderCopyData(data_provider)

        # Interpret raw buffer safely
        buffer = np.ndarray(
            shape=(height, bytes_per_row // 4, 4),
            dtype=np.uint8,
            buffer=data
        )

        # Crop visible screen (left side) and drop alpha channel
        rgb_image = buffer[:, :width, :3]

        return rgb_image
