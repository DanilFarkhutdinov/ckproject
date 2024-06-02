import pandas as pd


class Data:
    file = 'tab3_zpl_2023.xlsx'

    df = pd.read_excel(file, index_col=0)

    df.to_numpy()
