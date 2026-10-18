## object-oriented implementation of yolo detection

import YoloDetection


if __name__ == '__main__':
    data_url = "sd"
    detector = YoloDetection.YoloDetection(data_url)
    print("test: ")
    detector.detect()
