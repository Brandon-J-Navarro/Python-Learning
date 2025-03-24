import os

def create_files(count, file_path):
    os.makedirs(file_path, exist_ok=True)  # Ensure the directory exists

    for i in range(1, count + 1):
        file_size = i * 1024 * 1024 # Calculate file size in bytes
        file_name = os.path.join(file_path, f"file_{i}.test")

        with open(file_name, "wb") as f:
            f.write(b"0" * file_size)  # Write the specified number of bytes

        print(f"Created: {file_name} ({file_size} bytes)")

# Example usage:
# create_files(5, "./output_files")
if __name__ == "__main__":
    create_files(100, "C:\\Users\\bnavarro\\Documents\\Test Files\\Python")