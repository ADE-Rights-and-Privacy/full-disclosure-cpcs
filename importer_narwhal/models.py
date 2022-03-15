from django.db import models


class ImportBatch(models.Model):
    start_time = models.DateTimeField(auto_now=True)
    target_model_name = models.CharField(max_length=256)
    number_of_rows = models.IntegerField()
    errors_encountered = models.BooleanField()
    submitted_file_name = models.CharField(max_length=1024)

    def __str__(self):
        # number, import time, filename, model, number of records,
        # and whether it succeeded or not.
        return f"{self.pk} | {self.start_time:%Y-%m-%d %H:%M:%S} | {self.submitted_file_name} | " \
               f"{self.target_model_name} | {self.number_of_rows} | "\
               f"{'Errors encountered' if self.errors_encountered else 'No errors'}"


class ImportedRow(models.Model):
    import_batch = models.ForeignKey(ImportBatch, on_delete=models.CASCADE, related_name='imported_rows')
    row_number = models.IntegerField()
    imported_record_name = models.CharField(max_length=1024)
    imported_record_pk = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.row_number} | {self.imported_record_name} | {self.imported_record_pk}"
