import pandas as pd

def load_data(file_path):
    return pd.read_excel(file_path)

def remove_duplicates(df):
    unique_df = df.drop_duplicates(subset=['accountId', 'productId'], keep='first')
    return unique_df


def save_data(df, file_path):
    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Saved unique data to {file_path}")


if __name__ == "__main__":
    input_file = "../../preprocessed_orders_data.xlsx"
    output_file = "../../orders_data_after_drop_duplication.xlsx"

    df = load_data(input_file)
    unique_df = remove_duplicates(df)
    save_data(unique_df, output_file)
