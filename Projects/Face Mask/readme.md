# Behind the Mask: Deep Learning for Face Mask Detection

This project employs `PyTorch` to construct and train a neural network for face mask detection, leveraging a dataset containing images labeled with 'WithMask' and 'WithoutMask' classes.
You can find the dataset [here](https://www.kaggle.com/datasets/ashishjangra27/face-mask-12k-images-dataset).
<p align="center">
	<img src="./images/crowd-of-people-wearingface-mask.png" alt="" width="500">
</p>

## Introduction

Amidst the challenges posed by COVID-19, enforcing mask-wearing in public spaces became crucial for public health. Recognizing the limitations of manual oversight, I developed a face mask detection model to automate the process. Leveraging supervised learning with `'WithMask'` and `'WithoutMask'` labels, I expedited the training process using the pretrained `'MobileNet'` model. This not only saved significant time and resources but also facilitated seamless integration with a custom sequential model tailored to our specific use case. The resulting model efficiently identifies individuals wearing or not wearing masks, offering a practical solution for authorities to ensure public safety.

## Model Architecture

The model architecture is based on the `MobileNetV2`, a pretrained neural network that serves as the foundation for face mask detection. This architecture is augmented to adapt to the specific task of identifying individuals wearing or not wearing masks.

### Model Freezing and New Layers

The pretrained `MobileNetV2` layers are frozen to retain learned features while additional layers are introduced for fine-tuning. The classifier part of the model is modified to better suit the face mask detection task. The added layers include fully connected and dropout layers, enhancing the model's ability to discern relevant features.

## Image Transformation

To prepare the input data for the model, images undergo a series of transformations using PyTorch's torchvision library. These transformations include resizing images to (224, 224) pixels, converting them to tensors, and normalizing pixel values to ensure consistency during training.

## Results

The trained model achieves impressive accuracy and generalization on the test set, as demonstrated by the evaluation notebook's visualizations and metrics.

## Feedback
Feel free to provide any feedback, suggestions, or improvements. Contributions are welcome!

## Libraries

To accomplish the project, I used:

- [<img src="images/PyTorch.png" alt="PyTorch" width="100" /> ](https://pytorch.org/)
- [<img src="images/Opencv.png" alt="Opencv" width="100"/> ](https://opencv.org/)
- [<img src="images/Matplotlib.png" alt="Matplotlib" width="100"/>](https://matplotlib.org/)
- [<img src="images/Numpy.png" alt="Numpy" width="100"/> ](https://numpy.org/)

## Tags
- Computer Vision
- PyTorch
- Neural Network
- Image Classification
- Deep Learning
- Image Processing
- Data Preprocessing
- Model Training
- Covid19
- Matplotlib
- Numpy
