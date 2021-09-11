        
import ephem
from datetime import datetime
current_date = (datetime.date(datetime.now()))

# user_text = input(' input ')
# planet = getattr(ephem, user_text)()
# planet.compute(ephem.Date(current_date))
# const = ephem.constellation(planet)
# print(const)
print(ephem.next_full_moon(current_date))

