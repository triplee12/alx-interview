# Log Parser

Write a script that reads stdin line by line and computes metrics:

- Input format: ``<IP Address> - [<date>]`` "GET /projects/260 HTTP/1.1" ``<status code> <file size>`` (if the format is not this one, the line must be skipped)
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
  - Total file size: File size: ``<total size>``
  - where ``<total size>`` is the sum of all previous ``<file size>`` (see input format above)
  - Number of lines by status code:
    - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
    - if a status code doesn’t appear or is not an integer, don’t print anything for this status code
    - format: ``<status code>: <number>``
    - status codes should be printed in ascending order

<!-- Testing -->
## Run Test

Run the python scripts in this format:

  - ``bash
  ./0-generator.py | ./0-stats.py
  ``

## Expected Result format

```ecpected output format

  Total file size: 3856
200: 2
301: 1
400: 1
401: 1
403: 2
404: 1
500: 2

Total file size: 9479
200: 5
301: 2
400: 1
401: 1
403: 2
404: 3
405: 2
500: 4

Total file size: 13763
200: 5
301: 3
400: 4
401: 2
403: 3
404: 3
405: 5
500: 5
```
