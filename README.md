# Junior Python Developer Task

To run the program enter python task.py in Terminal

Exit the program by using Ctrl+C

To run the tests enter pytest test_task.py in Terminal

## File overview:

- task.py -- main file
- test_task.py -- PyTest file
- Requirements.txt -- packages needed to run the script
- log.txt -- error log file

## Assumptions, hard parts

- Task related: "The program should not crash even if the input is wrong" (What input should there be in the program?)

- How specific does the error handling need to be?

## Improvements

- Custom exceptions?

- More specific error handling?

## Examples

First, the program tries to read and print `/posts` endpoint results

```
Printing posts:
[
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    } ...
```

Then the same is done on `/comments` endpoint

```
Printing comments:
[
    {
        "postId": 1,
        "id": 1,
        "name": "id labore ex et quam laborum",
        "email": "Eliseo@gardner.biz",
        "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
    } ...
```

After that, results from posts and comments are merged by `postId`

```
Printing posts + comments:
[
    {
        "userId": 1,
        "id": 1,
        "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
        "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto",
        "comments": [
            {
                "postId": 1,
                "id": 1,
                "name": "id labore ex et quam laborum",
                "email": "Eliseo@gardner.biz",
                "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
            } ...
```

Any errors are printed to the terminal and saved to the log.txt file

```
log.txt

ERROR:root:Request error: 404 Client Error: Not Found for url: https://jsonplaceholder.typicode.com/postss
ERROR:root:Request error: 404 Client Error: Not Found for url: https://jsonplaceholder.typicode.com/commentss
```
