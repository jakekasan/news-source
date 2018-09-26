from news_wrangler import News_Wrangler
from config import config

def main():
    guardian_config = config["sources"]["guardian"]
    guardian = News_Wrangler(guardian_config["address"],guardian_config["API_KEY"])

    guardian.search("RBS")

if __name__ == '__main__':
    main()