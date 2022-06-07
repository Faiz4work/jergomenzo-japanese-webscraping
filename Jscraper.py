from get_all_posts import get_all_post_of_user
from save_posts import save_all_posts

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
}

def get_posts_link():
    # Reading user profile links, approx 2400+
    f = open("user_profiles.txt", 'r')
    user_links = [i.strip() for i in f.readlines()]
    f.close()

    total_links_scraped = []

    # getting all users post
    for link in user_links:
        all_posts_link = get_all_post_of_user(link)

        # Appending all posts link to a .txt file:
        with open("all_users_post_link.txt", 'a') as f:
            for i in all_posts_link:
                f.write(i + '\n')
                all_posts_link.append(i)
        print(f"Added: {len(all_posts_link)} posts link!")

get_posts_link()


# Saving post to final .txt file
# save_all_posts("sample_posts", "all_sample_post_link.txt")
