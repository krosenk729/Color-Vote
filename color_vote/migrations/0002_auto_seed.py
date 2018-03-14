from django.db import migrations, models
from django.core.management import call_command

def seed_data(apps, schema_editor):
    Word = apps.get_model('color_vote', 'Word')
    Word(name = "passionate").save()
    Word(name = "playful").save()
    Word(name = "aggravated").save()
    Word(name = "peeved").save()
    Word(name = "provoked").save()
    Word(name = "irked").save()
    Word(name = "offended").save()
    Word(name = "furious").save()
    Word(name = "bewildered").save()
    Word(name = "perplexed").save()
    Word(name = "puzzled").save()
    Word(name = "clueless").save()
    Word(name = "lost").save()
    Word(name = "cornered").save()
    Word(name = "alarmed").save()
    Word(name = "apprehensive").save()
    Word(name = "edgy").save()
    Word(name = "terrified").save()
    Word(name = "fantastic").save()
    Word(name = "enchanted").save()
    Word(name = "exhilarated").save()
    Word(name = "jubilant").save()
    Word(name = "joyful").save()
    Word(name = "thrilled").save()
    Word(name = "optimistic").save()
    Word(name = "overjoyed").save()
    Word(name = "peaceful").save()

class Migration(migrations.Migration):

    dependencies = [
    ('color_vote', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data)
    ]
