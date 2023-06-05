import os

# Define the directory where the files will be created
#directory = r"C:\Users\Sinkukumar\PycharmProjects\IntegrationServicesAutomation\Files"


def generate_files(directory, number_of_files, file_extension):
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    # Generate 1000 files
    for i in range(1, number_of_files+1):
        file_name = f"File_{i}{file_extension}"
        file_path = os.path.join(directory, file_name)
        try:
            with open(file_path, 'w') as file:
                file.write("This is file number {}".format(i))
                print(f"Created file: {file_name}")
        except FileExistsError:
            print(f"File already exists: {file_name}, don't create it again and again!")
    return 1