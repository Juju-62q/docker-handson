import requests


def main():
    target_url = "https://get.docker.com"
    r = requests.get(target_url)
    print(r.text)


if __name__ == "__main__":
    main()
