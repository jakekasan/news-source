from news_wrangler import News_Wrangler
from guardian import Guardian
from config import config

def main():
    guardian_config = config["sources"]["guardian"]
    
    guardian = Guardian()

    print(guardian.search("RBS"))

if __name__ == '__main__':
    main()