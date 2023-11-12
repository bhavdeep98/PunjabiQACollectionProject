import pandas as pd

def read_excel_file_as_dataframe(file_path):
  """Reads an Excel file and returns a Pandas DataFrame."""


  # Read the Excel file into a Pandas DataFrame
  df = pd.read_excel(file_path)

  # Return the DataFrame
  return df

def read_text_file(file_path):
  """Reads a text file and returns its contents as a string.

  Args:
    file_path: The path to the text file.

  Returns:
    A string containing the contents of the text file.
  """

  with open(file_path, "r", encoding="utf-8") as f:
    file_contents = f.read()

  return file_contents

