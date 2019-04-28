# Generated by Django 2.0.13 on 2019-04-28 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('votes2', models.IntegerField(default=0)),
                ('Partida', models.CharField(default='Partida', max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='escolha',
            name='Equipe_da_casa',
            field=models.OneToOneField(default='10', on_delete=django.db.models.deletion.CASCADE, related_name='casa', to='votacoes.Time'),
        ),
        migrations.AddField(
            model_name='escolha',
            name='Equipe_de_fora',
            field=models.OneToOneField(default='10', on_delete=django.db.models.deletion.CASCADE, related_name='fora', to='votacoes.Time'),
        ),
    ]
