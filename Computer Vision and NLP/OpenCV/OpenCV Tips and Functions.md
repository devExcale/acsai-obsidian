# OpenCV Tips and Functions

*TK*

## Tips

> [!tip] Alpha Channel
> 
> Generally, OpenCV removes the alpha channel when loading an image. To enable it back, (*TK*)

> [!warning] Colour Format
> 
> When using the `rgb` colour format, the pixels are represented as a tuple using the inverted format `(b,g,r)`. For example, the pixel `(0,0,255)` represents a full intensity red.


## Functions

*TK* imread imwrite

#### imshow

The `cv2.imshow` function opens a window containing an image.

The prototype of the function is `cv2.imshow(window, img)`, where:

- `window` is the title of the window;
- `img` is the [matrix](/Computer%20Vision%20and%20NLP/NumPy/NumPy%20Matrix.md) representing the image.

#### split

The `cv2.split` function splits the different channels into the grayscale components of each channel.

The prototype of the function is `cv2.split(img)`, where:

- `img` is the [matrix](/Computer%20Vision%20and%20NLP/NumPy/NumPy%20Matrix.md) representing the image.

> [!tip] Split vs NumPy slicing
> 
> The `merge` function has an advantage over NumPy slicing only if all the grayscale components of the channels of an image are needed. If just a subset of the channels are needed, generally NumPy slicing is faster.

#### merge

The `cv2.merge` function merges different image channels into a single image.

The prototype of the function is `cv2.merge(channels)`, where:

- `channels` is a tuple containing the channels to merge.

#### line

The `cv2.line` function draws a line over an image.

The prototype of the function is `cv2.line(img, start, end, color, thickness)`, where:

- `img` is the [matrix](/Computer%20Vision%20and%20NLP/NumPy/NumPy%20Matrix.md) containing the image;
- `start` is the point `(x,y)` where the line should start;
- `end` is the point `(x,y)` where the line should end;
- `color` is a tuple `(b,g,r)` containing the colour of the line;
- `thickness` is the thickness of the line.

#### rectangle

The `cv2.rectangle` function draws a rectangle over an image.

The prototype of the function is `cv2.rectangle(img, start, end, color, thickness)`, where:

- `img` is the [matrix](/Computer%20Vision%20and%20NLP/NumPy/NumPy%20Matrix.md) containing the image;
- `start` are the coordinates `(x,y)` of the top-left corner of the rectangle;
- `end` are the coordinates `(x,y)` of the bottom-right corner of the rectangle;
- `color` is a tuple `(b,g,r)` containing the colour of the rectangle;
- `thickness` is the thickness of the border.

> [!tip] Thickness
> 
> - If the thickness has a positive value, then the rectangle will be hollow and the border will have the specified thickness.
> - If the thickness equals to $-1$, then the rectangle will be filled.

#### circle

The `cv2.circle` function draws a circle over an image.

The prototype of the function is `cv2.rectangle(img, center, radius, color, thickness)`, where:

- `img` is the [matrix](/Computer%20Vision%20and%20NLP/NumPy/NumPy%20Matrix.md) containing the image;
- `center` are the coordinates `(x,y)` of the centre of the circle;
- `radius` is the radius of the circle;
- `color` is a tuple `(b,g,r)` containing the colour of the circle;
- `thickness` is the thickness of the border.

> [!tip] Thickness
> 
> - If the thickness has a positive value, then the circle will be hollow and the border will have the specified thickness.
> - If the thickness equals to $-1$, then the circle will be filled.
