import csv
from django.core.management.base import BaseCommand
from TradePortal.models import Company

class Command(BaseCommand):
    help = 'Imports company data from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.stdout.write(self.style.SUCCESS(f'Importing data from {csv_file_path}'))

                imported_count = 0
                skipped_count = 0
                
                for row in reader:
                    try:
                        scripcode_value = row.get('scripcode')
                        if scripcode_value:
                            scripcode_value = int(float(scripcode_value))
                        else:
                            self.stdout.write(self.style.WARNING(f"Skipping row with missing scripcode: {row}"))
                            skipped_count += 1
                            continue
                        
                        Company.objects.create(
                            company_name=row['company_name'],
                            symbol=row['symbol'],
                            scripcode=scripcode_value
                        )
                        imported_count += 1
                    except (ValueError, KeyError, TypeError) as e:
                        self.stdout.write(self.style.ERROR(f"Error processing row {row}: {e}"))
                        skipped_count += 1

                self.stdout.write(self.style.SUCCESS(f'Successfully imported {imported_count} companies.'))
                self.stdout.write(self.style.WARNING(f'Skipped {skipped_count} invalid rows.'))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Error: The file '{csv_file_path}' was not found."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An unexpected error occurred: {e}"))
