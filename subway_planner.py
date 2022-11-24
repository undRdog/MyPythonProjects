line1 = [
    "vörösmarty tér",
    "deák ferenc tér",
    "bajcsy-zsilinszky út",
    "opera",
    "oktogon",
    "vörösmarty utca",
    "kodály körönd",
    "bajza utca",
    "hősök tere",
    "széchenyi fürdő",
    "mexikói út",
]

line2 = [
    "déli pályaudvar",
    "széll kálmán tér",
    "batthyány tér",
    "kossuth lajos tér",
    "deák ferenc tér",
    "astoria",
    "blaha lujza tér",
    "keleti pályaudvar",
    "puskás ferenc stadion",
    "pillangó utca",
    "örs vezér tere",
]

line3 = [
    "újpest-központ",
    "újpest-városkapu",
    "gyöngyösi utca",
    "forgách utca",
    "göncz árpád városközpont",
    "dózsa györgy út",
    "lehel tér",
    "nyugati pályaudvar",
    "arany jános utca",
    "deák ferenc tér",
    "ferenciek tere",
    "kálvin tér",
    "corvin-negyed",
    "semmelweis klinikák",
    "nagyvárad tér",
    "népliget",
    "ecseri út",
    "pöttyös utca",
    "határ út",
    "kőbánya-kispest",
]

line4 = [
    "kelenföld vasútállomás",
    "bikás park",
    "újbuda-központ",
    "móricz zsigmond körtér",
    "szent gellért tér",
    "fővám tér",
    "kálvin tér",
    "rákóczi tér",
    "ii. jános pál pápa tér",
    "keleti pályaudvar",
]


def main():
    # The first four lines validate the input and find which lines are involved
    start_station = input_validation("Start")
    end_station = input_validation("End")

    line_of_start = find_line(start_station, end_station)
    line_of_end = find_line(end_station, start_station)

    # Finding out how many stops you should ride each line
    stops_first_line = stops(start_station)
    stops_sec_line = stops(end_station)

    # If both stops are on the same line, the program exits with the following output:
    if line_of_start == line_of_end:
        print(
            f"After {stops_first_line} stops, you arrive the station {end_station.title()}. You don't need to change lines"
        )

    # If change is needed, this part find out where. Line 1-2-3 has a common station, Line4 is crossing Line3 only:
    elif line_of_start != line_of_end:
        if line_of_start != "Line 4" and line_of_end != "Line 4":
            print(
                f"After {stops_first_line} stops, you need to change lines at Deák Ferenc Tér"
            )
            print(
                f"From Deák Ferenc Tér, you need to ride {stops_sec_line} stops on {line_of_end} until the station {end_station.title()}"
            )
        elif (line_of_start == "Line 4" and line_of_end == "Line 3") or (
            line_of_start == "Line 3" and line_of_end == "Line 4"
        ):
            print(
                f"After {stops_first_line} stops, you need to change lines at Kálvin Tér"
            )
            print(
                f"From Kálvin Tér, you need to ride {stops_sec_line} stops on {line_of_end} until the station {end_station.title()}"
            )
    # This part and function decides whether you are need to buy a 30 or 90 minutes ticket. 12 stops are about 30 minutes in rush hour.
    total_stops, ticket = fares(
        stops_first_line, stops_sec_line, line_of_start, line_of_end
    )
    print(f"For this {total_stops} stops ride please purchase a {ticket} ticket.")


def fares(first, sec, line_of_start, line_of_end):
    if line_of_start != line_of_end:
        total_stops = first + sec
    elif line_of_start == line_of_end:
        total_stops = first
    if total_stops > 12:
        ticket = "90-minute"
        return total_stops, ticket
    elif total_stops <= 12:
        ticket = "30-minute"
        return total_stops, ticket


# Connection planner if user needs to change between lines
def find_line(s, e):
    if s == "deák ferenc tér":
        if e in line1:
            return "Line 1"
        elif e in line2:
            return "Line 2"
        elif e in line3:
            return "Line 3"
    elif s == "kálvin tér":
        if e in line3:
            return "Line 3"
        elif e in line4:
            return "Line 4"
    else:

        if s in line1:
            return "Line 1"
        elif s in line2:
            return "Line 2"
        elif s in line3:
            return "Line 3"
        elif s in line4:
            return "Line 4"


# Returning the number of stops needed on each line to reach destination
def stops(s):
    station_index = []
    conn_index = []
    i = 0
    if s in line1:
        length = len(line1)
        line = line1
        conn_station = "deák ferenc tér"
    elif s in line2:
        length = len(line2)
        line = line2
        conn_station = "deák ferenc tér"
    elif s in line3:
        length = len(line3)
        line = line3
        conn_station = "deák ferenc tér"
    elif s in line4:
        length = len(line4)
        line = line4
        conn_station = "kálvin tér"

    while i < length:
        if s == line[i]:
            station_index.append(i)
        if conn_station == line[i]:
            conn_index.append(i)
        i += 1

    stops = abs(station_index[0] - conn_index[0])

    return stops


# Accepting exact station names (case insensitive), or partial station names with question yes/no
def input_validation(s):
    while True:
        try:
            n = input(f"{s} station: ")
            n_lower = n.lower()
            if (
                n_lower in line1
                or n_lower in line2
                or n_lower in line3
                or n_lower in line4
            ):
                return n_lower
            else:
                print("Sorry, we can't recognize this station.")

        except:
            ValueError


if __name__ == "__main__":
    main()
