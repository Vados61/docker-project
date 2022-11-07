# Generated by Django 4.1.2 on 2022-10-23 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='количество')),
                ('fire_ex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='storage.fireextingusher', verbose_name='огнетушитель')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='storage.order')),
            ],
            options={
                'verbose_name': 'Огнетушитель в партии',
                'verbose_name_plural': 'Огнетушители в партии',
            },
        ),
        migrations.DeleteModel(
            name='FireExQuaInOrder',
        ),
        migrations.AlterField(
            model_name='order',
            name='fire_extingushers',
            field=models.ManyToManyField(through='storage.Position', to='storage.fireextingusher', verbose_name='Огнетушители'),
        ),
    ]