import pandas as pd

def load_data(orders_file, view_counts_file):
    orders_df = pd.read_excel(orders_file)
    view_count_df = pd.read_excel(view_counts_file)
    return orders_df, view_count_df

def merge_data(orders_df, view_counts_df):
    # accountId와 productId를 통해 데이터프레임을 합침
    merged_df = pd.merge(orders_df, view_counts_df, on=['accountId', 'productId'])
    return merged_df

def preprocess_data(merged_df):
    # merged된 dataframe과 viewcount의 상관관계 따지기 >> 안 나온 경우는 0으로 채움
    merged_df['viewCount'] = merged_df['viewCount'].fillna(0)
    return merged_df

def export_data_to_excel(df, filePath):
    df.to_excel(filePath, index=False, engine='openpyxl')
    print(f"전처리 완료 : {filePath}")

if __name__ == "__main__":
    orders_info_file = "../../orders_data.xlsx"
    view_count_info_file = "../../view_counts_data.xlsx"
    output_file = "../../preprocessed_orders_data.xlsx"

    orders_df, view_counts_df = load_data(orders_info_file, view_count_info_file)
    merged_df = merge_data(orders_df, view_counts_df)
    preprocessed_df = preprocess_data(merged_df)
    export_data_to_excel(preprocessed_df, output_file)