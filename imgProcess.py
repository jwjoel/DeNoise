import numpy as np
import matplotlib.pylab as plt

def denoise_image(img_path = "", filter_size = 3, method = ""):

    """ (str, int, str) -> list
    Perform noise reduction on the image.
    """

    #Global exception handling of the function.
    try:
        #Check whether the passed parameters are complete.
        if img_path == "" or method == "":
            raise Exception('Missing Parameter')
        temp_area, processed_img, half_filter = [], [], filter_size // 2
        #Import pictures and convert them into numpy arrays.
        img_data = plt.imread(img_path)
        #According to the length and width of the picture, create an empty array with the same shape to save the result.
        processed_img = np.zeros((len(img_data),len(img_data[0])))
        #According to the length and width of the picture, traverse each pixel.
        for height in range(len(img_data)):
            for width in range(len(img_data[0])):
                #According to the block size, scan the pixels around a specific pixel on height.
                for point_y in range(filter_size):
                    #Check if the pixel reached the border of the image
                    if height + point_y - half_filter < 0 or height + point_y + half_filter > len(img_data) - 1:
                        #If so, use white to replace it.
                        temp_area.append(255)
                    else:
                        #According to the block size, scan the pixels around a specific pixel on width.
                        for point_x in range(filter_size):
                            #Check if the pixel reached the border of the image
                            if width + point_x - half_filter < 0 or width + point_x + half_filter > len(img_data[0]) - 1:
                                #If so, use white to replace it.
                                temp_area.append(255)
                            else:
                                #Imported the pixels around each pixel into a new array.
                                temp_area.append(img_data[height + point_y - half_filter][width + point_x - half_filter])
                #Determine the method used for image noise reduction.
                if method == "median_filter":
                    #Sort the pixels to ensure that the middle value is taken. 
                    temp_area.sort()
                    #Then pass the intermediate value to a new array to save the result.
                    processed_img[height][width] = np.median(temp_area)
                elif method == "local_average":
                    #Find the average of the new array, and then pass it to a new array, used to save the results.
                    processed_img[height][width] = np.mean(temp_area)
                else:
                    raise Exception('Wrong Parameter')
                #Reset the variables that temporarily store pixels.
                temp_area = []
        #Return the processed image array.
        return processed_img
    #Through the exception.
    except Exception as e:
        print(e)

def plot_example(filter_size):
    #Plot the pictuire.
    plt.figure(figsize=(12, 6))
    plt.subplot(2,3,1)
    plt.title('Salt & pepper noise image', fontsize=10)
    plt.imshow(plt.imread("saltpepper.bmp"), cmap="gray")
    plt.subplot(2,3,2)
    plt.title('Salt & pepper noise image - local averaging', fontsize=10)
    plt.imshow(denoise_image("saltpepper.bmp", filter_size, "local_average"), cmap="gray")
    plt.subplot(2,3,3)
    plt.title('Salt & pepper noise image - median filtering', fontsize=10)
    plt.imshow(denoise_image("saltpepper.bmp", filter_size, "median_filter"), cmap="gray")
    plt.subplot(2,3,4)
    plt.title('Gaussian noise image', fontsize=10)
    plt.imshow(plt.imread("gaussian.bmp"), cmap="gray")
    plt.subplot(2,3,5)
    plt.title('Gaussian noise image - local averaging', fontsize=10)
    plt.imshow(denoise_image("gaussian.bmp", filter_size, "local_average"), cmap="gray")
    plt.subplot(2,3,6)
    plt.title('Gaussian noise image - median filtering', fontsize=10)
    plt.imshow(denoise_image("gaussian.bmp", filter_size, "median_filter"), cmap="gray")
    plt.show()

plot_example(3)