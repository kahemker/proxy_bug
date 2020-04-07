import pandas as pd
import datetime
from pvlib.forecast import GFS

# specify location (Tucson, AZ)
latitude, longitude, tz = 32.2, -110.9, 'US/Arizona'

# specify time range.
start = pd.Timestamp(datetime.date.today(), tz=tz)

end = start + pd.Timedelta(days=7)

irrad_vars = ['ghi', 'dni', 'dhi']

model = GFS()

processed_data = model.get_processed_data(latitude=latitude,
                                          longitude=longitude,
                                          start=start,
                                          end=end,
                                          headers={'User-Agent': 'UserNoAuth',
                                                   'Front-End-Https': 'on'},
                                          verify=False)
