import requests, json, time, logging

# Setting up logging
logging.basicConfig(filename="log.txt", level=logging.ERROR)

BASE_API_URL = "https://jsonplaceholder.typicode.com"


# fetches data from endpoint and returns a json object
def fetch_data(endpoint):
    try:
        response = requests.get(BASE_API_URL + endpoint)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        logging.error(f"Request error: {e}")
        return None
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {e}")
        print(f"JSON decode error: {e}")
        return None


# Merges post with comments and returns an array
def merge_posts_and_comments(posts, comments):
    merged_data = []
    for post in posts:
        post_id = post["id"]
        post["comments"] = [
            comment for comment in comments if comment["postId"] == post_id
        ]
        merged_data.append(post)
    return merged_data


# Prints specified data to terminal
def print_data(data):
    if data is None:
        print("Error occurred while printing data.")
        logging.error("Error occurred while printing data.")
    else:
        print(json.dumps(data, indent=4))


def main():
    try:
        while True:
            # Fetch data from /posts and /comments
            posts = fetch_data("/posts")
            comments = fetch_data("/comments")

            print("Printing posts:")
            print_data(posts)
            print("Printing comments:")
            print_data(comments)
            merged_data = merge_posts_and_comments(posts, comments)
            print("Printing posts + comments:")
            print_data(merged_data)

            # TESTING
            """ 
            with open("posts.json", "w") as outfile:
                json.dump(posts, outfile)
            with open("comments.json", "w") as outfile:
                json.dump(comments, outfile)
            with open("merged.json", "w") as outfile:
                json.dump(merged_data, outfile) 
            """

            # Sleep for 30 seconds before making next request
            print("Use Ctrl+C to EXIT")
            time.sleep(30)
    except KeyboardInterrupt:
        print("Program terminated")
    except Exception as e:
        logging.error(f"Unhandled exception {e}")
        print(f"Unhandled exception {e}")


if __name__ == "__main__":
    main()
