from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornitore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('tipo_servizio_offerto', models.CharField(max_length=200)),
                ('indirizzo', models.CharField(blank=True, max_length=250)),
                ('citta', models.CharField(blank=True, max_length=200)),
                ('referente', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('telefono', models.CharField(blank=True, max_length=200)),
                ('annotazioni', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Fornitori',
            },
        ),
        migrations.CreateModel(
            name='PuntoVendita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('indirizzo', models.CharField(blank=True, max_length=250)),
                ('citta', models.CharField(blank=True, max_length=200)),
                ('responsabile', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('telefono', models.CharField(blank=True, max_length=200)),
                ('annotazioni', models.TextField(blank=True)),
                ('fornitori_preferiti', models.ManyToManyField(blank=True, related_name='punti_vendita', to='interventi.Fornitore')),
                ('utenti_preferiti', models.ManyToManyField(blank=True, related_name='punti_vendita', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'PuntiVendita',
            },
        ),
    ]
