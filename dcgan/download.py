import torchvision
import torchvision.datasets as datasets
import argparse

parser = argparse.ArgumentParser(description="Download Torchvision Datasets by name.")
parser.add_argument('--save-dir', required='true', help='save directory')
parser.add_argument('--dataset', required='true', help='dataset name')

args = parser.parse_args()

if args.dataset == "mnist":
    datasets.MNIST(root=args.save_dir, download=True)
if args.dataset == "cifar10":
    datasets.CIFAR10(root=args.save_dir, download=True)
if args.dataset == "fashionmnist":
    datasets.FashionMNIST(root=args.save_dir, download=True)

