# Generated by Django 4.1.5 on 2023-01-05 17:18

from django.db import migrations
def insert_sample_restaurants(apps,schema_editor):
    Restaurant = apps.get_model('Elite_eats_app', 'Restaurant')
    Restaurant.objects.create(name="The Chelsea House", address="235 Ninth Ave", city="New York", state="NY", zip_code="10001")
    Restaurant.objects.create(name="212 Steakhouse", address="316 E 53rd St", city="New York", state="NY", zip_code="10022")
    Restaurant.objects.create(name="Nostrand Station Bar & Lounge", address="822 Nostrand Ave", city="Brooklyn", state="NY", zip_code="11216")
    Restaurant.objects.create(name="Brooklyn Beso", address="370 Lewis Ave", city="Brooklyn", state="NY", zip_code="11233")
    Restaurant.objects.create(name="Papi Steak", address="736 1st St", city="Miami Beach", state="FL", zip_code="33139")
    Restaurant.objects.create(name="STK Miami", address="1100 Biscayne Blvd", city="Miami Beach", state="FL", zip_code="33139")
    Restaurant.objects.create(name="Sexy Fish Miami", address="1001 S Miami Ave", city="Miami", state="FL", zip_code="33130")
    Restaurant.objects.create(name="The Capital Grille", address="255 East Paces Ferry Rd NE", city="Atlanta", state="GA", zip_code="30305")
    Restaurant.objects.create(name="Footprints", address="4185 Snapfinger Woods Dr", city="Decatur", state="GA", zip_code="30035")
    Restaurant.objects.create(name="Andiamo Steakhouse", address="301 E Fremont St", city="Las Vegas", state="NV", zip_code="89101")
    

class Migration(migrations.Migration):

    dependencies = [
        ('Elite_eats_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_sample_restaurants)
    ]