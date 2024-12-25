import hashlib
import time


class Blob:
    def __init__(self, content):
        self.content = content
        self.hash = self._generate_hash(content)

    def _generate_hash(self, content):
        """Generate SHA-1 hash of the file content"""
        return hashlib.sha1(content.encode("utf-8")).hexdigest()

    def __repr__(self):
        return f"Blob({self.hash})"


# Test Blob
blob = Blob("Hello, world!")
print(blob)


class Tree:
    def __init__(self):
        self.entries = {}  # filename -> Blob or Tree

    def add_entry(self, name, obj):
        """Add a file or subdirectory to the Tree"""
        self.entries[name] = obj

        return f"Tree({self.entries})"


# Test Tree
tree = Tree()
blob1 = Blob("Hello, world!")
tree.add_entry("file1.txt", blob1)
print(tree)


class Commit:
    def __init__(self, tree, message, author):
        self.tree = tree  # Pointing to the current directory state of the Tree
        self.message = message
        self.author = author
        self.timestamp = int(time.time())
        self.hash = self._generate_commit_hash()

    def _generate_commit_hash(self):
        """Generate the hash for the Commit"""
        content = f"{self.tree_hash()}{self.message}{self.author}{self.timestamp}"
        return hashlib.sha1(content.encode("utf-8")).hexdigest()

    def tree_hash(self):
        """Generate the hash for the Tree"""
        return "".join(blob.hash for blob in self.tree.entries.values())

    def __repr__(self):
        return f"Commit({self.hash}, {self.message})"


# Test Commit
commit = Commit(tree, "Initial commit", "John Doe")
print(commit)


# Create file Blob
blob1 = Blob("Hello, world!")
blob2 = Blob("This is a second file.")

# Create directory Tree
tree = Tree()
tree.add_entry("file1.txt", blob1)
tree.add_entry("file2.txt", blob2)

# Create Commit
commit = Commit(tree, "Initial commit", "John Doe")

# Output result
print(commit)
