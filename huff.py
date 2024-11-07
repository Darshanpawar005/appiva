import heapq
from collections import Counter

# Step 1: Define the Node for Huffman Tree
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define the comparator for PriorityQueue
    def __lt__(self, other):
        return self.freq < other.freq

# Step 2: Build Huffman Tree
def build_huffman_tree(text):
    # Frequency dictionary
    frequency = Counter(text)
    
    # Priority queue for building the Huffman Tree
    priority_queue = []
    for char, freq in frequency.items():
        node = Node(char, freq)
        priority_queue.append(node)
    
    heapq.heapify(priority_queue)
    
    # Construct the tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        merged = Node()
        merged.freq = left.freq + right.freq
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0] if priority_queue else None

# Step 3: Generate Huffman Codes
def generate_codes(node, current_code="", codes={}):
    if node is None:
        return

    # If this is a leaf node, store the code
    if node.char is not None:
        codes[node.char] = current_code

    # Traverse left
    generate_codes(node.left, current_code + "0", codes)
    # Traverse right
    generate_codes(node.right, current_code + "1", codes)

    return codes

# Step 4: Encode Text
def encode(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text

# Step 5: Decode Text
def decode(encoded_text, root):
    decoded_text = ""
    current = root
    for bit in encoded_text:
        # Traverse the tree based on the bit
        if bit == "0":
            current = current.left
        else:
            current = current.right

        # If it's a leaf node, add the character to decoded_text
        if current.left is None and current.right is None:
            decoded_text += current.char
            current = root  # Go back to root for the next character

    return decoded_text

# Main function to execute encoding and decoding
def huffman_encoding_decoding(text, encoded_text):
    # Build Huffman Tree
    huffman_tree_root = build_huffman_tree(text)
    
    # Generate Huffman Codes
    codes = generate_codes(huffman_tree_root)
    print("Huffman Codes:", codes)
    
    # Encode the text
    encoded_text_generated = encode(text, codes)
    print("Encoded Text:", encoded_text_generated)
    
    # Decode the encoded text (either the generated one or a user-provided one)
    decoded_text = decode(encoded_text, huffman_tree_root)
    print("Decoded Text:", decoded_text)
    return encoded_text_generated, decoded_text

# Example Usage
text = input("Enter text to encode: ")
encoded_text = input("Enter encoded text to decode (optional): ")

if not encoded_text:
    encoded_text = None

encoded_text_generated, decoded_text = huffman_encoding_decoding(text, encoded_text or "")