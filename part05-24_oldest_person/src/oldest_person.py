# Write your solution here

def oldest_person(people: list):
    dates = []
    
    for person in people:
        dates.append(person[1])
    
    oldest_year = dates.index(min(dates))
    return people[oldest_year][0]


















if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))