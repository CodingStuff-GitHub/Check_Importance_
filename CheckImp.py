from googlesearch import search
import requests

sites_points = {"stack":5, "github":5}

def point_counter(website_name):
    for i in sites_points.keys():
        if website_name.find(i) != -1:
            return sites_points[i]
    return 1
        
words = ["process_cpu_usage", "system_cpu_usage"]
no_of_results = 20
for query in words:
    website_list = list(search(query, num_results = no_of_results))
    total_points = 0
    for i in range(no_of_results):
        print(website_list[i])
        
    for i in range(no_of_results):
        points = point_counter(website_list[i])
        page = requests.get(website_list[i])
        contents = str(page.content)
        occurences = contents.count(query)
        print(points, end = " ")
        print(occurences)
        total_points += occurences * points
    print(query, total_points)
