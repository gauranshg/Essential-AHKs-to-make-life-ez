import os
import csv

def list_files_in_directory(directory_path):
    """
    List all files in the given directory and its subdirectories.
    
    Args:
    directory_path (str): The path of the directory to list files from.
    
    Returns:
    List of tuples containing file paths and file names.
    """
    files_list = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            files_list.append((root, file))
    return files_list

def save_files_to_csv(file_list, output_csv_path):
    """
    Save the list of file paths and file names to a CSV file.
    
    Args:
    file_list (list): List of tuples containing file paths and file names to save.
    output_csv_path (str): The path of the CSV file to write to.
    """
    try:
        with open(output_csv_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['File Path', 'File Name'])  # Write the header
            for file_path, file_name in file_list:
                writer.writerow([file_path, file_name.split('.')[0]])
        print(f"File names saved to {output_csv_path}")
    except Exception as e:
        print(f"An error occurred while writing to CSV: {e}")

if __name__ == "__main__":
    # Specify the directory path and output CSV file path
    directory_path = r'D:\JSON'
    output_csv_path = 'file_names.csv'
    
    # Get the list of files in the directory and its subdirectories
    file_list = list_files_in_directory(directory_path)
    
    # Save the file paths and names to a CSV file
    save_files_to_csv(file_list, output_csv_path)
