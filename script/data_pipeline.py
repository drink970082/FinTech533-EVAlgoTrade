import shinybroker as sb
import datetime
import numpy as np
import pandas as pd


class shinyDataFetcher:
    def __init__(self, asset: str, durationStr: str = "1 M", barSizeSetting: str = "1 day", useRTH: bool = True, endDateTime: str = ""):
        self.asset = asset
        self.durationStr = durationStr
        self.barSizeSetting = barSizeSetting
        self.useRTH = useRTH
        self.endDateTime = endDateTime
        self.contract = sb.Contract({"symbol": asset, "secType": "STK", "exchange": "SMART", "currency": "USD"})

    def fetch_asset_data(self) -> pd.DataFrame:
        try:
            historical_data = sb.fetch_historical_data(
                contract=self.contract,
                durationStr=self.durationStr,
                barSizeSetting=self.barSizeSetting,
                useRTH=self.useRTH,
                endDateTime=self.endDateTime,
                timeout=10,
            )
        except:
            print(f"Error fetching data for {self.asset}. Please check the parameters or network connection.")
            return pd.DataFrame()
        return historical_data["hst_dta"]


if __name__ == "__main__":
    tsla_daily = shinyDataFetcher(asset="TSLA", durationStr="1 Y", barSizeSetting="1 day", useRTH=True, endDateTime="")
    rivn_daily = shinyDataFetcher(asset="RIVN", durationStr="1 Y", barSizeSetting="1 day", useRTH=True, endDateTime="")
    print("TSLA Daily Data:")
    print("========================================")                   
    print(tsla_daily.fetch_asset_data().head(5))
    print("RIVN Daily Data:")
    print("========================================")
    print(rivn_daily.fetch_asset_data().head(5))
