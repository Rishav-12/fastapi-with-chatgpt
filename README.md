# fastapi-with-chatgpt

As part of Major League Hacking's [Global Hack Week](https://ghw.mlh.io/) January, this was a daily challenge on Day 4 to build a hack with ChatGPT. So I decided to try it out.

The code is mostly written by ChatGPT, though I did make some adjustmets, and it is mind-blowing how awesome ChatGPT is :rocket:

Learn more about this project on [devpost](https://devpost.com/software/chatgpt-generated-fastapi-app)

## How to install and run

Clone the repo locally:

```
git clone https://github.com/Rishav-12/fastapi-with-chatgpt.git
```

Go inside the directory:

```
cd fastapi-with-chatgpt
```

Create a virtual environment:

```
python -m venv env
```

Activate the virtual environment:

On Windows:
```
env\Scripts\activate.bat
```

Or on Linux/macOS:
```
source env/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the app:
```
uvicorn main:app --reload
```

This will start serving the API on http://localhost:8000 and will automatically reload if the `main.py` file is changed

Test it out and have fun!
