import requests

url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=6a4842dbd350406391d5e04625e2949a"

r = requests.get(url)
data = r.json()

def getSources():
    sources = set()
    for i in range(len(data['articles'])):
        source = data['articles'][i]['source']['name']
        sources.add(source)
        
    return list(sources)

def getTitles(newsChannel):
    titles = list()
    for i in range(len(data['articles'])):
        source = data['articles'][i]['source']['name']
        if(source == newsChannel):
            title = data['articles'][i]['title']
            titles.append(title)
    
    return titles

def showNews(source, title):
    print("\n\n")
    for i in range(len(data['articles'])):
        currSource = data['articles'][i]['source']['name']
        currTitle = data['articles'][i]['title']

        if(currSource == source and currTitle == title):
            date = data['articles'][i]['publishedAt']
            author = data['articles'][i]['author']
            description = data['articles'][i]['description']
            content = data['articles'][i]['content']

    print(f"SOURCE: {source}")
    print(f"DATE: {date}")
    print(f"\nDESCRIPTION: {description}")
    print(f"\n{content}")
    print(f"\nWRITTEN BY: {author}")
    print("\n\n")

if __name__ == "__main__":
    print("news app".upper().center(100))

    channels = getSources()
    print("Select News Channel")

    i = 0
    for channel in channels:
        print(f"{i}: {channel}")
        i += 1

    newsChannel = int(input("\nEnter Your Choice: "))
    newsChannel = channels[newsChannel]

    titles = getTitles(newsChannel)
    print("Available News: -")

    i = 0
    for title in titles:
        print(f"{i}: {title}")
        i += 1

    title = int(input("\nEnter Your Choice: "))
    title = titles[title]

    showNews(newsChannel, title)

    