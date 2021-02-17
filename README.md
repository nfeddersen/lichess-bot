# lichess-bot

This file contains the instructions on how to set up a Lichess bot, using the official Lichess API and Stockfish 12 chess engine. BOT DOES NOT PLAY VARIANTS.

1) Create API access token and upgrade to BOT account (will allow bot to play with the Lichess API) -- BOT ACCOUNTS CAN NOT HAVE PLAYED ANY GAMES BEFORE BEING CONVERTED TO A BOT ACCOUNT
	--  a) Navigate to: https://lichess.org/account/oauth/token
	--  b) Click on the blue + button
	--  c) Give your token a description (eg: All Permissions Enabled)
	--  d) Scroll down and toggle all permissions to enabled
	--  e) Click submit
	--  f) COPY TOKEN and paste it somewhere safe that you'll remember. This lets the bot use the API to play games. If you lose this token you'll need to create a new one.
	--  g) Open a Terminal window (Search for Terminal on Mac, Command Prompt on PC)
	--  h) Add your token to the following command, then paste it into the Terminal and press Enter: 

	curl -d '' https://lichess.org/api/bot/account/upgrade -H "Authorization: Bearer 	REPLACE_THIS_WITH_TOKEN"
	
	--  i) If you have followed the steps correctly you will get a OK response from the Lichess server. Your account is now a Bot and should have the purple BOT title next to its username.

2) Download Bot files from Github Repo
	--  a) Download Lichess-Bot repo at: https://github.com/nfeddersen/lichess-bot
	--  b) Extract the downloaded folder

3) Download Python
	--  a) Python is the programming language this bot is written in
	--  b) Download the latest version from here: https://www.python.org/downloads/
	--  c) This bot uses Python 3 (Python 2 does not work)

4) Check if PIP is installed
	--  a) run command: python -m pip --version
	--  b) Unix systems may require python3 instead of python
	--  c) If PIP is not installed on your machine follow the following steps. Otherwise, skip to the next step:
		-- a) Open a new Terminal window
		-- b) Select extracted Bot folder and copy its full path
		--  c) Enter the following command into the terminal and hit enter: cd PASTE_COMPLETE_PATH_HERE
		--  d) Ensure you have changed your current directory then enter this command and hit enter:
			python get-pip.py

5) Create Virtual Environment
	-- a) Enter the following command into the terminal (ensure you are still located in bot directory in command line, and if not run Step 4 (c)):
		python3 -m venv PASTE_COMPLETE_PATH_YOU_USED_EARLIER_HERE
	-- b)  Wait for command to complete; may take a little bit especially on older machines

6) Install all neccessary packages using requirements.txt file
	--  a) This installs all the packages program needs to run properly
	--  b) Move requirements.txt file from downloaded folder into Bot folder
	-- c ) Using your Terminal window that is still located in bot directory, enter the following command:
		pip install -r requirements.txt
	--  d) You should see a message in the Terminal saying that the packages have been succesfully installed. If all packages have been installed, move onto the next step.

7) Configure Lichess-Bot files
	--  a) Open the file with Notepad or Notepad++ (if you have a Python IDE you can use this, but its not required)
	--  b) Anywhere that says BOT_NAME or YOUR_BOT_NAME replace with your bots username
	--  c) Replace text within quotes at LINE 9 with your API key you downloaded earlier. THE QUOTES MUST REMAIN AROUND KEY OR BOT WILL NOT WORK!!

8) Run your Bot!
	--  a) Log into your bot account if you wish for your bot to be online (simply running program does not make bot online)
	--  b) Using your terminal window you have used so far, enter the following command:
		python LichessBotMain.py
	--  c) If on a Unix system , python 3 instead of python may be required
	--  d) Program will run until Terminal window is closed
	--  e) Challenge the bot to normal games of chess -- VARIANTS ARE NOT ACCEPTED
	--  f) If the bot has not been challenged, output on terminal will read:
		Request Response is Empty
	--  g) If output says that it has been challenged and lists moves, it is playing a game.

9) IN CASE OF ERRORS
	-- a) If the program stops working and throws an error, something has gone wrong. Most likely something happened with its internet connection.
	--  b) If it is in a game, you must manually resign the game -- bot will not remember position
	--  c) Run command 8 (b) again to bring bot back online
