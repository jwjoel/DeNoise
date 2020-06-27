# NoiseReduction

(a) Local averaging is a common method to denoise images (i.e. suppress noise) where a small square neighbourhood of odd size (e.g. 3x3, 5x5) around each pixel from the noisy image is taken and the average of this neighbourhood is computed. A new ‘denoised’ image is then formed where each pixel is the average from the local neighbourhood of the corresponding pixel  in  the  noisy  image.  Note  that  you  will  need  to  have  special  considerations  for  the ‘border pixels’ (i.e. pixels close  to  the  border/edge  of  the  image)  as  the  neighbourhood concept may not work precisely for these pixels. 

(b)Median   filtering   is   an   alternate   method   to   denoise   images   where   a   small   square neighbourhood of odd size (e.g. 3x3, 5x5) around each pixel from the noisy image is taken and the median value of this neighbourhood is computed. A new ‘denoised’ image is then formed where each pixel is the median from the local neighbourhood of the corresponding pixel  in  the  noisy  image.  Note  that  you  will  need  to  have  special  considerations  for  the ‘border pixels’ (i.e. pixels close to the border/edge of the image) as the neighbourhood concept may not work precisely for these pixels.

##This is a Python program, using matplotlib and numpy, to read both these noisy images (‘saltpepper.bmp’ and ‘gaussian.bmp’) and try to supress the noise using both the local averaging and median filtering methods.

![avatar](http://api.jovel.net/show.png)