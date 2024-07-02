

import pandas as pd

def loadData(ordersFile, viewCountsFile):
    ordersDf = pd.read_excel(ordersFile)
    viewCountsDf = pd.read_excel(viewCountsFile)
    return ordersDf, viewCountsDf

def mergeData(ordersDf, viewCountsDf):
    mergedDf = pd.merge(ordersDf, viewCountsDf, on=['accountId', 'productId'])
    return mergedDf


def preprocessData(mergedDf):
    mergedDf['viewCount'] = mergedDf['viewCount'].fillna(0)
    return mergedDf


def exportDataToExcel(df, filePath):
    df.to_excel(filePath, index=False, engine='openpyxl')
    print(f"전처리 완료: {filePath}")

if __name__ == "__main__":
    ordersInfoFile = "../../orders_data.xlsx"
    viewCountsInfoFile = "../../view_counts_data.xlsx"
    outputFile = "../../preprocessed_orders_data.xlsx"

    ordersDf, viewCountsDf = loadData(ordersInfoFile, viewCountsInfoFile)
    mergedDf = mergeData(ordersDf, viewCountsDf)
    preprocessdDf = preprocessData(mergedDf)
    exportDataToExcel(preprocessdDf, outputFile)