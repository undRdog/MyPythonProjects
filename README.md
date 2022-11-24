# Subway trip planner Budapest
This tiny software helps you if you are not familiar with hungarian words and station names and rather you are counting how many stops are left.

### Author
Tibor Seres, 1986
Budapest, Hungary
https://github.com/undRdog


### Description:
This program prompts the user to input the start station and the end station of his journey and outputs many useful informations:

- If you need to change between lines or not
- How many stops you need to ride before changing
- Where do you change between lines
- How many stops you need to ride on the second line
- Helps you decide between 30-minutes and 90-minutes ticket

Beside the "main", the program has four functions:

- "input_validation": This function prompts the user for input until both the start and end station is a valid station name. else it prompts again with an error message.
- "find_line": This function finds which line to belong the station inputed. The result is neccessary in order to decide if user needs to change lines or not. It takes two arguement because if one of the stations is a connecting station, it belongs to several lines and you decide which line to assign depending on the other station.
- "stops": Returning the number of stops needed on each line to reach destination, using a while loop to find the station indexes, and the abs() funtion to find the difference between the two indexes.
- "fares": It helps to decide the ticket you need, depending on the number of total stops. 30 minutes are usually enough for ~12 stations, above that it is safer to buy the 90-minutes ticket.





