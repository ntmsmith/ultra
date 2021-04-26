# Ultra - UserBot
A stable pluggable Telegram userbot, based on Telethon.

<p align="center">
  <img src="./resources/extras/logo_rdm.png" alt="TeamUltra">
</p>

[![Stars](https://img.shields.io/github/stars/TeamUltra/Ultra?style=flat-square&color=green)](https://github.com/TeamUltra/Ultra/stargazers)
[![Forks](https://img.shields.io/github/forks/TeamUltra/Ultra?style=flat-square&color=green)](https://github.com/TeamUltra/Ultra/fork)
[![Python Version](https://img.shields.io/badge/Python-v3.9-blue)](https://www.python.org/)
[![Contributors](https://img.shields.io/github/contributors/TeamUltra/Ultra?style=flat-square&color=green)](https://github.com/TeamUltra/Ultra/graphs/contributors)
[![License](https://img.shields.io/badge/License-AGPL-blue)](https://github.com/TeamUltra/Ultra/blob/main/LICENSE)
[![Size](https://img.shields.io/github/repo-size/TeamUltra/Ultra?style=flat-square&color=green)](https://github.com/TeamUltra/Ultra/)

<details>
<summary>More Info</summary>
<br>
  <b>Documentation</b> - <a href="https://Ultra.tech">Ultra.tech</a>  <br />
</details>

# Deploy 
- [Heroku](https://github.com/TeamUltra/Ultra#Deploy-to-Heroku)
- [Local Machine](https://github.com/TeamUltra/Ultra#Deploy-Locally)

## Deploy to Heroku
- Get your `API_ID` and `API_HASH` from [here](https://my.telegram.org/)    
- Get your `SESSION` from [here](https://repl.it/@TeamUltra/UltraStringSession#main.py).   
and click the below button!  <br />  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Deploy Locally
- Get your `API_ID` and `API_HASH` from [here](https://my.telegram.org/)
- Get your `REDIS_URI` and `REDIS_PASSWORD` from [here](https://redislabs.com), tutorial [here](./resources/extras/redistut.md).
- Clone the repository: <br />
`git clone https://github.com/TeamUltra/Ultra.git`
- Go to the cloned folder: <br />
`cd Ultra`
- Create a virtual env:   <br />
`virtualenv -p /usr/bin/python3 venv`   
`. ./venv/bin/activate`
- Install the requirements:   <br />
`pip install -r requirements.txt`   
- Generate your `SESSION`:   
`bash sessiongen`
or
`bash -c "$(curl -fsSL https://del.dog/Ultra)"`
- Fill your details in a `.env` file, as given in [`.env.sample`](https://github.com/TeamUltra/Ultra/blob/main/.env.sample).    
(You can either edit and rename the file or make a new file.)
- Run the bot:   
`bash resources/startup/startup.sh`

Made with 💕 by [@TeamUltra](https://t.me/TeamUltra). <br />

# Credits
* [Lonami](https://github.com/LonamiWebs/) for [Telethon](https://github.com/LonamiWebs/Telethon)

