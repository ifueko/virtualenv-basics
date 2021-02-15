# Virtual Environment Basics for Machine Learning in Python

### View the main tutorial in Colab [here](https://colab.research.google.com/drive/1Zw7sfAjcJgZDnmwwntOWQsHMQGXLpPIi?usp=sharing)!

### Using the Virtual Environment

To use the virtual environment package, ensure that you have `python3 python3-pip` installed on your system and `virtualenv` installed with `pip3`.

To create a virtual environment, use the path `virtualenv <path-to-venv-dir>`, for example, `virtualenv venv` is quite common usage.

After, source your environment, install requirements using any `requirements.txt` files, and you will be good to go. 
To exit a virtual evironment, simply type `decativate` into your terminal.

Example usage:
```
git clone git@github.com:ifueko/virtualenv-basics.git
cd virtualenv-basics
virtualenv venv
source venv/bin/activate
cd dcgan
pip intall -r requirements.txt
python main.py --dataset fashionmnist

```
