# Trump-Tweet-Generator

![screenshot](https://i.imgur.com/I0L0W89.png)

This is a project to finetune a GPT-2 338M model on US President Donald Trump's twitter feed, along with a basic Flask website to display some generated outputs from the model. 

To run:

* Install from the Git repo

* From the Windows command line, enter "set FLASK_APP=Trump_Tweet_Gen" (or "export FLASK_APP=Trump_Tweet_Gen" if on a Unix system)

* Enter "flask init-db" to initialize the application's database

* Enter "flask run" to start the web server

You should be able to access to application in your web browser using the given IP address.

The model was finetuned on a dataset of Trump's tweets obtained from http://www.trumptwitterarchive.com/, tweets from before the start of his 2016 Presidential Campaign were excluded, as well as any retweets and tweet threads. The [GPT-2-Simple](https://github.com/minimaxir/gpt-2-simple) API was of great help finetuning the model. A sample of 10k generated results were exported, and the Flask web application randomly selects one to display when accessed. 
