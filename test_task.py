import requests_mock, json

# Importing task functions
from task import fetch_data, merge_posts_and_comments, print_data


def test_fetch_data_posts_success():
    # Create a requests_mock object
    with requests_mock.Mocker() as m:
        # Mock a sucessfull API response
        expected = [
            {
                "userId": 1,
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
            }
        ]
        m.get("https://jsonplaceholder.typicode.com/posts", text=json.dumps(expected))

        # Call the fetch_data function
        result = fetch_data("/posts")

        # Assert the result is the expected data
        assert result == expected


def test_fetch_data_comments_success():
    # Create a requests_mock object
    with requests_mock.Mocker() as m:
        # Mock a sucessfull API response
        expected = [
            {
                "postId": 1,
                "id": 1,
                "name": "id labore ex et quam laborum",
                "email": "Eliseo@gardner.biz",
                "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium",
            }
        ]
        m.get(
            "https://jsonplaceholder.typicode.com/comments", text=json.dumps(expected)
        )

        # Call the fetch_data function
        result = fetch_data("/comments")

        # Assert the result is the expected data
        assert result == expected


def test_fetch_data_failed():
    # Create a requests_mock object
    with requests_mock.Mocker() as m:
        # Mock a failed API response
        m.get("https://jsonplaceholder.typicode.com/posts", status_code=404)

        # Call the fetch_data function
        result = fetch_data("/posts")

        # Assert the result is None
        assert result is None


# Mock a response with invalid JSON data
def test_fetch_data_json_decode_error():
    with requests_mock.Mocker() as m:
        # Mock a response with invalid JSON data
        m.get(
            "https://jsonplaceholder.typicode.com/posts", text="Invalid JSON Response"
        )

        try:
            # Call the fetch_data function, which should raise JSONDecodeError
            fetch_data("/posts")
        except json.decoder.JSONDecodeError as e:
            # Assert that the exception message matches expected error message
            assert str(e) == "Expecting value: line 1 column 1 (char 0)"


def test_merge_posts_and_comments():
    # Mock data for posts and comments
    posts = [
        {"id": 1, "title": "Mock Post 1"},
        {"id": 2, "title": "Mock Post 2"},
        {"id": 3, "title": "Mock Post 3"},
    ]
    comments = [
        {"postId": 1, "text": "Mock Comment 1"},
        {"postId": 2, "text": "Mock Comment 2"},
    ]

    # Call the merge_posts_and_comments function
    merged_data = merge_posts_and_comments(posts, comments)

    # Assert that each post includes its comments
    assert merged_data[0]["comments"] == [{"postId": 1, "text": "Mock Comment 1"}]
    assert merged_data[1]["comments"] == [{"postId": 2, "text": "Mock Comment 2"}]
    assert merged_data[2]["comments"] == []


def test_print_data(capfd):
    # Capture the printed output
    data = [{"id": 1, "title": "Mock Post 1"}, {"id": 2, "title": "Mock Post 2"}]
    print_data(data)
    captured = capfd.readouterr()

    # Assert the printed output matches the expected JSON
    expected_output = json.dumps(data, indent=4) + "\n"
    assert captured.out == expected_output
