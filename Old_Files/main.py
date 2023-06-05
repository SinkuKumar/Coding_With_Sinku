from generate_files import generate_files
import rename_files

# Define the directory where the files will be created
directory = r"C:\Users\Sinkukumar\PycharmProjects\IntegrationServicesAutomation\Files"

# Generate 1000 files
generate_files(directory, 1000, ".txt")

# Rename the files
rename_files.rename_file(directory, ".txt", ".bat")