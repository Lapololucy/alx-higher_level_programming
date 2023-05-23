# 0x14. JavaScript - Web scraping
Scripting API JavaScript

## Resources
**Read or watch:**
- [Working with JSON data](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://medium.com/@vietkieutie/the-workflow-of-accessing-the-attributes-of-a-simply-created-json-object-82a5b33e2319)
- [request module](https://github.com/request/request)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)
- [Star wars API``(for advnced task:100-starwars_characters.js & 101-starwars_characters.js)``](https://swapi-api.hbtn.io/)

## Learning Objectives
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use ``request`` and fetch API
- How to read and write a file using ``fs`` module

## General Requirements
- Allowed editors: ``vi``, ``vim``, ``emacs``
- All files are interpreted on Ubuntu 14.04 LTS using ``node`` (version 10.14.x)
- All files end with a new line
- The first line of all files was exactly ``#!/usr/bin/node``
- Your code should be ``semistandard`` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons](https://github.com/standard/semistandard) on top. Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All files are executable
- The length of the files will be tested using ``wc``
- Not allowed to use ``var``

## Installation
**Install Node 10**
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```
**Install semi-standard**<br>
[Documentation](https://github.com/standard/semistandard)
```
$ sudo npm install semistandard --global
OR
$ sudo npm install semistandard --global --fix
```
**Install ``request`` module and use it**<br>
[Documentation](https://github.com/request/request)
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
**Notes:** Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

## Files & Descriptions
| Files			     | Descriptions                                                                           |
| -------------------------- |:-------------------------------------------------------------------------------------- |
| 0-readme.js                | Read and prints the content of a file                                                  |
| 1-writeme.js               | Writes a string to a file                                                              |
| 2-statuscode.js            | Display the status code of a get request                                               |
| 3-starwars_title.js        | Prints the title of a Star Wars movie where the episode number matches a given integer |
| 4-starwars_count.js        | prints the number of movies where the character “Wedge Antilles” is present            |
| 5-request_store.js         | Gets the contents of a webpage and stores it in a file.                                |
| 6-completed_tasks.js       | Computes the number of tasks completed by user id.                                     |
| 100-starwars_characters.js | Prints all characters of a Star Wars movie                                             |
| 101-starwars_characters.js | Prints all characters of a Star Wars movie in the right order                          |
