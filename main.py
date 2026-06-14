from monitor.monitoring import monitoring
from monitor.log_monitor import save_log

urls = [
    "https://www.google.com",
    "https://www.bing.com",
    "https://duckduckgo.com",
    "https://www.facebook.com",
    "https://www.instagram.com",
    "https://www.linkedin.com",
    "https://www.x.com",
    "https://www.tiktok.com",
    "https://www.reddit.com",
    "https://www.netflix.com",
    "https://www.spotify.com",
    "https://www.youtube.com",
    "https://www.twitch.tv",
    "https://www.github.com",
    "https://www.gitlab.com",
    "https://www.stackoverflow.com",
    "https://www.python.org",
    "https://www.mozilla.org",
    "https://api.github.com",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://httpbin.org/get",
]
# counter for indicate the numbers of requisitions.
counter = 1

# Loop that iterates ihn URL list, do the requisition and sav in .log archive.
for url in urls:
    res = monitoring(url)
    print(counter)
    counter += 1
    save_log(res)
print("End the monitoring")