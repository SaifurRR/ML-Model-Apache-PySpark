{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "gpuType": "T4"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Introduction to Machine Learning: Neural Networks\n",
        "\n",
        "In this notebook, we will explain the structure of neural networks and build an example to show how they can be used to develop machine learning models. They has been around since the 1950s and have gone through several iterations. The current state-of-the-art neural network structure is often referred to as deep-learning.\n",
        "\n",
        "Neural networks are maching learning model inspired by how our brains work and are particularly good at recognizing patterns and classification. A neuron is a cell in the nervous system that receives and transmits information. Perceptrons are artificial versions of a single neuron in neural networks. For a mathematical model, we abstract the actual working of neurons into three numbers:\n",
        "\n",
        "- activation - a value representing the excitement of a neuron\n",
        "- default bias - a value representing a default or bias (sometimes called a threshold)\n",
        "- weight - a value representing a connection to another neuron\n",
        "\n",
        "In addition, there is a transfer function that takes all the incoming activations time their associated weights plus the bias and squashed the resulting sum within a range.\n",
        "\n",
        "The following basic NN performs a simple weighted summation of the inputs. The values $x_1$, $x_2$, and $x_3$ are the inputs to our NN and the constant value 1 is our bias.\n",
        "\n",
        "![image](https://miro.medium.com/v2/resize:fit:720/format:webp/1*UWJ52M5qNZp-38j11STT5g.png)\n",
        "\n",
        "Neurons are grouped together in layers to build a network. A typical Artifical Neural Network (ANN) is composed of three layers: input, hidden, and output. Each layer contains a set of neurons, or nodes. Typically, the nodes in a layer are fully connected to the nodes in the next layer.\n",
        "\n",
        "Information is propagated forward from the input layer through the hidden layer and finally through the output layer to produce a response.\n",
        "\n",
        "![image](https://www.tibco.com/sites/tibco/files/media_entity/2021-05/neutral-network-diagram.svg)\n"
      ],
      "metadata": {
        "id": "7zK4UdPUM907"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "In the simple perceptron shown above, the output node on the right takes the weighted sum and applies an activation function f and outputs a value. A single perceptron can perfrom basic linear classification problems such as computing the logical AND, OR, and NOT functions. A single perceptron can be trained to compute any function which is linearly separable, but cannot solve any function that is not linearly separable. To learn how to code a simple perceptron and train it with Python, checkout [this tutorial](https://carpentries-incubator.github.io/machine-learning-novice-sklearn/06-neural-networks/index.html).\n",
        "\n",
        "## Activation functions\n",
        "\n",
        "The most simple activation function is the `step function` used by the Perceptron algorithm.\n",
        "\n",
        "The step function is not differentiable, which can lead to problems when applying gradient descent and training the network. Instead, a more common activation function is the sigmoid function.\n",
        "\n",
        "![image](https://b2633864.smushcdn.com/2633864/wp-content/uploads/2021/04/activation_functions-768x585.png?lossy=1&strip=1&webp=1)\n",
        "\n",
        "While sigmoid is continuous and differentiable everywhere ad is symmetric around the y-axis, the outputs of the sigmoid are not zero-centered and saturated neurons kill the gradient.\n",
        "\n",
        "The hyperbolic tangent is zero-centered with higher gradients. Rectified Linear Unit (ReLU) or ramp functions is not saturable and is extremely computationally efficient. Empirically, the ReLU activation function tends to outperform both the sigmoid and tanh in nearly all applications. A variant of ReLU called Leaky ReLUs allow for a small non-zero gradient when the unit is not active to make ReLU differentiable everywhere.\n",
        "\n",
        "## Network architecture\n",
        "\n",
        "A single perceptron cannot be used to solve a non-linearly separable function. For that, we need to use multiple perceptrons and typically multiple layers of perceptrons. The most common architecture is the feedforward network, where a connection between nodes is only allowed from nodes in layer i to nodes in layer i+1. There are no backward or inter-layer connection allowed.  To learn more about building developing a simple neural network, read [this tutorial](https://towardsdatascience.com/building-a-simple-neural-network-from-scratch-a5c6b2eb0c34).\n",
        "\n",
        "Multi-layer perceptrons need to be trained by showing them a set of training data and measuring the error between the network’s predicted output and the true value. There are a number of training algorithms available for neural networks, but we are going to use one of the best established and well known, the backpropagation algorithm (backward propagation of errors) for feedforward neural networks.\n",
        "\n",
        "The goal of training a neural network is to adjust the weights of the connections between neurons so that the network can make accurate predictions on new, unseen data. Backpropagation networks fall under the category of supervised learning and is called backpropagation because it takes the error calculated between an output of the network and the true value and takes it back through the network to update the weights. The algorithm computes the gradients of the loss with respect to the network's weights, layer by layer, starting from the output layer and moving backward to the input layer.\n",
        "\n",
        "![image](https://miro.medium.com/v2/resize:fit:720/1*KNZZYteeBqkJViS1_LT1CQ.gif)\n",
        "\n",
        "Unlike feedforward neural networks, where data flows strictly in one direction (from input to output), Recurrent Neural Networks have connections that allow information to be passed backward, forming a loop within the network. RNNs are designed to handle sequential data as the network maintains a form of memory. As RNNs can process sequences of varying length, they are well-suited for time series analysis, natural language processing, and video and audio analysis. More advanced architectures such Long Short-term memory (LSTM) networks, have been developed to address RNN limitations in capturing long-term dependencies.\n",
        "\n"
      ],
      "metadata": {
        "id": "igl0QGuts5e4"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Deep Learning\n",
        "\n",
        "The term \"deep\" in deep learning refers to the multiple layers in these neural networks. Deep learning algorithms aim to automatically learn hierarchical representations of data by progressively extracting more abstract features from the raw input. They are often used with GPU (Graphical Processing Unit) which are good at executing multiple operations simultaneously.\n",
        "\n",
        "Scikit learn is not really setup for Deep Learning. Thus, we have to rely on other libraries. Common choices include:\n",
        "\n",
        "- [TensorFlow](https://www.tensorflow.org/): Developed by Google, TensorFlow is one of the most widely used libraries for building and training neural networks. It offers excellent support for deep learning, including convolutional neural networks and recurrent neural networks, and provides a high level of flexibility and control over the model architecture. TensorFlow is known for its high performance and scalability, making it a good choice for large-scale production applications.\n",
        "\n",
        "- [PyTorch](https://pytorch.org/): Developed by Facebook, PyTorch is another popular library for neural networks. It is known for its ease of use and flexibility, and is especially popular among researchers and academics. PyTorch offers dynamic computational graphs, which allow for more flexible and efficient model building, and provides excellent support for deep learning, including convolutional neural networks and recurrent neural networks.\n",
        "\n",
        "- [Keras](https://keras.io/): Keras is a high-level neural network library that runs on top of TensorFlow, Theano, or Microsoft Cognitive Toolkit. It is known for its ease of use and simplicity, making it a good choice for beginners or those who want to quickly prototype and experiment with different models. Keras offers a range of pre-built models and layers.\n",
        "\n",
        "### Convolutional Neural Networks\n",
        "\n",
        "Convolutional neural networks are simply a special case of feedforward neural networks designed for processing grid-like data, such as images. CNNs are particularly powerful in computer vision tasks because they can automatically learn hierarchical features and patterns from raw pixel data, making them well-suited for image recognition, object detection, image generation, and other visual tasks. CNNs use convolutional layers, which involve sliding small filters (also called kernels) over the input data for localized feature extraction.\n",
        "\n",
        "![image](https://miro.medium.com/v2/resize:fit:720/format:webp/1*7_BCJFzekmPXmJQVRdDgwg.png)\n",
        "\n",
        "The concept for this exercise has been adapted from a similar exercise presented at the [IVADO/MILA Deep Learning School](https://mila.quebec/en/the-6th-ivado-mila-deep-learning-school-a-chance-to-stay-at-the-forefront-of-technological-development/)."
      ],
      "metadata": {
        "id": "gEHG60AztIUi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import torch\n",
        "import matplotlib\n",
        "\n",
        "use_gpu = torch.cuda.is_available()\n",
        "device = torch.device(\"cuda:0\" if use_gpu else \"cpu\")\n",
        "\n",
        "print(\"Torch version: \", torch.__version__)\n",
        "print(\"GPU Available: {}\".format(use_gpu))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jcQxbavMXTok",
        "outputId": "3bb94449-37c0-4e5b-d798-4468b284dee3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Torch version:  2.0.1+cu118\n",
            "GPU Available: True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "*PyTorch* is a Python library that supports a vibrant ecosystem of tools and libraries for ML in vision, NLP, and more. It provides two high-level features:\n",
        "<ul>\n",
        "<li> operations on <a href=\"https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py\">tensors</a> (such as NumPy) with GPU support,</li>\n",
        "<li> operations for creating and optimizing computational graphs with an automatic differentiation system called <a href=\"https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html#sphx-glr-beginner-blitz-autograd-tutorial-py\">Autograd</a>.</li>\n",
        "</ul>\n",
        "\n",
        "<a href=\"https://pytorch.org/docs/stable/torch.html\">PyTorch docs</a> contain the API documentation and <a href=\"https://pytorch.org/tutorials/\">many tutorials</a>.\n",
        "Also, PyTorch offers several data processing utilities. One of these utilities is the class <a href=\"http://pytorch.org/docs/master/data.html#\"> `torch.utils.data.Dataset`</a> which offers an easy to use interface to handle a data set. For more information, please refer to the following urls:\n",
        "<ul>\n",
        "<li>PyTorch data sets: <a href=\"http://pytorch.org/docs/master/data.html\"> PyTorch - datasets</a>.</li>\n",
        "<li>A tutorial for loading data: <a href=\"http://pytorch.org/tutorials/beginner/data_loading_tutorial.html\"> PyTorch - data loading tutorial</a>.</li>\n",
        "</ul>\n",
        "\n",
        "<a href=\"http://pytorch.org/docs/master/cuda.html#module-torch.cuda\">`torch.cuda`</a> is a package that provides the same functions as CPU tensors but for  CUDA tensors, which are used for GPU computing. <a href=\"http://pytorch.org/docs/master/cuda.html#torch.cuda.is_available\">`torch.cuda.is_available()`</a> returns a boolean indicating if CUDA is currently available. Finally, we recommend using a `device` variable that identifies the device on which you want to perform computations. We can assign a tensor to a device with the method `.to(device)`. By default, the tensors are CPU tensors."
      ],
      "metadata": {
        "id": "0LLxB8ieaPP6"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## How to define a model in PyTorch\n",
        "\n",
        "The <a href=\"https://pytorch.org/docs/stable/nn.html\">PyTorch NN package</a> contains many useful classes for creating computation graphs.\n",
        "<ul>\n",
        "<li> The class <a href=\"http://pytorch.org/docs/master/nn.html#module\">torch.nn.Module</a>:\n",
        "any new module must inherit from this class or its descendants (subclasses).\n",
        "</li>   \n",
        "<li> The `forward` method:  any class defining a module must implement the `forward(...)` method, which defines the transformation of inputs to outputs.</li>  \n",
        "<li> The class <a href=\"http://pytorch.org/docs/master/nn.html#torch.nn.Linear\">`torch.nn.Linear(in_features, out_features)`</a>: this class implements a linear transformation. By default, it takes two parameters:\n",
        "    <ul>\n",
        "    <li>`in_features`: the size of the data at the input of the module. </li>\n",
        "    <li>`out_features`: the size of the data at the output of the module. </li>\n",
        "    </ul>\n",
        "</li>\n",
        "<li> The module <a href=\"http://pytorch.org/docs/master/nn.html#torch-nn-functional\">`torch.nn.functional`</a>:\n",
        "it defines a set of functions that can be applied directly to any tensor. As examples, we have:\n",
        "    <ul>\n",
        "    <li> non-linear functions: sigmoid(...), tanh(...), relu(...), etc...</li>\n",
        "    <li> cost functions: mse_loss(...), nll(...., cross_entropy(...), etc ... </li>\n",
        "    <li> regularization functions: droupout(...), etc ... </li>\n",
        "    <li> ...</li>\n",
        "    </ul>\n",
        "</li>\n",
        "</ul>"
      ],
      "metadata": {
        "id": "73h8iGe_aXY4"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "# The MNIST dataset\n",
        "MNIST is the classic go-to **classification dataset** used in **computer vision**. It is available here: <a href=\"http://yann.lecun.com/exdb/mnist/\">Yann LeCun's website</a>.\n",
        "\n",
        "Each datum is an **image of a handwritten digit**. Here are a few examples from this dataset:\n",
        "\n",
        "![Alt Text](https://github.com/mila-iqia/ecole_dl_mila_ivado/blob/master/tutoriaux/CNN/images/mnist.png?raw=true)\n",
        "\n",
        "Each image also comes with a **class label** which indicates which digit does the image correspond to. For example, the labels of the examples above are 5, 0, 4, and 1 respectively. The classes are balanced which means that all digits appear (roughly) the same number of times in the dataset.\n",
        "\n",
        "The dataset is composed of **60 000 training examples** and **10 000 test examples**. All images have exactly the same size (**28x28 pixels** or 28 rows by 28 columns). Each pixel is represented by a number between 0 and 255 which represents its grey level (0 is white and 255 is black). Depending on the model, each image may have to be flattened (to a 784-length vector)."
      ],
      "metadata": {
        "id": "dZUZMEh0X5jt"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Objective\n",
        "\n",
        "Our goal is to find a model that correctly classifies these images. In particular, our model will take as input (features/covariates/independant-variables) an image and will predict its digit (label/dependant variable). This problem can be formalized as follows:\n",
        "\n",
        "`f(image) = predicted digit`\n",
        "\n",
        "where `f` is a function.\n",
        "\n",
        "In this tutorial, we will consider both **multi-layer perceptrons (MLPs)** and **convolutional neural networks** as functions for solving this prediction problem. Both models take as inputs pixel intensities which will be modified using mathematical operations through the layers of the networks. Their output is a vector of size *1x10* where each entry corresponds to the (normalized) score that the input image is a particular digit. The sum over these 10 values is 1, and each score is non-negative. This is why these scores can be interpreted as probabilities. Our final prediction will be the entry with the highest score. For example, this prediction\n",
        "\n",
        "`[0.8, 0.1, 0, 0, 0, 0.05, 0.05, 0.0, 0.0, 0.0, 0.0]`\n",
        "\n",
        "indicates that the model assigns a score of 0.8 to class 0.\n",
        "\n",
        "Learning implies finding the parameters of a model that will maximize the model's performance. To learn, we will start by randomly initializing the parameters of our model. Then we iterate through examples. For each example we will obtain the network's prediction, compare it with the true label, and then update the parameters of the models to obtain a better prediction. We do this until we reach some predetermined stopping criteria."
      ],
      "metadata": {
        "id": "WmyrfSPSYAq-"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Download the dataset and create the data loader\n",
        "\n",
        "Before we begin training, we have to obtain the MNIST dataset. It turns out that there are built-in functions within PyTorch to do so.\n",
        "\n",
        "### Tool box\n",
        "**Note:** PyTorch comes with function to load, shuffle, and augment data.\n",
        "\n",
        "Here is an easy way to load the data in PyTorch:\n",
        "<ol>\n",
        "<li>Subclass <a href=\"http://pytorch.org/docs/master/data.html#torch.utils.data.Dataset\">`torch.utils.data.Dataset`</a> and add  `__getitem__` and `__len__` methods.</li>\n",
        "<li>Then you can use<a href=\"http://pytorch.org/docs/master/data.html#torch.utils.data.DataLoader\">`torch.utils.data.DataLoader`</a> to read and load the data into memory.</li>\n",
        "</ol>\n",
        "\n",
        "It is even easier for MNIST in PyTorch since there is already a subclass of \"datasets\" defined for it: <a href=\"http://pytorch.org/docs/master/torchvision/datasets.html#mnist\">`torchvision.datasets.MNIST`</a>.\n",
        "\n",
        "<a href=\"http://pytorch.org/docs/master/torchvision/datasets.html\">Other datasets are also similarly available</a>\n",
        "\n",
        "**Note:** <a href=\"http://pytorch.org/docs/master/tensors.html#torch.Tensor.view\">`torch.Tensor.view()`</a> returns a new tensor with the same data as the original tensor but a different shape. For example, it can be used to flatten an image."
      ],
      "metadata": {
        "id": "mf9q6ZvsYBcP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import random\n",
        "import torch\n",
        "from torch.utils.data import sampler, DataLoader\n",
        "from torchvision.datasets import MNIST\n",
        "import torchvision.transforms as transforms\n",
        "\n",
        "\n",
        "manualSeed = 1234\n",
        "use_gpu = torch.cuda.is_available()\n",
        "\n",
        "# Fixing random seed\n",
        "random.seed(manualSeed)\n",
        "np.random.seed(manualSeed)\n",
        "torch.manual_seed(manualSeed)\n",
        "if use_gpu:\n",
        "   torch.cuda.manual_seed_all(manualSeed)\n",
        "\n",
        "class ChunkSampler(sampler.Sampler):\n",
        "    \"\"\"Samples elements sequentially from some offset.\n",
        "    From: https://github.com/pytorch/vision/issues/168\n",
        "\n",
        "    Parameters\n",
        "    ----------\n",
        "    num_samples: int\n",
        "      # of desired datapoints\n",
        "    start: int\n",
        "      Offset where we should start selecting from\n",
        "    \"\"\"\n",
        "    def __init__(self, num_samples, start=0):\n",
        "        self.num_samples = num_samples\n",
        "        self.start = start\n",
        "\n",
        "    def __iter__(self):\n",
        "        return iter(range(self.start, self.start + self.num_samples))\n",
        "\n",
        "    def __len__(self):\n",
        "        return self.num_samples\n",
        "\n",
        "\n",
        "train_dataset = MNIST(root='../data',\n",
        "                      train=True,\n",
        "                      transform=transforms.ToTensor(),\n",
        "                      download=True)\n",
        "\n",
        "test_dataset = MNIST(root='../data',\n",
        "                     train=False,\n",
        "                     transform=transforms.ToTensor())\n",
        "\n",
        "train_dataset_sizes = len(train_dataset)\n",
        "num_train_samples = int(0.8 * train_dataset_sizes)\n",
        "num_valid_samples = train_dataset_sizes - num_train_samples\n",
        "num_test_samples = len(test_dataset)\n",
        "\n",
        "print('# of train examples: {}'.format(num_train_samples))\n",
        "print('# of valid examples: {}'.format(num_valid_samples))\n",
        "print('# of test examples: {}'.format(num_test_samples))\n",
        "\n",
        "batch_size = 100\n",
        "\n",
        "train_loader = DataLoader(dataset=train_dataset,\n",
        "                          sampler=ChunkSampler(num_train_samples, 0),\n",
        "                          batch_size=batch_size,\n",
        "                          shuffle=False)\n",
        "\n",
        "valid_loader = DataLoader(dataset=train_dataset,\n",
        "                          sampler=ChunkSampler(\n",
        "                              num_valid_samples, num_train_samples),\n",
        "                          batch_size=batch_size,\n",
        "                          shuffle=False)\n",
        "\n",
        "test_loader = DataLoader(dataset=test_dataset,\n",
        "                         batch_size=batch_size,\n",
        "                         shuffle=False)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "V6NG-Nh0Xlo0",
        "outputId": "526de0db-e741-4051-ead4-a0c64e031c58"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz\n",
            "Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to ../data/MNIST/raw/train-images-idx3-ubyte.gz\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "100%|██████████| 9912422/9912422 [00:00<00:00, 179974421.97it/s]"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Extracting ../data/MNIST/raw/train-images-idx3-ubyte.gz to ../data/MNIST/raw\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz\n",
            "Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz to ../data/MNIST/raw/train-labels-idx1-ubyte.gz\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "100%|██████████| 28881/28881 [00:00<00:00, 24496601.38it/s]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Extracting ../data/MNIST/raw/train-labels-idx1-ubyte.gz to ../data/MNIST/raw\n",
            "\n",
            "Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz\n",
            "Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz to ../data/MNIST/raw/t10k-images-idx3-ubyte.gz\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "100%|██████████| 1648877/1648877 [00:00<00:00, 65629366.63it/s]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Extracting ../data/MNIST/raw/t10k-images-idx3-ubyte.gz to ../data/MNIST/raw\n",
            "\n",
            "Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz\n",
            "Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz to ../data/MNIST/raw/t10k-labels-idx1-ubyte.gz\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "100%|██████████| 4542/4542 [00:00<00:00, 16479696.17it/s]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Extracting ../data/MNIST/raw/t10k-labels-idx1-ubyte.gz to ../data/MNIST/raw\n",
            "\n",
            "# of train examples: 48000\n",
            "# of valid examples: 12000\n",
            "# of test examples: 10000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%matplotlib inline\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "inputs, classes = next(iter(train_loader))\n",
        "\n",
        "print('Inputs size: {}'.format(inputs.size()))\n",
        "print('Classes size: {}'.format(classes.size()))\n",
        "\n",
        "# Random image of the batch\n",
        "img1 = 255 - inputs[np.random.randint(len(inputs))] * 255\n",
        "\n",
        "# Plot the image\n",
        "print('\\n\\nDisplay the first image:')\n",
        "img1 = img1.numpy()[0, :, :]\n",
        "plt.imshow(img1, cmap='gray', vmin=0, vmax=255)\n",
        "plt.grid(False)\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 515
        },
        "id": "p60k4aGCYO72",
        "outputId": "bd6b7429-a43d-415f-baaa-df69c2f3a00c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Inputs size: torch.Size([100, 1, 28, 28])\n",
            "Classes size: torch.Size([100])\n",
            "\n",
            "\n",
            "Display the first image:\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# CPU or GPU\n",
        "**Note:** <a href=\"http://pytorch.org/docs/master/cuda.html#module-torch.cuda\">`torch.cuda`</a> is a library which can perform tensor operations using GPUs. Specifically, the library includes CUDA tensors which offer the same operations as regular tensors but instead run on GPUs, instead of CPUs.\n",
        "<a href=\"http://pytorch.org/docs/master/cuda.html#torch.cuda.is_available\">`torch.cuda.is_available()`</a> returns whether or not CUDA is available. Adding `.to(\"cuda:0\")` to the variable identifying a CPU tensor, returns the equivalent GPU tensor.\n",
        "\n",
        "For more information about using GPUs on colab, please refer to this [tutorial](https://colab.research.google.com/drive/1y3ZE4m-D7lPoMzsypSEXessYmjWfKGqD#scrollTo=3IEVK-KFxi5Z).\n"
      ],
      "metadata": {
        "id": "Rg4Ijnl_YSwz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "use_gpu = torch.cuda.is_available()\n",
        "\n",
        "print(\"GPU Available: {}\".format(use_gpu))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FXp3BnXCYUo0",
        "outputId": "7056bc9f-15f0-42d0-f7f1-ca9ff55e5d54"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "GPU Available: True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "We are going to compare the performance of a CNN to the performance of a vanilla MLP. Below is a quick reminder of MLPs, the architecture of the MLP we will be using, as well as the code to train the MLP.\n",
        "\n",
        "# Multi-layer perceptron (MLP)\n",
        "A multi-layer perceptron is a vanilla few-forward neural network. Our instanciation will take as input an image, will transform it through a series of hidden layers and then will pass it to an output layer. This output is a vector of 10 numbers where each represents the normalized score of a particular class (this is sometimes interpreted as a probability).\n",
        "\n",
        "For example, here an MLP architecture to classify MNIST images:\n",
        "![Alt Text](https://github.com/mila-iqia/ecole_dl_mila_ivado/blob/master/tutoriaux/CNN/images/mlp.png?raw=true)\n",
        "\n",
        "Whenever you are trying to solve a prediction task, the process usually goes as follows:\n",
        "<ol>\n",
        "<li>Determine the network's artchitecture. This will implicitely determine the number of parameters (weights and biases) of the network.</li>\n",
        "<li>Determine the cost function and the optimization method.</li>\n",
        "<li>Train the weights of the network (i.e., fit the model to train data).</li>\n",
        "<li>Test the network (i.e., evaluate its performance on test data).</li>\n",
        "</ol>\n",
        "\n",
        "This procedure is general and applies to all types of (deep) neural networks.\n",
        "\n",
        "### Toolbox\n",
        "\n",
        "A (deep) neural network can be coded by using the library <a href=\"http://pytorch.org/docs/master/nn.html\">`torch.nn`</a>. `nn` uses <a href=\"http://pytorch.org/docs/master/autograd.html\">`torch.autograd`</a> to instantiate and computer the gradients (of the loss function with respect to the parameters)."
      ],
      "metadata": {
        "id": "BVSgnVxWYY1M"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import torch.nn as nn\n",
        "import copy\n",
        "\n",
        "input_size = 784\n",
        "hidden_size = 500\n",
        "num_classes = 10\n",
        "\n",
        "class MLP(nn.Module):\n",
        "    def __init__(self, input_size, hidden_size, num_classes):\n",
        "        super(MLP, self).__init__()\n",
        "\n",
        "        self.hidden_layer = nn.Sequential(\n",
        "            nn.Linear(input_size, hidden_size),\n",
        "            nn.ReLU(),\n",
        "            nn.Linear(hidden_size, hidden_size),\n",
        "            nn.ReLU())\n",
        "\n",
        "        self.output_layer = nn.Sequential(\n",
        "            nn.Linear(hidden_size, num_classes))\n",
        "\n",
        "    def forward(self, x):\n",
        "\n",
        "        out = self.hidden_layer(x)\n",
        "\n",
        "        out = self.output_layer(out)\n",
        "\n",
        "        return out\n",
        "\n",
        "model = MLP(input_size, hidden_size, num_classes)\n",
        "# switch model to GPU\n",
        "model = model.to(device)\n",
        "\n",
        "print(model)\n",
        "\n",
        "print(\"\\n\\n# Parameters: \", sum([param.nelement() for param in model.parameters()]))\n",
        "\n",
        "# Save the initial weights of model\n",
        "init_model_wts = copy.deepcopy(model.state_dict())\n",
        "\n",
        "learning_rate = 1e-2\n",
        "\n",
        "criterion = nn.CrossEntropyLoss()\n",
        "\n",
        "optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LFS5QhmaYZmU",
        "outputId": "0016b512-ea1e-45ce-f8b2-4c1f5a6087f3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "MLP(\n",
            "  (hidden_layer): Sequential(\n",
            "    (0): Linear(in_features=784, out_features=500, bias=True)\n",
            "    (1): ReLU()\n",
            "    (2): Linear(in_features=500, out_features=500, bias=True)\n",
            "    (3): ReLU()\n",
            "  )\n",
            "  (output_layer): Sequential(\n",
            "    (0): Linear(in_features=500, out_features=10, bias=True)\n",
            "  )\n",
            ")\n",
            "\n",
            "\n",
            "# Parameters:  648010\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import time\n",
        "from torch.autograd import Variable\n",
        "\n",
        "model.load_state_dict(init_model_wts)\n",
        "\n",
        "since = time.time()\n",
        "\n",
        "num_epochs = 10\n",
        "train_loss_history = []\n",
        "valid_loss_history = []\n",
        "\n",
        "print(\"# Start training #\")\n",
        "for epoch in range(num_epochs):\n",
        "\n",
        "    train_loss = 0\n",
        "    train_n_iter = 0\n",
        "\n",
        "    # Set model to train mode\n",
        "    model.train()\n",
        "\n",
        "    # Iterate over train data\n",
        "    for images, labels in train_loader:\n",
        "\n",
        "        # put images on proper device (GPU)\n",
        "        images = images.to(device)\n",
        "        labels = labels.to(device)\n",
        "\n",
        "        # Flatten the images\n",
        "        images = images.view(-1, 28*28)\n",
        "\n",
        "        # Zero the gradient buffer\n",
        "        optimizer.zero_grad()\n",
        "\n",
        "        # Forward\n",
        "        outputs = model(images)\n",
        "\n",
        "        loss = criterion(outputs, labels)\n",
        "\n",
        "        # Backward\n",
        "        loss.backward()\n",
        "\n",
        "        # Optimize\n",
        "        optimizer.step()\n",
        "\n",
        "        # Statistics\n",
        "        train_loss += loss.item()\n",
        "        train_n_iter += 1\n",
        "\n",
        "    valid_loss = 0\n",
        "    valid_n_iter = 0\n",
        "\n",
        "    # Set model to evaluate mode\n",
        "    model.eval()\n",
        "\n",
        "    # Iterate over valid data\n",
        "    for images, labels in valid_loader:\n",
        "\n",
        "        # put images on proper device (GPU)\n",
        "        images = images.to(device)\n",
        "        labels = labels.to(device)\n",
        "\n",
        "        # Flatten the images\n",
        "        images = images.view(-1, 28*28)\n",
        "\n",
        "\n",
        "        # Forward\n",
        "        outputs = model(images)\n",
        "\n",
        "        loss = criterion(outputs, labels)\n",
        "\n",
        "        # Statistics\n",
        "        valid_loss += loss.item()\n",
        "        valid_n_iter += 1\n",
        "\n",
        "    train_loss_history.append(train_loss / train_n_iter)\n",
        "    valid_loss_history.append(valid_loss / valid_n_iter)\n",
        "\n",
        "    print('\\nEpoch: {}/{}'.format(epoch + 1, num_epochs))\n",
        "    print('\\tTrain Loss: {:.4f}'.format(train_loss / train_n_iter))\n",
        "    print('\\tValid Loss: {:.4f}'.format(valid_loss / valid_n_iter))\n",
        "\n",
        "time_elapsed = time.time() - since\n",
        "\n",
        "print('\\n\\nTraining complete in {:.0f}m {:.0f}s'.format(\n",
        "    time_elapsed // 60, time_elapsed % 60))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zK2mNFbyYinC",
        "outputId": "d77b1a4c-b8c0-4ae0-e55f-6304b45a7dd9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "# Start training #\n",
            "\n",
            "Epoch: 1/10\n",
            "\tTrain Loss: 2.0848\n",
            "\tValid Loss: 1.5925\n",
            "\n",
            "Epoch: 2/10\n",
            "\tTrain Loss: 1.0058\n",
            "\tValid Loss: 0.6334\n",
            "\n",
            "Epoch: 3/10\n",
            "\tTrain Loss: 0.5535\n",
            "\tValid Loss: 0.4530\n",
            "\n",
            "Epoch: 4/10\n",
            "\tTrain Loss: 0.4410\n",
            "\tValid Loss: 0.3867\n",
            "\n",
            "Epoch: 5/10\n",
            "\tTrain Loss: 0.3902\n",
            "\tValid Loss: 0.3516\n",
            "\n",
            "Epoch: 6/10\n",
            "\tTrain Loss: 0.3600\n",
            "\tValid Loss: 0.3287\n",
            "\n",
            "Epoch: 7/10\n",
            "\tTrain Loss: 0.3387\n",
            "\tValid Loss: 0.3114\n",
            "\n",
            "Epoch: 8/10\n",
            "\tTrain Loss: 0.3218\n",
            "\tValid Loss: 0.2974\n",
            "\n",
            "Epoch: 9/10\n",
            "\tTrain Loss: 0.3075\n",
            "\tValid Loss: 0.2853\n",
            "\n",
            "Epoch: 10/10\n",
            "\tTrain Loss: 0.2949\n",
            "\tValid Loss: 0.2746\n",
            "\n",
            "\n",
            "Training complete in 1m 21s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Save history for later\n",
        "mlp_train_loss_history = train_loss_history\n",
        "mlp_valid_loss_history = valid_loss_history\n",
        "\n",
        "# Plot training and validation curve\n",
        "x = range(1, num_epochs + 1)\n",
        "plt.plot(x, mlp_train_loss_history, label='train')\n",
        "plt.plot(x, mlp_valid_loss_history, label='valid')\n",
        "\n",
        "plt.xlabel('# epochs')\n",
        "plt.ylabel('Loss')\n",
        "plt.legend()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 449
        },
        "id": "eprAMX0fYlng",
        "outputId": "5ab31c0e-4822-4625-c80d-f70c89b48a80"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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qoqIiAjdPV1E3E4BSES8as2aNaSkpBAREcGmTZscN0oUEXEnBSAR8arVq1czduxYAL766ivH89N5+eWX6d+/P6GhofTr14+///3vjtfqlqfefvttxowZQ2hoKIMGDWLlypVOfaxcuZJRo0YREhJCQkIC9913H9XV1Y7XbTYbTzzxBL179yYkJIRu3brx6KOPOvWxe/duLrjgAsLDw0lJSWHNmjWO1/bu3cuECROIiYkhIiKCgQMHsnTp0jP+NxIRN/DYbVdFRGrt3bvXsFgshsViMYKCgozQ0FDDYrEYwcHBRkhIiGGxWIzbbrvtpO9/4403jISEBOPdd981du/ebbz77rtGbGyssWDBAsMwDCM7O9sAjK5duxr//ve/ja1btxq33HKLERUVZRw+fNgwDMPYt2+fER4ebvzhD38wtm3bZrz//vtGp06djJkzZzo+59577zViYmKMBQsWGDt37jS+/PJL46WXXnL6jH79+hkffvihsX37duOKK64wunfvblRVVRmGYRiXXXaZcfHFFxvfffedsWvXLuO///2vsXLlSjf9q4rImVAAEhGPq6qqMrKzs41vv/3WCAoKMr799ltj586dRmRkpLFy5UojOzvbOHTo0Enf36tXL2PRokVO52bNmmWkpaUZhlEfTh5//HGnz+zatasxZ84cwzAM4/777zf69u1r2Gw2R5t58+YZkZGRRk1NjWG1Wo2QkBBH4Gms7jNefvllx7ktW7YYgLFt2zbDMAxj8ODBxkMPPXSG/zoi4gmBXp1+EhG/FBgYSI8ePVi8eDEjR45kyJAhrFq1iri4OM4777xTvre0tJRdu3Zx8803c+uttzrOV1dXY7FYnNqmpaU5feaIESPYtm0bANu2bSMtLQ2TyeRoM3bsWEpKSti3bx/5+flUVFRw0UUXnXI8Q4YMcTxPSEgA4ODBg/Tr148//vGP3HbbbXzyySekp6fzy1/+0qm9iHiPApCIeNzAgQPZu3cvVVVV2Gw2IiMjqa6uprq6msjISLp3786WLVuafG9JSQkAL730EqmpqU6vmc1ml40xLCysWe2CgoIcz+vClM1mA+CWW24hIyODjz76iE8++YTZs2fz9NNPc+edd7psnCLSMiqCFhGPW7p0KVlZWcTHx/PGG2+QlZXFoEGDmDt3LllZWacsFI6LiyMxMZHdu3fTu3dvpyM5Odmp7dq1ax3Pq6ur2bhxI/379wegf//+rFmzBsMwHG1WrVpFVFQUXbt2pU+fPoSFhZGZmdmq75qUlMTvf/973nvvPe6++25eeumlVvUnIq6hGSAR8bju3buTn59PQUEBEydOxGQysWXLFn75y186lpFO5eGHH+aPf/wjFouFSy+9lIqKCjZs2MCxY8eYOnWqo928efPo06cP/fv359lnn+XYsWP85je/AeAPf/gDc+fO5c477+SOO+5g+/btzJw5k6lTpxIQEEBoaCh//vOfuffeewkODmbs2LEcOnSILVu2cPPNNzfre06ZMoXx48dz9tlnc+zYMT7//HNHABMR71IAEhGvWLFiBSNHjiQ0NJQvv/ySrl27Niv8gH1pKTw8nCeffJJ77rmHiIgIBg8ezJQpU5zaPf744zz++ONkZWXRu3dvPvjgAzp16gTAWWedxdKlS7nnnntISUkhNjaWm2++mf/7v/9zvP/BBx8kMDCQGTNmcODAARISEvj973/f7O9YU1PD7bffzr59+4iOjubSSy/l2Wefbfb7RcR9TEbD+V8RkXZgz549JCcn88033zB06FBvD0dEfJBqgERERMTvKACJiIiI39ESmIiIiPgdzQCJiIiI31EAEhEREb+jACQiIiJ+RwFIRERE/I4CkIiIiPgdBSARERHxOwpAIiIi4ncUgERERMTv/D9Oe1hgtco9bQAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Set model to evaluate mode\n",
        "model.eval()\n",
        "\n",
        "correct = 0\n",
        "total = 0\n",
        "\n",
        "# Iterate over test data\n",
        "for images, labels in test_loader:\n",
        "\n",
        "    # put images on proper device (GPU)\n",
        "    images = images.to(device)\n",
        "    labels = labels.to(device)\n",
        "\n",
        "    # Flatten the images\n",
        "    images = images.view(-1, 28*28)\n",
        "\n",
        "\n",
        "    # Forward\n",
        "    outputs = model(images)\n",
        "    _, predicted = torch.max(outputs.data, 1)\n",
        "\n",
        "    # Statistics\n",
        "    total += labels.size(0)\n",
        "    correct += torch.sum(predicted == labels.data)\n",
        "\n",
        "print('Accuracy on the test set: {:.2f}%'.format(100 * correct / total))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PgthQz7pYvY-",
        "outputId": "e84ba361-690f-40fa-8b5b-3977563aeff9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy on the test set: 92.17%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Convolutional Neural Networks\n",
        "\n",
        "We first review the basic concepts that underlie CNNs.\n",
        "\n",
        "### Convolution\n",
        "\n",
        "A convolution \"slides\" a filter *K* along image *I* to obtain an output *I*\\**K*.\n",
        "\n",
        "Here is an example of a 2D convolution:\n",
        "\n",
        "![Alt Text](https://github.com/mila-iqia/ecole_dl_mila_ivado/blob/master/tutoriaux/CNN/images/numerical_no_padding_no_strides.gif?raw=true)\n",
        "\n",
        "\n",
        "### Filters\n",
        "\n",
        "Filters (or kernels) are used to extract information useful to the task from their input. Filters are generally of size *n* \\* *n* where *n* is usually odd. The filters are parametrized by weights, one for each of its entry, which are learned by the convolutional network.\n",
        "\n",
        "The filter used in the previous example is:\n",
        "\n",
        "![Alt Text](https://github.com/mila-iqia/ecole_dl_mila_ivado/blob/master/tutoriaux/CNN/images/d7acc4aeb74d9e9cb5fb51482a302196594837fe.png?raw=true)\n",
        "\n",
        "### Depth\n",
        "\n",
        "We typically use *M* of filters which can be understood as the depth of the layer (see below). Note that this is different from the depth of the network (which is the number of layers). M is a hyperparameter. Here, each filter's output (blue circles) is represented as a single depth dimension on the output.\n",
        "\n",
        "![Alt Text](https://github.com/mila-iqia/ecole_dl_mila_ivado/blob/master/tutoriaux/CNN/images/Conv_layer.png?raw=true)\n",
        "\n",
        "### Stride\n",
        "\n",
        "The stride corresponds to the number of pixels the filter moves over in between each step of the convolution. The stride is measured in terms of a number of pixels. We typically use strides of 1 or 2. The larger the stride, the smaller the dimension of the output.\n",
        "\n",
        "### Zero padding\n",
        "\n",
        "Zero padding consists in padding (adding) a border of zeros around the input image. This can be useful to preserve the dimension from input to output.\n",
        "\n",
        "Below is an example of a zero padding which preserves the dimensions from input to output. Here, zero padding is set to 1, stride is set to 1, and the filter has size 3x3.\n",
        "\n",
        "![Alt Text](https://github.com/mila-iqia/ecole_dl_mila_ivado/blob/master/tutoriaux/CNN/images/same_padding_no_strides.gif?raw=true)\n",
        "\n",
        "\n",
        "### Max Pooling\n",
        "\n",
        "In addition to convolutions, CNNs usually have pooling layers. The goal of pooling is to reduce the dimensionality of the input in-between two convolution layers to reduce the number of parameters in the network. For example, the famous LeNet CNN, uses max pooling with 2x2 filters and a stride of 2. Max pooling outputs the max value in a 2x2 region. This output is then the input of the next layer.\n",
        "\n",
        "Here is an example of the max pooling operation:\n",
        "\n",
        "![Alt Text](https://github.com/mila-iqia/ecole_dl_mila_ivado/blob/master/tutoriaux/CNN/images/maxpool.jpeg?raw=true)\n",
        "\n",
        "\n",
        "### Receptive Field\n",
        "\n",
        "The receptive field is a measure of the CNNs' capacity to perceive information at different input scales. In an MLP (fully connected), the features are connected to every neuron. The receptive field of this MLP is the full image.\n",
        "\n",
        "For CNNs, convolution operations typically imply sparse connections. In other words, each filter only has a local receptive field. However, each successive layer will have access to a slightly larger receptive field.\n",
        "\n",
        "Let's look at an example. Imagine a 3x3 filter with stride set to 1. In this case, the first layer's receptive field is a maximum of 3x3. However, the more layer we add the more we increase the network's receptive field. Adding a second layer with 3xe3 filters and a stride of 1, our receptive field is increased to 5x5. Adding a third 3x3 layer further increases our receptive field to 7x7.\n",
        "\n",
        "What is the advantage of using multiple smaller successive filters instead of a single larger one? A single large filter of 7x7 implies 49 parameters. Instead 3 layers of 3x3 filters requires only 27 parameters (9 \\* 3). It is therefore more efficient to use multiple successive filters and in both cases the receptive field is the same (7x7). In addition, by using multiple successive filters, we can introduce more non-linearities in the model (one after each filter).\n",
        "\n",
        "Here the 3x3 filter (in grey) with a stride of 1 has a receptive field of 5x5 (yellow region):\n",
        "\n",
        "![Alt Text](https://github.com/mila-iqia/ecole_dl_mila_ivado/blob/master/tutoriaux/CNN/images/sNBmKMKAz-yJeCuS14usSqw.png?raw=true)\n"
      ],
      "metadata": {
        "id": "WDyj5MYjY0Gs"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "## LeNet\n",
        "CNNs have been developed to model images. They can model images more efficiently (with fewer parameters) than an equivalent MLP. LeNet is a basic CNN for classification. It comes in several versions.\n",
        "\n",
        "We will use a \"LeNet 5\" to classify MNIST digit images:\n",
        "\n",
        "![Alt Text](https://github.com/mila-iqia/ecole_dl_mila_ivado/blob/master/tutoriaux/CNN/images/lenet5.png?raw=true)\n",
        "\n",
        "\n",
        "To solve a prediction task, the process usually goes as follows (it is the same for MLPs and CNNs):\n",
        "<ol>\n",
        "<li>Determine the network's architecture. This will implicitly determine the number of parameters (weights and biases) of the network.</li>\n",
        "<li>Determine the cost function and the optimization method.</li>\n",
        "<li>Train the weights of the network (i.e., fit the model to train data).</li>\n",
        "<li>Test the network (i.e., evaluate its performance on test data).</li>\n",
        "</ol>\n",
        "\n",
        "\n",
        "## Determining the network's architecture\n",
        "### Toolbox\n",
        "**Recall:** To instantiate a particular network in PyTorch, one first subclasses <a href=\"http://pytorch.org/docs/master/nn.html#torch.nn.Module\">`torch.nn.Module`</a> and then writes the following methods :\n",
        "<ul>\n",
        "<li>The `__init__` method defines the layers. </li>\n",
        "<li>The `forward(input)` method returns the `output`.</li>\n",
        "</ul>\n",
        "\n",
        "\n",
        "For LeNet 5's '`__init__`, the following classes can be used:\n",
        "<ul>\n",
        "<li><a href=\"http://pytorch.org/docs/master/nn.html#torch.nn.Conv2d\">`torch.nn.Conv2d(in_channels, out_channels, kernel_size)`</a> applies a 2D convolution on the input channels.</li>\n",
        "<li><a href=\"http://pytorch.org/docs/master/nn.html#torch.nn.MaxPool2d\">`torch.nn.MaxPool2d(kernel_size)`</a> applies 2D max pooling on the input channels.</li>\n",
        "<li><a href=\"http://pytorch.org/docs/master/nn.html#torch.nn.Linear\">`torch.nn.Linear(in_features, out_features)`</a> applies a linear transformation on its input: y = Ax + b.</li>\n",
        "<li><a href=\"http://pytorch.org/docs/master/nn.html#torch.nn.ReLU\">`torch.nn.Relu()`</a> applies an elementwise Relu activation: Relu(x) = max(0, x).</li>\n",
        "<li><a href=\"http://pytorch.org/docs/master/nn.html#torch.nn.Softmax\">`torch.nn.Softmax(dim)`</a> applies a softmax activation to an n-dimensional tensor (normalizes the exponentiated entries).</li>\n",
        "<li><a href=\"http://pytorch.org/docs/master/nn.html#torch.nn.Sequential\">`torch.nn.sequential`</a> a sequential container in which to add modules in the order in which they will be constructed.</li>\n",
        "</ul>\n",
        "\n",
        "`forward(input)` successively applies the input data to the different layers defined in  `__init__`.\n",
        "\n",
        "Finally, `model.to(\"cuda:0\")` passes the model to an available GPU.\n",
        "\n",
        "### Implementation"
      ],
      "metadata": {
        "id": "DRqPOlv7ZAJE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class LeNet5(nn.Module):\n",
        "    def __init__(self):\n",
        "        super(LeNet5, self).__init__()\n",
        "        self.block1 = nn.Sequential(\n",
        "            nn.Conv2d(1, 16, kernel_size=5, padding=2),\n",
        "            nn.ReLU(),\n",
        "            nn.MaxPool2d(2))\n",
        "\n",
        "        self.block2 = nn.Sequential(\n",
        "            nn.Conv2d(16, 32, kernel_size=5, padding=2),\n",
        "            nn.ReLU(),\n",
        "            nn.MaxPool2d(2))\n",
        "\n",
        "        self.fc = nn.Linear(7*7*32, 10)\n",
        "\n",
        "\n",
        "    def forward(self, x):\n",
        "        out = self.block1(x)\n",
        "\n",
        "        out = self.block2(out)\n",
        "\n",
        "        # Flatten the output of block2\n",
        "        out = out.view(out.size(0), -1)\n",
        "\n",
        "        out = self.fc(out)\n",
        "\n",
        "        return out\n",
        "\n",
        "model = LeNet5()\n",
        "model = model.to(device)\n",
        "\n",
        "print(model)\n",
        "print(\"\\n\\n# Parameters: \", sum([param.nelement() for param in model.parameters()]))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X2xIJ71PZCl7",
        "outputId": "e22de298-604b-40eb-adbe-5fd3e3f0c6c0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "LeNet5(\n",
            "  (block1): Sequential(\n",
            "    (0): Conv2d(1, 16, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))\n",
            "    (1): ReLU()\n",
            "    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)\n",
            "  )\n",
            "  (block2): Sequential(\n",
            "    (0): Conv2d(16, 32, kernel_size=(5, 5), stride=(1, 1), padding=(2, 2))\n",
            "    (1): ReLU()\n",
            "    (2): MaxPool2d(kernel_size=2, stride=2, padding=0, dilation=1, ceil_mode=False)\n",
            "  )\n",
            "  (fc): Linear(in_features=1568, out_features=10, bias=True)\n",
            ")\n",
            "\n",
            "\n",
            "# Parameters:  28938\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "We note that LeNet4 has 28 938 parameters versus 648 010 parameters for an somewhat equivalent MLP with two hidden layers. This reduction in the number of parameters is significant.\n",
        "\n",
        "Here is how we calculate the number of parameters for LeNet5:\n",
        "\n",
        "```\n",
        "1st layer: 16 filters of size 5x5 + 16 biases = 16*5*5 + 16 = 416\n",
        "2nd layer: 16 * 32 filters of size 5x5 + 32 biases = 16*32*5*5 + 32 = 12 832\n",
        "FC layer: 7*7*32*10 + 10 biases = 15 690\n",
        "\n",
        "Total = 416 + 12 832 + 15 690 = 28 938\n",
        "```\n",
        "\n",
        "As a comparison, here is how we calculate the number of parameters of the two hidden layer MLP:\n",
        "The input flattens the 28x28 images into a vector of size 784. The second layer has 500 neurons. Each neuron requires 784 weights + 1 bias. So 500\\*785 parameters. This is then fed to another layer of 500 neurons which adds 501\\*500 parameters. Finally, the output layer has 10 neurons, each with 500 weights and a single bias for a total of 10\\*501 parameters.\n",
        "\n",
        "So in total we have:\n",
        "```\n",
        "500*785 + 501*500 + 10*501 = 648010\n",
        "``` parameters."
      ],
      "metadata": {
        "id": "ZoHgcXEQZHcX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Save the initial weights of model\n",
        "init_model_wts = copy.deepcopy(model.state_dict())"
      ],
      "metadata": {
        "id": "crZvPMUaZRmt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Determine the cost function and the optimization method\n",
        "### Toolbox\n",
        "**Recall:** A common choice for a multi-class task are the following:\n",
        "<ul>\n",
        "<li>**Cost function :** <a href=\"http://pytorch.org/docs/master/nn.html#torch.nn.CrossEntropyLoss\">`torch.nn.CrossEntropyLoss()`</a>. The cross entropy is often used in this context. It compares a (multivariate) distribution $p$ with a reference distribution $t$. It is minimized for $p=t$ and it is expressed mathematically by: $-\\sum_j t_{ij} \\log(p_{ij})$ where $p$ is the prediction, $t$ the target, $i$ are examples and $j$ the target class.</li>\n",
        "<li>**Optimization method :** <a href=\"http://pytorch.org/docs/master/optim.html#torch.optim.SGD\">`torch.optim.SGD(net.parameters(), lr=learning_rate)`</a> a standard stochastic gradient descent (SGD) implementation</li>\n",
        "</ul>\n",
        "\n",
        "### Implementation\n"
      ],
      "metadata": {
        "id": "PZeA1R3gZYDu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "criterion = nn.CrossEntropyLoss()\n",
        "optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)"
      ],
      "metadata": {
        "id": "DOx2yJXzZZ23"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Train the weights of a network\n",
        "### Toolbox\n",
        "**Recall:** Training a network usually involves iterating for multiple epochs over the training dataset. One epoch corresponds to one pass over the full dataset.\n",
        "\n",
        "The dataset is usually divided into batches. Each epoch will then receive sequentially batches. For each batch we do the following operations:\n",
        "<ol>\n",
        "<li>`optimizer.zero_grad()`: we clear the previously stored gradients.</li>\n",
        "<li>`loss.backward()`: we evaluate the cost, the gradients, and backpropagate the gradients through the computation graph.</li>\n",
        "<li>`optimizer.step()`: we update the parameters using the previously calculated gradients. For SGD, the update is: `weight = weight - learning_rate * gradient`.</li>\n",
        "</ol>\n",
        "\n",
        "### Implementation\n",
        "\n"
      ],
      "metadata": {
        "id": "eBbYXQ3FZbvy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "model.load_state_dict(init_model_wts)\n",
        "\n",
        "since = time.time()\n",
        "\n",
        "num_epochs = 10\n",
        "train_loss_history = []\n",
        "valid_loss_history = []\n",
        "\n",
        "print(\"# Start training #\")\n",
        "for epoch in range(num_epochs):\n",
        "\n",
        "    train_loss = 0\n",
        "    train_n_iter = 0\n",
        "\n",
        "    # Set model to train mode\n",
        "    model.train()\n",
        "\n",
        "    # Iterate over train data\n",
        "    for images, labels in train_loader:\n",
        "\n",
        "        # put images on proper device (GPU)\n",
        "        images = images.to(device)\n",
        "        labels = labels.to(device)\n",
        "\n",
        "        # Zero the gradient buffer\n",
        "        optimizer.zero_grad()\n",
        "\n",
        "        # Forward pass\n",
        "        outputs = model(images)\n",
        "\n",
        "        loss = criterion(outputs, labels)\n",
        "\n",
        "        # Backward\n",
        "        loss.backward()\n",
        "\n",
        "        # Optimize\n",
        "        optimizer.step()\n",
        "\n",
        "        # Statistics\n",
        "        train_loss += loss.item()\n",
        "        train_n_iter += 1\n",
        "\n",
        "    valid_loss = 0\n",
        "    valid_n_iter = 0\n",
        "\n",
        "    # Set model to evaluate mode\n",
        "    model.eval()\n",
        "\n",
        "    # Iterate over valid data\n",
        "    for images, labels in valid_loader:\n",
        "\n",
        "        # put images on proper device (GPU)\n",
        "        images = images.to(device)\n",
        "        labels = labels.to(device)\n",
        "\n",
        "        # Forward\n",
        "        outputs = model(images)\n",
        "\n",
        "        loss = criterion(outputs, labels)\n",
        "\n",
        "        # Statistics\n",
        "        valid_loss += loss.item()\n",
        "        valid_n_iter += 1\n",
        "\n",
        "    train_loss_history.append(train_loss / train_n_iter)\n",
        "    valid_loss_history.append(valid_loss / valid_n_iter)\n",
        "\n",
        "    print('\\nEpoch: {}/{}'.format(epoch + 1, num_epochs))\n",
        "    print('\\tTrain Loss: {:.4f}'.format(train_loss / train_n_iter))\n",
        "    print('\\tValid Loss: {:.4f}'.format(valid_loss / valid_n_iter))\n",
        "\n",
        "time_elapsed = time.time() - since\n",
        "\n",
        "print('\\n\\nTraining complete in {:.0f}m {:.0f}s'.format(\n",
        "    time_elapsed // 60, time_elapsed % 60))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rASx0PYZZdUj",
        "outputId": "befc523c-bd90-498a-8c0d-b6d43e018f97"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "# Start training #\n",
            "\n",
            "Epoch: 1/10\n",
            "\tTrain Loss: 1.1627\n",
            "\tValid Loss: 0.3954\n",
            "\n",
            "Epoch: 2/10\n",
            "\tTrain Loss: 0.3145\n",
            "\tValid Loss: 0.2489\n",
            "\n",
            "Epoch: 3/10\n",
            "\tTrain Loss: 0.2233\n",
            "\tValid Loss: 0.1857\n",
            "\n",
            "Epoch: 4/10\n",
            "\tTrain Loss: 0.1773\n",
            "\tValid Loss: 0.1541\n",
            "\n",
            "Epoch: 5/10\n",
            "\tTrain Loss: 0.1498\n",
            "\tValid Loss: 0.1342\n",
            "\n",
            "Epoch: 6/10\n",
            "\tTrain Loss: 0.1311\n",
            "\tValid Loss: 0.1203\n",
            "\n",
            "Epoch: 7/10\n",
            "\tTrain Loss: 0.1175\n",
            "\tValid Loss: 0.1099\n",
            "\n",
            "Epoch: 8/10\n",
            "\tTrain Loss: 0.1070\n",
            "\tValid Loss: 0.1020\n",
            "\n",
            "Epoch: 9/10\n",
            "\tTrain Loss: 0.0987\n",
            "\tValid Loss: 0.0958\n",
            "\n",
            "Epoch: 10/10\n",
            "\tTrain Loss: 0.0919\n",
            "\tValid Loss: 0.0909\n",
            "\n",
            "\n",
            "Training complete in 1m 35s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Save history for later\n",
        "lenet5_train_loss_history = train_loss_history\n",
        "lenet5_valid_loss_history = valid_loss_history\n",
        "\n",
        "# Plot training and validation curve\n",
        "x = range(1, num_epochs + 1)\n",
        "plt.plot(x, lenet5_train_loss_history, label='train')\n",
        "plt.plot(x, lenet5_valid_loss_history, label='valid')\n",
        "\n",
        "plt.xlabel('# epochs')\n",
        "plt.ylabel('Loss')\n",
        "plt.legend()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 450
        },
        "id": "dTUO5hLoZjPU",
        "outputId": "d9e73002-3f1d-4b4a-84ab-5c8f157f6909"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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oxH1er2oUqlEtVot6vV68a677mr1/e+8846YnJwsfvTRR+LBgwfFjz76SIyNjRVXrlwpiqIoHjp0SAQgdu/eXfzwww/FvXv3irfffrsYFRUlVlRUiKIoisePHxcjIiLEu+++W8zPzxfXrFkjxsXFiXPnznVf54EHHhC7dOkirly5UiwsLBS/++47ccWKFU2ukZ6eLn7++ediQUGBeM0114g9e/YU6+rqRFEUxcsvv1y85JJLxN9++008cOCA+Nlnn4lbt2710b8qEbUXww0ReV1dXZ146NAhcffu3aJSqRR3794tFhYWijqdTty6dat46NAhsby8vNX3n3POOeKqVauaHJs3b544cuRIURQbgsfChQubXLN79+7iokWLRFEUxYcffljs37+/6HA43OcsXbpU1Ol0ot1uF41Go6hWq91h5kyua7z++uvuY3v27BEBiPn5+aIoiuK5554rPvbYYx381yEiX1NIOmxERCFJoVAgLS0N77//PoYNG4aBAwfihx9+QGJiIi688EKP7zWbzThw4ABuu+023HHHHe7jNpsNer2+ybkjR45scs2hQ4ciPz8fAJCfn4+RI0dCEAT3OaNGjYLJZMLx48dRUlICq9WKiy++2GM9AwcOdH+fnJwMACgrK0N6ejr++c9/4q677sJXX32FsWPH4uqrr25yPhFJg+GGiLwuKysLR44cQV1dHRwOB3Q6HWw2G2w2G3Q6HXr27Ik9e/a0+F6TyQQAWLFiBUaMGNHkNblc7rUatVptu85TKpXu711ByeFwAABuv/12jBs3DuvWrcNXX32FBQsW4LnnnsM//vEPr9VJRB3HhmIi8rr169cjLy8PSUlJeOedd5CXl4cBAwZgyZIlyMvL89h0m5iYiJSUFBw8eBB9+vRp8ujVq1eTc3/66Sf39zabDTt27EBGRgYAICMjA9u2bYMoiu5zfvjhB0RFRaF79+7o27cvtFotNm3adFY/a2pqKu688058/PHH+Ne//oUVK1ac1ecR0dnjyA0ReV3Pnj1RUlKC0tJSXHnllRAEAXv27MHVV1/tntrx5PHHH8c///lP6PV6jB8/HlarFb/++itOnz6NmTNnus9bunQp+vbti4yMDDz//PM4ffo0br31VgDA3XffjSVLluAf//gH7rnnHhQUFGDu3LmYOXMmZDIZNBoNHnzwQTzwwANQqVQYNWoUysvLsWfPHtx2223t+jlnzJiBCRMmoF+/fjh9+jQ2b97sDldEJB2GGyLyiS1btmDYsGHQaDT47rvv0L1793YFG8A53RMREYFnnnkG999/PyIjI3HuuedixowZTc5buHAhFi5ciLy8PPTp0wdr165FXFwcAKBbt25Yv3497r//fmRnZyM2Nha33XYb/v3vf7vf/+ijj0KhUGDOnDkoKipCcnIy7rzzznb/jHa7HdOnT8fx48cRHR2N8ePH4/nnn2/3+4nINwSx8ZgtEVEQOHz4MHr16oVdu3Zh0KBBUpdDRAGGPTdEREQUUhhuiIiIKKRwWoqIiIhCCkduiIiIKKQw3BAREVFIYbghIiKikMJwQ0RERCGF4YaIiIhCCsMNERERhRSGGyIiIgopDDdEREQUUhhuiIiIKKT8fzlhCQqdXrKMAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Plot training and validation curve\n",
        "x = range(1, num_epochs + 1)\n",
        "plt.plot(x, mlp_train_loss_history, label='MLP train')\n",
        "plt.plot(x, mlp_valid_loss_history, label='MLP valid')\n",
        "plt.plot(x, lenet5_train_loss_history, label='LeNet5 train')\n",
        "plt.plot(x, lenet5_valid_loss_history, label='LeNet5 valid')\n",
        "\n",
        "plt.xlabel('# epochs')\n",
        "plt.ylabel('Loss')\n",
        "plt.legend()\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 449
        },
        "id": "MqBM-HlZZkiR",
        "outputId": "4bf7cdfd-0a93-4bbf-eaca-e3daa70687c8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkAAAAGwCAYAAABB4NqyAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAACDTUlEQVR4nO3dd3hUZf738ff0SZ000iCQ0JEWQIiAYEMBURcrugiCuvtYUFlUlN0Vu4Aurj8UZXXFYEFQUVQWUUDpCIJEpYUWIAGS0NKTqef5YzJDBhIIyWRmknxf13WumTlz5j73kLj57F1ViqIoCCGEEEI0I2p/V0AIIYQQwtckAAkhhBCi2ZEAJIQQQohmRwKQEEIIIZodCUBCCCGEaHYkAAkhhBCi2ZEAJIQQQohmR+vvCgQih8PB0aNHCQsLQ6VS+bs6QgghhKgFRVEoLi4mMTERtfr8bTwSgKpx9OhRkpKS/F0NIYQQQtRBdnY2rVq1Ou81EoCqERYWBjj/AcPDw/1cGyGEEELURlFREUlJSe6/4+cjAagarm6v8PBwCUBCCCFEI1Ob4SsyCFoIIYQQzY4EICGEEEI0OxKAhBBCCNHsyBggIYQQAclut2O1Wv1dDRFAdDodGo3GK2VJABJCCBFQFEUhNzeXgoICf1dFBKCIiAji4+PrvU6fBCAhhBABxRV+YmNjCQ4OlgVpBeAMxmVlZeTn5wOQkJBQr/IkAAkhhAgYdrvdHX6io6P9XR0RYIKCggDIz88nNja2Xt1hMghaCCFEwHCN+QkODvZzTUSgcv1u1Hd8mAQgIYQQAUe6vURNvPW7IQFICCGEEM2OBCAhhBBCNDsSgIQQQghxjvT0dCIiIvxdjQYjAciHFEXh4IlSjhSU+7sqQgghvGzcuHGoVCoeeOCBc957+OGHUalUjBs3zuP6kSNH1lhecnIyKpUKlUpFSEgIvXv35vPPP6/x+lWrVqFSqby2ftKoUaPYs2ePV8oKRBKAfOjl/+3iyn+t4sMNB/1dFSGEEA0gKSmJBQsWUF5+5v/oVlRUMH/+fFq3bn3R5b3wwgscO3aMbdu20bdvX0aNGsWGDRvqVUeLxVKr64KCgoiNja3XvQKZBCAf6t7KBMCavSf8XBMhhGg8FEWhzGLz+aEoykXXtXfv3iQlJfHll1+6z3355Ze0bt2aXr16XXR5YWFhxMfH07FjR2bPnk1QUBDffvvtOdcdPHiQq666CoDIyEiP1qYrr7ySCRMmMHHiRGJiYhg6dCgAr7/+Ot27dyckJISkpCQeeughSkpK3GWe3QX23HPPkZqaykcffURycjImk4k777yT4uLii/5egUAWQvShy9vHoFLBrmNF5BdXEBtm9HeVhBAi4JVb7Vwy9Xuf33fnC0MJ1l/8n8l7772XDz74gNGjRwMwd+5cxo8fz6pVq+pVH61Wi06nq7YFJykpiUWLFnHrrbeSmZlJeHi4e9FAgHnz5vHggw+yfv169zm1Ws2sWbNISUnhwIEDPPTQQ0yePJm33367xjrs37+fxYsXs2TJEk6fPs0dd9zB9OnTefnll+v13fxBWoB8KDrUQLdEZyvQOmkFEkKIJunuu+9m3bp1HDp0iEOHDrF+/XruvvvuepVpsViYNm0ahYWFXH311ee8r9FoiIqKAiA2Npb4+HhMJpP7/Q4dOvDqq6/SqVMnOnXqBMDEiRO56qqrSE5O5uqrr+all17is88+O289HA4H6enpdOvWjUGDBjFmzBhWrlxZr+/mL9IC5GODOsTwx5FC1uw5zi29W/m7OkIIEfCCdBp2vjDUL/etixYtWjBixAjS09NRFIURI0YQExNTp7Keeuop/vnPf1JRUUFoaCjTp09nxIgRF11Onz59zjm3YsUKpk2bxu7duykqKsJms1FRUUFZWVmNK3EnJycTFhbmfp2QkODem6uxkQDkY4M7tuDtVftZu/cEDoeCWi2rnQohxPmoVKo6dUX507333suECRMAmD17dp3LefLJJxk3bhyhoaHExcXVeRXkkJAQj9cHDx7khhtu4MEHH+Tll18mKiqKdevWcd9992GxWGoMQDqdzuO1SqXC4XDUqU7+1rh+o5qA3q0jCdFrOFlqYeexIrq1NF34Q0IIIRqVYcOGYbFYUKlU7kHHdRETE0P79u1rda1erwecG8peyNatW3E4HMycORO12jka5kLdX02NBCAf02vV9G8XzYpd+azZe1wCkBBCNEEajYZdu3a5n9eksLCQjIwMj3PR0dEkJSVd9D3btGmDSqViyZIlXH/99QQFBREaGlrtte3bt8dqtfLmm29y4403sn79eubMmXPR92zMZBC0Hwzu2AKANXuO+7kmQgghGkp4eDjh4eHnvWbVqlX06tXL43j++efrdL+WLVvy/PPP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kCFDiI+Pv+Au7evWrWPQoEEEBQWRlJTEo48+SmlpKQBXXnklhw4d4m9/+5u7laeq6Oho4uPj3YdOp6v2HgcPHuSqq64CIDIyEpVKxbhx49z3mDBhAhMnTiQmJoahQ4cC8Prrr9O9e3dCQkJISkrioYceoqSkxF3m2V1gzz33HKmpqXz00UckJydjMpm48847KS4uvvA/aD1JAApQYUYdvVtHArIqtBCieVMUhTJrmc8PRfHeYrQFBQVcffXV9OrViy1btrBs2TLy8vK44447PK7TaDS88sorvPnmm+Tk5FRb1v79+xk2bBi33norv//+OwsXLmTdunVMmDABgC+//JJWrVrxwgsvuFt5qrrpppuIjY3l8ssv55tvvqmxzklJSSxatAiAzMxMjh07xv/93/+53583bx56vZ7169czZ84cANRqNbNmzWLHjh3MmzePH3/8kcmTJ5/332b//v0sXryYJUuWsGTJElavXn1ON2BD0Db4HUSdDeoQw+aDp1iz5zij09r4uzpCCOEX5bZy0uan+fy+m/68iWBdsFfKeuutt+jVqxevvPKK+9zcuXNJSkpiz549dOzY0X3+5ptvJjU1lWeffZb333//nLKmTZvG6NGjmThxIgAdOnRg1qxZXHHFFbzzzjtERUWh0WgICwsjPj7e/bnQ0FBmzpzJwIEDUavVLFq0iJEjR7J48WJuuummc+6j0WiIiooCIDY29pzByx06dODVV1/1OOeqEzjHIb300ks88MADvP322zX+2zgcDtLT0wkLCwNgzJgxrFy5kpdffrnGz3iDBKAANrhjC2Yu38OGfSex2R1oNdJgJ4QQjdFvv/3GTz/9RGho6Dnv7d+/3yMAAcyYMYOrr76aJ554otqyfv/9dz755BP3OUVRcDgcZGVl0aVLl2rrEBMTw6RJk9yv+/bty9GjR3nttdeqDUAXUt3YoRUrVjBt2jR2795NUVERNpuNiooKysrKCA6uPkwmJye7ww9AQkIC+fn5F12fiyUBKIB1a2kiMljH6TIrGdkFXJoc5e8qCSGEzwVpg9j0501+ua+3lJSUcOONNzJjxoxz3ktISDjn3ODBgxk6dChTpkxxj7upWtb/+3//j0cfffScz7Vu3fqi6pWWlsby5csv6jMuISEhHq8PHjzIDTfcwIMPPsjLL79MVFQU69at47777sNisdQYgM4e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y7p16zh16hRfffVVrT9fV35dCFFcPJ1GTf920Szfmceavcfp3sp04Q8JIUQjppSXk9nbt900AJ1+3YoqONgrZb311lv06tWLV155xX1u7ty5JCUlsWfPHjp27Og+f/PNN5Oamsqzzz7L+++/f05Z06ZNY/To0UycOBGADh06MGvWLK644greeecdoqKi0Gg0hIWFeSwKHBoaysyZMxk4cCBqtZpFixYxcuRIFi9ezE033VRtvUePHs3MmTM5fPgwrVu3xuFwsGDBAv75z3+6r3HVA5xjj1566SUeeOAB3n777Vr927zxxhtMmTKFW265BYA5c+bw/fff1+qz9dEoB0E3dzIdXgghGpfffvuNn376idDQUPfh2qdy//7951w/Y8YM5s2bx65du6otKz093aOsoUOH4nA4yMrKqrEOMTExTJo0ibS0NPr27cv06dO5++67ee2112r8TGpqKl26dHG3Aq1evZr8/HyPLahWrFjBNddcQ8uWLQkLC2PMmDGcPHmSsrKyC/67FBYWcuzYMdLS0tzntFotl1566QU/W1/SAtQIDe4QA8DWQ6cpMdsINciPUQjRdKmCguj061a/3NdbSkpKuPHGG5kxY8Y571U3S3nw4MEMHTqUKVOmMG7cuHPK+n//7//x6KOPnvO51q1bX1S90tLSWL58+XmvGT16NPPnz+fpp59m/vz5DBs2zD2I+eDBg9xwww08+OCDvPzyy0RFRbFu3Truu+8+LBYLwV5qQWsI8pezEWoTHUKb6GAOnSzj5/0nGXJJnL+rJIQQDUalUnmtK8pfevfuzaJFi0hOTkarrd2f3unTp5OamkqnTp3OKWvnzp20b9++xs/q9XrsdvsF75GRkXHBZWL+/Oc/889//pOtW7fyxRdfMGfOHPd7W7duxeFwMHPmTNRqZ6fS+RYePpvJZCIhIYFNmzYxePBgAGw2G1u3bqV37961LqcupAuskRpU2Qok22IIIUTgKCwsdC/v4jqys7N5+OGHOXXqFHfddRe//PIL+/fv5/vvv2f8+PE1BpXu3bszevRoZs2a5XH+qaeeYsOGDUyYMIGMjAz27t3L119/7R4EDc6xOGvWrOHIkSPumWbz5s3j008/Zffu3ezevZtXXnmFuXPn8sgjj5z3OyUnJzNgwADuu+8+7Ha7x3ih9u3bY7VaefPNNzlw4AAfffSRR0Cqjccee4zp06ezePFidu/ezUMPPURBQcFFlVEXEoAaKdd6QDIOSAghAseqVavcy7u4jueff57ExETWr1+P3W7nuuuuo3v37kycOJGIiAh3y0l1XnjhBRwOh8e5Hj16sHr1avbs2cOgQYPcy8ckJiZ6fO7gwYO0a9fOYxmYF198kT59+pCWlsbXX3/NwoULGT9+/AW/1+jRo/ntt9+4+eabCarSNdizZ09ef/11ZsyYQbdu3fjkk08uOIX/bI8//jhjxozhnnvuoX///oSFhXHzzTdfVBl1oVJ8Mdm+kSkqKsJkMlFYWBiw+4IVV1jp9cJybA6FNU9eRevoxt08LIQQABUVFWRlZZGSkoLRaPR3dUQAOt/vyMX8/ZYWoEYqzKijd+tIQLrBhBBCiIslAagRG9yxchyQdIMJIYQQF0UCUCPmWg9o4/6TWO2OC1wthBBCCBcJQI1Y10QTkcE6is02MrIL/F0dIYQQotGQANSIadQqLnftDi/dYEKIJkTm54iaeOt3QwJQI+daFXr13hMXuFIIIQKfa2fy2myjIJon1+9GTbvY15asBN3IDapsAfo9p4DTpRYiQ/R+rpEQQtSdRqMhIiKC/Px8AIKDg1GpVH6ulQgEiqJQVlZGfn4+ERERaDSaepUnAaiRizcZ6RQXRmZeMev3n+CGHokX/pAQQgQw1w7mrhAkRFUREREeu9zXlQSgJmBwxxgy84pZs+e4BCAhRKOnUqlISEggNjYWq9Xq7+qIAKLT6erd8uMiAagJGNShBe+tzWLNnhMoiiLNxUKIJkGj0Xjtj50QZ5NB0L5kKYVd30Ludq8W2y8lCoNWTW5RBfvyS7xathBCCNEUSQDype//AQvvhq0feLVYo05DWttoAFbLdHghhBDigiQA+VKn652Pu5eCl9e4cE2HXyPT4YUQQogLkgDkSymDQRcCxUfh6DavFu3aFmPTgZNUWO1eLVsIIYRoaiQA+ZLOCB2GOJ9nLvVq0R1iQ4kPN2K2Ofjl4Cmvli2EEEI0NRKAfK3TCOfj7v95tViVSsWgDrI7vBBCCFEbEoB8reN1oNJA/k44dcCrRbu6wdbKOCAhhBDivCQA+VpQJCQPdD7f7d1usMvbx6BSwe7cYvKKKrxathBCCNGUSADyh843OB+9PA4oMkRPj5YmQFqBhBBCiPORAOQPnYY7Hw9vhNKTXi3a1Q0m44CEEEKImkkA8oeI1hDfAxQH7Fnm1aJdu8Ov23cCh8O7aw0JIYQQTYUEIH/p3DCzwXq1jiDUoOVUqYUdR4u8WrYQQgjRVEgA8hdXANr/I1jKvFasTqNmQDvnthhr9ko3mBBCCFEdCUD+EtcNTK3BVg4HfvJq0YMqxwHJvmBCCCFE9fwagNasWcONN95IYmIiKpWKxYsXn/f6VatWoVKpzjlyc3M9rps9ezbJyckYjUbS0tLYvHlzA36LOlKpqnSDeXc22BWV44B+PXSaErPNq2ULIYQQTYFfA1BpaSk9e/Zk9uzZF/W5zMxMjh075j5iY2Pd7y1cuJBJkybx7LPP8uuvv9KzZ0+GDh1Kfn6+t6tff50rN0fd8x04vLd/V+voYJKjg7E5FDbu9+4sMyGEEKIp8GsAGj58OC+99BI333zzRX0uNjaW+Ph496FWn/kar7/+On/5y18YP348l1xyCXPmzCE4OJi5c+fWWJ7ZbKaoqMjj8InWA8AYAWUnIXuTV4t2zQaT6fBCCCHEuRrlGKDU1FQSEhK49tprWb9+vfu8xWJh69atDBkyxH1OrVYzZMgQNm7cWGN506ZNw2QyuY+kpKQGrb+bRgsdhzmfe3k22JltMSQACSGEEGdrVAEoISGBOXPmsGjRIhYtWkRSUhJXXnklv/76KwAnTpzAbrcTFxfn8bm4uLhzxglVNWXKFAoLC91HdnZ2g34PD1WnwyveW7enf7totGoVB0+Wcfik92aZCSGEEE2B1t8VuBidOnWiU6dO7tcDBgxg//79/Pvf/+ajjz6qc7kGgwGDweCNKl68dleDxgCnsyB/F8Rd4pViQw1aereJZHPWKVbvPc6Y6DZeKVcIIYRoChpVC1B1+vXrx759+wCIiYlBo9GQl5fncU1eXh7x8fH+qN6FGUKh3VXO55ne7Qa7wtUNJuOAhBBCCA+NPgBlZGSQkJAAgF6vp0+fPqxcudL9vsPhYOXKlfTv399fVbywTpWzwbw9DqhyIPSG/Sex2h1eLVsIIYRozPzaBVZSUuJuvQHIysoiIyODqKgoWrduzZQpUzhy5AgffvghAG+88QYpKSl07dqViooK/vvf//Ljjz/yww8/uMuYNGkS99xzD5deein9+vXjjTfeoLS0lPHjx/v8+9Vap+HwrQqOboPCI2Bq6ZViuyaGExWi51SphYzsAvomR3mlXCGEEKKx82sA2rJlC1dddZX79aRJkwC45557SE9P59ixYxw+fNj9vsVi4fHHH+fIkSMEBwfTo0cPVqxY4VHGqFGjOH78OFOnTiU3N5fU1FSWLVt2zsDogBIaC0n9nFPhM5dCv794pVi1WsXl7WP45rejrNlzXAKQEEIIUUmlKF6cetREFBUVYTKZKCwsJDw83Dc3XfcGrHjWOSh6zFdeK/bzLdk8+cXv9Gxl4usJl3utXCGEECLQXMzf70Y/BqjJ6HyD8zFrLVQUeq1Y13pAvx8p5HSpxWvlCiGEEI2ZBKBAEdMeYjqCwwp7l3ut2LhwI53jw1AUWLfvhNfKFUIIIRozCUCBxLUoYqZ3N0cd1CEGkG0xhBBCCBcJQIGkU2UA2rscbN7rrjqzLcYJZMiXEEIIIQEosLTsA6FxYC6Cg2u9Vmzf5CgMWjW5RRXszS/xWrlCCCFEYyUBKJCo1c41gcCriyIadRrS2kYD0g0mhBBCgASgwOOaDZb5HTi8t3rzYNc4oL0yEFoIIYSQABRoUgaDPhSKj8KxbV4r1rUv2KYDJ6mw2r1WrhBCCNEYSQAKNFoDtB/ifL7be7PB2seGEh9uxGxzsDnrlNfKFUIIIRojCUCByDUd3ovjgFQqFYM7OrvB1u6VcUBCCCGaNwlAgajDtaDWwvFdcHK/14p1TYdfs0fGAQkhhGjeJAAFoqBIaDPQ+dyLiyIObBeDSgWZecXkFVV4rVwhhBCisZEAFKhcs8G8OA4oMkRPj1YRgEyHF0II0bxJAApUrvWAsn+GUu91WV0h0+GFEEIICUABKyIJEnqC4oA9y7xW7KDKcUDr9h7H4ZBtMYQQQjRPEoACWSfvzwZLTYogzKDldJmV7UcLvVauEEII0ZhIAApkrunw+38CS5lXitRp1AxoL9tiCCGEaN4kAAWyuK4Q0Rps5bD/R68VO6hD5XR4GQckhBCimZIAFMhUqip7g3lvNphrW4xfD52muMLqtXKFEEKIxkICUKDrdL3zMfM7sNu8UmRSVDDJ0cHYHAob95/0SplCCCFEYyIBKNC17u9cGLH8FGRv8lqxrlWh10o3mBBCiGZIAlCg02ih4zDncy/OBhvsHgckA6GFEEI0PxKAGgN3N9j/QPHO2j2XtYtGq1Zx6GQZh06WeqVMIYQQorGQANQYtL8GtEY4fRDyd3qlyFCDlj5tIgGZDSaEEKL5kQDUGOhDoO2Vzude3BvszO7w0g0mhBCieZEA1Fi4FkXcvcRrRbrGAW3cfxKr3eG1coUQQohAJwGoseg4DFDBsQwozPFKkV0Tw4kO0VNitrHtcIFXyhRCCCEaAwlAjUVoLCSlOZ9nfueVItVqFZe7doeXbjAhhBDNiASgxqRz5WwwL06Hd22LsVamwwshhGhGJAA1Jq5tMQ6uhfICrxQ5uLIF6PcjhZwqtXilTCGEECLQSQBqTKLbQUwncNhg3wqvFBkbbqRzfBiKAuv2yXR4IYQQzYNfA9CaNWu48cYbSUxMRKVSsXjx4vNe/+WXX3LttdfSokULwsPD6d+/P99//73HNc899xwqlcrj6Ny5cwN+Cx9zzwbz4qrQrm0xZByQEEKIZsKvAai0tJSePXsye/bsWl2/Zs0arr32WpYuXcrWrVu56qqruPHGG9m2bZvHdV27duXYsWPuY926dQ1Rff9wBaC9y8Fm9kqRVbfFULy00rQQQggRyLT+vPnw4cMZPnx4ra9/4403PF6/8sorfP3113z77bf06tXLfV6r1RIfH1/rcs1mM2bzmTBRVFRU68/6XGJvCI2HklznWKD2Q+pd5KXJkRh1avKKzOzJK6FTfJgXKiqEEEIErkY9BsjhcFBcXExUVJTH+b1795KYmEjbtm0ZPXo0hw8fPm8506ZNw2QyuY+kpKSGrHb9qNXQqTI0eqkbzKjTkJYSDchsMCGEEM1Dow5A//rXvygpKeGOO+5wn0tLSyM9PZ1ly5bxzjvvkJWVxaBBgyguLq6xnClTplBYWOg+srOzfVH9unPNBsv8DhzeWcHZNQ5otYwDEkII0Qz4tQusPubPn8/zzz/P119/TWxsrPt81S61Hj16kJaWRps2bfjss8+47777qi3LYDBgMBgavM5ekzII9GFQfAyOboNWfepdpGs6/OasU1RY7Rh1mnqXKYQQQgSqRtkCtGDBAu6//34+++wzhgw5/xiYiIgIOnbsyL59+3xUOx/QGqBD5ffO9E43WPvYUBJMRsw2B5uzTnmlTCGEECJQNboA9OmnnzJ+/Hg+/fRTRowYccHrS0pK2L9/PwkJCT6onQ918u50eJVKdWY2mHSDCSGEaOL8GoBKSkrIyMggIyMDgKysLDIyMtyDlqdMmcLYsWPd18+fP5+xY8cyc+ZM0tLSyM3NJTc3l8LCQvc1TzzxBKtXr+bgwYNs2LCBm2++GY1Gw1133eXT79bgOlwLai0c3w0n93ulyEEdnd1ga/fKgohCCCGaNr8GoC1bttCrVy/3FPZJkybRq1cvpk6dCsCxY8c8ZnC9++672Gw2Hn74YRISEtzHY4895r4mJyeHu+66i06dOnHHHXcQHR3Nzz//TIsWLXz75RpaUAQkX+587qVWoMvbx6BWQWZeMbmFFV4pUwghhAhEKkVWvjtHUVERJpOJwsJCwsPD/V2dmm1+D5Y+Aa37w73LvFLkyNnrycgu4NXbenDHpQG8HIAQQghxlov5+93oxgCJKlzrAR3+GUq8M27HNRtMusGEEEI0ZRKAGjNTK0hIBRTY450WINd6QOv2HsfukMZBIYQQTZMEoMbOy5ujpiZFEGbQcrrMyvYjhRf+gBBCCNEISQBq7FwB6MBPYCmtd3FajZoB7WVbDCGEEE2bBKDGLvYSiGgDtgrY/6NXinR1g63ZI+OAhBBCNE0SgBo7lapKN9hSrxTpWhDx18OnKa6weqVMIYQQIpBIAGoKXAFoz3dgt9W7uKSoYFJiQrA5FDbuP1nv8oQQQohAIwGoKUi6DIIiofw0ZP/slSJd0+HXyDggIYQQTZAEoKZAo4WOlWsCeWk2mIwDEkII0ZTVKQBlZ2eTk5Pjfr1582YmTpzIu+++67WKiYvU+Xrn4+7/gRcW976sbTQ6jYrDp8o4dLL+s8uEEEKIQFKnAPTnP/+Zn376CYDc3FyuvfZaNm/ezD/+8Q9eeOEFr1ZQ1FK7q0FrhIJDkLej3sWFGLT0aRMJyO7wQgghmp46BaDt27fTr18/AD777DO6devGhg0b+OSTT0hPT/dm/URt6UOg7VXO55lemg1W2Q22WrrBhBBCNDF1CkBWqxWDwQDAihUruOmmmwDo3Lkzx44d817txMXx8qrQrunwG/efwGp3eKVMIYQQIhDUKQB17dqVOXPmsHbtWpYvX86wYcMAOHr0KNHR0V6toLgIHYcBKjiWAYU5F7r6gi5JCCc6RE+pxc6vh07XuzwhhBAiUNQpAM2YMYP//Oc/XHnlldx111307NkTgG+++cbdNSb8ILQFtL7M+Tzzu3oXp1aruFx2hxdCCNEE1SkAXXnllZw4cYITJ04wd+5c9/m//vWvzJkzx2uVE3XQyTUbbIlXinN1g8l6QEIIIZqSOgWg8vJyzGYzkZHOWUKHDh3ijTfeIDMzk9jYWK9WUFwk1zigg+ugvKDexQ2qbAH640ghp0ot9S5PCCGECAR1CkB/+tOf+PDDDwEoKCggLS2NmTNnMnLkSN555x2vVlBcpOh20KIzOGywd3m9i4sNN9I5PgxFgXX7pBtMCCFE01CnAPTrr78yaNAgAL744gvi4uI4dOgQH374IbNmzfJqBUUduFqBMr0zG+wK96rQ0g0mhBCiaahTACorKyMsLAyAH374gVtuuQW1Ws1ll13GoUOHvFpBUQedKgPQ3uVgM9e7ONd6QGv3HkfxwirTQgghhL/VKQC1b9+exYsXk52dzffff891110HQH5+PuHh4V6toKiDxF4QlgCWEshaW+/i+rSJxKhTk1dkZk9eiRcqKIQQQvhXnQLQ1KlTeeKJJ0hOTqZfv370798fcLYG9erVy6sVFHWgVkMn1+ao9Z8NZtRpuKytc30n6QYTQgjRFNQpAN12220cPnyYLVu28P3337vPX3PNNfz73//2WuVEPbjHAX0Hjvqv4izT4YUQQjQl2rp+MD4+nvj4ePeu8K1atZJFEANJ8iDQh0FJLhz9FVpdWq/iBnd0TofflHWKCqsdo07jjVoKIYQQflGnFiCHw8ELL7yAyWSiTZs2tGnThoiICF588UUcXmhtEF6gNUCHa53PvbA3WLsWoSSajFhsDjZlnap3eUIIIYQ/1SkA/eMf/+Ctt95i+vTpbNu2jW3btvHKK6/w5ptv8swzz3i7jqKuvLg5qkqlcs8Gk3FAQgghGrs6dYHNmzeP//73v+5d4AF69OhBy5Yteeihh3j55Ze9VkFRDx2uBbUOTmTCiX0Q075exQ3q0IIFv2SzVsYBCSGEaOTq1AJ06tQpOnfufM75zp07c+qUdI8EDKMJki93PvfCooiXt49BrYI9eSUcKyyvd3lCCCGEv9QpAPXs2ZO33nrrnPNvvfUWPXr0qHelhBe5u8GW1rsoU7COnkkRgOwOL4QQonGrUxfYq6++yogRI1ixYoV7DaCNGzeSnZ3N0qX1/0MrvKjT9bD0CcjeBCX5EFq/zWoHdWjBtsMFrNlznDsuTfJSJYUQQgjfqlML0BVXXMGePXu4+eabKSgooKCggFtuuYUdO3bw0UcfebuOoj5MLZ0rQ6PAnmX1Lu6Kyunw6/adwO6QbTGEEEI0TnUKQACJiYm8/PLLLFq0iEWLFvHSSy9x+vRp3n///VqXsWbNGm688UYSExNRqVQsXrz4gp9ZtWoVvXv3xmAw0L59e9LT08+5Zvbs2SQnJ2M0GklLS2Pz5s0X8c2aoE7emw3Ws1UEYUYtBWVWth8prHd5QgghhD/UOQB5Q2lpKT179mT27Nm1uj4rK4sRI0Zw1VVXkZGRwcSJE7n//vs9VqNeuHAhkyZN4tlnn+XXX3+lZ8+eDB06lPz8/Ib6GoGv8/XOx/0/gbl+e3lpNWoGtnO2Asl0eCGEEI2VXwPQ8OHDeemll7j55ptrdf2cOXNISUlh5syZdOnShQkTJnDbbbd5bL/x+uuv85e//IXx48dzySWXMGfOHIKDg5k7d26N5ZrNZoqKijyOJiX2EohMBrsZ9v9Y7+Ku6ORcD2j+5sMUV1jrXZ4QQgjha34NQBdr48aNDBkyxOPc0KFD2bhxIwAWi4WtW7d6XKNWqxkyZIj7mupMmzYNk8nkPpKSmtjgXpXqTDdYZv0HqY9MbUmb6GCOFVbwytLd9S5PCCGE8LWLmgV2yy23nPf9goKC+tTlgnJzc4mLi/M4FxcXR1FREeXl5Zw+fRq73V7tNbt31/yHesqUKUyaNMn9uqioqOmFoM4j4OfZzoHQdhto6rwNHEF6DTNu7cGd7/7Mp5sPc0OPBAa2j/FiZYUQQoiGdVEtQFVbSao72rRpw9ixYxuqrg3GYDAQHh7ucTQ5SWkQFAXlp+Fwza1htXVZ22jGXNYGgKcW/U6p2VbvMoUQQghfuahmgA8++KCh6lEr8fHx5OXleZzLy8sjPDycoKAgNBoNGo2m2mvi4+N9WdXAo9FCp+GQ8YlzNljKoHoX+fTwzvy4O5+c0+W89n0mz93U1QsVFUIIIRpeoxoD1L9/f1auXOlxbvny5e7FGPV6PX369PG4xuFwsHLlSvc1/lZQUUCZtcw/N+9UORss83+g1H8NnxCDlhm3Olf+Tt9wkM2yS7wQQohGwq8BqKSkhIyMDDIyMgDnNPeMjAwOHz4MOMfmVO1Se+CBBzhw4ACTJ09m9+7dvP3223z22Wf87W9/c18zadIk3nvvPebNm8euXbt48MEHKS0tZfz48T79btWZu30u135xLZ/v+dw/FWh3NWiDoOAw5O3wSpGXd4jhzr7O8VKTv/iNcovdK+UKIYQQDcmvAWjLli306tWLXr16Ac7w0qtXL6ZOnQrAsWPH3GEIICUlhf/9738sX76cnj17MnPmTP773/8ydOhQ9zWjRo3iX//6F1OnTiU1NZWMjAyWLVt2zsBof4gwRFBhr+DDnR9itfth+rg+GNpd5XzuhUURXf4+ogvx4UYOnizj9eWZXitXCCGEaCgqRfFCX0gTU1RUhMlkorCw0KsDoi12C0MXDeVE+Qlevvxlbmp3k9fKrrVtH8PXD0NCT/h/a7xW7E+78xmf/gtqFXzx4AB6t470WtlCCCFEbVzM3+9GNQaosdNr9IzuMhqAD7Z/gF+yZ8dhoFLDsd+gINtrxV7VOZZberfEocDkL36nwipdYUIIIQKXBCAfu6PTHQRrg9lXsI91R9b5vgIhMZB0mfN55ndeLXrqDZfQIszAvvwSZq3c69WyhRBCCG+SAORj4fpwbut4GwAf7PDTsgKuvcF2L/FqsRHBel4a2Q2A/6w5wB85slmqEEKIwCQByA/GXDIGrUrLL7m/sP3Edt9XwDUd/tB658KIXjS0azw39EjA7lB48ovfsNgcXi1fCCGE8AYJQH4QHxLP8JThgHMskM9Ft4MWXcBhg73LvV788zd1JTpEz+7cYmb/tM/r5QshhBD1JQHIT8Z1GwfAisMryC7y3mDkWutcuTmqF6fDu0SHGnj+T85VoWf/tI9dx4q8fg8hhBCiPiQA+UnHyI4MbDkQh+Jg3s55vq+AaxzQvhVgM3u9+BHdExjaNQ5bZVeY1S5dYUIIIQKHBCA/urfrvQB8ve9rTlX4eBuJhF4QlgiWEsjy3npALiqVihdHdsMUpGP7kSLeXXPA6/cQQggh6koCkB/1je/LJdGXUGGvYMHuBb69uVrt3BwVvD4bzCU2zMizN14CwP+t2MvevOIGuY8QQghxsSQA+ZFKpWJ8N+ceZZ/u/pRyW7lvK+AaB5T5HTgapovq5l4tubpzLBa7gye/+B27QxYeF0II4X8SgPxsSOshtAxtSYG5gMX7Fvv25smDwBAOJXlwZGuD3EKlUvHyzd0IM2jJyC5g7rqsBrmPEEIIcTEkAPmZVq3lnq73APDhjg+xOWw+vLkeOlzrfJ7p/dlgLgmmIP55QxcA/vVDJgeOlzTYvYQQQojakAAUAEa2H0mEIYKckhxWHF7h25u7FkVsgOnwVd1xaRKDOsRgtjl4atHvOKQrTAghhB9JAAoAQdog7up8F+CHTVI7XAtqHZzYAycabv8ulUrFtFu6E6LX8MvB03y48WCD3UsIIYS4EAlAAeLOzndi0BjYeXInv+T+4rsbG02QMsj5vIFbgVpFBvP09c6usBnLMsk+Vdag9xNCCCFqIgEoQEQZoxjZfiTgh01SXd1gmUsb/Faj+7XmsrZRlFvtPLXod9+2dgkhhBCVJAAFkHsuuQe1Ss26I+vYc3qP727sCkDZm6Ekv0FvpVarmHFrD4w6NRv2n2T+5sMNej8hhBCiOhKAAkhSeBJDWg8BYN4OH26PYWoJib0AxbkmUANrEx3Ck0M7AzBt6W6OFPh4/SMhhBDNngSgAONaGHHpgaXklub67sYNuDlqdcYNSKZPm0hKzDamfPmHdIUJIYTwKQlAAaZbTDf6xvfFptj4eOfHvrtxp8oAdGAVmBt+nR5NZVeYXqtmzZ7jfLE1p8HvKYQQQrhIAApA47qOA+DzPZ9TZCnyzU1ju0BkCtjNsH+lT27ZPjaUSdd2BODFJTvJK6rwyX2FEEIICUABaFDLQbSPaE+ZrYzPMz/3zU1VqirdYA0/G8zl/stT6NnKRFGFjX98JV1hQgghfEMCUABSqVTuVqCPd32MxW7xzY1dAWjPMrBbfXJLrUbNq7f1RKdRsWJXPt/8dtQn9xVCCNG8SQAKUNenXE9scCwnyk/wvwO+GZhMUhoER0NFARze6Jt7Ap3iw3j06g4APPvNDo4Xm312byGEEM2TBKAApdPoGNNlDOBcGNGhOBr+pmoNdBzufO7DbjCAB65sxyUJ4RSUWXn2m+0+vbcQQojmRwJQALut422E6kLJKsxiTc4a39y0c5XNUX04HkenUfPa7T3QqlUs/SOXpX8c89m9hRBCND8SgAJYqD6U2zvdDjg3SfWJtleBNggKD0Oeb1tiuiaaePDKdgBM/Xo7p0p9NPZJCCFEsyMBKMDd3eVutGotv+b/SkZ+RsPfUB8M7a52PvfRoohVTbi6PR3jQjlRYuH5b3f4/P5CCCGaBwlAAS42OJYb2t4AQPqOdN/c1MerQldl0Gp47baeqFXwdcZRlu/M83kdhBBCNH0SgBoB15T4Hw//yMHCgw1/w47DQKWG3N+hwPeblfZMiuAvg9sC8I+v/qCwzDdT8oUQQjQfEoAagXYR7bii1RUoKMzb6YNNUkOioXV/53MfbI5anb8N6UjbFiHkF5t58X87/VIHIYQQTVdABKDZs2eTnJyM0WgkLS2NzZs313jtlVdeiUqlOucYMWKE+5px48ad8/6wYcN88VUajGuT1G/2fcOJ8hMNf8NOrtlgSxr+XtUw6jS8dlsPVCr4YmsOqzLz/VIPIYQQTZPfA9DChQuZNGkSzz77LL/++is9e/Zk6NCh5OdX/wfvyy+/5NixY+5j+/btaDQabr/9do/rhg0b5nHdp59+6ouv02B6x/amR0wPLA4L83fNb/gbuqbDH1wP5acb/n7V6NMmivEDUgCY8uUfFFdIV5gQQgjv8HsAev311/nLX/7C+PHjueSSS5gzZw7BwcHMnTu32uujoqKIj493H8uXLyc4OPicAGQwGDyui4yM9MXXaTAqlcrdCrQwcyFl1rKGvWFUW4i9BBQ77PmhYe91Hk8M7UjrqGCOFVYw7bvdfquHEEKIpsWvAchisbB161aGDBniPqdWqxkyZAgbN9ZuK4b333+fO++8k5CQEI/zq1atIjY2lk6dOvHggw9y8uTJGsswm80UFRV5HIHoqqSraB3WmiJLEV/u/bLhb+iaDZbp+9lgLsF6LTNu7QHA/E2H2bDPB91/Qgghmjy/BqATJ05gt9uJi4vzOB8XF0dubu4FP79582a2b9/O/fff73F+2LBhfPjhh6xcuZIZM2awevVqhg8fjt1ur7acadOmYTKZ3EdSUlLdv1QD0qg13NP1HgA+3PkhVkcDdwm5xgHtXQHWioa913n0bxfNmMvaADB50e+Umm1+q4sQQoimwe9dYPXx/vvv0717d/r16+dx/s477+Smm26ie/fujBw5kiVLlvDLL7+watWqasuZMmUKhYWF7iM7O9sHta+bm9rdRJQximOlx/jhYAN3TSX2grBEsJZClo+24qjBU8M70zIiiJzT5bz2faZf6yKEEKLx82sAiomJQaPRkJfnudhdXl4e8fHx5/1saWkpCxYs4L777rvgfdq2bUtMTAz79u2r9n2DwUB4eLjHEaiMWiN/7vxnwLkwotKQ+3WpVFX2BvPPbDCXUIOW6bd2ByB9w0E2Z53ya32EEEI0bn4NQHq9nj59+rBy5Ur3OYfDwcqVK+nfv/95P/v5559jNpu5++67L3ifnJwcTp48SUJCQr3rHAhGdRpFkDaI3ad2s/FY7cZK1Zl7HNB34PDBjvTnMahDC0Zd6uyenPzFb5Rbqu/SFEIIIS7E711gkyZN4r333mPevHns2rWLBx98kNLSUsaPd854Gjt2LFOmTDnnc++//z4jR44kOjra43xJSQlPPvkkP//8MwcPHmTlypX86U9/on379gwdOtQn36mhRRgjuKXDLQCkb09v2Ju1uRwM4VCaD0e2NOy9auEfN3QhPtzIwZNlvL5cusKEEELUjd8D0KhRo/jXv/7F1KlTSU1NJSMjg2XLlrkHRh8+fJhjx455fCYzM5N169ZV2/2l0Wj4/fffuemmm+jYsSP33Xcfffr0Ye3atRgMBp98J18Yc8kYNCoNG49tZNfJXQ13I60eOlzrfO6HvcHOFm7U8cot3QB4f10Wvx72zxpFQgghGjeV0qCDSBqnoqIiTCYThYWFAT0eaPKayXyX9R3Xp1zPjMEzGu5G2xfBF/dCdAd4xP+tQACTFmbw5bYjtI8NZckjl2PUafxdJSGEEH52MX+//d4CJOpufFdnN+H3B7/naMnRhrtR+2tBrYOTe+H4noa7z0WYeuMlxIQa2JdfwqyVe/1dHSGEEI2MBKBGrEt0Fy5LuAy7YuejnR813I2M4ZAy2Pncj4siVhURrOelkc6usP+sOcAfOYV+rpEQQojGRAJQI+dqBVq0dxGF5gYMAe7p8Esb7h4XaVi3eG7okYDdofDkF79hsfl3lpoQQojGQwJQI9c/sT+dIjtRbitnYebChruRa1XonF+gOO/81/rQ8zd1JSpEz+7cYt5eVf06T0IIIcTZJAA1ciqVinHdxgHwya5PMNvNDXOj8ERI7A0osOe7hrlHHUSHGnj+pq4AvPXjPnYdC8x93IQQQgQWCUBNwNDkoSSEJHCq4hTf7P+m4W7kWhQxAKbDV3VDjwSuuyQOW2VXmNUuXWFCCCHOTwJQE6BT6xhzyRgAPtzxIXZHA62Q7ApAB1aDuaRh7lEHKpWKl0Z2wxSkY/uRIt5dc8DfVRJCCBHgJAA1Ebd2uJVwfTgHiw6yKntVw9ykRWeIagt2M+xfeeHrfSg23MjUGy4B4P9W7GVvXrGfaySEECKQSQBqIoJ1wYzqNAqAuTvmNswmqSrVmcHQAdYNBnBL75Zc1akFFruDJ7/4HbtD1vgUQghRPQlATcifu/wZvVrP78d/Z1v+toa5SecbnI97vge7tWHuUUcqlYpXbulOmEFLRnYBc9dl+btKQgghApQEoCYkJiiGG9vdCMAHOz5omJsk9YPgGKgogEMbGuYe9ZBgCuIfI7oA8K8fMsk6UernGgkhhAhEEoCamHu63oMKFauyV3GgoAEGA6s10GmY8/mGN6HslPfvUU+j+iZxefsYzDYHT33xOw7pChNCCHEWCUBNTIophauSrgJg3s55DXOT1NGACvYth7cuhW0fgyNwpp6rVCqm3dKdYL2GzQdP8eHGg/6ukhBCiAAjAagJGt/NuT3Gt/u/5XjZce/foM0AGLfEOSus7CR8/TB8MAxy//D+veooKSqYKcM7AzBjWSbZp8r8XCMhhBCBRAJQE5Qam0qv2F5YHVY+2fVJw9wk+XJ4YB1c+yLoQiB7E/xnMHz3NFQExsako9PakJYSRbnVzlOLfm+YmXFCCCEaJQlATZRrk9TPMj+j1NpAA4E1Ohj4KEz4BS4ZCYoDNr0Db/WF3z8DPwcOtVrFjFt7YNSp2bD/JJ9uzvZrfYQQQgQOCUBN1BVJV5BiSqHYWswXe75o2JuZWsId8+DuLyGqHZTkwZd/gXk3Qv7uhr33BSTHhPDEdZ0AeGXpLo4UlPu1PkIIIQKDBKAmSq1SM67rOAA+2vkRVocP1uxpfw08tBGu/idojXBwLcwZCMun+nXrjPEDU+jdOoISs42/f/mHdIUJIYSQANSU3dD2BmKCYsgry2NZ1jLf3FRrgMFPwsObnatGO2yw/v9gdj/Y+bVfusU0ahWv3tYTvVbN6j3H+WJrjs/rIIQQIrBIAGrC9Bo9o7uMBpwLI/q05SOyDdz1Kdy1ACJaQ9ER+GwsfHwrnNzvu3pUah8byt+GdATgxSU7ySuq8HkdhBBCBA4JQE3c7R1vJ1gbzN7Te1l/dL3vK9BpODy0ydkqpNE7N1F9+zL48WWw+nY8zl8GpdCjlYmiChv/+Eq6woQQojmTANTEmQwmbu14KwAfbG+g7TEuRB/sHBf00M/Q7mqwW2DNqzA7DTJ91DUHaDVqXrutJzqNihW78vnmt6M+u7cQQojAIgGoGRjTZQxalZbNuZvZcWKH/yoS3c45U+yODyG8JRQcgk9Hwad3welDPqlCp/gwHrm6AwDPfrOD48Vmn9xXCCFEYJEA1AwkhCYwLMW5f1eDbZJaWyoVXPIn5yDpAY+CWguZS52tQWteA1vDB5IHr2xHl4RwCsqsPPvN9ga/nxBCiMAjAaiZcE2JX35oOdnFAbAgoCEUrnvRuZp0m8vBVg4/vgTvDID9PzborXUaNa/d1gOtWsXSP3L5+OdD2GXDVCGEaFYkADUTnaI6MTBxIA7FwYc7PvR3dc6I7eLcV+yW9yAkFk7ug49uhs/ugcIjDXbbbi1NPHhlOwD+uXg7A6avZPp3u9l/3H/rFQkhhPAdlSJTYc5RVFSEyWSisLCQ8PBwf1fHazYd28T9P9yPUWPkh9t+INIY6e8qeaoohJ9egc3vOrfV0IXAlU/DZQ86t93wMovNwczlmXz2Szany84sFNm7dQS3X5rEDT0SCDN6/75CCCEaxsX8/ZYAVI2mGoAURWHUklHsOrWLh3o+xIOpD/q7StU79jv873HI2ex83aILjJgJyQMb5HZmm50fd+Xz+dYcVu857u4OM+rUDOsaz+2XJtG/bTRqtapB7i+EEMI7JADVU1MNQADLspbx5JoniTRE8v1t3xOkDfJ3larncEDGJ7DiWSg76TzXY5Rz9/mwuAa7bX5RBV9tO8LnW3PYl3+mO6xlRBC39mnFbb1b0To6uMHuL4QQou4kANVTUw5ANoeNG766gSMlR/hH2j+4s/Od/q7S+ZWdgpUvwNZ0QAFDuHNNoUvvA422wW6rKAq/5RTy+ZZsvvntKMUVNvd7aSlR3H5pEtd3jydY33B1EEIIcXEkANVTUw5AAPN3zWfa5mm0Cm3FkpuXoFFr/F2lCzuyFZZMgmMZztfx3WHEvyGpb4PfusJq5/sduXyxNYd1+064tzML0Wu4vnsCt1+aRN/kSFQq6SITQgh/upi/3wExC2z27NkkJydjNBpJS0tj8+bNNV6bnp6OSqXyOIxGo8c1iqIwdepUEhISCAoKYsiQIezdu7ehv0ajMbL9SEwGEzklOaw4vMLf1amdln3gLz86xwIZTZD7B7w/BL6eAKUnG/TWRp2GP6W25KP70lj/1NU8cV1HkqODKbXY+XxrDnf8ZyNX/WsVb/24l6MFvt3eQwghRN34PQAtXLiQSZMm8eyzz/Lrr7/Ss2dPhg4dSn5+fo2fCQ8P59ixY+7j0CHPVYRfffVVZs2axZw5c9i0aRMhISEMHTqUigrZABMgWBfMXZ3vAiB9e3rj2RNLrYG+98OErZDq3OSVbR/BW32cXWQOR4NXITEiiAlXd+CnJ67ks//XnzsubUWIXsPBk2X864c9DJzxI2Pe38TXGUeosNobvD5CCCHqxu9dYGlpafTt25e33noLAIfDQVJSEo888ghPP/30Odenp6czceJECgoKqi1PURQSExN5/PHHeeKJJwAoLCwkLi6O9PR07rzzwmNemnoXGMCpilNc98V1mO1m5g6dS9/4hu9K8rpDG2HpE5BXuZpzyz7OFqLEXj6tRqnZxnfbc/l8Szabsk65z4cZtdzUM5Hb+rQiNSlCusiEEKKBNZouMIvFwtatWxkyZIj7nFqtZsiQIWzcuLHGz5WUlNCmTRuSkpL405/+xI4dZ/a3ysrKIjc316NMk8lEWlpajWWazWaKioo8jqYuyhjFyPYjAT9uklpfbfrDX1fD0GmgD3OOE3r3KucU+vLTPqtGiEHLbX1asfD/9WfNk1fx6DUdaBkRRHGFjU82Hebmtzdw7b/X8J/V+8kvklZIIYQIBH4NQCdOnMButxMX5zmtOS4ujtzc3Go/06lTJ+bOncvXX3/Nxx9/jMPhYMCAAeTk5AC4P3cxZU6bNg2TyeQ+kpKS6vvVGoWxl4xFhYq1R9ay93QjHSOl0UL/h2DCL9DtNkCBX/4Lb14KGZ+Cjxs4W0cHM+najqydfBWf3J/Gzb1aYtSp2ZdfwrTvdtN/+o/cm/4L3/1xDIut4bvshBBCVM/vY4AuVv/+/Rk7diypqalcccUVfPnll7Ro0YL//Oc/dS5zypQpFBYWuo/s7ADYK8sHWoe3ZkgbZ0tZ+o50/1amvsIT4Lb3Yew3ENMRyk7A4gfgg+shb8eFP+9larWKge1j+PeoVDb/YwjTbulO79YR2B0KP+7O58FPfiXtlRU8980Oth8p9Hn9hBCiufNrAIqJiUGj0ZCXl+dxPi8vj/j4+FqVodPp6NWrF/v27QNwf+5iyjQYDISHh3sczcX4ruMBWHpgKbml1beQNSptr4AH1sOQ50AXDIc3wJxB8P0/wFzslyqFG3Xc1a81Xz40kJWPX8GDV7YjLtzA6TIr6RsOcsOb6xj+f2uZuy6LU6UWv9RRCCGaG78GIL1eT58+fVi5cqX7nMPhYOXKlfTv379WZdjtdv744w8SEhIASElJIT4+3qPMoqIiNm3aVOsym5PuLbpzadyl2BQbn+z6xN/V8Q6tHi7/Gzy8GbrcCIodNr4Fb/WFP77webdYVe1ahPLUsM6sf+pqPhjflxHdE9Br1Ow6VsQLS3aS9soK/t9HW1ixMw+bXbrIhBCiofh9FtjChQu55557+M9//kO/fv144403+Oyzz9i9ezdxcXGMHTuWli1bMm3aNABeeOEFLrvsMtq3b09BQQGvvfYaixcvZuvWrVxyySUAzJgxg+nTpzNv3jxSUlJ45pln+P3339m5c+c5awZVpznMAqtqTc4aHl75MCG6EJbftpwwfZi/q+Rde1c4Z4udznK+TrnCOVsspoN/61WpoMzCN78d5fMtOfxRpTssJtTALb1bcnufVnSIa2I/EyGEaAAX8/fb7+v4jxo1iuPHjzN16lRyc3NJTU1l2bJl7kHMhw8fRq0+01B1+vRp/vKXv5Cbm0tkZCR9+vRhw4YN7vADMHnyZEpLS/nrX/9KQUEBl19+OcuWLatV+GmOLm95Oe0j2rOvYB+f7/mce7vd6+8qeVeHIfDQz7D+/2DtTMhaDW/3hwGPwOAnQB/i1+pFBOsZ2z+Zsf2T2Z1bxBdbcvhq2xFOlJh5d80B3l1zgJ6tTNx2aRI39UjEFCw71AshRH35vQUoEDW3FiCAxfsW88z6Z2gR1IJlty5Dr9H7u0oN41QWfPcU7P3e+dqUBGkPQFIaJPQArcG/9atktTv4abdzh/qfdudjq9yhXq9Vc90lcdx+aRKXt49BIzvUCyGEm+wFVk/NMQBZ7VaGLRpGfnk+Lwx4gZs73OzvKjUcRYHMpfDd01B4+Mx5jQESekJSP+fRqp9zdpmfnSgxs3jbEb7YmsPu3DMDuRNMRm7p3ZLb+iSREuPfViwhhAgEEoDqqTkGIHAuiPj61tdpa2rLV3/6CrWq0a2ScHEsZbD1A8haC9mboPzUudeYkqBV3zOBKL67c5C1HyiKwvYjRXyxNZvFGUcpLLe637u0TSRDLomjU1wYHePDSDQZZeVpIUSzIwGonpprACq2FHPdF9dRYi3hravf4oqkK/xdJd9RFDh1ALI3Q85myP4F8neActZMLK0RElKdu9C3qmwpCqvdkg3eZLbZWbEzn8+3ZrNmz3EcZ/1XHGrQ0iEu1BmI4sLoFB9Gh7hQWoQaJBgJIZosCUD11FwDEMDrW17ngx0f0Du2N/OGz/N3dfzLXAxHfj0TiHI2V7/Fhqm1ZyCK7w4a3w1Uziuq4JuMo/yWU8DevBL2Hy9xjxk6W2Swjo6VoahjfFhlQAolIriJjvkSQjQrEoDqqTkHoLzSPIZ9OQybw8bH139MzxY9/V2lwKEocHJ/ZSCqPPJ3Amf9J6QNcm7IWjUUhcb6rJoWm4ODJ0vJzC1mb14xmXnF7Mkr4dDJ0nNailxiwwx0iq8MRnGhdIwLo0NcGKEGv08UFUKIWpMAVE/NOQAB/HPdP/l6/9cMaT2Ef1/1b39XJ7BVFDk3Yc35pbL77BeoKDj3uog2Z8YRJfWFuG4+bSUCqLDa2Zdfwp7KULQ3r4TM3GKOFJTX+JmWEUHuYNQpPpQOsWG0jw3FqNP4sOZCCFE7EoDqqbkHoH2n93HzNzejQsW3N39Lm/A2/q5S4+FwwMl9Z1qJcn6B/F1U20rUsrfnAOvQFn6pconZxt68YmcwynUGpD15xeQXm6u9Xq2C5OiQM61FlV1pyTEh6DRNfOC8ECKgSQCqp4YKQIqi4CgtQxMa+FOWH175MGty1nB7x9uZ2n+qv6vTuFUUQs6WKq1EW8BczQaokSmVYagyFMV2de527yenSy3uMLQnr6SyK62YgjJrtdfrNCraxrgCUSgd4pzBKCkqWNYrEkL4hASgemqoAFS6cSM5jzxKxKg7iBozBl0tN3z1hy25Wxj//Xj0aj3f3/Y9MUEx/q5S0+FwwIk9nq1Ex3efe50u5NxWopBo39e3CkVROF5iZk9uZSDKLWZPvvOx1GKv9jNGnZr2sc5xRZ2qDMCWqfpCCG+TAFRPDRWAjj0zlYLPP3e+0GoJv3440ePHY+zSxWv38BZFURi9dDR/nPiDv/b4K4/0esTfVWraygvgyJYzs81ytoC56NzrotqeGUfUqh/EXuLXViIXRVE4UlDuHFdUGYwy84rZl1+C2Vb9pq6hBq17wLVM1RdCeIMEoHpqsC4wh4OS1as5NfcDyn75xX0+ZEB/osaPJ+TyywPqf/iXH1rOpFWTCNeHs/y25QTrgv1dpebD4XC2ClWdgn9iz7nX6UMrW4n6QdwlzoUbTa0gNB7U/h+PY3coHD5VdtaMtGIOHC+tcap+iF5DXLiR2HADceFG5/OwM8/jwg3EhhkJ0stAbCGEJwlA9eSLQdDlf2zn1AcfUPT992B3dh0YOnQgavx4wm8YgVrv/3VZ7A47Ny2+icPFh3m639OM7jLa31Vq3spOOWecuRZrzNkKluLqr1XrIDzxTCByH0kQkQThLcEQ6tv6V1F1qr5z8HUxe/NLOHiylNr+L1K4UXsmIFWGpTNByRmSYsMNGLQSlIRoLiQA1ZMvZ4FZco5w+qMPKfj8CxxlZQBoW7Qg8u67ibxzFBqTqUHvfyGfZX7Giz+/SGJIIv+75X9o1f7vbhGVHHZnK5FrHNGpLCjMgaIjoFQ/HsdDUOSZUFTdY2icz1uRKqx2jhaUk1dkJr+4gryiCvKLzOQVmyufV5BbVEGFtfputepEBusqQ5KRuKoBqUqLUkyoQWawCdEESACqJ39Mg7cXFVHw2Wec+vAjbPn5AKiCg4m49Vai7hmLvlUrn9TjbBW2CoYuGsqpilPMGDSD69te75d6iItgt0FJrjMMFeZAYfaZ5wWVz6ubhXY2VytSROuzWpGqhCS972c0KopCsdlGflEFeUXOYOR6dIYms/vRUsP4o7OpVBAdoic2zBmI3IEp3EBc2JmgFB1qkBltQgQwCUD15M91gBSLhaLvvuPk3A8wZ2Y6T6rVhF13HdH3jieoRw+f1gdgzm9zmJ0xmy5RXVh4w8KAGqck6qiiEAqPVAlIVUJSYQ4UHa1lK1LUWa1HrZxdbK7XIbF+G4ukKAqF5dYqIamC/OIzz/OKzORXnqtpPNLZ1CpoEebqbqsSllznKl9HBetRS1ASwuckANVTICyEqCgKpRs2cGruB5SuX+8+H3RpH6LHjyf0qqtQ+egPS0FFAdctuo5yWznvXvsu/RP7++S+wo/sNig+Vn0rkut1dbPUzqbWgallZSCqZjySqaVfWpGqcjgUTpVZKrvaKs5pWXJ1xR0vNte4lcjZtGoV0aF6IoP1mIJ0RATrnM+DdUQE6YkMdp4zBemJDHGeiwjWyQrbQtSTBKB6CoQAVFVFZianPkin8H//A6tzETp9cjJR48ZhGvkn1EZjg9dh2qZpzN89nwGJA/jPtf9p8PuJRqCi8NyAVFAlKBUfBaUWXVDB0Z6tSGHxzpal4OjKo/J5UCSo/RcQ7A6FkyXmKt1tnt1ursB0stRc64HcZzPq1O4wZApyhqaIYB2mygAVURmmIirPS3ASwpMEoHoKtADkYs3L4/THH3N6wUIcxc7ZP5rISCL//Gci/3wX2uiGWyQvpziHEV+NwKE4+PzGz+kc1bnB7iWaCI9WpGq62Qqya57FVi0VBEVUE45cASkwQpPV7uB4sZlTpRYKyqycLrNQUG6lsMzC6TIrBWVWCstdzy0UljvP1bYbrjpVg1PVYHQmKFV57mqNCpLgJJoeCUD1FKgByMVeUkrhl4s4lT4P69GjAKgMBkx/+hNR48ZhaJvSIPedvHoy3x38jhFtRzB90PQGuYdoZsoLzmpFyoaS41B2EspPOR/LTjpbm+qkcYQmRVEoMdsoqAxIBeWWyueVj+XOIFVYzXN7PYNT1W66iMouOVNlgIqsbIkKNegIM2oJM2oJNWoJN+owaNUyHlAEHAlA9RToAchFsdkoXr6ck+/PpWL7dvf50Kuvdg6Y7tPHq/8DtfPkTkYtGYVGpWHpLUtJDE30WtlCnJfdBuWnzw1GZSed6yOVnWp2oQnOzIgrrAxO1bU2eYSpytamgjJLrccz1USrVrkDUZhBVxmMtIQatIQZna/DjFrCKl+HVXnPHaYMWrSy/IDwIglA9dRYApCLoiiUb9nCybkfUPLTT+7zxu7dib53PGHXXotK6531e+7/4X42HdvE3V3u5ql+T3mlTCEahL9DU1AEGMLBGF7lMQwMpnPP6UOdc/F9xOFQKLHYKCg9E5BOV+mOq9rCVFBmocRso6TCRnGFjRKLrc5jnKoTpNOcE5acQakyXBl15w1WoUYtIXqNtEYJQAJQvTW2AFSV+cABTqXPo3DxYhSLBQBdy5ZE3TOWiFtvRR1Svxk364+s54EVDxCkDWL5bcsxGfy7UKMQXlVjaDrl+eiV0FSFSn1uODKEnRWUXOdM1ZyrfO6DViiHQ6HUYqPE7AxEzsPqfl1S+bqownWN53vO89aLWszyQtQqCDE4u+bODk+usBRq0BJi0BJi0BCsd74O1msIqXwMNWgJNmgJ1mlkCYNGTAJQPTXmAORiO3mS05/M5/T8+dgLCgBQh4cTOWoUkXffjS4utk7lKorCbd/exp7TexjcajC3dLiF/gn9ZZ8w0XzVFJrKC5xLBVQUVXksdi5CWfVcbdZbqi196FmtTWe3QIXXcK5KsNL6Zhseq93hblUqNlvPhCeztUpQqgxQ7usqg1Tl9cUVtnqNgapJsN4ZkkIMGkL0Z0LTmddnwlOIXkOwoYZAVfmZIJ20UPmKBKB6agoByMVRXk7h119z6oN0LIcOOU/qdJhGjCBq/HiMnTpedJmuTVJdtGotl8ZdyqCWg7i81eWkhKfIf+xC1IaigLXMGYzcoajQ+ehxrup7xecGK7vZe3XSGs9qWQoDfZhzvSb3EVr9c0PYuec1+gbr3lMUhQqrwzNAVQakorNeF1fYKLPYKTXbKLU4n5eYbZSZ7ZRabJSabfUeF1UTlQpC9FVCkytQuUOUlmCDZ2hytlJVCV6u6yrDmVEng9CrIwGonppSAHJRHA5KfvqJk3M/oHzrVvf5kMsvJ/re8QT3739R/zFtyd3CisMrWJOzhuzibI/3WoW2YlCrQQxqOYi+8X0xaht+nSIhmjWbuTIwFXqGo+qClbsl6qwQZS1tmLqptecPTfrQs15f6NoQ0AV5PVQpioLZ5qDUXCUcWWyUml2hyU5ZZddf1dBUarFTZq68zlIlZFW+15CCdBqC9RqC9K5HZxdekOucrsp5vbMlynVtjed1WoL0GvTaxjk4XQJQPTXFAFRVeUYGJz9Ip3j5cnA4++ENnToRfe94wocPR3WRO9EfKjrE2py1rD2yll9yf8HqsLrfM2gM9Ivvx6BWg7i85eUkhSV59bsIIbzEbnOuy3R2q5O5GCylVY6SGh7Pem6raLi6qtQXCE1nvw4DfTDoXEfQmSB19jkvjqNyOBQqbGe3NFUGJXN1rVFVg5bd/bq0ShgrtzZsqHLRqlUewSjI3fqkwairEqJ0WncI8wxkNZ8P0mkabE89CUD11NQDkIslO5tT8z6kYNEilPJyALRxcUSNuZuIO+5AU4fvXmYtY3PuZtbmrGXNkTXkluZ6vJ9iSmFQy0EMajWI3rG90Wt8M95ACOFjdpuzVenscGQuOSs0nSdEuV9XnrOWNXy9NfqzQlHV4OSFc/VsvbI7FMqtdsotzqPM6gxQ5Ra789Fqp7wyVNV0vtxqd79fYXUGLte19VmQ82IYtGr+Orgtj1/XyavlSgCqp+YSgFzsBQWcXrCQU598jP34CQDUwcFE3H47UWPHoGvZsk7lKorC/oL9rD3ibB3alrcNm2Jzvx+sDeayhMvcrUPxIfFe+T5CiCbKYXeGoAsGp6phq8pra7nz8+6jHCyVz/Hhn8LzBqXKVqnzndMaQWcEbdCZUKU1VnkMBo2uTkHLYnM4w1XVYGQ9E6bKzwpc1YWoMoudMqudisqAVjWEVU0cj17dnkkSgAJLcwtALg6LhaJvl3Dyg7lY9u13ntRoCB86lKh77yWoW9d6lV9sKebnYz+7u8tOlJ/weL9jZEd361DPFj3Rqr2zdpEQQpyXoji77FwByVJWc1Cq8Vx1n61yzpsD1WtDpa4MSMYzj7qgas4FnxWeqgtUQdV/tmoA0+guWCXXoHVXuArRa4kM8W4vgASgemquAchFURRK163j5Ny5lG382X0+uF8/osaPI/SKK+q9E71DcZB5KtPZOpSzlt9P/I6jysaZYbowBrQcwKCWgxjYciAxQTH1up8QQviVq/XKIyiVO7sJLxSeql7nGl9lrQBbeZXHysOXLVlVqTSeLVA647mtUmeHp7ZXQMehXq2GBKB6au4BqKqKnTs5+UE6Rd99BzZn95W+bVuixo8jfNgwNGFhXrlPQUUBG45uYO2Rtaw7so4Cc4HH+12ju7pnlnWN7orGj7uCCyFEQFIUsFucQcjdolV+VlCqqOFc2ZnPeHy2oprHsjOfrY/LJ8GQZ73z3Ss1ugA0e/ZsXnvtNXJzc+nZsydvvvkm/fr1q/ba9957jw8//JDtlXtf9enTh1deecXj+nHjxjFv3jyPzw0dOpRly5bVqj4SgM5lPXaMUx99TMHChThKK6fLqlQY2rcjKDWVoNReBPVKRZ+cXO/WIbvDzo6TO9ytQztO7vB4P9IQycCWAxnUchADEgcQYYyo1/2EEELUgaI4l2Co2gLl0TpVQ4hyBbCUwdB+iFer1KgC0MKFCxk7dixz5swhLS2NN954g88//5zMzExiY89drXj06NEMHDiQAQMGYDQamTFjBl999RU7duygZeVg3XHjxpGXl8cHH3zg/pzBYCAyMrJWdZIAVDN7SQkFn39BwYIFZxZWrEJtMhGU2pPg1FSCevUiqHv3em+/caL8BOuPrGftkbVsOLKBYmvxmfup1PSI6eFuHeoc1VkWBxNCiGaqUQWgtLQ0+vbty1tvvQWAw+EgKSmJRx55hKeffvqCn7fb7URGRvLWW28xduxYwBmACgoKWLx4cZ3qJAGodmwnTlCekUF5RgZlGRlU/LEdxXzWQD+1GkPHjgT1SnWGotRUdK1b1zmkWB1Wfj/+u3ua/d7Tez3ebxHUgstbXs6gVoO4LOEywvTe6aITQggR+BpNALJYLAQHB/PFF18wcuRI9/l77rmHgoICvv766wuWUVxcTGxsLJ9//jk33HAD4AxAixcvRq/XExkZydVXX81LL71EdHR0tWWYzWbMVf5wFxUVkZSUJAHoIikWCxWZmZRv2+YORbajx865ThMV5ew2qwxFxm7dUAcF1emeuaW57q6yn4/9THmVPmmtSkuvuF7OmWUtB9Euop20DgkhRBPWaALQ0aNHadmyJRs2bKB///7u85MnT2b16tVs2rTpgmU89NBDfP/99+zYsQOj0bnlwoIFCwgODiYlJYX9+/fz97//ndDQUDZu3IhGc+7g2eeee47nn3/+nPMSgOrPmpdH+TZnK1H5tm1U7NyJYrV6XqTVYuzc2SMUaRMTLzqsWOwWtuZtdQeig0UHPd5PCElwT7PvF99PNnAVQogmptkEoOnTp/Pqq6+yatUqevToUeN1Bw4coF27dqxYsYJrrrnmnPelBch3HGYzFTt2urvOyrdtw3b8+DnXaVu0cI4hquw2M3a9BLXBcFH3yi7Kdi/C+EvuL5irrMOhU+voG9+XQS0HkRqbSltTWwlEQgjRyF1MAPLrSnMxMTFoNBry8vI8zufl5REff/5Vgf/1r38xffp0VqxYcd7wA9C2bVtiYmLYt29ftQHIYDBguMg/rqJu1AYDwb17Edy7F+Bcc8h29ChlGRnulqKK3buxHT9O8Q8/UPzDDwCodDqMl1xyJhT1SkUXF3feeyWFJ/Hn8D/z5y5/ptxWzi+5v7gXYTxScoQNRzew4egG9/WJIYm0jWhL+4j2tDVVPka0JURXv0HcQgghAk9ADILu168fb775JuAcBN26dWsmTJhQ4yDoV199lZdffpnvv/+eyy677IL3yMnJoXXr1ixevJibbrrpgtfLIGj/cpSXU7F9u0cosp86dc512sQE98DqoF69MHbujEpXu9VIs4qyWJuzlg1HN5B5KpOTFSdrvD4+JJ52Ee1oZ2rnDkVtTW1lgLUQQgSYRtMFBs5p8Pfccw//+c9/6NevH2+88QafffYZu3fvJi4ujrFjx9KyZUumTZsGwIwZM5g6dSrz589n4MCB7nJCQ0MJDQ2lpKSE559/nltvvZX4+Hj279/P5MmTKS4u5o8//qhVS48EoMCiKArW7GzKt21zhqKM3zBnZrp3sndRGQwYu3c7E4pSU9HG1G4F6YKKAg4UHmBfwb4zjwUHOF5+bvecS1xwHO0i2rlbi9pFtKNtRFvC9fI7I4QQ/tCoAhDAW2+95V4IMTU1lVmzZpGWlgbAlVdeSXJyMunp6QAkJydzqJr1Z5599lmee+45ysvLGTlyJNu2baOgoIDExESuu+46XnzxReIu0GXiIgEo8NlLSqnY/odzttm2bVRk/Ia9sPCc63RJSR6Dqw0dO6LS1r7nt9BcyIHCA+wv2H/mKNxPfll+jZ+JDYo905UW0ZZ2pna0i2iHyWCq03cVQghRO40uAAUaCUCNj6IoWLIOuqfgl2dsw7xvP5z1660KDiaoe3d3KArq2RNtLRfIrKrIUsSBggPuQHSgwNlqlFeWV+NnYoJi3GHIfZjayUrWQgjhJRKA6kkCUNNgLy6m/Lffz4Si337DUVJyznXaFi3QtWqFLqkV+lat0LVsha5VK/StWqKNj0dVzdIJNSmxlHi0GO0rdHalHSs9dz0klyhjlHvgddVwFGWMqtP3FkKI5koCUD1JAGqaFIcD8759ldPvnYOrLVlZ5/+QVosuMRF9q5buYKRr1RJ9UhK6Vq3QREbWar2iUmups8Wo8ExX2oHCAxwpOVLjZyINkee0FrWNaEu0MVoWdBRCiGpIAKonCUDNh72wEMvhw1izs7HkHMGak4M1JwfLkRysR4/B2Ys2nkUVHIy+ZcvKYNQKfVJlSGrpbEG60D5oZdYysgqz2Fewz6Mr7XzBKMIQcU5rUTtTO2KCYiQYCSGaNQlA9SQBSAAodju2vDwsOTlYXeHoSI47KNnyah7v46KJjESXlHRuC1KrVugSElDp9dV+rsxaRlZR1plxRpVjjXKKc1Co/j9Zo8ZIbHAsscGxxIXEOR+D486cC44jJigGrdqvy38JIUSDkQBUTxKARG04zGasR45iPVLZauQKStnZWI4cwVHNrDQPajXa+Dj01XSt6Vq2QtsiBpVa7fGRClsFWYVZ53SlZRdn41AcNdzoDBUqooOiPcLR2SEpNjiWUH1off5phBDCLyQA1ZMEIOEN9uLiaoJR5fMjR1AqKs77eZVej66ye02f1OqcFiSN6cy0erPdTF5pHnlleeSX5buPqq+Plx3HpthqVfdgbbC7JalqQKoakqKN0WjUtR8gLoQQDU0CUD1JABINTVEU7CdOVOley/bsasvNBbv9vGWow8OdYagyGGnjYtFGRaGJjEITGYk2KhJNVBTqyk2CHYqDUxWnnKGo9NyA5DqKrcW1+g4alYbooGjig+M9AtLZrUqyx5oQwlckANWTBCDhb4rVijUvr3JwdpVglJOD5cgR7CdO1LosVXAw2khnGNJERaKtDEiaqEh3YHKFJU1UFBV6Ffnl1bciuV6fKD9Rqy43gDBdmHtMUnUBKTY4lihjFGqV+sKFCSHEeUgAqicJQCLQOcrKsB454hGObCdOYD99Ctup09hPncJ2+vQFZ7FVR6XTVQakymAUGXXW80hUEeEUB6s5abCSry0jr+J4tV1vZbayWt1Tq9YSG+QMQ9FB0UQYIgg3hGPSmzAZTEQYIjAZTITrw93PjVrjRX83IUTTJgGoniQAiaZAURQcJSXYT53Cfvq0MxidPoXt1Cns7pBU5XlBAUpZ7QKLB7UaTUTEmdalqCg0kRFoo6KwhYdQEqLmdJCdkwYrufpyjmpKyLWcCUwny0/WOLPtfAwaAyaDMyCZ9FVCkqEyJFWGp6rXSHASommTAFRPEoBEc+UoL/cIS/ZTZ1qU7AWnzzyvbGFyFBXV6T7qsDB3YFJHRmAND6Y8VEdRsIoSo0Kx3k6h1kqBxsxpjZmTmjLyVSUcV4ooshTXejB3dYwao7N1ydWyVE1QcrdAVWl9MmguvJGyEMK/LubvtywIIoRwUwcFoQ4KQpeYWKvrFasV2+nT2E+f9mxpOrt1yfW8oAAcDhzFxTiKi7EeOuwuSwNEVh41V1CNOjQUVUgESrARe7ABW5AOi1FLhUFNuR5K9Q6KdXaKdDZngNJWcEJdznFVCSV6B+WGco7bys+7oW11jBpjtS1KrsMVplwtUGH6MEJ0IQRrg2W2nBABSAKQEKLOVDoduthYdLGxtbpecTiwFxa6A5O7O67K2CV7cRGOklIcJSXOLrzSUhzFxeBwOMNTURFUtjypAF3lcf41t6upS7ARe9CZAGU2qikzQJlOqQxQVgq0Vk5rKiqDUxnlhnLK9LmcMkC5HsoN4FBfePXtIG0QwdpgQnQhzlCkq3yurfK86nvas65zvacNJkgbJCt+C+EFEoCEED6jUqvRRkaijYyEtm1r/TlFUVAqKrAXFzvDUWllOCopOROWqjlnLyn2DFMlJWBzdp+pyirQllWgBeozKsim12IN0lBh0FBugFK9QoneQYnGSoVOwawFs64Ei64Ui/Y4Zh2V56BIB2adCkvla/ejzvlYXbhSq9QEa4M9QtTZYalqiDrnPa1nqNJrql+NXIimTgKQECLgqVQqVJXdc9SusalaiqKgWCwegcgjUBUXewQqj4BVUoK99MxrxWwGQGuxobXYCOIC3Xd1GOht04ClMiBVaBVnMNKCWWfFoit0hyZLlVBl0akorhKkXKGqatCq+p7doCXIEFp9a1Rl0DJqjBi1zsOgMRCkDcKgMWDUGgnSBGHQOp+7r9OcuVa2XhGBSn4zhRDNhkqlQmUwoDYYIDq6XmUpFouze64yHJ0TqEpLcVRUoFRU4CivwFFRjlJhdj6WVzjfKy/HUVFx5pzZjFJeDpVzU7R20NoVzl1K8nxh6mKDlh2b2oxZd9KjFcr53BmarFpnGDNroUTjfG3VVAY0rQpb5Wtr1fe0YNGAotOg1htRGfSo9QY0BiNagxGNMQitwYjOEILOaMSoDfIIVlVDV9VA5RG+qjw3aAyylpS4KBKAhBCiDlR6PVq9HiLP3+5zsVytVO5wVF7uDFFVwpRSUV4lVFWcG7SqBqzKUOURtCrfc9E6QGuGEPM5talNjS/wvgO48HpUlsrQVDVEuYJUuQaKtSrPgFX1uspHRadF0etAp0Wt14Ne7wxeOgMagwG1To9Kp0OrN6LWG9Dq9M5ApjOg0RvR6Q1oDUHo9UFoDEb0eiMGXRB6tR6dRodBY0Cv0TsPtfPRoDGgU+vQa/TS2tXIyE9LCCECiKuVCoOBhpw7VmPQcgWsCrM7aClWi/Nai8UZqCxW92vFYnaet1hQzGeus5srcJgrsFe+73oPqxWsNlRWz6UM9HbncZ4a1+JbWalN2LoYdpUzbNk1UK6G4srwZVd7Pjqfq3Bo1Tg0ahStGkWrcR4aDeg0oNU6D50WlVaLSqdDpdWh0utQ63TOoKbTo9br0egNaLRVAprBgFZnRKd3vtYaDGi1BjR6AzqdAa3eiK7yfV3lc70+CI1WJ4PmayABSAghmiFfBa2aKA4HirUySJnNZwKWKyy5QpfZ7DxnsTiDl+taqzOMOcxmbOZyrOZybBXl2M0V7vDlsJhxuIKXxYJis4HNDjYbKpvdedgdqGx21DYHarsD1Vk5S6OAxgbUaukpBbBXHr7hAMyVR01samdQc2hU7keHWuUMaprKR7UKRaN2Hlo1ilqDolWDRgNajftRpdGi0jjDnKrKodbqnI86HWqNK9Dp0Gj1zkedAY3rUatDqzMQ1qELUV1TffMPVQ0JQEIIIXxOpVa7AxhhYf6uDuBsFcNuR7HZnOHMZkOxWMFmPfPaavV4z2Y1YzWXYbOYnSHMUuE8rGbs5gpsFjN2qwWH+9GCw2bFYbVUKcuKYrU5W8cqAxqugFZ5qO0Od0hT2xVUDgWNXUHt4MxjDY1kWofzwOa6wPXou6Dm4oqHFmD7jamMeO1Tn9fBRQKQEEIIgbNVzNWygbHxbZmiOBwoNhtWSwVWa8WZR7Pz0WYxY7OZsVnNzudWM3arGZvVgsNqwW6zYLdasFutzrBms+KwWXBYrThsNhSbFYfVimKvfF4Z1lwta4rdBna7M7zZHc5Hh7OFDXtlC5vdgcquoHY4IN674+culgQgIYQQoglQqdWo9HoMej0GZBunC5E5g0IIIYRodiQACSGEEKLZkQAkhBBCiGZHApAQQgghmh0JQEIIIYRodiQACSGEEKLZkQAkhBBCiGZHApAQQgghmh0JQEIIIYRodgIiAM2ePZvk5GSMRiNpaWls3rz5vNd//vnndO7cGaPRSPfu3Vm6dKnH+4qiMHXqVBISEggKCmLIkCHs3bu3Ib+CEEIIIRoRvweghQsXMmnSJJ599ll+/fVXevbsydChQ8nPz6/2+g0bNnDXXXdx3333sW3bNkaOHMnIkSPZvn27+5pXX32VWbNmMWfOHDZt2kRISAhDhw6loqLCV19LCCGEEAFMpShKDfvH+kZaWhp9+/blrbfeAsDhcJCUlMQjjzzC008/fc71o0aNorS0lCVLlrjPXXbZZaSmpjJnzhwURSExMZHHH3+cJ554AoDCwkLi4uJIT0/nzjvvvGCdioqKMJlMFBYWEh4u+6kIIYQQjcHF/P32awuQxWJh69atDBkyxH1OrVYzZMgQNm7cWO1nNm7c6HE9wNChQ93XZ2VlkZub63GNyWQiLS2txjLNZjNFRUUehxBCCCGaLr8GoBMnTmC324mLi/M4HxcXR25ubrWfyc3NPe/1rseLKXPatGmYTCb3kZSUVKfvI4QQQojGQevvCgSCKVOmMGnSJPfrwsJCWrduLS1BQgghRCPi+rtdm9E9fg1AMTExaDQa8vLyPM7n5eURHx9f7Wfi4+PPe73rMS8vj4SEBI9rUlNTqy3TYDBgMBjcr13/gNISJIQQQjQ+xcXFmEym817j1wCk1+vp06cPK1euZOTIkYBzEPTKlSuZMGFCtZ/p378/K1euZOLEie5zy5cvp3///gCkpKQQHx/PypUr3YGnqKiITZs28eCDD9aqXomJiWRnZxMWFoZKparz92vKioqKSEpKIjs7WwaKBwD5eQQW+XkEFvl5BJaG/HkoikJxcTGJiYkXvNbvXWCTJk3innvu4dJLL6Vfv3688cYblJaWMn78eADGjh1Ly5YtmTZtGgCPPfYYV1xxBTNnzmTEiBEsWLCALVu28O677wKgUqmYOHEiL730Eh06dCAlJYVnnnmGxMREd8i6ELVaTatWrRrk+zY14eHh8j8oAUR+HoFFfh6BRX4egaWhfh4Xavlx8XsAGjVqFMePH2fq1Knk5uaSmprKsmXL3IOYDx8+jFp9Zqz2gAEDmD9/Pv/85z/5+9//TocOHVi8eDHdunVzXzN58mRKS0v561//SkFBAZdffjnLli3DaDT6/PsJIYQQIvD4fR0g0TjJWkmBRX4egUV+HoFFfh6BJVB+Hn5fCVo0TgaDgWeffdZj8LjwH/l5BBb5eQQW+XkElkD5eUgLkBBCCCGaHWkBEkIIIUSzIwFICCGEEM2OBCAhhBBCNDsSgIQQQgjR7EgAErU2bdo0+vbtS1hYGLGxsYwcOZLMzEx/V0tUmj59unshUOE/R44c4e677yY6OpqgoCC6d+/Oli1b/F2tZslut/PMM8+QkpJCUFAQ7dq148UXX6zVPlGi/tasWcONN95IYmIiKpWKxYsXe7yvKApTp04lISGBoKAghgwZwt69e31WPwlAotZWr17Nww8/zM8//8zy5cuxWq1cd911lJaW+rtqzd4vv/zCf/7zH3r06OHvqjRrp0+fZuDAgeh0Or777jt27tzJzJkziYyM9HfVmqUZM2bwzjvv8NZbb7Fr1y5mzJjBq6++yptvvunvqjULpaWl9OzZk9mzZ1f7/quvvsqsWbOYM2cOmzZtIiQkhKFDh1JRUeGT+sk0eFFnx48fJzY2ltWrVzN48GB/V6fZKikpoXfv3rz99tu89NJLpKam8sYbb/i7Ws3S008/zfr161m7dq2/qyKAG264gbi4ON5//333uVtvvZWgoCA+/vhjP9as+VGpVHz11VfuLakURSExMZHHH3+cJ554AoDCwkLi4uJIT0/nzjvvbPA6SQuQqLPCwkIAoqKi/FyT5u3hhx9mxIgRDBkyxN9Vafa++eYbLr30Um6//XZiY2Pp1asX7733nr+r1WwNGDCAlStXsmfPHgB+++031q1bx/Dhw/1cM5GVlUVubq7H/26ZTCbS0tLYuHGjT+rg973AROPkcDiYOHEiAwcO9NiHTfjWggUL+PXXX/nll1/8XRUBHDhwgHfeeYdJkybx97//nV9++YVHH30UvV7PPffc4+/qNTtPP/00RUVFdO7cGY1Gg91u5+WXX2b06NH+rlqzl5ubC+De99MlLi7O/V5DkwAk6uThhx9m+/btrFu3zt9Vabays7N57LHHWL58uWz0GyAcDgeXXnopr7zyCgC9evVi+/btzJkzRwKQH3z22Wd88sknzJ8/n65du5KRkcHEiRNJTEyUn4eQLjBx8SZMmMCSJUv46aefaNWqlb+r02xt3bqV/Px8evfujVarRavVsnr1ambNmoVWq8Vut/u7is1OQkICl1xyice5Ll26cPjwYT/VqHl78sknefrpp7nzzjvp3r07Y8aM4W9/+xvTpk3zd9Wavfj4eADy8vI8zufl5bnfa2gSgEStKYrChAkT+Oqrr/jxxx9JSUnxd5WatWuuuYY//viDjIwM93HppZcyevRoMjIy0Gg0/q5iszNw4MBzlobYs2cPbdq08VONmreysjLUas8/cxqNBofD4acaCZeUlBTi4+NZuXKl+1xRURGbNm2if//+PqmDdIGJWnv44YeZP38+X3/9NWFhYe5+WpPJRFBQkJ9r1/yEhYWdM/4qJCSE6OhoGZflJ3/7298YMGAAr7zyCnfccQebN2/m3Xff5d133/V31ZqlG2+8kZdffpnWrVvTtWtXtm3bxuuvv869997r76o1CyUlJezbt8/9Oisri4yMDKKiomjdujUTJ07kpZdeokOHDqSkpPDMM8+QmJjoninW4BQhagmo9vjggw/8XTVR6YorrlAee+wxf1ejWfv222+Vbt26KQaDQencubPy7rvv+rtKzVZRUZHy2GOPKa1bt1aMRqPStm1b5R//+IdiNpv9XbVm4aeffqr2b8Y999yjKIqiOBwO5ZlnnlHi4uIUg8GgXHPNNUpmZqbP6ifrAAkhhBCi2ZExQEIIIYRodiQACSGEEKLZkQAkhBBCiGZHApAQQgghmh0JQEIIIYRodiQACSGEEKLZkQAkhBBCiGZHApAQQgghmh0JQEIIUQcHDx5EpVKRkZHh76oIIepAApAQwq+OHz+OXq+ntLQUq9VKSEiI7J4uhGhwEoCEEH61ceNGevbsSUhICL/++qt7o0QhhGhIEoCEEH61YcMGBg4cCMC6devczy/kv//9L126dMFoNNK5c2fefvtt93uu7qkFCxYwYMAAjEYj3bp1Y/Xq1R5lrF69mn79+mEwGEhISODpp5/GZrO533c4HLz66qu0b98eg8FA69atefnllz3KOHDgAFdddRXBwcH07NmTjRs3ut87dOgQN954I5GRkYSEhNC1a1eWLl160f9GQogG4LNtV4UQotKhQ4cUk8mkmEwmRafTKUajUTGZTIper1cMBoNiMpmUBx98sMbPf/zxx0pCQoKyaNEi5cCBA8qiRYuUqKgoJT09XVEURcnKylIApVWrVsoXX3yh7Ny5U7n//vuVsLAw5cSJE4qiKEpOTo4SHBysPPTQQ8quXbuUr776SomJiVGeffZZ930mT56sREZGKunp6cq+ffuUtWvXKu+9957HPTp37qwsWbJEyczMVG677TalTZs2itVqVRRFUUaMGKFce+21yu+//67s379f+fbbb5XVq1c30L+qEOJiSAASQvic1WpVsrKylN9++03R6XTKb7/9puzbt08JDQ1VVq9erWRlZSnHjx+v8fPt2rVT5s+f73HuxRdfVPr3768oyplwMn36dI97tmrVSpkxY4aiKIry97//XenUqZPicDjc18yePVsJDQ1V7Ha7UlRUpBgMBnfgOZvrHv/973/d53bs2KEAyq5duxRFUZTu3bsrzz333EX+6wghfEHr1+YnIUSzpNVqSU5O5rPPPqNv37706NGD9evXExcXx+DBg8/72dLSUvbv3899993HX/7yF/d5m82GyWTyuLZ///4e97z00kvZtWsXALt27aJ///6oVCr3NQMHDqSkpIScnBxyc3Mxm81cc801561Pjx493M8TEhIAyM/Pp3Pnzjz66KM8+OCD/PDDDwwZMoRbb73V43ohhP9IABJC+FzXrl05dOgQVqsVh8NBaGgoNpsNm81GaGgobdq0YceOHdV+tqSkBID33nuPtLQ0j/c0Go3X6hgUFFSr63Q6nfu5K0w5HA4A7r//foYOHcr//vc/fvjhB6ZNm8bMmTN55JFHvFZPIUTdyCBoIYTPLV26lIyMDOLj4/n444/JyMigW7duvPHGG2RkZJx3oHBcXByJiYkcOHCA9u3bexwpKSke1/7888/u5zabja1bt9KlSxcAunTpwsaNG1EUxX3N+vXrCQsLo1WrVnTo0IGgoCBWrlxZr++alJTEAw88wJdffsnjjz/Oe++9V6/yhBDeIS1AQgifa9OmDbm5ueTl5fGnP/0JlUrFjh07uPXWW93dSOfz/PPP8+ijj2IymRg2bBhms5ktW7Zw+vRpJk2a5L5u9uzZdOjQgS5duvDvf/+b06dPc++99wLw0EMP8cYbb/DII48wYcIEMjMzefbZZ5k0aRJqtRqj0chTTz3F5MmT0ev1DBw4kOPHj7Njxw7uu+++Wn3PiRMnMnz4cDp27Mjp06f56aef3AFMCOFfEoCEEH6xatUq+vbti9FoZO3atbRq1apW4QecXUvBwcG89tprPPnkk4SEhNC9e3cmTpzocd306dOZPn06GRkZtG/fnm+++YaYmBgAWrZsydKlS3nyySfp2bMnUVFR3Hffffzzn/90f/6ZZ55Bq9UydepUjh49SkJCAg888ECtv6Pdbufhhx8mJyeH8PBwhg0bxr///e9af14I0XBUStX2XyGEaAIOHjxISkoK27ZtIzU11d/VEUIEIBkDJIQQQohmRwKQEEIIIZod6QITQgghRLMjLUBCCCGEaHYkAAkhhBCi2ZEAJIQQQohmRwKQEEIIIZodCUBCCCGEaHYkAAkhhBCi2ZEAJIQQQohmRwKQEEIIIZqd/w+Jfnj2ATZeEQAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Set model to evaluate mode\n",
        "model.eval()\n",
        "\n",
        "correct = 0\n",
        "total = 0\n",
        "\n",
        "# Iterate over data.\n",
        "for images, labels in test_loader:\n",
        "\n",
        "    # put images on proper device (GPU)\n",
        "    images = images.to(device)\n",
        "    labels = labels.to(device)\n",
        "\n",
        "    # No need to flatten the images here !\n",
        "\n",
        "\n",
        "    # Forward\n",
        "    outputs = model(images)\n",
        "    _, predicted = torch.max(outputs.data, 1)\n",
        "\n",
        "    # Statistics\n",
        "    total += labels.size(0)\n",
        "    correct += torch.sum(predicted == labels.data)\n",
        "\n",
        "print('Accuracy on the test set: {:.2f}%'.format(100 * correct / total))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yNKmcyL4Z70P",
        "outputId": "8319867d-7637-4414-9b3d-479120dda36f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy on the test set: 97.68%\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Reproducibility\n",
        "\n",
        "We have seen that there is place for a lot of randomness in machine learning experiments, specifically when:\n",
        "- splitting an original dataset into training/validation/test sets.\n",
        "- initializing the parameters of a model.\n",
        "- splitting a training set into batches to train a model.\n",
        "\n",
        "Therefore, we normally get different results each time we run the same experiment. To allow reproducibility of your results, it is required to fix the **random seed** before creating each dataset and model. Hence, to be reproducible it is best practice to manually set:\n",
        "\n",
        "1. Python pseudorandom number generator at a fixed value:\n",
        "```\n",
        "import random\n",
        "random.seed(seed_value)\n",
        "```\n",
        "\n",
        "2. NumPy pseudorandom number generator at a fixed value:\n",
        "```\n",
        "import numpy as np\n",
        "np.random.seed(seed_value)\n",
        "```\n",
        "\n",
        "3. PyTorch pseudorandom number generator at a fixed value for all devices (both CPU and GPU):\n",
        "```\n",
        "import torch\n",
        "torch.manual_seed(seed_value)\n",
        "```\n",
        "\n",
        "4. PyTorch pseudorandom number generator at a fixed value for the GPU(s):\n",
        "```\n",
        "import torch\n",
        "torch.cuda.manual_seed(seed_value)  # Current GPU.\n",
        "torch.cuda.manual_seed_all(seed_value)  # All GPUs.\n",
        "```\n",
        "\n",
        "5. CuDNN algorithms (an extension of CUDA for deep learning) to be deterministic in PyTorch:\n",
        "```\n",
        "import torch\n",
        "torch.backends.cudnn.deterministic = True\n",
        "torch.backends.cudnn.benchmark = False\n",
        "```\n",
        "\n",
        "Note that deterministic algorithms can make computations dramatically slower. While manually fixing random seeds helps reproducibility, completely reproducible results are not guaranteed across PyTorch releases and different platforms, devices or drivers.\n",
        "\n",
        "Furthermore, more randomness comes in when doing hyperparameter tuning or using multiple GPU devices in parallel, but that's beyond the scope of this tutorial.\n",
        "\n",
        "Finally, a good practice, implemented in Scikit-Learn, is to create a local RandomState object instead of using the global RandomState object and to pass it to every module using randomness. However, the Pytorch API does not allow it, and for now, using global RNGs is recommended."
      ],
      "metadata": {
        "id": "xy0h7_0Iam4p"
      }
    }
  ]
}
