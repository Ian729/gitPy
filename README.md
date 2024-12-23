# gitPy: A Python-based Git Simulation

## Description

gitPy is a simplified, Python-based simulation of Git’s core data structures and operations. It demonstrates how Git handles files, directories, and commits using basic Python classes such as Blob, Tree, and Commit. While this is not a full implementation of Git, it helps to understand how Git internally manages data and tracks changes over time.

## Features
- Simulates Git’s Blob, Tree, and Commit objects.
- Provides basic functionality to create files (Blob), organize them into directories (Tree), and record commits (Commit).
- Implements basic hashing for each object, similar to how Git uses SHA-1 hashes for tracking changes.
- Allows users to simulate adding files to directories and making commits.

## Installation

### Prerequisites

Ensure you have the following dependencies installed:
- Python 3.x

No additional libraries are required as this project only uses standard Python libraries (hashlib, time).

### Steps to Install
1. Clone the repository:
```
git clone https://github.com/your-username/gitPy.git
```

2. Navigate to the project directory:
```
cd gitPy
```

 3. Optional: Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

 4. Run the simulation:
```
python gitpy.py
```


## Usage

### Running the Simulation

After setting up, you can run the simulation by executing the gitPy_simulation.py file. The simulation will create Blob objects for files, a Tree object to organize them, and a Commit object to record the changes.

python gitpy.py

### Example Usage

Here is an example of how the Git-like objects are created and used:
```
# Creating Blob objects to represent files
blob1 = Blob("Hello, world!")
blob2 = Blob("This is a second file.")

# Creating a Tree object to represent the directory
tree = Tree()
tree.add_entry("file1.txt", blob1)
tree.add_entry("file2.txt", blob2)

# Creating a Commit object to record the change
commit = Commit(tree, "Initial commit", "John Doe")

# Printing the commit object
print(commit)
```
### Output Example

The output will show the commit object along with its hash and message:
```
Commit(a3c7f4a2c19b... , Initial commit)
```