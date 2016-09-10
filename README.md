## NowKnowMore

Hackathon Project


#### Running

```
pip install -r requirements.txt
python app.py
```


#### Hosting On OpenShift

Create the app and add postgresql db.

```bash
# create it in a different location
rhc app create nowknowmore python-2.7
rhc cartridge add postgresql-9.2 -a nowknowmore
```
Then set the env vars.

```bash
rhc env set CONFIG=config.OpenShiftConfig -a nowknowmore
rhc env list -a nowknowmore  # list the vars
```
Finally sync the database.

```bash
rhc ssh -a nowknowmore
# shell opens
cd app-root/repo
python manage.py db upgrade
```
Done.
