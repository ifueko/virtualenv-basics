import torchvision
import torchvision.datasets as datasets
import argparse

parser = argparse.ArgumentParser(description="Download Torchvision Datasets by name.")
parser.add_argument('--dir', required='true', help='save directory')
parser.add_argument('--data', required='true', help='dataset name')

args = parser.parse_args()

if args.data == "mnist":
    datasets.MNIST(root=args.dir, download=True)
if args.data == "cifar10":
    datasets.CIFAR10(root=args.dir, download=True)
if args.data == "fashionmnist":
    datasets.FashionMNIST(root=args.dir, download=True)

