# Noise Reduction in Images

Are you wondering how to reduce noise in pictures? You've come to the right place!

## Overview
NoiseReduction is a Python program that reduces noise in images using two methods: local averaging and median filtering. The program utilizes matplotlib and numpy to read noisy images (`saltpepper.bmp` and `gaussian.bmp`) and suppress the noise using the mentioned methods.

### Local Averaging
Local averaging is a common method to denoise images where a small square neighborhood of odd size (e.g. 3x3, 5x5) around each pixel from the noisy image is taken, and the average of this neighborhood is computed. A new 'denoised' image is then formed where each pixel is the average from the local neighborhood of the corresponding pixel in the noisy image. Special considerations are needed for border pixels as the neighborhood concept may not work precisely for these pixels.

### Median Filtering
Median filtering is an alternative method to denoise images where a small square neighborhood of odd size (e.g. 3x3, 5x5) around each pixel from the noisy image is taken, and the median value of this neighborhood is computed. A new 'denoised' image is then formed where each pixel is the median from the local neighborhood of the corresponding pixel in the noisy image. Special considerations are needed for border pixels as the neighborhood concept may not work precisely for these pixels.

## Getting Started

1. Clone the repository.
2. Install the required dependencies (matplotlib and numpy).
3. Run the program with your noisy images.

## Contributing

We appreciate any contributions to improve NoiseReduction. Please feel free to submit a pull request, report a bug, or suggest a new feature. Refer to the [contributing guidelines](link-to-contributing-guidelines) for more information on how to contribute to this project.

## License

This project is licensed under the [MIT License](link-to-license).
