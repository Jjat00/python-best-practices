#from tests.load_image import test_load_image
#test_load_image()

from src.images_processing import ImagesProcessing


if __name__ == "__main__":
    images_processing = ImagesProcessing()
    images = images_processing.list_images('resources/json/label-images')
    #images_processing.images_processing(images)
    images_processing.image_preprocessing_2(images)
