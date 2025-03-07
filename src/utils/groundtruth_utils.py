import pandas as pd

def convert_groundtruth_to_csv():
    """
    Convert the ground truth Excel file to CSV.
    """
    # Read the Excel ground truth file
    df = pd.read_excel("data/ground_truth.xlsx")
    
    # Only keep the columns we need (Filename, Title, Author, Publication Year and Groundwater level mentioned)
    df = df[["Filename", "Title", "Author", "Publication Year", "Groundwater level mentioned"]]
    
    # Remove the ".pdf" extension from the filename values in the "Filename" column
    df["Filename"] = df["Filename"].str.replace(".pdf", "")
    
    # Save as CSV
    df.to_csv("data/groundtruth.csv", index=False)
    print("Ground truth data saved as CSV.")