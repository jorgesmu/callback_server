# Reply Server

Reply Server is a Python simple and lightweight server that replies with the headers, path, and body that came in to easily debug your outbound requests on developing time.

Why?

When developing HTTP web applications many frameworks and HTTP clients introduce many encoding issues if not implemented and used properly. Test your server against a raw simple server instead of a complicated Framework to understand if your HTTP client is sending the right data.

Disclaimer: Proper automated tests should be done, this is a playground for developing time.

Implemented HTTP actions:
- Get
- Post (Currently needed to test server callbacks from a cron job)

Usage: 

```bash
python3 reply_server.py
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)